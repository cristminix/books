# Synthetic Data Generation

Recent research has shown that the diversity of synthetic data plays an important role in improving downstream model performance (chen_diversity_2024,zhu2025bareleveragingbaselanguage). So we further evaluate VS on synthetic data generation, including incorrect synthetic data in Section [negative synthetic data](#negative-synthetic-data).

## Synthetic Data Generation Setup

We prompt two models, GPT-4.1 and Gemini-2.5-flash, with different prompting methods to generate N=1,000 synthetic competition math questions, with k=5 in each call. We use a small k to ensure the generation quality as it is a complex task. See Appendix [experiment prompt](#appendix-experiment-prompt) for the prompts. Then we use Qwen3-32B to generate their corresponding reasoning trajectory and answers, as the model is proficient on math benchmarks and capable of producing reliable reasoning traces. See Section [positive data](#appendix-positive-data) for more implementation detail.

## Fine-tuning on Synthetic Data

With this 1K synthetic dataset, we follow the SFT setting in LIMO (ye2025limoreasoning), an effective method to improve reasoning performance with small dataset size, and finetune the following models on this 1K dataset: Qwen2.5-7B, Qwen3-1.7B-Base, and Qwen3-4B-Base (qwen2025qwen25technicalreport, yang2025qwen3technicalreport).

## Benchmarks and Evaluation

We evaluate the fine-tuned models' downstream task performance on three widely used math benchmark datasets: MATH500 (hendrycksmath2021), OlympiadBench (he2024olympiadbench), and Minerva Math (lewkowycz2022solving), which cover a wide range of topics, including algebra, geometry, and competitive mathematics. We use `math_verify`[^1] for the evaluation.

[^1]: https://github.com/huggingface/Math-Verify

| Gen Model | GPT-4.1 | | | Gemini-2.5-Flash | | | |
|:----------|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| SFT Model | Qwen2.5-7B | Q3-1.7B-Base | Q3-4B-Base | Qwen2.5-7B | Q3-1.7B-Base | Q3-4B-Base | Average |
| Baseline | 27.2 | 30.5 | 40.7 | 27.2 | 30.5 | 40.7 | 32.8 |
| Direct | 26.1 | 31.4 | 34.5 | 24.9 | 29.5 | 36.9 | 30.6 |
| CoT | 30.1 | 32.5 | 39.4 | 27.6 | 32.1 | 40.5 | 33.7 |
| Sequence | 30.5 | 31.0 | 42.1 | 28.2 | 31.7 | 42.5 | 34.3 |
| Multi-Turn | 29.9 | 31.9 | 41.3 | 27.1 | 32.2 | 37.1 | 33.2 |
| *Our Methods* | | | | | | | |
| &nbsp;&nbsp;VS-Standard | 32.7 | 33.6 | 45.5 | 28.6 | 33.3 | 42.8 | 36.1 |
| &nbsp;&nbsp;VS-CoT | 33.4 | 33.7 | **45.9** | 29.4 | **35.8** | 43.4 | 36.9 |
| &nbsp;&nbsp;VS-Multi | **34.8** | **34.9** | 45.0 | **31.7** | 34.8 | **43.6** | **37.5** |

Table: Downstream accuracy averaged across MATH500, OlympiadBench and Minerva Math. "Gen Models" show the models used to generate the 1K synthetic questions. "SFT Models" are the ones used to finetune on the 1K synthetic data. VS and its variants improve the downstream tasks.

## Results

Table [synthetic_results](#synthetic-results) shows the average accuracy across the three datasets. VS and its variants improve the downstream performance on math tasks across the board, with VS-multi achieving the strongest average accuracy of 37.5%. In contrast, using direct prompting may even hurt the performance due to mode collapse. This suggests that it is a promising direction to apply VS for synthetic data generation to enhance downstream task performance. See Tables [results_qwen_7b](#results_qwen_7b), [results_qwen_1.7b](#results_qwen_1.7b), and [results_qwen_4b](#results_qwen_4b) in Section [positive data](#appendix-positive-data) for the results on individual datasets.

> **Key Takeaway**: VS generates more diverse synthetic data, improving downstream performance on math tasks. This work highlights the capability of LLMs to generate diverse synthetic data, pointing toward a promising paradigm for training more capable models.