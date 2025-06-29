# <a href="https://arxiv.org/abs/2411.16778" target="_blank"><div style="width: 65px; height: 65px; vertical-align: middle;"><img src="./imgs/favicon.ico" alt="Image Alt Text" width="36" />GEMeX: A Large-Scale, Groundable, and Explainable Medical VQA Benchmark for Chest X-ray Diagnosis</div></a>


![GEMeX Display](assets/gemex.gif)

## News
- [2025/06/28] 🧠 Building on **GEMeX**, we now introduce [**ThinkVG**](https://arxiv.org/pdf/2506.17939), which helps LVLMs **think** while perform **visually grounding**. 
- [2025/06/26] 🎉 **Great News!** Our paper has been accepted to **ICCV 2025**!
- [2025/01/17] We release pre-trained [LLaVA-Med-GEMeX](https://huggingface.co/BoKelvin/GEMeX-VQA-Model-Simple), a simple baseline model based on GEMeX VQA data.
- [2024/12/01] We release part of data and complete training code.



## How to fine-tune:
```bash
git clone https://github.com/Awenbocc/GEMeX-Project.git
cd llava-med
bash fine_tune_gemex.sh # modify data location
```



