# Dialogue Simulation {#sec:dialogue_simulation_task}

Simulating multi-turn dialogues with LLMs is crucial for applications like social simulation[^1][^2] and LLM evaluation[^3]. But existing methods suffer from generic responses and low realism against human dialogues. We therefore test VS on this task.

## Benchmark

We use the _PersuasionForGood_ task[^4], which contains 1,017 dialogues where one participant persuades another to donate to the organization, "Save the Children". We choose this dataset as it includes participant personas and a clear, verifiable outcome, the final donation amount, allowing for comparison between the human interactions and our simulation ones. After filtering out dialogues with inconsistent donation amounts, we obtain 939 valid instances, which we partition into 739 for training and 200 for testing.

## Experiment Setup

In our experiments, we focus on simulating the persuadee to assess the realism of persuasion outcomes. The model is given a task instruction and a persona to match the human participant. It interacts with a GPT-4.1-based persuader, prompted with the persuader instruction and persona (see Appendix for prompts). To establish a strong supervised baseline for the simulation, we also fine-tuned Llama-3.1-8B on the persuadee responses in the _PersuasionForGood_ training set.

Unlike single-output creativity writing, dialogue simulation is a multi-turn task, so we need to select a response to continue the interaction at each turn. We explore two design choices at each turn: (1) _Number of candidates_: either a model-decided variable or a human-decided constant (k=5); (2) _Response sampling strategy_: probability-weighted (using verbalized probabilities) or random (uniform over candidates). Empirical results show that model-decided random sampling and human-decided probability-weighted sampling best balance the response quality and diversity; so we adopt these two designs in our experiments.

![**VS performance in Persuasive Dialogue Simulation.** **(a) Donation Amount Distributions** simulated by small, large, and reasoning models with direct and VS, compared against fine-tuned model (green) and human (blue). We see that VS simulates donation distributions more similar to human, especially for the larger and reasoning-focused models. **(b) Linguistic Alignment** on Distinct-1/2/3, semantic diversity, and readability. Black dashed lines denote human levels; closer values indicate better stylistic match. VS achieves higher diversity than the direct prompting, approaching human levels. But the readability score remains higher, suggesting room for improvement.](../figures/dialogue_simulation/combined_visualization.png)

## Evaluation

We evaluate our simulation on the _PersuasionForGood_ human-human test set across two dimensions: donation amount and linguistic style. (1) For **donation amount alignment**, we compare the human and simulated donation amounts with the (i) Kolmogorov-Smirnov (KS) test[^5] for distributional alignment and (ii) L1 distance for per-dialogue alignment. (2) For **linguistic alignment**, we assess three metrics: (i) lexical diversity using Distinct-N[^6], which is the proportion of unique n-grams, (ii) semantic diversity using pairwise embedding-based diversity on persuadee responses within a dialogue, and (iii) readability using the Flesch–Kincaid Grade Level[^7].

## Results

### Donation Amount Alignment

Figure (a) shows the distribution of donation amounts, with the human ground truth in blue. Across models, VS simulates donation distributions more aligned with human behaviors than direct prompting. We also observe an _emergent trend_ that larger models (e.g., GPT-4.1 vs. GPT-4.1-mini) and reasoning-focused models like DeepSeek-R1 benefit more from VS. Notably, GPT-4.1 with VS matches a fine-tuned Llama-3.1-8B persuadee simulator, and DeepSeek-R1 even surpasses it in simulating the median donation amount. The qualitative example shows that VS can generate human-like behaviors, such as resistance and changes of mind (see Table). We did not evaluate other VS variants due to high simulation costs. Quantitative results on KS tests and L1 distance are provided in Table.

### Linguistic Alignment

Figure (b) shows the results. On the diversity side, VS with different settings (model-decided random sampling and human-decided weighted sampling) outperforms direct prompting on Distinct-1/2/3 and semantic diversity, approaching the fine-tuned model's performance and the human distribution. Qualitative analysis shows that VS simulates more substantive responses than direct prompting (see Table and Table). On the readability side, VS still simulates more complex responses than fine-tuned models and humans, suggesting room for improvement. Full linguistic results are provided in Table.

> **Key Takeaway**: VS helps models better simulate multi-turn dialogues, leading to more diverse conversations and donation distributions that are closer to actual human donation behavior.

---

[^1]: lin2025usersimulators
[^2]: anthisposition
[^3]: zhou2024sotopiainteractiveevaluationsocial
[^4]: wang-etal-2019-persuasion
[^5]: ks-test
[^6]: li-etal-2016-diversity
[^7]: flesch1948new
