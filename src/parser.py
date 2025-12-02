import os
import re
import json
import base64
import fitz  # PyMuPDF
import requests
import urllib.parse
from openai import OpenAI

# 配置 API Key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_KEY"


def encode_image_to_base64(image_bytes):
    """将图片字节流转换为Base64字符串"""
    return base64.b64encode(image_bytes).decode('utf-8')


def extract_first_page_as_image(pdf_path):
    """
    读取PDF路径，将第一页裁切并转换为PNG字节流
    """
    try:
        doc = fitz.open(pdf_path)
        # 获取第一页 (索引为0)
        page = doc[0]

        # 将页面渲染为像素图 (dpi=150 通常足够清晰且Token消耗较少)
        pix = page.get_pixmap(dpi=150)

        # 转换为PNG字节数据
        img_bytes = pix.tobytes("png")
        doc.close()
        return img_bytes
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None


def parse_paper_metadata(pdf_path, model="gpt-5-mini"):
    """
    主函数：输入PDF路径，返回解析后的JSON数据
    """
    client = OpenAI()

    # 1. 获取第一页图片
    image_bytes = extract_first_page_as_image(pdf_path)
    if not image_bytes:
        return {"error": "Failed to extract image"}

    # 2. 编码图片
    base64_image = encode_image_to_base64(image_bytes)

    # 3. 构造 Prompt
    system_prompt = """
    You are an expert academic assistant. Your task is to extract metadata from the image of the first page of a research paper.

    Extract the following fields and return them in this format (pay attention to the track, Industry or Workshop, omit research track):
    First author name et al., [Paper title](), publication'year track
    
    - "First author name": The first author's full name.
    - "Paper title": The full title of the paper.
    - "publication": The name of the journal, conference, or proceedings (e.g., "CVPR", "NIPS", "OOPSLA", "arXiv"). Look at the header or footer. If not explicitly found, return null.
    - "year": The publication year (integer), 19 for 2019; 87 for 1987 If not found, return null.

    For example:
    Junyang Wang et al., [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](), ICLR'24 Workshop
    Minh Duc Vu et al., [GPTVoiceTasker: Advancing Multi-step Mobile Task Efficiency Through Dynamic Interface Exploration and Learning](), OOPSLA'24 
    Jiazheng Sun et al., [Fairy: Interactive Mobile Assistant to Real-world Tasks via LMM-based Multi-agent](), arXiv'25
    Kong Qichao et al., [ProphetAgent: Automatically Synthesizing GUI Tests from Test Cases in Natural Language for Mobile Apps](), FSE'25 Industry  
    """

    # 4. 调用 OpenAI API
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": [
                    {"type": "text", "text": "Please analyze this image of the paper's first page."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]}
            ],
            # 强制输出 JSON 格式 (OpenAI API 特性)
            # response_format={"type": "json_object"},
            # temperature=0.1  # 降低随机性，提高准确度
        )

        # 5. 解析返回结果
        result_content = response.choices[0].message.content
        return result_content

    except Exception as e:
        return {"error": f"API Call failed: {str(e)}"}


def search_arxiv_url(title):
    """根据论文标题搜索 arXiv，返回精确匹配的 URL，没找到返回 None"""
    import difflib
    query = urllib.parse.quote(title.replace(':', '').replace('"', ''))
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&max_results=5"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            # 找到所有 entry 的 title 和 id
            entries = re.findall(r"<entry>(.*?)</entry>", r.text, re.S)
            for entry in entries:
                # 提取 title
                title_match = re.search(r"<title>(.*?)</title>", entry, re.S)
                if not title_match:
                    continue
                entry_title = title_match.group(1).strip().replace('\n', ' ')
                # 精确匹配或相似度匹配
                ratio = difflib.SequenceMatcher(None, title.lower(), entry_title.lower()).ratio()
                if ratio > 0.9:  # 可以调节阈值
                    # 提取 id
                    id_match = re.search(r"<id>http://arxiv.org/abs/([^<]+)</id>", entry)
                    if id_match:
                        return f"https://arxiv.org/abs/{id_match.group(1)}"
    except Exception as e:
        print("arXiv 搜索失败:", e)
    return None



def search_acm_url(title):
    """根据论文标题搜索 ACM DL 返回 URL，没找到返回 None"""
    query = urllib.parse.quote(title)
    search_url = f"https://dl.acm.org/action/doSearch?AllField={query}"
    # 这里简单返回搜索页 URL，精确匹配可以用 BeautifulSoup 或 ACM API
    return search_url


if __name__ == "__main__":
    # PDF 文件夹路径
    pdf_folder = "../PDF/"
    # 输出 Markdown 文件
    output_md = "../PDF/output.md"

    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]
    pdf_files.sort()  # 按文件名排序

    with open(output_md, "w", encoding="utf-8") as f_out:
        for idx, pdf_file in enumerate(pdf_files, start=1):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            print(f"正在解析: {pdf_path} ...")

            metadata = parse_paper_metadata(pdf_path)

            title_match = re.search(r"\[([^\]]+)\]\(\s*\)", metadata)  # 匹配 []() 中括号为空的情况
            if title_match:
                title = title_match.group(1).strip()
                # 搜索 URL
                url = search_arxiv_url(title) or search_acm_url(title) or pdf_path
                # 直接替换空括号 ()
                md_line = re.sub(r"\(\s*\)", f"({url})", metadata)
            else:
                md_line = metadata

            f_out.write(md_line + "\n")

    print(f"解析完成，结果已写入: {output_md}")
