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
    - [Navigation VLMs](#navigation-vlms)
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
  - [Empirical Study](#empirical-study-issta23)
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

* Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception. [Paper](https://arxiv.org/abs/2401.16158) [Repo](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v1)

#### Agent Knowledge

* **[MobiCom'24]** AutoDroid: LLM-powered Task Automation in Android. [Paper](https://arxiv.org/abs/2308.15272)
* **[MobiCom'24]** MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation. [Paper](https://dl.acm.org/doi/pdf/10.1145/3636534.3690682)
* **[UIST'24]** GPTVoiceTasker: Advancing Multi-step Mobile Task Efficiency Through Dynamic Interface Exploration and Learning. [Paper](https://arxiv.org/abs/2401.14268)
* **[MM'25]** PG-Agent: An Agent Powered by Page Graph. [Paper](https://arxiv.org/abs/2509.03536)
* **[CHI'25]** AppAgent: Multimodal Agent as Smartphone Users. [Paper](https://arxiv.org/abs/2312.13771) [Repo](https://github.com/TencentQQGYLab/AppAgent)
* **[ACL'25]** GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent. [Paper](https://arxiv.org/abs/2505.16827)

#### Agent for A11y

* **[UIST'25]** Morae: Proactively Pausing UI Agents for User Choices. [Paper](https://dl.acm.org/doi/pdf/10.1145/3746059.3747797)

#### Multi-agent

* **[NIPS'24]** Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration. [Paper](https://arxiv.org/abs/2406.01014) [Repo](https://github.com/X-PLUG/MobileAgent/tree/main/Mobile-Agent-v2)
* **[ICLR'25 Workshop]** PC-Agent: A Hierarchical Multi-Agent Collaboration Framework for Complex Task Automation on PC. [Paper](https://arxiv.org/abs/2502.14282) [Repo](https://github.com/X-PLUG/MobileAgent/tree/main/PC-Agent)
* Fairy: Interactive Mobile Assistant to Real-world Tasks via LMM-based Multi-agent. [Paper](https://arxiv.org/abs/2509.20729)

### GUI Test Execution

#### Crash

* **[ISSTA'24]** Guardian: A Runtime Framework for LLM-Based UI Exploration. [Paper](https://dl.acm.org/doi/pdf/10.1145/3650212.3680334)
* **[ASE'24 Industry]** Enabling Cost-Effective UI Automation Testing with Retrieval-Based LLMs: A Case Study in WeChat. [Paper](https://arxiv.org/abs/2409.07829)
* **[FSE'25 Industry]** ProphetAgent: Automatically Synthesizing GUI Tests from Test Cases in Natural Language for Mobile Apps. [Paper](https://dl.acm.org/doi/pdf/10.1145/3696630.3728543)
* **[ICSE'25 Industry]** Agent for User: Testing Multi-User Interactive Features in TikTok. [Paper](https://arxiv.org/abs/2504.15474)
* **[ICSE'26]** Breaking Single-Tester Limits: Multi-Agent LLMs for Multi-User Feature Testing. [Paper](https://arxiv.org/abs/2506.17539)
* **[ASE'25 Industry]** From Redundancy to Efficiency: Exploiting Shared UI Interactions towards Efficient LLM-Based Testing.

#### Functional Bugs

* **[CHI'24]** AXNav: Replaying Accessibility Tests from Natural Language. [Paper](https://arxiv.org/abs/2310.02424)
* **[TSE'25]** Seeing is Believing: Vision-driven Non-crash Functional Bug Detection for Mobile Apps. [Paper](https://arxiv.org/abs/2407.03037)
* AUITestAgent: Automatic Requirements Oriented GUI Function Testing. [Paper](https://arxiv.org/abs/2407.09018) [Repo](https://github.com/bz-lab/AUITestAgent)
* **[FSE'25]** Automated Soap Opera Testing Directed by LLMs and Scenario Knowledge: Feasibility, Challenges, and Road Ahead. [Paper](https://arxiv.org/abs/2412.08581)

### Bug Report Reproduce

* **[ICSE'24]** Prompting Is All You Need: Automated Android Bug Replay with Large Language Models. [Paper](https://arxiv.org/abs/2306.01987)
* **[ICSE'24]** Enhancing Exploratory Testing by Large Language Model and Knowledge Graph. [Paper](https://dl.acm.org/doi/pdf/10.1145/3597503.3639157)
* **[ISSTA'24]** Feedback-Driven Automated Whole Bug Report Reproduction for Android Apps. [Paper](https://arxiv.org/abs/2407.05165)
* **[TSE'25]** One Sentence Can Kill the Bug: Auto-replay Mobile App Crashes from One-sentence Overviews. [Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10869838)

### VLMs for Downstream Tasks

#### Grounding VLMs

##### SFT

* **[ACL'24]** SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents. [Paper](https://arxiv.org/abs/2401.10935)
* **[ICLR'25]** OS-ATLAS: Foundation Action Model for Generalist GUI Agents. [Paper](https://arxiv.org/abs/2410.23218)
* **[ICLR'25]** Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents. [Paper](https://arxiv.org/abs/2410.05243)

##### RL

* **[AAAI'26]** UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning. [Paper](https://arxiv.org/abs/2503.21620)
* GUI-G^2: Gaussian Reward Modeling for GUI Grounding. [Paper](https://arxiv.org/abs/2507.15846)
* UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning. [Paper](https://arxiv.org/abs/2510.20286)

#### Navigation VLMs

##### SFT

* **[CVPR'24]** CogAgent: A Visual Language Model for GUI Agents. [Paper](https://arxiv.org/abs/2312.08914)
* UI-TARS: Pioneering Automated GUI Interaction with Native Agents. [Paper](https://arxiv.org/abs/2501.12326)
* **[CVPR'25]** ShowUI: One Vision-Language-Action Model for GUI Visual Agent. [Paper](https://arxiv.org/abs/2411.17465)
* **[ASE'25 Industry]** Element-Aware Fine-Tuning of Vision-Language Models for Cost-Efficient GUI Testing in an Industrial Setting.

##### RL

* **[ISSTA'25 Workshop]** TestFlow: Advancing Mobile UI Testing through Multi-Step Reinforcement Learning. [Paper](https://dl.acm.org/doi/pdf/10.1145/3713081.3732930)
* **[NAACL'25]** ReachAgent: Enhancing Mobile Agent via Page Reaching and Operation. [Paper](https://arxiv.org/abs/2502.02955)
* UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning. [Paper](https://arxiv.org/abs/2509.02544)
* GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents. [Paper](https://arxiv.org/abs/2504.10458)
* **[NIPS'25]** BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent. [Paper](https://arxiv.org/abs/2509.15566)
* VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model. [Paper](https://arxiv.org/abs/2502.18906)

#### Training Data Generation

* **[EMNLP'20]** Widget Captioning: Generating Natural Language Description for Mobile User Interface Elements. [Paper](https://arxiv.org/abs/2010.04295)
* **[ACL'25 Findings]** Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents. [Paper](https://arxiv.org/abs/2502.11357)
* **[ICLR'25]** Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents in Realistic Environments. [Paper](https://arxiv.org/abs/2501.10893)

### Benchmark

#### Testbed

* **[UIST'24]** LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Task Automation. [Paper](https://arxiv.org/abs/2404.16054)

#### Grounding Benchmarks

* **[ACL'24]** SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents. [Paper](https://arxiv.org/abs/2401.10935)
* **[ICLR'25]** OS-ATLAS: Foundation Action Model for Generalist GUI Agents. [Paper](https://arxiv.org/abs/2410.23218)
* **[ICLR'25 Workshop]** Screenspot-pro: Gui grounding for professional high-resolution computer use. [Paper](https://arxiv.org/abs/2504.07981)

#### Navigation Benchmarks

* **[NIPS'23]** Android in the Wild: A Large-Scale Dataset for Android Device Control. [Paper](https://arxiv.org/abs/2307.10088)
* **[NIPS'23 Workshop]** WebArena: A Realistic Web Environment for Building Autonomous Agents. [Paper](https://arxiv.org/abs/2307.13854)
* **[NIPS'24]** OSWORLD: benchmarking multimodal agents for open-ended tasks in real computer environments. [Paper](https://arxiv.org/abs/2404.07972)
* **[ICCV'25]** GUIOdyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices. [Paper](https://arxiv.org/abs/2406.08451)
* **[ICLR'25]** AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents. [Paper](https://arxiv.org/abs/2405.14573)

#### Mixed Benchmarks

* **[ECCV'24]** OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web. [Paper](https://arxiv.org/abs/2402.17553)
* **[NIPS'24]** On the Effects of Data Scale on UI Control Agents. [Paper](https://arxiv.org/abs/2406.03679)

### Empirical Study

* **[ISSTA'25]** Are Autonomous Web Agents Good Testers?. [Paper](https://arxiv.org/abs/2504.01495)

GUI Understanding
-----------------

### Dataset

* **[CHI'24]** MUD: Towards a Large-Scale and Noise-Filtered UI Dataset for Modern Style UI Modeling. [Paper](https://arxiv.org/abs/2405.07090)

### Tool

* **[FSE'23 Industry]** Appaction: Automatic GUI Interaction for Mobile Apps via Holistic Widget Perception. [Paper](https://dl.acm.org/doi/pdf/10.1145/3611643.3613885)
* **[CVPR'25]** MP-GUI: Modality Perception with MLLMs for GUI Understanding. [Paper](https://arxiv.org/abs/2503.14021)
* **[ICSE'25]** SeeAction: Towards Reverse Engineering How-What-Where of HCI Actions from Screencasts for UI Automation. [Paper](https://arxiv.org/abs/2503.12873)
* **[ICSE'25 Industry]** GUIWatcher: Automatically Detecting GUI Lags by Analyzing Mobile Application Screencasts. [Paper](https://arxiv.org/abs/2502.04202)

Functional Bugs
---------------

### Empirical Study (ISSTA'23)

* **[ISSTA'23]** An Empirical Study of Functional Bugs in Android Apps. [Paper](https://dl.acm.org/doi/pdf/10.1145/3597926.3598138)

### App-specific Bugs

* **[OOPSLA'21]** Fully Automated Functional Fuzzing of Android Apps for Detecting Non-crashing Logic Bugs. [Paper](https://arxiv.org/abs/2008.03585)
* **[ASE'24]** General and Practical Property-based Testing for Android Apps. [Paper](https://ieeexplore.ieee.org/document/10764962)
* **[ICSE'25 Industry]** KuiTest: Leveraging Knowledge in the Wild as GUI Testing Oracle for Mobile Apps. [Paper](https://ieeexplore.ieee.org/document/11121717)
* **[ISSTA'25]** GUIPilot: A Consistency-based Mobile GUI Testing Approach for Detecting Application-specific Bugs. [Paper](https://arxiv.org/abs/2506.07385)

### Display Bugs

* **[ASE'25 Industry]** Minuku: Detecting Diverse Display Issues in Mobile Apps with Small-scale Dataset.

### Various Bug Types

* **[ISSTA'23]** ωTest: WebView-Oriented Testing for Android Applications. [Paper](https://arxiv.org/abs/2306.03845)
* **[ICSE'24 Industry]** AutoConsis: Automatic GUI-driven Data Inconsistency Detection of Mobile Apps. [Paper](https://ieeexplore.ieee.org/document/10554689)
* **[TOSEM'25]** An Empirical Study on Common Sense-Violating Bugs in Mobile Apps. [Paper](https://dl.acm.org/doi/pdf/10.1145/3709356)
* **[ICSE'25]** EP-Detector: Automatic Detection of Error-prone Operation Anomalies in Android Applications. [Paper](https://ieeexplore.ieee.org/document/11029849)

### Accessibility

#### BLV Users

* **[CHI'24]** Unblind Text Inputs: Predicting Hint-text of Text Input in Mobile Apps via LLM. [Paper](https://dl.acm.org/doi/pdf/10.1145/3613904.3642939)
* **[TOSEM'25]** Distinguishing GUI Component States for Blind Users using Large Language Models. [Paper](https://dl.acm.org/doi/pdf/10.1145/3722106)

#### A11y Testing

* **[ICSE'25]** Scenario-Driven and Context-Aware Automated Accessibility Testing for Android Apps. [Paper](https://ieeexplore.ieee.org/document/11029746)

Random Testing
--------------

### Coverage

* **[ICSE'22 Industry]** Automated Visual Testing for Mobile Apps in an Industrial Setting. [Paper](https://dl.acm.org/doi/pdf/10.1145/3510457.3513027)
* **[TOSEM'24]** Enhancing GUI Exploration Coverage of Android Apps with Deep Link-Integrated Monkey. [Paper](https://arxiv.org/abs/2404.19307)

### Efficiency

* **[TOSEM'25]** Improving Test Efficacy for Large-Scale Android Applications by Exploiting GUI and Functional Equivalence. [Paper](https://dl.acm.org/doi/pdf/10.1145/3729225)

### LLM-assisted Testing

* **[ICSE'23]** Fill in the Blank: Context-Aware Automated Text Input Generation for Mobile GUI Testing. [Paper](https://arxiv.org/abs/2212.04732)
* **[ICSE'24]** Make LLM a Testing Expert: Bringing Human-like Interaction to Mobile GUI Testing via Functionality-aware Decisions. [Paper](https://arxiv.org/abs/2310.15780)
* **[FSE'25]** LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance. [Paper](https://dl.acm.org/doi/pdf/10.1145/3715763)
* **[FSE'25]** Standing on the Shoulders of Giants: Bug-Aware Automated GUI Testing via Retrieval Augmentation. [Paper](https://dl.acm.org/doi/pdf/10.1145/3715755)

Model-based Testing
-------------------

### UTG

* **[ICSE'19]** StoryDroid: Automated Generation of Storyboard for Android Apps. [Paper](https://arxiv.org/abs/1902.00476)
* **[ASE'23]** Scene-Driven Exploration and GUI Modeling for Android Apps. [Paper](https://arxiv.org/abs/2308.10228)
* **[ICSE'25]** TacDroid: Detection of Illicit Apps through Hybrid Analysis of UI-based Transition Graphs. [Paper](https://shhaos.github.io/papers/icse25.pdf)

Test Case Management
--------------------

### Test Case Generation

* **[ICSE'25]** Feature-Driven End-To-End Test Generation. [Paper](https://arxiv.org/abs/2408.01894)

### Test Case Transfer

* **[ISSTA'25]** Automated Test Transfer across Android Apps using Large Language Models. [Paper](https://arxiv.org/abs/2411.17933)

UI2Code
-------

### DL Methods

### LLM-based Methods

* **[ISSTA'25]** MLLM-Based UI2Code Automation Guided by UI Layout Information. [Paper](https://arxiv.org/abs/2506.10376)
