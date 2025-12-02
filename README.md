# Awesome-SE-Paper

Awesome-SE-Paper is my continuously updated reading list of SE and GUI agent research, you can hit the **STAR** to follow the updates.

## Table of Contents 📇


- [GUI Agents](#gui-agents)
  - [GUI Assistant](#gui-assistant)
    - [GUI Understanding](#gui-understanding)
    - [Agent Knowledge](#agent-knowledge)
    - [Agent for A11y](#agent-for-a11y)
    - [Multi-agent](#multi-agent)
  - [GUI Test Execution](#gui-test-execution)
    - [Crash](#crash)
    - [Functional Bugs](#functional-bugs)
  - [Bug Report Reproduce](#bug-report-reproduce)
  - [VLMs for Downstream Tasks](#vlms-for-downstream-tasks)
    - [Grounding VLMs](#grounding-vlms)
      - [SFT](#sft)
      - [RL](#rl)
    - [Navigation VLMs](#navigation-vlms)
      - [SFT](#sft-1)
      - [RL](#rl-1)
    - [Training Data Generation](#training-data-generation)
  - [Benchmark](#benchmark)
    - [Testbed](#testbed)
    - [Grounding Benchmarks](#grounding-benchmarks)
    - [Navigation Benchmarks](#navigation-benchmarks)
    - [Mixed Benchmarks](#mixed-benchmarks)
  - [Empirical Study](#empirical-study)
- [GUI Understanding](#gui-understanding-1)
  - [Dataset](#dataset)
  - [Tool](#tool)
- [Functional Bugs](#functional-bugs-1)
  - [Empirical Study (ISSTA'23)](#empirical-study-issta23)
  - [App-specific Bugs](#app-specific-bugs)
  - [Display Bugs](#display-bugs)
  - [Various Bug Types](#various-bug-types)
  - [Accessibility](#accessibility)
    - [BLV Users](#blv-users)
    - [A11y Testing](#a11y-testing)
- [Random Testing](#random-testing)
  - [Coverage](#coverage)
  - [Efficiency](#efficiency)
  - [LLM-assisted Testing](#llm-assisted-testing)
- [Model-based Testing](#model-based-testing)
  - [UTG](#utg)
- [Test Case Management](#test-case-management)
  - [Test Case Generation](#test-case-generation)
  - [Test Case Transfer](#test-case-transfer)
- [UI2Code](#ui2code)
  - [DL Methods](#dl-methods)
  - [LLM-based Methods](#llm-based-methods)
---


GUI Agents
----------

### GUI Assistant

#### GUI Understanding

[1] Junyang Wang et al., Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception, ICLR'24, [Paper](https://arxiv.org/abs/2401.16158)[Repo](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1)


#### Agent Knowledge

[1] Hao Wen et al., AutoDroid: LLM-powered Task Automation in Android, MobiCom'24, [Paper](https://arxiv.org/abs/2308.15272)

[2] Lee Sunjae et al., MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation, MobiCom'24, [Paper](https://dl.acm.org/doi/pdf/10.1145/3636534.3690682)

[3] Minh Duc Vu et al., GPTVoiceTasker: Advancing Multi-step Mobile Task Efficiency Through Dynamic Interface Exploration and Learning, UIST'24, [Paper](https://arxiv.org/abs/2401.14268)

[4] Weizhi Chen et al., PG-Agent: An Agent Powered by Page Graph, MM'25, [Paper](https://arxiv.org/abs/2509.03536)

[5] Chi Zhang et al., AppAgent: Multimodal Agent as Smartphone Users, CHI'25, [Paper](https://arxiv.org/abs/2312.13771)[Repo](https://github.com/TencentQQGYLab/AppAgent)

[6] Bin Xie et al., GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent, ACL'25, [Paper](https://arxiv.org/abs/2505.16827)


#### Agent for A11y

[1] Peng Yi-Hao et al., Morae: Proactively Pausing UI Agents for User Choices, UIST'25, [Paper](https://dl.acm.org/doi/pdf/10.1145/3746059.3747797)


#### Multi-agent

[1] Junyang Wang et al., Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration, NIPS'24, [Paper](https://arxiv.org/abs/2406.01014)[Repo](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v2)

[2] Haowei Liu et al., PC-Agent: A Hierarchical Multi-Agent Collaboration Framework for Complex Task Automation on PC, ICLR'25 Workshop, [Paper](https://arxiv.org/abs/2502.14282)[Repo](https://github.com/X-PLUG/MobileAgent/tree/main/PC-Agent)

[3] Jiazheng Sun et al., Fairy: Interactive Mobile Assistant to Real-world Tasks via LMM-based Multi-agent, arxiv 25, [Paper](https://arxiv.org/abs/2509.20729)


### GUI Test Execution

#### Crash

[1] Ran Dezhi et al., Guardian: A Runtime Framework for LLM-Based UI Exploration, ISSTA'24, [Paper](https://dl.acm.org/doi/pdf/10.1145/3650212.3680334)

[2] Sidong Feng et al., Enabling Cost-Effective UI Automation Testing with Retrieval-Based LLMs: A Case Study in WeChat, ASE'24 Industry, [Paper](https://arxiv.org/abs/2409.07829)

[3] Kong Qichao et al., ProphetAgent: Automatically Synthesizing GUI Tests from Test Cases in Natural Language for Mobile Apps, FSE'25 Industry, [Paper](https://dl.acm.org/doi/pdf/10.1145/3696630.3728543)

[4] Sidong Feng et al., Agent for User: Testing Multi-User Interactive Features in TikTok, ICSE'25 Industry, [Paper](https://arxiv.org/abs/2504.15474)

[5] Sidong Feng et al., Breaking Single-Tester Limits: Multi-Agent LLMs for Multi-User Feature Testing, ICSE'26, [Paper](https://arxiv.org/abs/2506.17539)

[6] Xuan Wang et al.,From Redundancy to Efficiency: Exploiting Shared UI Interactions towards Efficient LLM-Based Testing,ASE'25.

#### Functional Bugs

[1] Maryam Taeb et al., AXNav: Replaying Accessibility Tests from Natural Language, CHI'24, [Paper](https://arxiv.org/abs/2310.02424)

[2] Zhe Liu et al., Seeing is Believing: Vision-driven Non-crash Functional Bug Detection for Mobile Apps, TSE'25, [Paper](https://arxiv.org/abs/2407.03037)

[3] Yongxiang Hu et al., AUITestAgent: Automatic Requirements Oriented GUI Function Testing, arxiv 24, [Paper](https://arxiv.org/abs/2407.09018)[Repo](https://github.com/bz-lab/AUITestAgent)

[4] Yanqi Su et al., Automated Soap Opera Testing Directed by LLMs and Scenario Knowledge: Feasibility, Challenges, and Road Ahead, FSE'25, [Paper](https://arxiv.org/abs/2412.08581)


### Bug Report Reproduce

[1] Sidong Feng et al., Prompting Is All You Need: Automated Android Bug Replay with Large Language Models, ICSE'24, [Paper](https://arxiv.org/abs/2306.01987)

[2] Su Yanqi et al., Enhancing Exploratory Testing by Large Language Model and Knowledge Graph, ICSE'24, [Paper](https://dl.acm.org/doi/pdf/10.1145/3597503.3639157)

[3] Dingbang Wang et al., Feedback-Driven Automated Whole Bug Report Reproduction for Android Apps, ISSTA'24, [Paper](https://arxiv.org/abs/2407.05165)

[4] Yuchao Huang et al., One Sentence Can Kill the Bug: Auto-replay Mobile App Crashes from One-sentence Overviews,TSE'25. [Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10869838)

### VLMs for Downstream Tasks

#### Grounding VLMs

##### SFT

[1] Kanzhi Cheng et al., SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents, ACL'24, [Paper](https://arxiv.org/abs/2401.10935)

[2] Zhiyong Wu et al., OS-ATLAS: Foundation Action Model for Generalist GUI Agents, ICLR'25, [Paper](https://arxiv.org/abs/2410.23218)

[3] Boyu Gou et al., Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents, ICLR'25, [Paper](https://arxiv.org/abs/2410.05243)


##### RL

[1] Zhengxi Lu et al., UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning, AAAI'26, [Paper](https://arxiv.org/abs/2503.21620)

[2] Fei Tang et al., GUI-G^2: Gaussian Reward Modeling for GUI Grounding, arxiv 25, [Paper](https://arxiv.org/abs/2507.15846)

[3] Liangyu Chen et al., UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning, arxiv 25, [Paper](https://arxiv.org/abs/2510.20286)


#### Navigation VLMs

##### SFT

[1] Wenyi Hong et al., CogAgent: A Visual Language Model for GUI Agents, CVPR'24, [Paper](https://arxiv.org/abs/2312.08914)

[2] Yujia Qin et al., UI-TARS: Pioneering Automated GUI Interaction with Native Agents, arxiv 25, [Paper](https://arxiv.org/abs/2501.12326)

[3] Kevin Qinghong Lin et al., ShowUI: One Vision-Language-Action Model for GUI Visual Agent, CVPR'25, [Paper](https://arxiv.org/abs/2411.17465)

[4] Mengzhou Wu et al., Element-Aware Fine-Tuning of Vision-Language Models for Cost-Efficient GUI Testing in an Industrial Setting, ASE'25 Industry.

##### RL

[1] Tang Xiaoxuan et al., TestFlow: Advancing Mobile UI Testing through Multi-Step Reinforcement Learning, ISSTA'25 Workshop, [Paper](https://dl.acm.org/doi/pdf/10.1145/3713081.3732930)

[2] Qinzhuo Wu et al., ReachAgent: Enhancing Mobile Agent via Page Reaching and Operation, NAACL'25, [Paper](https://arxiv.org/abs/2502.02955)

[3] Haoming Wang et al., UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning, arxiv 25, [Paper](https://arxiv.org/abs/2509.02544)

[4] Run Luo et al., GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents, arxiv 25, [Paper](https://arxiv.org/abs/2504.10458)

[5] Shaojie Zhang et al., BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent, NIPS'25, [Paper](https://arxiv.org/abs/2509.15566)

[6] Jiani Zheng et al., VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model, arxiv 25, [Paper](https://arxiv.org/abs/2502.18906)


#### Training Data Generation

[1] Yang Li et al., Widget Captioning: Generating Natural Language Description for Mobile User Interface Elements, EMNLP'20, [Paper](https://arxiv.org/abs/2010.04295)

[2] Vardaan Pahuja et al., Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents, ACL'25 Findings, [Paper](https://arxiv.org/abs/2502.11357)

[3] Hongjin Su et al., Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents in Realistic Environments, ICLR'25, [Paper](https://arxiv.org/abs/2501.10893)


### Benchmark

#### Testbed

[1] Li Zhang et al., LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Task Automation, UIST'24, [Paper](https://arxiv.org/abs/2404.16054)


#### Grounding Benchmarks

[1] Kanzhi Cheng et al., SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents, ACL'24, [Paper](https://arxiv.org/abs/2401.10935)

[2] Zhiyong Wu et al., OS-ATLAS: Foundation Action Model for Generalist GUI Agents, ICLR'25, [Paper](https://arxiv.org/abs/2410.23218)

[3] Kaixin Li et al., Screenspot-pro: Gui grounding for professional high-resolution computer use, ICLR'25 Workshop, [Paper](https://arxiv.org/abs/2504.07981)


#### Navigation Benchmarks

[1] Christopher Rawles et al., Android in the Wild: A Large-Scale Dataset for Android Device Control, NIPS'23, [Paper](https://arxiv.org/abs/2307.10088)

[2] Shuyan Zhou et al., WebArena: A Realistic Web Environment for Building Autonomous Agents, NIPS'23 Workshop, [Paper](https://arxiv.org/abs/2307.13854)

[3] Tianbao Xie et al., OSWORLD: benchmarking multimodal agents for open-ended tasks in real computer environments, NIPS'24, [Paper](https://arxiv.org/abs/2404.07972)

[4] Quanfeng Lu et al., GUIOdyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices, ICCV'25, [Paper](https://arxiv.org/abs/2406.08451)

[5] Christopher Rawles et al., AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents, ICLR'25, [Paper](https://arxiv.org/abs/2405.14573)


#### Mixed Benchmarks

[1] Raghav Kapoor et al., OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web, ECCV'24, [Paper](https://arxiv.org/abs/2402.17553)

[2] Wei Li et al., On the Effects of Data Scale on UI Control Agents, NIPS'24, [Paper](https://arxiv.org/abs/2406.03679)


### Empirical Study

[1] Antoine Chevrot et al., Are Autonomous Web Agents Good Testers?, ISSTA'25, [Paper](https://arxiv.org/abs/2504.01495)


GUI Understanding
-----------------

### Dataset

[1] Sidong Feng et al., MUD: Towards a Large-Scale and Noise-Filtered UI Dataset for Modern Style UI Modeling, CHI'24, [Paper](https://arxiv.org/abs/2405.07090)


### Tool

[1] Hu Yongxiang et al., Appaction: Automatic GUI Interaction for Mobile Apps via Holistic Widget Perception, FSE'23 Industry, [Paper](https://dl.acm.org/doi/pdf/10.1145/3611643.3613885)

[2] Ziwei Wang et al., MP-GUI: Modality Perception with MLLMs for GUI Understanding, CVPR'25, [Paper](https://arxiv.org/abs/2503.14021)

[3] Dehai Zhao et al., SeeAction: Towards Reverse Engineering How-What-Where of HCI Actions from Screencasts for UI Automation, ICSE'25, [Paper](https://arxiv.org/abs/2503.12873)

[4] Wei Liu et al., GUIWatcher: Automatically Detecting GUI Lags by Analyzing Mobile Application Screencasts, ICSE'25 Industry, [Paper](https://arxiv.org/abs/2502.04202)


Functional Bugs
---------------

### Empirical Study (ISSTA'23)

[1] Xiong Yiheng et al., An Empirical Study of Functional Bugs in Android Apps, ISSTA'23, [Paper](https://dl.acm.org/doi/pdf/10.1145/3597926.3598138)


### App-specific Bugs

[1] Ting Su et al., Fully Automated Functional Fuzzing of Android Apps for Detecting Non-crashing Logic Bugs, OOPSLA'21, [Paper](https://arxiv.org/abs/2008.03585)

[2] Yiheng Xiong et al., General and Practical Property-based Testing for Android Apps, ASE'24. [Paper](https://ieeexplore.ieee.org/document/10764962)

[3] Yongxiang Hu et al., KuiTest: Leveraging Knowledge in the Wild as GUI Testing Oracle for Mobile Apps, ICSE'25 Industry. [Paper](https://ieeexplore.ieee.org/document/11121717)

[4] Ruofan Liu et al., GUIPilot: A Consistency-based Mobile GUI Testing Approach for Detecting Application-specific Bugs, ISSTA'25, [Paper](https://arxiv.org/abs/2506.07385)


### Display Bugs

[1] Yongxiang Hu et al., Minuku: Detecting Diverse Display Issues in Mobile Apps with Small-scale Dataset, ASE'25 Industry.

### Various Bug Types

[1] Jiajun Hu et al., ωTest: WebView-Oriented Testing for Android Applications, ISSTA'23, [Paper](https://arxiv.org/abs/2306.03845)

[2] Yongxiang Hu et al., AutoConsis: Automatic GUI-driven Data Inconsistency Detection of Mobile Apps, ICSE'24 Industry. [Paper](https://ieeexplore.ieee.org/document/10554689)

[3] Fan Fu et al., An Empirical Study on Common Sense-Violating Bugs in Mobile Apps, TOSEM'25, [Paper](https://dl.acm.org/doi/pdf/10.1145/3709356)

[4] Chenkai Guo et al., EP-Detector: Automatic Detection of Error-prone Operation Anomalies in Android Applications, ICSE'25. [Paper](https://ieeexplore.ieee.org/document/11029849)

### Accessibility

#### BLV Users

[1] Liu Zhe et al., Unblind Text Inputs: Predicting Hint-text of Text Input in Mobile Apps via LLM, CHI'24, [Paper](https://dl.acm.org/doi/pdf/10.1145/3613904.3642939)

[2] Zhang Mengxi et al., Distinguishing GUI Component States for Blind Users using Large Language Models, TOSEM'25, [Paper](https://dl.acm.org/doi/pdf/10.1145/3722106)


#### A11y Testing

[1] Yuxin Zhang et al., Scenario-Driven and Context-Aware Automated Accessibility Testing for Android Apps, ICSE'25. [Paper](https://ieeexplore.ieee.org/document/11029746)

Random Testing
--------------

### Coverage

[1] Ran Dezhi et al., Automated Visual Testing for Mobile Apps in an Industrial Setting, ICSE'22 Industry, [Paper](https://dl.acm.org/doi/pdf/10.1145/3510457.3513027)

[2] Han Hu et al., Enhancing GUI Exploration Coverage of Android Apps with Deep Link-Integrated Monkey, TOSEM'24, [Paper](https://arxiv.org/abs/2404.19307)


### Efficiency

[1] Lu Yifei et al., Improving Test Efficacy for Large-Scale Android Applications by Exploiting GUI and Functional Equivalence, TOSEM'25, [Paper](https://dl.acm.org/doi/pdf/10.1145/3729225)


### LLM-assisted Testing

[1] Zhe Liu et al., Fill in the Blank: Context-Aware Automated Text Input Generation for Mobile GUI Testing, ICSE'23, [Paper](https://arxiv.org/abs/2212.04732)

[2] Zhe Liu et al., Make LLM a Testing Expert: Bringing Human-like Interaction to Mobile GUI Testing via Functionality-aware Decisions, ICSE'24, [Paper](https://arxiv.org/abs/2310.15780)

[3] Wang Chenxu et al., LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance, FSE'25, [Paper](https://dl.acm.org/doi/pdf/10.1145/3715763)

[4] Chen Mengzhuo et al., Standing on the Shoulders of Giants: Bug-Aware Automated GUI Testing via Retrieval Augmentation, FSE'25, [Paper](https://dl.acm.org/doi/pdf/10.1145/3715755)


Model-based Testing
-------------------

### UTG

[1] Sen Chen et al., StoryDroid: Automated Generation of Storyboard for Android Apps, ICSE'19, [Paper](https://arxiv.org/abs/1902.00476)

[2] Xiangyu Zhang et al., Scene-Driven Exploration and GUI Modeling for Android Apps, ASE'23, [Paper](https://arxiv.org/abs/2308.10228)

[3] Yanchen Lu et al., TacDroid: Detection of Illicit Apps through Hybrid Analysis of UI-based Transition Graphs, ICSE'25. [Paper](https://shhaos.github.io/papers/icse25.pdf)

Test Case Management
--------------------

### Test Case Generation

[1] Parsa Alian et al., Feature-Driven End-To-End Test Generation, ICSE'25, [Paper](https://arxiv.org/abs/2408.01894)


### Test Case Transfer

[1] Benyamin Beyzaei et al., Automated Test Transfer across Android Apps using Large Language Models, ISSTA'25, [Paper](https://arxiv.org/abs/2411.17933)


UI2Code
-------

### DL Methods

### LLM-based Methods

[1] Fan Wu et al., MLLM-Based UI2Code Automation Guided by UI Layout Information, ISSTA'25, [Paper](https://arxiv.org/abs/2506.10376)

