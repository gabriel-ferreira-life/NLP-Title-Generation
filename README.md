# 🧠 Title Generation from Abstracts

This project focuses on fine-tuning a Large Language Model (LLM) to generate concise, informative titles from scientific paper abstracts. The model is trained using parameter-efficient fine-tuning (PEFT) with the QLoRA technique and evaluated using BLEU and ROUGE scores.

---

## 📂 Dataset

We use abstracts and titles extracted from QTL-related research papers:

- `Abstract`: The input to the model.
- `Title`: The expected output (ground truth).
- Each entry is labeled as relevant or not to QTL curation.

---

## 🏗️ Model

The base model is a causal LLM (e.g., `LLaMA`, `Mistral`, etc.) fine-tuned using **QLoRA** via 🤗 `PEFT`.

### PEFT Configuration
```python
LoraConfig(
    r=64,
    lora_alpha=16,
    lora_dropout=0.0,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=...  # e.g., q_proj, v_proj
)
```
---

## 🧪 Training Setup

Trainer: SFTTrainer (Supervised Fine-Tuning)
Epochs: 1
Batch Size: 1 (with gradient_accumulation_steps=8)
Optimizer: paged_adamw_32bit
Scheduler: Cosine with warmup ratio 0.03
Mixed Precision: fp16

---

## 🧾 Prompt Template
You are an expert at writing concise and informative research paper titles based on abstracts.

Given the abstract below, generate only a clear, accurate, and concise title that best reflects the core idea of the abstract. I only need the title from you with no more than 45 words.

Abstract: {{abstract}}

Title:

## 📈 Evaluation

The generated titles are evaluated using:

BLEU (1–4 grams)
ROUGE-2 (bigram recall)
ROUGE-L (longest common subsequence)
Metrics are computed via 🤗 evaluate.

Example output:

```
BLEU: 0.23
ROUGE-2: 0.31
ROUGE-L: 0.37
```

## Report & Analysis
For a detailed report on findings and term analysis, refer to:
[Phrase Mining Report (PDF)](report/NLP-Title-Generation.pdf).  

## ⚙️ Repo Structure

```text
NLP-Short-Answer-Grading/
├── config/
│ ├── config.json # Configuration file with data paths
│ └── requirements.txt # Python dependencies
│
├── data/
│ ├── train.csv # Training dataset
│ └── test.csv # Test dataset
│
├── exploration/
│ └── eda.ipynb # Exploratory Data Analysis
│
├── few_shot_exploration/
│ ├── main.py # Entry point: loads data, formats prompt, runs predictions
│ └── prompts/
│  ├── few_shot.py # Functions to format few-shot examples
│  └── template.py # Prompt template used by the LLM
│
├── llama3.2/
│ ├── nlp-short-answer-grading-llama-fine-tunning.ipynb
│ └── nlp-short-answer-grading-llama-inference.ipynb
│
└── problem_description/
  └── Final project.pdf # Project Description

```