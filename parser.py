import re
import requests

input_file = ""
output_file = ""

def format_authors(authors):
    """只保留第一作者，多作者时加 et al."""
    if not authors:
        return "未知作者"
    first_author = authors[0]
    return f"{first_author} et al." if len(authors) > 1 else first_author

def normalize_doi(raw):
    """规范化 DOI：去掉尾部括号、标点和前缀"""
    if not raw:
        return None
    doi = raw.strip()
    # 去掉尾部的 ) ] . ; , 空格
    doi = re.sub(r"[)\].;,\s]+$", "", doi)
    # 去掉 doi.org 前缀（如果有）
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/)", "", doi, flags=re.I)
    return doi

def get_arxiv_authors(arxiv_id):
    """从 arXiv API 获取作者"""
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    resp = requests.get(url)
    if resp.status_code == 200:
        text = resp.text
        authors = re.findall(r"<name>(.*?)</name>", text)
        print(f"    [API] arXiv {arxiv_id} → authors={authors}")
        return format_authors(authors)
    return "未知作者"

def get_crossref_authors(doi):
    """从 CrossRef API 获取作者"""
    url = f"https://api.crossref.org/works/{doi}"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()["message"]
        authors = [f"{a.get('family','')} {a.get('given','')}" for a in data.get("author",[])]
        print(f"    [API] DOI {doi} → authors={authors}")
        return format_authors(authors)
    return "未知作者"

count = 0
current_section = None

with open(input_file, "r", encoding="utf-8") as f, open(output_file, "w", encoding="utf-8") as out_f:
    for line in f:
        # 检测小节标题（###、####、##### 开头）
        if line.strip().startswith("###"):
            current_section = line.strip()
            count = 0
            print(f"\n==================== Entering Section: {current_section} ====================")
            out_f.write(line)  # 保留原始标题行
            continue

        # 检测论文行
        if "[Paper]" in line and ("arxiv.org" in line or "doi" in line):
            # 提取出版物和年份
            match_pub = re.search(r"\*\*\[(.*?)\]\*\*", line)
            pub_info = match_pub.group(1) if match_pub else "未知出版物"
            year_match = re.search(r"\d{2,4}", pub_info) if pub_info != "未知出版物" else None
            year = year_match.group(0) if year_match else "未知年份"

            # 提取标题（去掉出版物标签）
            match_title = re.search(r"\* (.*?)(?:\.|\[Paper)", line)
            title = match_title.group(1).strip() if match_title else None
            if pub_info != "未知出版物" and title.startswith(f"**[{pub_info}]**"):
                title = title.replace(f"**[{pub_info}]**", "").strip()

            # 提取链接
            match_arxiv = re.search(r"https://arxiv.org/abs/(\d+\.\d+)", line)
            match_doi = re.search(r"(10\.\d{4,9}/[-._;()/:A-Z0-9]+)", line, re.I)

            # 特殊处理 dl.acm.org/doi/pdf 链接 → 提取 DOI
            if "dl.acm.org/doi/pdf/" in line:
                doi_match = re.search(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", line, re.I)
                if doi_match:
                    match_doi = doi_match

            author = "未知作者"
            doi = None
            if match_arxiv:
                author = get_arxiv_authors(match_arxiv.group(1))
            elif match_doi:
                doi_raw = match_doi.group(1) if match_doi.lastindex else match_doi.group(0)
                doi = normalize_doi(doi_raw)
                print(f"DEBUG: 提取到 DOI: {doi}")
                author = get_crossref_authors(doi)

            # 保留原始 [Paper](...) 链接
            paper_link_match = re.search(r"(\[Paper\]\(.*?\))", line)
            paper_link = paper_link_match.group(1) if paper_link_match else ""

            if title:
                count += 1
                ref = f"[{count}] {author}, {title}, {pub_info}, {paper_link}"

                # 调试输出
                print("\n原始行:", line.strip())
                print("提取结果:")
                print(f"  - 标题: {title}")
                print(f"  - 出版物: {pub_info}")
                print(f"  - 年份: {year}")
                if match_arxiv:
                    print(f"  - 链接: https://arxiv.org/abs/{match_arxiv.group(1)}")
                elif doi:
                    print(f"  - 链接: DOI {doi}")
                print("API返回:")
                print(f"  - 作者: {author}")
                print("最终引用:")
                print(f"  {ref}")

                out_f.write(ref + "\n\n")  # 多写一个换行
        else:
            # 非论文行原样保留
            out_f.write(line)

print("\n全部处理完成，结果已保存到", output_file)
