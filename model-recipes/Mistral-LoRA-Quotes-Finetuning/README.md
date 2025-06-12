# 🧠 Mistral-7B LoRA Fine-tuning on English Quotes (4-bit)

A simple and efficient recipe to fine-tune [Mistral-7B](https://huggingface.co/mistralai/Mistral-7B-v0.1) using 4-bit quantization and LoRA on a small quotes dataset — 100% Colab-compatible & open source.

---

## 📌 Highlights

✅ Fine-tuned Mistral-7B using LoRA + 4-bit quantization  
✅ Uses a lightweight dataset (English quotes)  
✅ Training done within 15–20 mins on Colab with 16GB GPU  
✅ Inference-ready output generation  
✅ No API keys, no heavy compute — works on free tier!

---

## 🛠️ Tech Stack

| Component     | Tool/Library                |
|---------------|-----------------------------|
| Model         | Mistral-7B-v0.1             |
| Finetuning    | LoRA (via `peft`)           |
| Quantization  | 4-bit NF4 (via `bitsandbytes`) |
| Tokenizer     | Hugging Face Transformers   |
| Dataset       | `Abirate/english_quotes`    |
| Training Loop | `Trainer` from HF           |

---

## 🔍 Notebook Overview

| Step | Description |
|------|-------------|
| 1.   | Load 4-bit Mistral model using `transformers` + `bitsandbytes` |
| 2.   | Apply LoRA adapter via `peft` |
| 3.   | Preprocess and tokenize `english_quotes` dataset |
| 4.   | Train using `Trainer` with memory-efficient arguments |
| 5.   | Run inference using the fine-tuned model |

---

## 💡 Example Output

**Prompt:**
> The secret of life is

**Generated:**
> The secret of life is to enjoy the passage of time and find joy in small things.

