# Typicality Bias Causes Mode Collapse

{#sec:typicality}

In this section, we show that *typicality bias* in human preference data is one pervasive cause of mode collapse. This bias sharpens the probability distribution towards a few stereotypical completions. When many high-quality completions are possible (e.g., in joke generation), this sharpening becomes a tie-breaker, resulting in mode collapse.

## Typicality Bias in Preference Data: Cognitive & Empirical Evidence

{#sec:mc-typicality}

### Typicality Bias Hypothesis

Cognitive psychology shows that people prefer text that is *familiar*, *fluent*, and *predictable*. This preference is rooted in various principles. For instance, the *mere-exposure effect* [^1] and *availability heuristic* [^2]  imply that frequent or easily recalled content feels more likely and is liked more. *Processing fluency*[3] suggests that easy-to-process content is automatically perceived as more truthful and higher quality. Moreover,  *schema congruity* theory[4] predicts that information that aligns with existing mental models will be accepted with less critical thought. 
We therefore hypothesize that these cognitive tendencies lead to a *typicality bias* in preference data, in which annotators systematically favor conventional text.

[^1]: Zajonc, R. B. (1968). Attitudinal effects of mere exposure. Journal of Personality and Social Psychology, 9(2), 1-27.

[^2]: Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. Cognitive Psychology, 5(2), 207-232.

[^3]: Alter, A. L., & Oppenheimer, D. M. (2009). Uniting the tribes of fluency to form a metatheory of fluency effects. Personality and Social Psychology Review, 13(3), 219-235.

[^4]: Mandler, J. M. (2014). The spatial foundations of language and cognition. In Space and Language (pp. 3-16).

### Modeling Rewards with Typicality Bias

To capture this hypothesized bias, we model the reward function, which reflects human preferences, as a combination of *true task utility* and *typicality bias*. For a tractable proxy of typicality bias, we employ the log-likelihood from a pretrained base model, $\log \pi_{\mathrm{ref}}(y\mid x)$: as the base model has been trained to maximize likelihood on massive text corpora, its probability scores inherently capture text typicality. {Without loss of generality, we use the Bradley-Terry model common in RLHF[5-7] and formulate this combination in reward models in Equation 1}: 

$$
r(x,y) \;=\; r_{\text{true}}(x,y) \;+\; \alpha \,\log \pi_{\text{ref}}(y \mid x) \;+\; \epsilon(x),
\label{eq:bt-assumption}
$$

where $r_{\text{true}}$ is the true task utility, 
$\alpha$ is the typicality bias weight, 
and
$\epsilon$ is a noise term. $\alpha>0$ means that, *holding the true utility fixed*,
higher typicality bias increases the reward.

[^5]: Bradley, R. A., & Terry, M. E. (1952). Rank analysis of incomplete block designs: I. The method of paired comparisons. Biometrika, 39(3/4), 324-345.

[^6]: Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human preferences. Advances in Neural Information Processing Systems, 30.

[^7]: Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., ... & Lowe, R. (2022). Training language models to follow instructions with human feedback. Advances in Neural Information Processing Systems, 35, 26722-26738.

### Verifying Typicality Bias in Preference Data

We test this hypothesis on HelpSteer[8], a preference dataset which provides per-response ratings for both *correctness* (true task utility) and *overall helpfulness* (the final reward). 
From the training set, we form 6,874 pairs of responses to the same prompt with the same correctness ratings. We then compute their per-token log-likelihoods under both *Llama 3.1 405B Base* and *GLM 4.5 Base*, the base models used as $\pi_{\text{ref}}$. 
Fitting these values to Equation 1, yields $\hat{\alpha}=0.57\pm0.07$ and $0.65\pm0.07$ with the respective base models (both $p<10^{-14}$). This provides empirical evidence for a positive $\alpha$ in Equation 1, i.e., human raters are biased towards responses more typical for the base model, independent of correctness (true task utility). See Section A and Section B for the verification experiments on more preference datasets.

[^8]: Wang, H., et al. (2023). HelpSteer: A multi-attribute helpfulness dataset. arXiv preprint arXiv:2307.11760.

## How Typicality Bias Causes Mode Collapse

Having confirmed typicality bias, we need to show how it leads to mode collapse. The RLHF optimization objective under the Bradley-Terry model is as follows, 

$$
\max_{\pi}\ \ \mathbb{E}_{x \sim \mathbb{D}, y\sim \pi(\cdot\mid x)}\!\big[r(x,y) -\;\beta\,\mathrm{KL}\!\big(\pi(\cdot\mid x)\,\|\,\pi_{\mathrm{ref}}(\cdot\mid x)\big) \big]\;,
\label{eq:objective}
$$

where $\beta>0$ is the KL coefficient, $\pi_{\text{ref}}$ is the reference policy (e.g., the base model), and $\pi$ is the learned policy. 

Plugging Equation 1 
into the closed-form solution of Equation 2 [^9]  yields an optimum, sharpened by $\gamma$ (derivation in Section C):

$$
\pi^*(y\mid x)\ \propto\ \pi_{\mathrm{ref}}(y\mid x)^{\,\gamma}\ \exp\!\left(\frac{r_{\text{true}}(x,y)}{\beta}\right),\qquad
\gamma\ :=\ 1+\frac{\alpha}{\beta}\ >\ 1\ \ \text{when}\ \alpha>0.
\label{eq:power}
$$

So any positive typicality bias weight $\alpha$ strictly *sharpens* the distribution of $\pi_{\text{ref}}$. Leaving all else fixed, larger $\alpha$ (stronger typicality in preference data) increases the strength of this effect.

Further, suppose there exists a subset $\mathcal{S}$ of responses such that for all $y,y'\!\in\!\mathcal{S}$^[For example, we can restrict our analysis to $\mathcal{S}$ with only meaningful responses, because nonsensical or erroneous responses are unlikely to be sampled from a well-trained $\pi^*$.] we have 
flat true rewards, $r_{\text{true}}(x,y)=r_{\text{true}}(x,y')$^[This assumption can be relaxed to approximate flatness. We just need bounds on the deviations of $r_{\mathrm{\text{true}}}$ between $y$ and $y'$ to claim mode collapse, but the overall argument (and result) is consistent.].
Then by Equation 3 the optimum within $\mathcal{S}$ reduces to

$$
\pi^*(\cdot\mid x)\ \propto\ \pi_{\mathrm{ref}}(\cdot\mid x)^{\,\gamma}\quad\text{on}\ \mathcal{S},
\qquad \gamma>1.
$$

This behaves like temperature scaling. As $\gamma$ grows very large, we will have $y^* \in \arg\max_y \pi_\text{ref}(y \mid x)$ for all $y^* \sim \pi(\cdot | x)$ with $y^* \in \mathcal{S}$.
This shows that the probability mass is *compressed* toward typical completions (those already favored by $\pi_{\mathrm{ref}}$), yielding a form of *mode collapse* on set $\mathcal{S}$. Intuitively this means that, when many answers are tied on true task utility (a common scenario in creative writing, social simulation, etc), typicality bias acts as a tiebreaker that sharpens the output of the aligned model into the *mode* of the base model. 

[^For example, we can restrict our analysis to $\mathcal{S}$ with only meaningful responses, because nonsensical or erroneous responses are unlikely to be sampled from a well-trained $\pi^*$.]: For example, we can restrict our analysis to $\mathcal{S}$ with only meaningful responses, because nonsensical or erroneous responses are unlikely to be sampled from a well-trained $\pi^*$.

[^This assumption can be relaxed to approximate flatness. We just need bounds on the deviations of $r_{\mathrm{\text{true}}}$ between $y$ and $y'$ to claim mode collapse, but the overall argument (and result) is consistent.]: This assumption can be relaxed to approximate flatness. We just need bounds on the deviations of $r_{\mathrm{\text{true}}}$ between $y$ and $y'$ to claim mode collapse, but the overall argument (and result) is consistent.

[^9]: Rafailov, R., Gordon, A., & Ermon, S. (2024). Direct preference optimization is inverse reinforcement learning with a generative model. International Conference on Learning Representations.

So this means that on the set of $\mathcal{S}$, as $\gamma$ increases, the probability mass of $\pi^*(\cdot\mid x)$ is *compressed* toward typical completions (those already favored by $\pi_{\mathrm{ref}}$), yielding a form of *mode collapse*. Intuitively this means that, when many answers are tied on task utility (common in creative writing, social simulation, etc), typicality bias acts as a tiebreaker that sharpens the output into a narrow peak, causing mode collapse.

The sharpening exponent $\gamma > 1$ in Equation 3 has a profound effect on the output distribution. As $\gamma$ increases, the distribution $\pi^*(y \mid x) \propto \pi_\text{ref}(y \mid x)^\gamma$ becomes increasingly concentrated on high-probability regions of $\pi_\text{ref}$—analogous to temperature scaling but in the opposite direction. In the limit $\gamma \to \infty$, the probability ratio between any suboptimal response $y$ and the mode $y^*$ vanishes as $[\pi_\text{ref}(y \mid x) / \pi_\text{ref}(y^* \mid x)]^\gamma \to 0$, causing $\pi^*$ to converge to a Dirac delta:

To observe mode collapse in practice, elements of $\mathcal{S}$ should not only share reward, but share a near optimal reward. Otherwise, the elements of S are unlikely to be sampled from pi star. The intuition remains that many high quality completions (jokes, poems, stories) can be semantically tied, and therefore, cause collapse.

We expect local flatness in tasks with many equally valid answers (poem/story/joke generation, dialogue simulation, pluralistic QA), and not in sharply peaked domains with essentially unique correct outputs (e.g., single-answer arithmetic). In the former, RLHF that inherits a typicality prior should reduce diversity (as we later observe); in the latter, typicality has little room to act. Finally, Equation 1 is an approximation: $\log \pi_{\mathrm{ref}}$ can correlate with $r_{\text{sem}}$, which is precisely why our controlled analyses (ii)–(iii) live in the appendix.

To validate the modeling hypothesis made in Equation 1, we test a base model's average per-token log-probabilities favor the *chosen* label more often than chance on human preference datasets. Across four datasets and multiple base models, we observe statistically significant above-chance agreement rates (Table 1), suggesting that typicality, proxied by $\log \pi_{\mathrm{ref}}$, is positively associated with preference labels.

To further verify this hypothesis, we control for the possible confounding between $\log \pi_{\mathrm{ref}}$ and semantic utility $r_{\text{sem}}$, and in doing so, confirm empirically that $\alpha > 0$. We therefore include two additional analyses in App. A: a controlled regression and a within-prompt Bradley–Terry identification. In doing so, we isolate a data-level cause of mode collapse—typicality-induced sharpening on semantic plateaus, motivating querying *distributions* rather than *instances*, and predicting diversity gains on tasks with many valid outputs.

## Connecting Typicality with Mode Collapse

People systematically favor text that is *familiar*, *fluent*, and *schema-congruent*. The availability heuristic and mere-exposure effect imply that frequent or easily recalled content feels more likely and is liked more [^10]. Processing fluency inflates perceived truth, quality, and aesthetic appeal [^11]. Schema-congruity accounts predict that responses fitting learned templates are judged more appropriate with less scrutiny [^12]. Related biases (representativeness, confirmation bias, illusory truth) further push raters toward prototypical strings [^13]. We therefore posit a *typicality preference* in RLHF data and use the base model's log-likelihood $\log \pi_{\mathrm{ref}}(y\mid x)$ as a tractable proxy for typicality.

### Setup and fixed point

Fix a prompt space $\mathcal{X}$ and a finite candidate set $\mathcal{Y}$. For $x\in\mathcal{X}$, let $\pi_{\mathrm{ref}}(\cdot\mid x)$ denote a fixed reference policy (e.g., the SFT/base model) and $\pi(\cdot\mid x)$ the trainable policy during post-training. With a scalar reward $r(x,y)$, the standard KL-regularized single-prompt objective is

$$
J(\pi)
\;=\;
\mathbb{E}_{y\sim \pi(\cdot\mid x)}\!\big[r(x,y)\big]
\;-\;
\beta\,D_{\mathrm{KL}}\!\big(\pi(\cdot\mid x)\,\|\,\pi_{\mathrm{ref}}(\cdot\mid x)\big),
\qquad \beta>0,
\label{eq:rlhf}
$$

whose maximizer over $\pi(\cdot\mid x)$ has the familiar exponential-tilt form

$$
\pi^*(y\mid x)
\;=\;
\frac{\pi_{\mathrm{ref}}(y\mid x)\,\exp\!\big(r(x,y)/\beta\big)}
{\sum_{y'\in\mathcal{Y}}\pi_{\mathrm{ref}}(y'\mid x)\,\exp\!\big(r(x,y')/\beta\big)}.
\label{eq:fixpoint}
$$

### Typicality hypothesis (data-level bias)

Guided by the cognitive evidence above, we model human preference data as mixing semantic utility with typicality:

$$
\boxed{\;
r(x,y)\;=\;r_{\mathrm{sem}}(x,y)\;+\;\alpha\,\log \pi_{\mathrm{ref}}(y\mid x)\;+\;c(x),
\quad \alpha>0\; }
\label{eq:typicality}
$$

where $r_{\mathrm{sem}}$ captures task utility and $\log \pi_{\mathrm{ref}}$ proxies how *typical* a response already is under the reference.^[For clarity we omit annotator-specific noise; our results go through under bounded perturbations and with standard random-effects augmentations.]
Substituting Equation 4 into Equation 3 yields

$$
\pi^*(y\mid x)\;\propto\;\big[\pi_{\mathrm{ref}}(y\mid x)\big]^{\,\gamma}\,
\exp\!\big(r_{\mathrm{sem}}(x,y)/\beta\big),
\qquad \gamma \;\equiv\; 1+\alpha/\beta \;>\; 1.
\label{eq:power}
$$

Thus, whenever $r_{\mathrm{sem}}$ is (approximately) flat over a slate of near ties, $\pi^*(\cdot\mid x)$ reduces to a *power-transformed sharpening* of $\pi_{\mathrm{ref}}$ on that slate.

### When sharpening becomes collapse

Consider creative or loosely specified tasks (e.g., jokes, stories, poems) where many completions are near-equivalent in semantic utility. Let $S\subseteq\mathcal{Y}$ collect such near ties with $r_{\mathrm{sem}}(x,y)\approx r_0$ for all $y\in S$. Then Equation 5 implies

$$
\pi^*(\cdot\mid x)\Big|_{S}\;\propto\;\pi_{\mathrm{ref}}(\cdot\mid x)^{\,\gamma},
\qquad \gamma>1,
$$

so any pre-existing skew in $\pi_{\mathrm{ref}}$ over $S$ is *strictly sharpened*. If the reference mode lies inside $S$, probability mass concentrates on that prototype as $\alpha/\beta$ grows—precisely the *mode collapse* phenomenon observed after alignment.

**Proposition 1 (Power-transform sharpening).**
*Fix $x$ and a slate $S\subset\mathcal{Y}$ with near-flat $r_{\mathrm{sem}}(x,y)\approx r_0$. Under the typicality model Equation 4 and KL-RLHF, the optimizer restricted to $S$ satisfies $\pi^*\!\big|_S \propto \pi_{\mathrm{ref}}^{\,\gamma}$ with $\gamma=1+\alpha/\beta>1$. Hence any skew in $\pi_{\mathrm{ref}}$ is strictly amplified; if $\arg\max_{y\in S}\pi_{\mathrm{ref}}(y\mid x)\in S$, then $\pi^*$ collapses toward that mode as $\alpha/\beta$ increases.* □

### Empirical evidence that α>0

We test the key implication of Equation 4—that base-model likelihood predicts human preference beyond semantics—at three levels (Figure 1):

- **(i) Global correlations across datasets and base models.** Using *non-RLHF* base models (Gemma-3-4B/27B, Qwen3-4B, Llama-3.1-8B/70B), the item with higher $\log p$ under the base model matches the human-preferred item *above chance* on four public preference datasets:
  - Summarize-from-Feedback: 52.4–56.4% agreement,
  - UltraFeedback (binarized): 57.5–60.2%,
  - HelpSteer: 56.2–60.8%,
  - Skywork-Reward: 58.8–61.7%.
  (95% CIs are tight; per-model tables are in App. B.)

- **(ii) Controlled regression (HelpSteer).** On the HelpSteer validation split ($n{=}1{,}789$), an *ordinal logistic regression* predicts overall helpfulness ratings (1–5) from **correctness** (1–5) and **average base-model log-likelihood**. Correctness is the dominant predictor (OR $\approx 27$, $p<10^{-3}$), but log-likelihood remains a *significant independent* predictor (OR $\approx 1.33$, $p<10^{-4}$). A likelihood-ratio test confirms that adding log-likelihood improves fit ($\chi^2(1)=21.4$, $p<10^{-5}$). These results indicate that annotators reward higher model confidence even after accounting for correctness.

- **(iii) Within-prompt Bradley–Terry identification of α.** On HelpSteer, we construct matched pairs with the same prompt and *equal correctness* but different helpfulness ($n{>}5{,}000$ pairs). A within-prompt Bradley–Terry analysis using $\Delta \log p$ from a base model estimates $\hat{\alpha}\approx 0.51$ ($p<10^{-3}$): a +1 SD increase in $\Delta\log p$ raises the odds of being chosen as more helpful by $\sim$37% (OR=1.37), with win probability rising from $\sim45\%\to\sim61\%$ from -1SD to +1SD, *holding correctness fixed*.

**Figure 1: Evidence that α>0 (triangulation).**
**A:** Across four preference datasets and five non-RLHF base models, the higher-likelihood item aligns with the human-preferred item above chance (52–62%; 95% CIs).
**B:** *HelpSteer* ordinal logistic regression: correctness is the dominant predictor (OR$\approx$27), but *base-model log-likelihood remains independently significant* (OR$\approx$1.33; LR $\chi^2(1){=}21.4$, $p{<}10^{-5}$).
**C:** *HelpSteer* within-prompt Bradley–Terry on matched pairs with equal correctness estimates $\hat\alpha\approx 0.51$; +1 SD in $\Delta\log p$ raises choice odds by $\sim$37% (win prob $\sim$45%$\to$61%). Appendix reports SFF matched-pair (55.0%) and Likert–probability correlation ($r{=}0.22$) as supportive evidence.

Together these results support $\alpha>0$ in real preference data and empirically justify the power-transform form in Equation 5. Full per-dataset$\times$model tables, regression specifications (including proportional-odds checks and length controls), and BT estimation details appear in Appendix.

### Takeaways and bridge to Section 3

The theory predicts—and our experiments later confirm—that collapse is most acute when: (1) **reward slates are flat** (creative/pluralistic tasks admit many near-equivalent completions, so $\pi^*$ inherits a sharpened $\pi_{\mathrm{ref}}^\gamma$ over $S$); and (2) **the reference mode is "good enough"** (if the reference mode lies in $S$, $\pi^*$ concentrates there as $\alpha/\beta$ grows; Proposition 1). These are exactly the settings (poems, stories, jokes; dialogue continuations; open-ended QA with many valid answers) where we observe narrowed output distributions after RLHF.

**Box 1 — Different modes for different queries.**
*Instance-level prompts* on near-flat slates pick a *prototype*: the sharpened mode of $\pi_{\mathrm{ref}}$. *Distribution-level prompts* make distributional fidelity the target ("return $c$ candidates with probabilities"), removing flat-reward pathologies and exposing the underlying diversity—this motivates our method in Section 3.

[^10]: Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. Cognitive Psychology, 5(2), 207-232.

[^11]: Alter, A. L., & Oppenheimer, D. M. (2009). Uniting the tribes of fluency to form a metatheory of fluency effects. Personality and Social Psychology Review, 13(3), 219-235.

[^12]: Mandler, J. M. (2014). The spatial foundations of language and cognition. In Space and Language (pp. 3-16).

[^13]: Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124-1131.

## Connecting Typicality with Mode Collapse (continued)

### Setup
Consider a fixed prompt space $\mathcal{X}$ and finite response set $\mathcal{Y}$. With $y \in \mathcal{Y}$ and $x \in \mathcal{X}$, let $\pi_{\mathrm{ref}}(\cdot\mid x)$ denote a fixed reference policy over strings in $\mathcal{Y}$ (typically the SFT model), let $\pi(\cdot\mid x)$ be a learnable policy, and let $r(x,y)$ be a latent, scalar reward in context of the Bradley-Terry preference model. Then, the standard KL-regularized objective in RLHF is given below:

$$
J(\pi)\;=\;\mathbb{E}_{x \sim \mathbb{D}, y\sim\pi(\cdot\mid x)}\!\big[r(x,y)\;-\;\beta\,D_{\mathrm{KL}}\!\big(\pi(\cdot\mid x)\,\|\,\pi_{\mathrm{ref}}(\cdot\mid x)\big)\;\big],\qquad \beta>0
\label{eq:rlhf}
$$

where $\mathbb{D}$ is the data distribution over the prompt space $\mathcal{X}$. For fixed latent reward $r$, the well-known maximizer over choice of $\pi$ is defined:

$$
\pi^*(y\mid x)\;=\;\frac{\pi_{\mathrm{ref}}(y\mid x)\,\exp\!\big(r(x,y)/\beta\big)}{\sum_{y'}\pi_{\mathrm{ref}}(y'\mid x)\,\exp\!\big(r(x,y')/\beta\big)}.
\label{eq:fixpoint}
$$

This closed-form solution underlies recent analyses of the impact *algorithmic bias* during RLHF and subsequent preference collapse, motivating existing preference-matching alternatives to KL regularization [^14].

[^14]: Xiao, L., et al. (2024). Algorithmic bias in language model alignment. arXiv preprint arXiv:2402.13446.

### Typicality Hypothesis
Contrary to this existing work, the main contribution of our theoretical inquiry is exploring the role of *data bias* in RLHF, specifically that stemming from a well-known cognitive bias in humans. We hypothesize mode collapse may also arise from *typicality bias*. To make this claim analytically tractable, we'll assume typicality presents in the latent reward $r$, which is implicitly determined by human annotators and the data they generate. The exact process we assume is described below:

$$
r(x,y)\;=\;r_{\mathrm{sem}}(x,y)\;+\;\alpha\,\log \pi_{\mathrm{ref}}(y\mid x)\;+\;c(x),\qquad \alpha>0.
\label{eq:typicality}
$$

Here $r_{\mathrm{sem}}$ captures semantic quality (i.e., an objective task utility), while $\log \pi_{\mathrm{ref}}$ proxies how typical a response already is under the reference model. Essentially, this postulates two points: (i) that the latent rewards motivating human preferences are in fact composed of *both* a functional utility for the human and a spurious correlation capturing typicality bias, and (ii) typicality bias is well-represented by the reference model's probability distribution.

### Verifying the Hypothesis
While the typicality hypothesis has significant backing in cognitive science literature, the functional form we've assumed is novel. We take a largely empirical approach to verifying the plausibility of the functional form in Equation 6.

Insert a description of the empirical study and basic results pointing to a figure.

### Narrowing the Scope of Inquiry
To arrive at a specific realization of mode collapse in RLHF, we need to specify the types of problems where this might occur, and moreover, where mode collapse is a problem. Specifically, the contexts where we prioritize output diversity from LLMs are often creative in nature or have purposefully loose specifications. These can include tasks like story, joke, and poem writing or tasks like synthetic data generation (e.g., synthetic dialogues). We observe a key trait that is common to all of these tasks. For a fixed prompt $x$, they can have **flat semantic rewards**:

$$
\exists \ \mathcal{S} \subset \mathcal{Y}, \ \forall \ y, y' \in \mathcal{S} \ : \ r_{\mathrm{sem}}(x,y) = r_{\mathrm{sem}}(x,y').
$$

That is, the functional utility of many completions can be equivalent or near equivalent:^[We assume identical latent rewards, but approximate flatness could be modeled via an $\epsilon$-sized bound on how $r_\mathrm{sem}$ varies. The behavior of the RLHF model would remain consistent, adding slack dependent on $\epsilon$.] many jokes are funny, many stories can be equally engaging, and many dialogues may be plausible reflections of an actual human exchange.

### Observation of Mode Collapse under Typicality
Plugging Equation 6 into Equation 5 for fixed $x$ yields:

$$
\pi^*(y\mid x)\;\propto\;\big(\pi_{\mathrm{ref}}(y\mid x)\big)^{\,1+\alpha/\beta}\,\exp\!\big(r_{\mathrm{sem}}(x,y)/\beta\big).
\label{eq:power}
$$

Now, assume we have a set $\mathcal{S}$ with semantically flat rewards. Then,

$$
\forall y \in \mathcal{S} \ : \ \pi^*(y\!\mid\!x)\propto \pi_{\mathrm{ref}}(\cdot\!\mid\!x)^{\gamma}
\label{eq:sharpen}
$$

with $\gamma=1+\alpha/\beta>1$. Already, we see that any pre-existing skew in $\pi_{\mathrm{ref}}$ is *sharpened* for completions in $\mathcal{S}$. This means, *we already have a form of collapse*. On any slate of near ties $\mathcal{S}$, the RLHF model $\pi^*$ is now *even more likely* to return the mode of $\pi_\textrm{ref}$ when compared to the original reference model. The extent of this sharpening is exponential in the bias parameter $\alpha$, indicating a potentially stark re-weighting of probability. We arrive at full-on mode collapse in cases where $\textrm{arg}\max_y \pi^*(y|x) \subset \mathcal{S}$ and $\mathcal{S}$ has nearly flat rewards. Flat reward sets, even containing optimal completions, are realistic in many creative generation tasks, since it can be hard to differentiate functional utility.

Our theoretical study demonstrates how mode collapse may come about from typicality, especially in creative generation tasks where we'd actually like to prioritize sample diversity. Specifically, it suggests that within any group of completions that all share a similar semantic reward, we observe a form of mode collapse that is exponential in the bias parameter $\alpha$. More generally, *every* set of completions $\mathcal{S}$ with highly similar rewards will experience a sharpening that shifts probability to just a single element of $\mathcal{S}$. When stuck in this situation, *how can we extract a good solution?* Our proposal is to restructure our prompt to work with the mode collapsed model. Specifically, consider the case where we ask the model for a distribution over completions: "write 10 different stories about pie and report their respective probabilities." The important feature of this prompt is that it explicitly requests a sequence of distinct items. Even if the mode of the policy is returned, it will *still* capture some level of sample diversity, e.g., as long as every story is actually distinct. As noted in the related works, the idea of requesting a sequence-like object (e.g., a list of respondents) has been studied before with demonstrated empirical success.

### Motivating Distribution-level Queries
However, our theory adds a complementary observation: the impact of flat semantic rewards. Indeed, in cases where completions can exhibit flat rewards, we observe the policy $\pi^*$ places greater weight on more typical completions (Equation 7) as quantified by their probability under the reference model. Prompts that ask for a list of respondents fall into this trap. For example, [Tokyo, Paris, Rome] and [New York, Amsterdam, Munich] are both semantically correct respondents, if asked for "a list of three cities." Our proposed modification -- requesting a probability distribution -- enforces a more strict notion of semantic correctness. The response must also encode correct probability information. In turn, latent semantic rewards will be proportional to how accurate the respondent story probabilities are and any set of completions will have varying (non-flat) rewards based on accuracy. Maintaining reward granularity avoids purely typical responses, which we expect to be less diverse.

## How to circumvent mode collapse?

Our theoretical study demonstrates how mode collapse may come about from typicality, especially in creative generation tasks where we'd actually like to prioritize sample diversity. Specifically, it suggests that within any group of completions that all share a similar semantic reward, we observe a form of mode collapse that is exponential in the bias parameter $\alpha$. More generally, *every* set of completions $\mathcal{S}$ with highly similar rewards will experience a sharpening that shifts probability to just a single element of $\mathcal{S}$. When stuck in this situation, *how can we extract a good solution?* Our proposal is to restructure our prompt to work with the mode collapsed model. Specifically, consider the case where we ask the model for a distribution over completions: "write 10 different stories about pie and report their respective probabilities." The important feature of this prompt is that it explicitly requests a sequence of distinct items. Even if the mode of the policy is returned, it will *still* capture some level of sample diversity, e.g., as long as every story is actually distinct. As noted in the related works, the idea of requesting a sequence-like object (e.g., a list of respondents) has been studied before with demonstrated empirical success.

However, our theory adds a complementary observation: the impact of flat semantic rewards. Indeed, in cases where completions can exhibit flat rewards, we observe the policy $\pi^*$ places greater weight on more typical completions (Equation 7) as quantified by their probability under the reference model. Prompts that ask for a list of respondents fall into this trap. For example, [Tokyo, Paris, Rome] and [New York, Amsterdam, Munich] are both semantically correct respondents, if asked for "a list of three cities." Our proposed modification -- requesting a probability distribution -- enforces a more strict notion of semantic correctness. The response must also encode correct probability information. In turn, latent semantic rewards will be proportional to how accurate the respondent story probabilities are and any set of completions will have varying (non-flat) rewards based on accuracy. Maintaining reward granularity avoids purely typical responses, which we expect to be less diverse.

## Summary

This section has shown that typicality bias in human preference data is a significant cause of mode collapse. Through cognitive and empirical evidence, we demonstrated that human annotators systematically favor responses that are more typical for the base model, independent of their actual quality or correctness. This bias sharpens the probability distribution towards stereotypical completions, which becomes a tie-breaker when many high-quality completions are possible, resulting in mode collapse.

The mathematical analysis shows that when the typicality bias weight α is positive, the optimized policy π* sharpens the distribution of the reference model π_ref, leading to compression of probability mass toward typical completions. This effect is particularly pronounced in creative tasks where many responses may have similar semantic utility, making typicality bias the deciding factor in which responses are favored.
