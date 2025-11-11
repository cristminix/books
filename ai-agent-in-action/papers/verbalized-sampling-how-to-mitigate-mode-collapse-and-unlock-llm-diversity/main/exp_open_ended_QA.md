# Open-Ended QA {#main:open_ended_qa}

Enumerative open‑ended QA exposes mode collapse because many answers are equally valid on true task utility.
Besides, for real-world tasks like survey simulation, generating a broad and more realistic range of answers is crucial. Building on our finding that VS improves diversity, this section evaluates its effectiveness in producing such distributions for open-ended questions with multiple valid answers.

## Benchmark

We adapt from the _CoverageQA_ [^1] benchmark, which contains simple QA questions with a wide range of valid answers (e.g., "Name a US state"). Our evaluation uses 40 questions (10 original, 30 new ones created in the same style), each with at least 20 ground-truth answers requiring no reasoning or external knowledge. For each question, we sample N=100 responses per method by generating k=20 candidates per LLM call, capturing both within-call and across-call diversity. Full prompts are in Appendix [appendix:experiment_prompt].

## Evaluation

We evaluate the performance using three metrics:

1. **KL divergence**: the deviation of the model's answer distribution from a realistic reference distribution estimated from the RedPajama [^2] pretraining corpus. Lower values indicate better alignment. Note that here we focus on the generated answers rather than the verbalized probabilities, so we calculate the answer distribution from the frequency of each unique answer, not from the verbalized probability distribution like in Figure [fig:qualitative].
2. **Coverage-N**: the fraction of unique ground-truth answers generated in N samples; higher values indicate broader coverage.
3. **Precision**: the proportion of correct answers among all samples; it measures if the increased diversity comes at the expense of correctness.

![Results on the **Open-Ended QA** task averaged across models. We perform one-tailed t-test between VS-Standard and baselines (*p<0.05, **p<0.01, ***p<0.001). **(a)** shows the average KL divergence between the response distribution and the corresponding pretraining distribution. VS achieves lower KL divergence compared to baseline methods, indicating closer alignment with the pretraining distribution. **(b)** shows the average Coverage-N across all models. This means VS can generate a broader range of correct answers than the baselines. **(c)** shows the average precision across all models. VS methods maintain answer quality comparable to baseline approaches.](../figures/bias/combined_kl_coverage_precision.png)

## Results

As shown in Figure [fig:open_ended_qa_combined_results], our methods outperform all baselines. VS-Standard significantly lowers KL divergence and improves coverage. VS-Multi achieves the best overall tradeoff, yielding the lowest KL divergence and the highest coverage. Crucially, these gains do not compromise answer quality, as precision remains near 1.0 across all methods. Detailed results are available in Table [tab:all_results_open_ended_qa_general].

> **Key Takeaway**: VS improves alignment with the pretraining distribution and increases answer coverage without compromising answer quality in open-ended QA with multiple valid answers.

[^1]: Wong, et al. (2024). Simple strategies for diversifying language models.
[^2]: Together (2023). RedPajama.
