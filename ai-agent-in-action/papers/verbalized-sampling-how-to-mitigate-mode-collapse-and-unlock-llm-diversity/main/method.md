# Method: Verbalized Sampling {#sec:vs}

We have shown that for a mode-collapsed model, any response $y^* \in \arg\max_y \pi_\text{ref}(y \mid x)$ on $\mathcal{S}$, which suggests the need to study the base model $\pi_\text{ref}$. Empirical studies [^1, ^2] have shown that base models do exhibit diversity. Therefore, we propose *Verbalized Sampling* as a prompting strategy to recover the diversity level of $\pi_{\textrm{ref}}$, to bypass mode collapse.

## Different Prompts Collapse to Different Modes {#subsec:constrained}

For a mode-collapsed LLM, we find that different prompts $x$ collapse to different modes of $\pi_\text{ref}$. This is how VS can mitigate mode collapse. We categorize prompting strategies into three types and provide their corresponding modes. Detailed assumptions and proof are provided in Section [appendix:anthony's proof on the mode for different prompts].

1. **Instance-level prompt**: This is the most traditional prompt $x$, requesting one instance (e.g., "Tell me a joke about coffee"). The mode is the mode instance (the mode joke) of the base model.

2. **List-level prompt**: This prompt $x$ requests a list of outputs (e.g., "Tell me $k$ jokes about coffee"), as used in [^3, ^4]. The mode is a uniform distribution of related items (a uniformly-distributed list of jokes) learned by the base model during pretraining.

3. **Distribution-level prompt (ours)**: We propose this prompt $x$ which requests $k$ outputs with corresponding probabilities (e.g., "Tell $k$ jokes about coffee with their probabilities"), and name it ***Verbalized Sampling (VS)***. The mode is a distribution capable of approximating the distribution of related items learned by the base model during pretraining. Figure [fig:qualitative] and Section [appendix:probing_pre_training_data] show that when an LLM is prompted to generate a distribution of the 50 US states, its verbalized probability distribution aligns with a proxy of the same distribution in a pre-training corpus (RedPajama), where the KL divergence is 0.12 for Claude-4-Sonnet.

Table: Comparison of different prompting methods, given the same computation budget of $N$ total responses. $k$ is the number of candidates generated per LLM call, specified in the prompt (e.g., $k=5$ for the joke task). $y_i$ denotes the $i$-th generated candidate, $\hat{p}_i$ denotes its verbalized probability, and $\pi(\cdot|x)$ represents the LLM's output distribution conditioned on the prompt $x$. For Multi-Turn and VS-Multi, $h_{i-1}$ denotes the conversation history up to turn $i-1$, and $t$ denotes the $t$-th turn.

| Method | LLM Calls | Candidates | Turns | Prompt Example | Definition |
|--------|-----------|------------|-------|----------------|------------|
| **_1. Instance-level Prompt_** |
|   Direct | $N$ | 1 | 1 | "Tell a joke about coffee" | $y_i \sim \pi(y|x)$ |
|   CoT | $N$ | 1 | 1 | "Think step-by-step, then tell a joke" | $y_i \sim \pi(y|x_{\text{CoT}})$ |
| **_2. List-level Prompt_** |
|   Sequence | $\lceil N/k \rceil$ | $k$ | 1 | "Tell 5 jokes about coffee" | $(y_1, ..., y_k) \sim \pi(y_1, ..., y_k|x_{\text{seq}})$ |
|   Multi-Turn | $N$ | 1 | $N$ | Turn 1: "Tell a joke about coffee"<br>Turn 2+: "Tell another joke about coffee" | $y_i \sim \pi(y|x_{\text{multi}}, h_{i-1})$ |
| **_3. Distribution-level Prompt (Ours)_** |
|   VS-Standard | $\lceil N/k \rceil$ | $k$ | 1 | "Tell 5 jokes with their probabilities" | $(y_1, \hat{p}_1), ..., (y_k, \hat{p}_k) \sim \pi(\cdot|x_{\text{VS}})$ |
|   VS-CoT | $\lceil N/k \rceil$ | $k$ | 1 | "Think step-by-step, then tell 5<br>jokes with probabilities" | $(y_1, \hat{p}_1), ..., (y_k, \hat{p}_k) \sim \pi(\cdot|x_{\text{VS-CoT}})$ |
|   VS-Multi | $\lceil N/k \rceil$ | $k$ | $\lceil N/k \rceil$ | Turn 1: "Tell 5 jokes with probabilities"<br>Turn 2+: "Tell 5 more with probabilities" | $(y_1^{(1)}, \hat{p}_1^{(1)}), ..., (y_k^{(t)}, \hat{p}_k^{(t)}) \sim \pi(\cdot|x_{\text{VS}}, h_{t-1})$ |

In Table [tab:method_comparison_table], we summarize how to implement different prompting methods in practice, under the same computation budget of $N$ total generated responses for a fair comparison. In theory, the number of candidates $k$ in each LLM call could be equal to $N$; but in practice, we notice that if $k$ is too large, the generation quality degrades, so usually $k < N$ and we will generate $N$ total responses across $\lceil N/k \rceil$ calls. For **(2) List-level prompt**, we test another variant, *multi-turn* [^1], which elicits $N$ responses across $N$ turns in a conversation. For **(3) Distribution-level prompt**, we propose two variants: ***VS-CoT*** and ***VS-Multi***, to further enhance diversity.

## Experimental Setup {#sec:experimental_setup}

**LLMs.** Our method is training-free, model-agnostic, and requires no logit access. We test it on a suite of models: (1) closed models like {GPT Series} (**GPT-4.1-mini**, **GPT-4.1**), {Gemini Series} (**Gemini-2.5-Flash**, **Gemini-2.5-Pro**) and {Claude Series} (**Claude-3.7-Sonnet**, **Claude-4-Sonnet**); (2) open ones like **Llama-3.1-70B-Instruct** and **Qwen3-235B-A22B-2507-Instruct-2507**; and (3) {reasoning models} like **OpenAI o3** and **DeepSeek R1**. See Section [appendix:experiment_settings] for generation hyperparameters.

**Tasks.** We conduct comprehensive experiments on creative writing (Section [sec:creative_writing]), dialogue simulation (Section [sec:dialogue_simulation_task]), open-ended QA (Section [main:open_ended_qa]), synthetic data generation (Section [sec:sythetic data] and Section [sec:negative synthetic data]), random number generation (Section [sec:random_number_generation]), along with commonsense reasoning (Section [appendix:commonsense]) and safety (Section [sec:safety]) to show that our method maintains factual accuracy and safety.

[^1]: West, et al. (2025). Base models beat aligned ones.
[^2]: Zhu, et al. (2025). Leveraging base language models.
[^3]: Wang, et al. (2023). Self.
[^4]: Dubois, et al. (2023). AlpacaFarm.