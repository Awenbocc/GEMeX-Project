# <a href="https://arxiv.org/abs/2411.16778" target="_blank"><div style="width: 65px; height: 65px; vertical-align: middle;"><img src="./imgs/favicon.ico" alt="Image Alt Text" width="36" />GEMeX: A Large-Scale, Groundable, and Explainable Medical VQA Benchmark for Chest X-ray Diagnosis</div></a>


![GEMeX Display](assets/gemex.gif)

## Update

- [2024/12/01] We release part of data and complete training code.
- [2025/01/17] We release pre-trained [LLaVA-Med-GEMeX](https://huggingface.co/BoKelvin/GEMeX-VQA-Model-Simple), a simple baseline model based on GEMeX VQA data.


## How to fine-tune:
```bash
git clone https://github.com/Awenbocc/GEMeX-Project.git
cd llava-med
bash fine_tune_gemex.sh # modify data location
```



