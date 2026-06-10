<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=mahin-aeroai&color=blueviolet&style=flat-square&label=Profile+Views)

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Waving%20Hand.png" alt="Waving Hand" width="60" />

# Hi, I'm Mahin

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=6E40C9&center=true&vCenter=true&random=false&width=700&lines=AI+%26+ML+Engineer+%7C+Aerospace+Background;LLM+Evaluation+%7C+RAG+Pipelines+%7C+Fine-Tuning;84%25+Spider+Accuracy+%7C+72%25+CodeBLEU;Building+Production+AI+Systems+from+Scratch+%F0%9F%9A%80)](https://git.io/typing-svg)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mahin_Nandipa-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mahin-nandipa-58189b392)
[![Medium](https://img.shields.io/badge/Medium-@mahin.nandipa-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@mahin.nandipa)
[![YouTube](https://img.shields.io/badge/YouTube-@mahinnandipa3049-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@mahinnandipa3049)

</div>

---

## 🚀 About Me

I'm an **AI/ML Engineer** with a B.Tech in Aerospace Engineering and a PG Certification in AI & ML from **IIIT Hyderabad** (TalentSprint × Accenture). I build production-grade LLM systems — from Text-to-SQL pipelines to RAG-augmented code generation — and have an engineering background that spans physical hardware builds to deep learning fine-tuning.

- 🎓 **PG Cert — AI & ML** · IIITH × TalentSprint × Accenture *(Sep 2025 – Present)*
- 🎓 **B.Tech — Aerospace Engineering** · VIT Bhopal · **CGPA 8.23 / 10** *(2021–2025)*
- 📍 Hyderabad, India
- 🔭 Currently: LLM benchmarking, RAG pipelines, LoRA fine-tuning on codegen-350M
- 🛸 Past: Built and flew a complete drone system at Dautya Aerospace (11 months)
- 🧠 Currently obsessed with: Reinforcement Learning for autonomous flight & Swarm Intelligence
- ✍️ Writing about AI & aerospace on [Medium](https://medium.com/@mahin.nandipa)
- 🌍 Mission: Democratise autonomous aerospace technology through open-source and education

---

## 🏗️ Featured Projects

### 🤖 BI Copilot — Personal Project · 2026
> **Natural Language → SQL → Live Chart → NL Insight · FastAPI + Streamlit deployed**

| Metric | Score |
|--------|-------|
| 🎯 Spider Execution Accuracy | **84%** |
| 🎯 BirdBench Execution Accuracy | **67%** |
| ⚡ p90 Latency | **< 3 seconds** |
| 🔁 LLM Retry Success Rate | **91%** |

Built a schema-aware RAG pipeline (FAISS-indexed table/column definitions, top-3 retrieval) — **+33pp over no-schema baseline**, +11pp over full-schema prompting. 5-stage pipeline: query understanding → schema RAG → CoT SQL generation → syntax validation + retry loop → auto Plotly chart + NL summary. Conversational memory (5-turn rolling window), read-only enforcement, prompt injection prevention.

`Python` `LangChain` `FAISS` `FastAPI` `Streamlit` `Plotly` `Docker` `SQLAlchemy`

---

### 🧠 CodeGen RAG System — IIITH AIML PGCP Capstone · Group 39 · 2025–26
> **Evaluating and enhancing codegen-350M-multi with retrieval augmentation and LoRA fine-tuning**
> Supervised by Prof. Anil Neelkanti · Team: Mahin Nandipa, Ashu Bagul, Abhinaya Thavishi

| Task | Baseline | RAG | Delta |
|------|----------|-----|-------|
| CodeBLEU | 38% | **72%** | **+34pp** |
| Spider EX (Text-to-SQL) | — | **78%** | — |
| New Language (LoRA FT) | 0% | **38%** | From zero |

FAISS RAG pipeline using 512-dim codegen encoder outputs. Top-K ablation (K=1,3,5,10) → **K=3 optimal**. Hybrid token-embedding + AST retrieval achieves 74% CodeBLEU. LoRA fine-tune: r=16, α=32, **0.07% trainable params**, <2pp catastrophic forgetting with 15% source mixing.

`HuggingFace` `FAISS` `LoRA/PEFT` `WandB` `FastAPI` `CodeBLEU` `BERTScore` `Spider` `BirdBench`

---

### 🛸 Acoustic Anti-Drone Detection System — B.Tech Thesis · May 2025
> **End-to-end hardware build · 64-page published report · Supervised by Dr. Prashant GK, VIT Bhopal**

Designed and physically built a full drone detection system: sound sensor + ultrasonic sensor + MAX9814 amplifier + servo-sweep 180° radar + SD card WAV recording. Two-stage precheck/postcheck pipeline. Arduino + Processing IDE real-time radar display. Audacity noise-gate DSP to isolate drone propeller acoustic signatures.

`Arduino UNO/Nano` `MAX9814 Amplifier` `Audacity DSP` `Fusion 360 CAD` `Processing IDE`

---

## 🛠️ Tech Stack

### 🤖 AI / ML
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![HuggingFace](https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge)](https://huggingface.co/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge)](https://langchain.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)

### 🚀 Deploy / Infra
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://kernel.org/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)

### ✈️ Aerospace & Robotics
[![ROS2](https://img.shields.io/badge/ROS2-22314E?style=for-the-badge&logo=ros&logoColor=white)](https://docs.ros.org/)
[![Gazebo](https://img.shields.io/badge/Gazebo-FF6600?style=for-the-badge)](https://gazebosim.org/)
[![PX4](https://img.shields.io/badge/PX4-0050FF?style=for-the-badge)](https://px4.io/)
[![MAVLink](https://img.shields.io/badge/MAVLink-0099CC?style=for-the-badge)](https://mavlink.io/)
[![MATLAB](https://img.shields.io/badge/MATLAB-FF6F00?style=for-the-badge)](https://www.mathworks.com/)
[![SolidWorks](https://img.shields.io/badge/SolidWorks-CC0000?style=for-the-badge)](https://www.solidworks.com/)
[![ANSYS](https://img.shields.io/badge/ANSYS-FFB71B?style=for-the-badge)](https://www.ansys.com/)
[![CATIA](https://img.shields.io/badge/CATIA-005386?style=for-the-badge)](https://www.3ds.com/products/catia/)

### 🔧 Embedded & Hardware
[![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white)](https://www.arduino.cc/)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white)](https://www.raspberrypi.com/)
[![NVIDIA Jetson](https://img.shields.io/badge/NVIDIA%20Jetson-76B900?style=for-the-badge&logo=nvidia&logoColor=white)](https://developer.nvidia.com/embedded-computing)
[![STM32](https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)](https://www.st.com/)

### 🗄️ Databases & Tools
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)

### 💻 Programming Languages
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)](https://isocpp.org/)
[![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://www.oracle.com/java/)
[![MATLAB](https://img.shields.io/badge/MATLAB-FF6F00?style=for-the-badge)](https://www.mathworks.com/)

### 🧩 Specialisations
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://en.wikipedia.org/wiki/Deep_learning)
[![Computer Vision](https://img.shields.io/badge/Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Reinforcement Learning](https://img.shields.io/badge/Reinforcement%20Learning-7B2FBE?style=for-the-badge&logoColor=white)](https://en.wikipedia.org/wiki/Reinforcement_learning)
[![SLAM](https://img.shields.io/badge/SLAM-00BFFF?style=for-the-badge&logoColor=white)](https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping)
[![Sensor Fusion](https://img.shields.io/badge/Sensor%20Fusion-FF6347?style=for-the-badge&logoColor=white)](https://en.wikipedia.org/wiki/Sensor_fusion)
[![GNC](https://img.shields.io/badge/GNC-4169E1?style=for-the-badge&logoColor=white)](https://en.wikipedia.org/wiki/Guidance,_navigation,_and_control)
[![Autonomous Navigation](https://img.shields.io/badge/Autonomous%20Navigation-32CD32?style=for-the-badge&logoColor=white)](https://en.wikipedia.org/wiki/Autonomous_robot)
[![Swarm Intelligence](https://img.shields.io/badge/Swarm%20Intelligence-FFD700?style=for-the-badge&logoColor=black)](https://en.wikipedia.org/wiki/Swarm_intelligence)

---

## 📊 GitHub Stats

<div align="center">

![Mahin's GitHub Stats](https://github-readme-stats-sigma-five.vercel.app/api?username=mahin-aeroai&show_icons=true&theme=tokyonight&hide_border=true&count_private=true)
&nbsp;
![Top Languages](https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=mahin-aeroai&layout=compact&theme=tokyonight&hide_border=true&langs_count=8)

</div>

---

## 🌐 Find Me Online

<div align="center">

[![YouTube](https://img.shields.io/badge/YouTube-@mahinnandipa3049-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@mahinnandipa3049)
[![Medium](https://img.shields.io/badge/Medium-@mahin.nandipa-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@mahin.nandipa)
[![Instagram](https://img.shields.io/badge/Instagram-@ecstamyn.cosride-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ecstamyn.cosride)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mahin_Nandipa-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mahin-nandipa-58189b392)

</div>

---

## 🤝 Let's Connect

<div align="center">

I'm open to **AI/ML engineering roles**, **LLM application development**, **research collaborations**, and **aerospace × AI projects**.

📧 mahin.nandipa@gmail.com |  m.nandipa@icloud.com

---

*"The sky is not the limit — it's just the beginning."* 🚀

**Mahin Nandipa** | Aerospace Engineer × AI/ML Specialist

</div>
