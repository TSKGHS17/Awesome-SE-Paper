# Awesome-SE-Paper

Awesome-SE-Paper is my continuously updated reading list of SE and GUI agent research, you can hit the **STAR** to follow the updates.

## Table of Contents 📇

- [GUI Agents](#gui-agents)
  - [GUI Assistant](#gui-assistant)
  - [GUI Test Execution](#gui-test-execution)
  - [Bug Report Reproduce](#bug-report-reproduce)
  - [VLMs for Downstream Tasks](#vlms-for-downstream-tasks)
    - [Grounding VLMs](#grounding-vlms)
    - [Navigation VLMs](#navigation-vlms)
    - [Training Data Generation](#training-data-generation)
  - [Benchmark](#benchmark)
  - [Empirical Study](#empirical-study)
- [GUI Understanding](#gui-understanding)
- [Functional Bugs](#functional-bugs)
- [Random Testing](#random-testing)
- [Model-based Testing](#model-based-testing)
- [Test Case Management](#test-case-management)
- [UI2Code](#ui2code)

## GUI Agents

### GUI Assistant

[1] Junyang Wang et al., [Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception](https://arxiv.org/abs/2401.16158), ICLR'24 Workshop

[2] Hao Wen et al., [AutoDroid: LLM-powered Task Automation in Android](https://arxiv.org/abs/2308.15272), MobiCom'24

[3] Lee Sunjae et al., [MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation](https://dl.acm.org/doi/pdf/10.1145/3636534.3690682), MobiCom'24

[4] Minh Duc Vu et al., [GPTVoiceTasker: Advancing Multi-step Mobile Task Efficiency Through Dynamic Interface Exploration and Learning](https://arxiv.org/abs/2401.14268), UIST'24 

[5] Junyang Wang et al., [Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration](https://arxiv.org/abs/2406.01014), NIPS'24  

[6] Weizhi Chen et al., [PG-Agent: An Agent Powered by Page Graph](https://arxiv.org/abs/2509.03536), MM'25 

[7] Chi Zhang et al., [AppAgent: Multimodal Agent as Smartphone Users](https://arxiv.org/abs/2312.13771), CHI'25  

[8] Bin Xie et al., [GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://arxiv.org/abs/2505.16827), ACL'25  

[9] Peng Yi-Hao et al., [Morae: Proactively Pausing UI Agents for User Choices](https://dl.acm.org/doi/pdf/10.1145/3746059.3747797), UIST'25

[10] Haowei Liu et al., [PC-Agent: A Hierarchical Multi-Agent Collaboration Framework for Complex Task Automation on PC](https://arxiv.org/abs/2502.14282), ICLR'25 Workshop  

[11] Jiazheng Sun et al., [Fairy: Interactive Mobile Assistant to Real-world Tasks via LMM-based Multi-agent](https://arxiv.org/abs/2509.20729), arXiv'25

### GUI Test Execution

[1] Ran Dezhi et al., [Guardian: A Runtime Framework for LLM-Based UI Exploration](https://dl.acm.org/doi/pdf/10.1145/3650212.3680334), ISSTA'24

[2] Sidong Feng et al., [Enabling Cost-Effective UI Automation Testing with Retrieval-Based LLMs: A Case Study in WeChat](https://arxiv.org/abs/2409.07829), ASE'24 Industry  

[3] Maryam Taeb et al., [AXNav: Replaying Accessibility Tests from Natural Language](https://arxiv.org/abs/2310.02424), CHI'24

[4] Yongxiang Hu et al., [AUITestAgent: Automatic Requirements Oriented GUI Function Testing](https://arxiv.org/abs/2407.09018), arXiv'24 

[5] Yanqi Su et al., [Automated Soap Opera Testing Directed by LLMs and Scenario Knowledge: Feasibility, Challenges, and Road Ahead](https://arxiv.org/abs/2412.08581), FSE'25

[6] Kong Qichao et al., [ProphetAgent: Automatically Synthesizing GUI Tests from Test Cases in Natural Language for Mobile Apps](https://dl.acm.org/doi/pdf/10.1145/3696630.3728543), FSE'25 Industry  

[7] Sidong Feng et al., [Agent for User: Testing Multi-User Interactive Features in TikTok](https://arxiv.org/abs/2504.15474), ICSE'25 Industry

[8] Sidong Feng et al., [Breaking Single-Tester Limits: Multi-Agent LLMs for Multi-User Feature Testing](https://arxiv.org/abs/2506.17539), ICSE'26 

[9] Zhe Liu et al., [Seeing is Believing: Vision-driven Non-crash Functional Bug Detection for Mobile Apps](https://arxiv.org/abs/2407.03037), TSE'25  

[10] Xuan Wang et al., [From Redundancy to Efficiency: Exploiting Shared UI Interactions towards Efficient LLM-Based Testing]( ), ASE'25 Industry

### Bug Report Reproduce

[1] Sidong Feng et al., [Prompting Is All You Need: Automated Android Bug Replay with Large Language Models](https://arxiv.org/abs/2306.01987), ICSE'24 

[2] Su Yanqi et al., [Enhancing Exploratory Testing by Large Language Model and Knowledge Graph](https://dl.acm.org/doi/pdf/10.1145/3597503.3639157), ICSE'24 

[3] Dingbang Wang et al., [Feedback-Driven Automated Whole Bug Report Reproduction for Android Apps](https://arxiv.org/abs/2407.05165), ISSTA'24  

[4] Yuchao Huang et al., [One Sentence Can Kill the Bug: Auto-replay Mobile App Crashes from One-sentence Overviews](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10869838), TSE'25

### VLMs for Downstream Tasks

#### Grounding VLMs

[1] Kanzhi Cheng et al., [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935), ACL'24 

[2] Zhiyong Wu et al., [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218), ICLR'25  

[3] Boyu Gou et al., [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://arxiv.org/abs/2410.05243), ICLR'25

[4] Zhengxi Lu et al., [UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620), AAAI'26

[5] Fei Tang et al., [GUI-G^2: Gaussian Reward Modeling for GUI Grounding](https://arxiv.org/abs/2507.15846), arXiv'25  

[6] Liangyu Chen et al., [UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning](https://arxiv.org/abs/2510.20286), arXiv'25

#### Navigation VLMs

[1] Wenyi Hong et al., [CogAgent: A Visual Language Model for GUI Agents](https://arxiv.org/abs/2312.08914), CVPR'24  

[2] Yujia Qin et al., [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326), arXiv'25 

[3] Kevin Qinghong Lin et al., [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://arxiv.org/abs/2411.17465), CVPR'25 

[4] Mengzhou Wu et al., [Element-Aware Fine-Tuning of Vision-Language Models for Cost-Efficient GUI Testing in an Industrial Setting]( ), ASE'25 Industry

[5] Tang Xiaoxuan et al., [TestFlow: Advancing Mobile UI Testing through Multi-Step Reinforcement Learning](https://dl.acm.org/doi/pdf/10.1145/3713081.3732930), ISSTA'25 Workshop  

[6] Qinzhuo Wu et al., [ReachAgent: Enhancing Mobile Agent via Page Reaching and Operation](https://arxiv.org/abs/2502.02955), NAACL'25  

[7] Haoming Wang et al., [UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544), arXiv'25 

[8] Run Luo et al., [GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents](https://arxiv.org/abs/2504.10458), arXiv'25  

[9] Shaojie Zhang et al., [BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent](https://arxiv.org/abs/2509.15566), NIPS'25  

[10] Jiani Zheng et al., [VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model](https://arxiv.org/abs/2502.18906), arXiv'25

#### Training Data Generation

[1] Yang Li et al., [Widget Captioning: Generating Natural Language Description for Mobile User Interface Elements](https://arxiv.org/abs/2010.04295), EMNLP'20  

[2] Vardaan Pahuja et al., [Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents](https://arxiv.org/abs/2502.11357), ACL'25 Findings  

[3] Hongjin Su et al., [Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents in Realistic Environments](https://arxiv.org/abs/2501.10893), ICLR'25

### Benchmark

[1] Christopher Rawles et al., [Android in the Wild: A Large-Scale Dataset for Android Device Control](https://arxiv.org/abs/2307.10088), NIPS'23  

[2] Shuyan Zhou et al., [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854), NIPS'23 Workshop 

[3] Li Zhang et al., [LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Task Automation](https://arxiv.org/abs/2404.16054), UIST'24

[4] Kanzhi Cheng et al., [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935), ACL'24  

[5] Raghav Kapoor et al., [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://arxiv.org/abs/2402.17553), ECCV'24  

[6] Wei Li et al., [On the Effects of Data Scale on UI Control Agents](https://arxiv.org/abs/2406.03679), NIPS'24

[7] Tianbao Xie et al., [OSWORLD: benchmarking multimodal agents for open-ended tasks in real computer environments](https://arxiv.org/abs/2404.07972), NIPS'24  

[8] Zhiyong Wu et al., [OS-ATLAS: Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218), ICLR'25  

[9] Kaixin Li et al., [Screenspot-pro: Gui grounding for professional high-resolution computer use](https://arxiv.org/abs/2504.07981), ICLR'25 Workshop

[10] Quanfeng Lu et al., [GUIOdyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices](https://arxiv.org/abs/2406.08451), ICCV'25  

[11] Christopher Rawles et al., [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://arxiv.org/abs/2405.14573), ICLR'25

### Empirical Study

[1] Antoine Chevrot et al., [Are Autonomous Web Agents Good Testers?](https://arxiv.org/abs/2504.01495), ISSTA'25

## GUI Understanding

[1] Hu Yongxiang et al., [Appaction: Automatic GUI Interaction for Mobile Apps via Holistic Widget Perception](https://dl.acm.org/doi/pdf/10.1145/3611643.3613885), FSE'23 Industry  

[2] Sidong Feng et al., [MUD: Towards a Large-Scale and Noise-Filtered UI Dataset for Modern Style UI Modeling](https://arxiv.org/abs/2405.07090), CHI'24

[3] Ziwei Wang et al., [MP-GUI: Modality Perception with MLLMs for GUI Understanding](https://arxiv.org/abs/2503.14021), CVPR'25  

[4] Dehai Zhao et al., [SeeAction: Towards Reverse Engineering How-What-Where of HCI Actions from Screencasts for UI Automation](https://arxiv.org/abs/2503.12873), ICSE'25  

[5] Wei Liu et al., [GUIWatcher: Automatically Detecting GUI Lags by Analyzing Mobile Application Screencasts](https://arxiv.org/abs/2502.04202), ICSE'25 Industry

## Functional Bugs

[1] Ting Su et al., [Fully Automated Functional Fuzzing of Android Apps for Detecting Non-crashing Logic Bugs](https://arxiv.org/abs/2008.03585), OOPSLA'21 

[2] Xiong Yiheng et al., [An Empirical Study of Functional Bugs in Android Apps](https://dl.acm.org/doi/pdf/10.1145/3597926.3598138), ISSTA'23

[3] Jiajun Hu et al., [ωTest: WebView-Oriented Testing for Android Applications](https://arxiv.org/abs/2306.03845), ISSTA'23  

[4] Yongxiang Hu et al., [AutoConsis: Automatic GUI-driven Data Inconsistency Detection of Mobile Apps](https://ieeexplore.ieee.org/document/10554689), ICSE'24 Industry  

[5] Yiheng Xiong et al., [General and Practical Property-based Testing for Android Apps](https://ieeexplore.ieee.org/document/10764962), ASE'24

[6] Chenkai Guo et al., [EP-Detector: Automatic Detection of Error-prone Operation Anomalies in Android Applications](https://ieeexplore.ieee.org/document/11029849), ICSE'25

[7] Yongxiang Hu et al., [KuiTest: Leveraging Knowledge in the Wild as GUI Testing Oracle for Mobile Apps](https://ieeexplore.ieee.org/document/11121717), ICSE'25 Industry  

[8] Ruofan Liu et al., [GUIPilot: A Consistency-based Mobile GUI Testing Approach for Detecting Application-specific Bugs](https://arxiv.org/abs/2506.07385), ISSTA'25

[9] Fan Fu et al., [An Empirical Study on Common Sense-Violating Bugs in Mobile Apps](https://dl.acm.org/doi/pdf/10.1145/3709356), TOSEM'25  

[10] Yongxiang Hu et al., [Minuku: Detecting Diverse Display Issues in Mobile Apps with Small-scale Dataset]( ), ASE'25 Industry

## Accessibility

[1] Liu Zhe et al., [Unblind Text Inputs: Predicting Hint-text of Text Input in Mobile Apps via LLM](https://dl.acm.org/doi/pdf/10.1145/3613904.3642939), CHI'24  

[2] Yuxin Zhang et al., [Scenario-Driven and Context-Aware Automated Accessibility Testing for Android Apps](https://ieeexplore.ieee.org/document/11029746), ICSE'25

[3] Zhang Mengxi et al., [Distinguishing GUI Component States for Blind Users using Large Language Models](https://dl.acm.org/doi/pdf/10.1145/3722106), TOSEM'25

## Random Testing

[1] Ran Dezhi et al., [Automated Visual Testing for Mobile Apps in an Industrial Setting](https://dl.acm.org/doi/pdf/10.1145/3510457.3513027), ICSE'22 Industry  

[2] Zhe Liu et al., [Fill in the Blank: Context-Aware Automated Text Input Generation for Mobile GUI Testing](https://arxiv.org/abs/2212.04732), ICSE'23 

[3] Zhe Liu et al., [Make LLM a Testing Expert: Bringing Human-like Interaction to Mobile GUI Testing via Functionality-aware Decisions](https://arxiv.org/abs/2310.15780), ICSE'24  

[4] Han Hu et al., [Enhancing GUI Exploration Coverage of Android Apps with Deep Link-Integrated Monkey](https://arxiv.org/abs/2404.19307), TOSEM'24

[5] Wang Chenxu et al., [LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance](https://dl.acm.org/doi/pdf/10.1145/3715763), FSE'25 

[6] Chen Mengzhuo et al., [Standing on the Shoulders of Giants: Bug-Aware Automated GUI Testing via Retrieval Augmentation](https://dl.acm.org/doi/pdf/10.1145/3715755), FSE'25

[7] Lu Yifei et al., [Improving Test Efficacy for Large-Scale Android Applications by Exploiting GUI and Functional Equivalence](https://dl.acm.org/doi/pdf/10.1145/3729225), TOSEM'25

## Model-based Testing

[1] Sen Chen et al., [StoryDroid: Automated Generation of Storyboard for Android Apps](https://arxiv.org/abs/1902.00476), ICSE'19  

[2] Xiangyu Zhang et al., [Scene-Driven Exploration and GUI Modeling for Android Apps](https://arxiv.org/abs/2308.10228), ASE'23  

[3] Yanchen Lu et al., [TacDroid: Detection of Illicit Apps through Hybrid Analysis of UI-based Transition Graphs](https://shhaos.github.io/papers/icse25.pdf), ICSE'25

## Test Case Management

[1] Parsa Alian et al., [Feature-Driven End-To-End Test Generation](https://arxiv.org/abs/2408.01894), ICSE'25

[2] Benyamin Beyzaei et al., [Automated Test Transfer across Android Apps using Large Language Models](https://arxiv.org/abs/2411.17933), ISSTA'25

## UI2Code

[1] Fan Wu et al., [MLLM-Based UI2Code Automation Guided by UI Layout Information](https://arxiv.org/abs/2506.10376), ISSTA'25
