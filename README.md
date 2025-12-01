# Awesome-SE-Paper 📚

- [GUI Agents](#gui-agents-🤖)
  - [GUI Assistant](#gui-assistant-🧑‍💻)
    - [GUI Understanding](#gui-understanding-👁️)
    - [Agent Knowledge](#agent-knowledge-🧠)
    - [Agent for A11y](#agent-for-a11y-♿)
    - [Multi-agent](#multi-agent-👥)
  - [GUI Test Execution](#gui-test-execution-🔧)
    - [Crash](#crash-💥)
    - [Functional Bugs](#functional-bugs-🐛)
  - [Bug Report Reproduce](#bug-report-reproduce-🔁)
  - [VLMs for Downstream Tasks](#vlms-for-downstream-tasks-🌐)
    - [Grounding VLMs](#grounding-vlms-📍)
    - [Navigation VLMs](#navigation-vlms-🧭)
    - [Training Data Generation](#training-data-generation-📈)
  - [Benchmark](#benchmark-📊)
    - [Testbed](#testbed-🧪)
    - [Grounding Benchmarks](#grounding-benchmarks-🎯)
    - [Navigation Benchmarks](#navigation-benchmarks-🗺️)
    - [Mixed Benchmarks](#mixed-benchmarks-🔀)
  - [Empirical Study](#empirical-study-📈)
- [GUI Understanding](#gui-understanding-👁️‍🗨️)
  - [Dataset](#dataset-📊)
  - [Tool](#tool-🔧)
- [Functional Bugs](#functional-bugs-🚫)
  - [Empirical Study](#empirical-study-📊)
  - [App-specific Bugs](#app-specific-bugs-📱)
  - [Display Bugs](#display-bugs-🖥️)
  - [Various Bug Types](#various-bug-types-🔍)
  - [Accessibility](#accessibility-♿)
- [Random Testing](#random-testing-🎲)
  - [Coverage](#coverage-📊)
  - [Efficiency](#efficiency-⚡)
  - [LLM-assisted Testing](#llm-assisted-testing-🤖)
- [Model-based Testing](#model-based-testing-📐)
  - [UTG](#utg-🕸️)
- [Test Case Management](#test-case-management-📋)
  - [Test Case Generation](#test-case-generation-📝)
  - [Test Case Transfer](#test-case-transfer-↔️)
- [UI2Code](#ui2code-🎨)
  - [DL Methods](#dl-methods-🧠)
  - [LLM-based Methods](#llm-based-methods-💬)

---

## GUI Agents 🤖

### GUI Assistant 🧑‍💻

#### GUI Understanding 👁️

* **Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception**. [Paper]()

#### Agent Knowledge 🧠

##### UTG 🕸️

* **[MobiCom'24]** AutoDroid: LLM-powered Task Automation in Android. [Paper]()
* **[UIST'24]** GPTVoiceTasker: Advancing Multi-step Mobile Task Efficiency Through Dynamic Interface Exploration and Learning. [Paper]()
* **[MM'25]** PG-Agent: An Agent Powered by Page Graph. [Paper]()

##### RAG 📚

* **[CHI'25]** AppAgent: Multimodal Agent as Smartphone Users. [Paper]()
* **[MobiCom'24]** MobileGPT: Augmenting LLM with Human-like App Memory for Mobile Task Automation. [Paper]()
* **[ACL'25]** GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent. [Paper]()

#### Agent for A11y ♿

* **[UIST'25]** Morae: Proactively Pausing UI Agents for User Choices. [Paper]()

#### Multi-agent 👥

* **[NIPS'24]** Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration. [Paper]()
* **[ICLR'25 Workshop]** PC-Agent: A Hierarchical Multi-Agent Collaboration Framework for Complex Task Automation on PC. [Paper]()
* **Fairy: Interactive Mobile Assistant to Real-world Tasks via LMM-based Multi-agent**. [Paper]()

### GUI Test Execution 🔧

#### Crash 💥

* **[ISSTA'24]** Guardian: A Runtime Framework for LLM-Based UI Exploration. [Paper]()
* **[ASE'24 Industry]** Enabling Cost-Effective UI Automation Testing with Retrieval-Based LLMs: A Case Study in WeChat. [Paper]()
* **[FSE'25 Industry]** ProphetAgent: Automatically Synthesizing GUI Tests from Test Cases in Natural Language for Mobile Apps. [Paper]()
* **[ICSE'25 Industry]** Agent for User: Testing Multi-User Interactive Features in TikTok. [Paper]()
* **[ICSE'26]** Breaking Single-Tester Limits: Multi-Agent LLMs for Multi-User Feature Testing. [Paper]()
* **[ASE'25 Industry]** From Redundancy to Efficiency: Exploiting Shared UI Interactions towards Efficient LLM-Based Testing. [Paper]()

#### Functional Bugs 🐛

* **[CHI'24]** AXNav: Replaying Accessibility Tests from Natural Language. [Paper]()
* **[TSE'25]** Seeing is Believing: Vision-driven Non-crash Functional Bug Detection for Mobile Apps. [Paper]()
* **AUITestAgent: Automatic Requirements Oriented GUI Function Testing**. [Paper]()
* **[FSE'25]** Automated Soap Opera Testing Directed by LLMs and Scenario Knowledge: Feasibility, Challenges, and Road Ahead. [Paper]()

### Bug Report Reproduce 🔁

* **[ICSE'24]** Prompting Is All You Need: Automated Android Bug Replay with Large Language Models. [Paper]()
* **[ICSE'24]** Enhancing Exploratory Testing by Large Language Model and Knowledge Graph. [Paper]()
* **[ISSTA'24]** Feedback-Driven Automated Whole Bug Report Reproduction for Android Apps. [Paper]()
* **[TSE'25]** One Sentence Can Kill the Bug: Auto-replay Mobile App Crashes from One-sentence Overviews. [Paper]()

### VLMs for Downstream Tasks 🌐

#### Grounding VLMs 📍

##### SFT

* **[ACL'24]** SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents. [Paper]()
* **[ICLR'25]** OS-ATLAS: Foundation Action Model for Generalist GUI Agents. [Paper]()
* **[ICLR'25]** Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents. [Paper]()

##### RL

* **[AAAI'26]** UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning. [Paper]()
* **GUI-G^2: Gaussian Reward Modeling for GUI Grounding**. [Paper]()
* **UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning**. [Paper]()

#### Navigation VLMs 🧭

##### SFT

* **[CVPR'24]** CogAgent: A Visual Language Model for GUI Agents. [Paper]()
* **UI-TARS: Pioneering Automated GUI Interaction with Native Agents**. [Paper]()
* **[CVPR'25]** ShowUI: One Vision-Language-Action Model for GUI Visual Agent. [Paper]()
* **[ASE'25 Industry]** Element-Aware Fine-Tuning of Vision-Language Models for Cost-Efficient GUI Testing in an Industrial Setting. [Paper]()

##### RL

* **[ISSTA'25 Workshop]** TestFlow: Advancing Mobile UI Testing through Multi-Step Reinforcement Learning. [Paper]()
* **[NAACL'25]** ReachAgent: Enhancing Mobile Agent via Page Reaching and Operation. [Paper]()
* **UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning**. [Paper]()
* **GUI-R1: A Generalist R1-Style Vision-Language Action Model For GUI Agents**. [Paper]()
* **[NIPS'25]** BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent. [Paper]()
* **VEM: Environment-Free Exploration for Training GUI Agent with Value Environment Model**. [Paper]()

#### Training Data Generation 📈

* **[EMNLP'20]** Widget Captioning: Generating Natural Language Description for Mobile User Interface Elements. [Paper]()
* **[ACL'25 Findings]** Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web Agents. [Paper]()
* **[ICLR'25]** Learn-by-interact: A Data-Centric Framework for Self-Adaptive Agents in Realistic Environments. [Paper]()

### Benchmark 📊

#### Testbed 🧪

* **[UIST'24]** LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Task Automation. [Paper]()

#### Grounding Benchmarks 🎯

* **[ACL'24]** SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents. [Paper]()
* **[ICLR'25]** OS-ATLAS: Foundation Action Model for Generalist GUI Agents. [Paper]()
* **[ICLR'25 Workshop]** Screenspot-pro: Gui grounding for professional high-resolution computer use. [Paper]()

#### Navigation Benchmarks 🗺️

* **[NIPS'23]** Android in the Wild: A Large-Scale Dataset for Android Device Control. [Paper]()
* **[NIPS'23 Workshop]** WebArena: A Realistic Web Environment for Building Autonomous Agents. [Paper]()
* **[NIPS'24]** OSWORLD: benchmarking multimodal agents for open-ended tasks in real computer environments. [Paper]()
* **[ICCV'25]** GUIOdyssey: A Comprehensive Dataset for Cross-App GUI Navigation on Mobile Devices. [Paper]()
* **[ICLR'25]** AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents. [Paper]()

#### Mixed Benchmarks 🔀

* **[ECCV'24]** OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web. [Paper]()
* **[NIPS'24]** On the Effects of Data Scale on UI Control Agents. [Paper]()

### Empirical Study 📈

* **[ISSTA'25]** Are Autonomous Web Agents Good Testers?. [Paper]()

---

## GUI Understanding 👁️‍🗨️

### Dataset 📊

* **[CHI'24]** MUD: Towards a Large-Scale and Noise-Filtered UI Dataset for Modern Style UI Modeling. [Paper]()

### Tool 🔧

* **[FSE'23 Industry]** Appaction: Automatic GUI Interaction for Mobile Apps via Holistic Widget Perception. [Paper]()
* **[CVPR'25]** MP-GUI: Modality Perception with MLLMs for GUI Understanding. [Paper]()
* **[ICSE'25]** SeeAction: Towards Reverse Engineering How-What-Where of HCI Actions from Screencasts for UI Automation. [Paper]()
* **[ICSE'25 Industry]** GUIWatcher: Automatically Detecting GUI Lags by Analyzing Mobile Application Screencasts. [Paper]()

---

## Functional Bugs 🚫

### Empirical Study 📊

* **[ISSTA'23]** An Empirical Study of Functional Bugs in Android Apps. [Paper]()

### App-specific Bugs 📱

* **[OOPSLA'21]** Fully Automated Functional Fuzzing of Android Apps for Detecting Non-crashing Logic Bugs. [Paper]()
* **[ASE'24]** General and Practical Property-based Testing for Android Apps. [Paper]()
* **[ICSE'25 Industry]** KuiTest: Leveraging Knowledge in the Wild as GUI Testing Oracle for Mobile Apps. [Paper]()
* **[ISSTA'25]** GUIPilot: A Consistency-based Mobile GUI Testing Approach for Detecting Application-specific Bugs. [Paper]()

### Display Bugs 🖥️

* **[ASE'25 Industry]** Minuku: Detecting Diverse Display Issues in Mobile Apps with Small-scale Dataset. [Paper]()

### Various Bug Types 🔍

* **[ISSTA'23]** ωTest: WebView-Oriented Testing for Android Applications. [Paper]()
* **[ICSE'24 Industry]** AutoConsis: Automatic GUI-driven Data Inconsistency Detection of Mobile Apps. [Paper]()
* **[TOSEM'25]** An Empirical Study on Common Sense-Violating Bugs in Mobile Apps. [Paper]()
* **[ICSE'25]** EP-Detector: Automatic Detection of Error-prone Operation Anomalies in Android Applications. [Paper]()

### Accessibility ♿

#### BLV Users

* **[CHI'24]** Unblind Text Inputs: Predicting Hint-text of Text Input in Mobile Apps via LLM. [Paper]()
* **[TOSEM'25]** Distinguishing GUI Component States for Blind Users using Large Language Models. [Paper]()

#### A11y Testing

* **[ICSE'25]** Scenario-Driven and Context-Aware Automated Accessibility Testing for Android Apps. [Paper]()

---

## Random Testing 🎲

### Coverage 📊

* **[ICSE'22 Industry]** Automated Visual Testing for Mobile Apps in an Industrial Setting. [Paper]()
* **[TOSEM'24]** Enhancing GUI Exploration Coverage of Android Apps with Deep Link-Integrated Monkey. [Paper]()

### Efficiency ⚡

* **[TOSEM'25]** Improving Test Efficacy for Large-Scale Android Applications by Exploiting GUI and Functional Equivalence. [Paper]()

### LLM-assisted Testing 🤖

* **[ICSE'23]** Fill in the Blank: Context-Aware Automated Text Input Generation for Mobile GUI Testing. [Paper]()
* **[ICSE'24]** Make LLM a Testing Expert: Bringing Human-like Interaction to Mobile GUI Testing via Functionality-aware Decisions. [Paper]()
* **[FSE'25]** LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance. [Paper]()
* **[FSE'25]** Standing on the Shoulders of Giants: Bug-Aware Automated GUI Testing via Retrieval Augmentation. [Paper]()

---

## Model-based Testing 📐

### UTG 🕸️

* **[ICSE'19]** StoryDroid: Automated Generation of Storyboard for Android Apps. [Paper]()
* **[ASE'23]** Scene-Driven Exploration and GUI Modeling for Android Apps. [Paper]()
* **[ICSE'25]** TacDroid: Detection of Illicit Apps through Hybrid Analysis of UI-based Transition Graphs. [Paper]()

---

## Test Case Management 📋

### Test Case Generation 📝

* **[ICSE'25]** Feature-Driven End-To-End Test Generation. [Paper]()

### Test Case Transfer ↔️

* **[ISSTA'25]** Automated Test Transfer across Android Apps using Large Language Models. [Paper]()

---

## UI2Code 🎨

### DL Methods 🧠

### LLM-based Methods 💬

* **[ISSTA'25]** MLLM-Based UI2Code Automation Guided by UI Layout Information. [Paper]()
