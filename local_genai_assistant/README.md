# Local GenAI Assistant (MVP)

This project is the groundwork for a local-first GenAI assistant. The goal is to incrementally build a smart assistant that can reason over personal documents, handle tasks, and respond via voice—all running locally, with no paid API dependencies.

## Day 1-8 Progress
- Wiring together agents, local LLMs, and document understanding
- Running `llama-cpp-python` for lightweight, local inference (tested on Colab)
- Planning to unify CrewAI, LangGraph, and LlamaIndex
- Laying the base blocks for a modular, clean, local-first architecture
- Focused on structuring the skeleton for future iterations

## Tech Stack Preview (subject to evolve)
- **llama-cpp-python**: Local LLM inference
- **CrewAI**: Agent orchestration
- **LlamaIndex**: Personal document ingestion
- **LangGraph**: Controlled reasoning flow
- **Local PDF + JSON I/O**: Offline workflows

> 📌 This is a very raw MVP—just structuring the basics and keeping the loop tight for future development.

## Usage
- Open `local_genai_assistant_mvp.ipynb` in Jupyter or VS Code to explore the current MVP code and experiments.
- Follow along as the project evolves! 