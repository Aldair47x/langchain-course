# LangChain Course – Project Index

This repository contains four independent LangChain examples. Each module ships with its own `pyproject.toml`, entrypoints, and sometimes a `.env`. Use a separate virtual environment per module to avoid dependency conflicts.

## Table of Contents
- [Modules](#modules)
- [Prerequisites](#prerequisites)
- [Setup (Windows PowerShell)](#setup-windows-powershell)
- [Quick Start](#quick-start)
- [Module Usage](#module-usage)
    - [intro-langchain](#intro-langchain)
    - [intro-rag](#intro-rag)
    - [ReAct-search-agent](#react-search-agent)
    - [search-agent](#search-agent)
- [Environment Variables](#environment-variables)
- [Tips & Troubleshooting](#tips--troubleshooting)
- [Next Steps](#next-steps)

## Modules

Folder map and primary files:

- `intro-langchain/`
    - `.env`, `.python-version`, `main.py`, `pyproject.toml`, `README.md`
- `intro-rag/`
    - `.python-version`, `ingestion.py`, `main.py`, `mediumblog1.txt`, `pyproject.toml`, `README.md`
- `ReAct-search-agent/`
    - `.env`, `.python-version`, `main.py`, `prompt.py`, `pyproject.toml`, `README.md`, `schemas.py`, `__pycache__/`
- `search-agent/`
    - `.env`, `.python-version`, `main.py`, `pyproject.toml`, `README.md`

Refer to each module’s README for details:
- [intro-langchain/README.md](intro-langchain/README.md)
- [intro-rag/README.md](intro-rag/README.md)
- [ReAct-search-agent/README.md](ReAct-search-agent/README.md)
- [search-agent/README.md](search-agent/README.md)

## Prerequisites
- Python version as specified in each module’s `.python-version` (install via pyenv or your preferred method).
- A separate virtual environment per module.
- Any required API keys set in a `.env` file (for modules that include `.env`).

## Setup (Windows PowerShell)
Create and activate a venv, install dependencies, configure environment variables, and run the app.

```powershell
# 1) Create and activate venv (example: intro-langchain)
cd .\intro-langchain
python -m venv .venv
 .\.venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -U pip
# If the module’s README specifies a tool (pip/poetry/pdm/uv), follow that. Otherwise:
# - Prefer: pip install .        (when pyproject.toml is installable)
# - Or:     manually install packages listed in pyproject.toml

# 3) Configure environment variables (modules that include .env)
# Create/update .env with provider keys (LLM/search)

# 4) Run the app
python .\main.py
```

## Quick Start
Pick a module and follow its minimal flow.

```powershell
# intro-langchain
cd .\intro-langchain; python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -U pip; pip install .; python .\main.py

# intro-rag (run ingestion first)
cd .\intro-rag; python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -U pip; pip install .; python .\ingestion.py; python .\main.py

# ReAct-search-agent
cd .\ReAct-search-agent; python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -U pip; pip install .; python .\main.py

# search-agent
cd .\search-agent; python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -U pip; pip install .; python .\main.py
```

## Module Usage

### intro-langchain
- Purpose: Minimal LangChain introduction and prompt-flow basics.
- Files: `main.py` (entrypoint), `.env` (provider keys, if required).
- Run:
    ```powershell
    cd .\intro-langchain
    python -m venv .venv; .\.venv\Scripts\Activate.ps1
    pip install -U pip; pip install .
    # Set .env if required
    python .\main.py
    ```

### intro-rag
- Purpose: Simple Retrieval-Augmented Generation over a local text source.
- Files: `ingestion.py` (preprocess/index `mediumblog1.txt`), `main.py` (query indexed data), `mediumblog1.txt` (sample corpus).
- Run:
    ```powershell
    cd .\intro-rag
    python -m venv .venv; .\.venv\Scripts\Activate.ps1
    pip install -U pip; pip install .
    python .\ingestion.py
    python .\main.py
    ```

### ReAct-search-agent
- Purpose: A search agent implementing a ReAct-style loop with tools.
- Files: `main.py` (entrypoint), `prompt.py` (ReAct prompt), `schemas.py` (tool I/O models), `.env` (search/LLM keys).
- Run:
    ```powershell
    cd .\ReAct-search-agent
    python -m venv .venv; .\.venv\Scripts\Activate.ps1
    pip install -U pip; pip install .
    # Set .env with required keys
    python .\main.py
    ```

### search-agent
- Purpose: A simpler search agent with tool integration.
- Files: `main.py` (entrypoint), `.env` (search/LLM keys).
- Run:
    ```powershell
    cd .\search-agent
    python -m venv .venv; .\.venv\Scripts\Activate.ps1
    pip install -U pip; pip install .
    # Set .env with required keys
    python .\main.py
    ```

## Environment Variables
- Populate `.env` only in modules that include the file.
- Typical keys (confirm per module README/code):
    - `OPENAI_API_KEY` or an alternative LLM provider key
    - A search provider key if the agent uses an external search tool
- Keep secrets out of source control.

## Tips & Troubleshooting
- Match Python version to `.python-version` per module.
- If `pip install .` fails, open `pyproject.toml` and install listed dependencies manually.
- Run `ingestion.py` before `main.py` in `intro-rag`.
- If the app cannot find API keys, confirm your `.env` is present and loaded (some modules use `python-dotenv` or equivalent).
- Use separate venvs to avoid dependency conflicts across modules.

## Next Steps
- See each module’s README for module-specific instructions:
    - [intro-langchain/README.md](intro-langchain/README.md)
    - [intro-rag/README.md](intro-rag/README.md)
    - [ReAct-search-agent/README.md](ReAct-search-agent/README.md)
    - [search-agent/README.md](search-agent/README.md)
- Extend prompts, add tools, and swap models incrementally to compare behaviors across modules.

