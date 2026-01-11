# LangChain Basic Project

Minimal starter repository for experimenting with LangChain and an LLM provider (OpenAI, etc.). Includes a small example to get you up and running quickly.

## Features
- Simple LLM prompt -> response example using LangChain
- Clear env/config pattern
- Recommendations for local development

## Prerequisites
- Python 3.10+
- An LLM API key (e.g. OpenAI `OPENAI_API_KEY`)
- Git (optional)

## Quick start

1. Clone or create the project folder
2. Create and activate a virtual environment:
    - Windows: `python -m venv .venv && .venv\\Scripts\\activate`
    - macOS / Linux: `python -m venv .venv && source .venv/bin/activate`
3. Install dependencies:
    - Create `requirements.txt` with:
      ```
      langchain
      openai
      python-dotenv
      ```
    - Then run:
      ```
      pip install -r requirements.txt
      ```
4. Create a `.env` file in the project root:
    ```
    OPENAI_API_KEY=sk-...
    ```
    (Use your provider's key name if different.)

## Example: basic_chat.py

Save this as `examples/basic_chat.py` and run `python examples/basic_chat.py`.

```python
from dotenv import load_dotenv
import os
from langchain import OpenAI, LLMChain, PromptTemplate

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
     raise RuntimeError("Missing OPENAI_API_KEY in environment")

# create an LLM wrapper (model_name can be changed)
llm = OpenAI(temperature=0.2, model_name="gpt-3.5-turbo")

# simple prompt template
template = "You are a helpful assistant. Answer the question concisely.\n\nQuestion: {question}\n\nAnswer:"
prompt = PromptTemplate.from_template(template)

# create and run the chain
chain = LLMChain(llm=llm, prompt=prompt)
resp = chain.run({"question": "What is LangChain used for?"})
print(resp)
```

Notes:
- Adjust `model_name` to the model you have access to.
- For other providers, follow their LangChain integration docs and set the proper environment variables.

## Project layout (suggested)
- README.md
- requirements.txt
- .env
- examples/
  - basic_chat.py
- src/
  - chains/
  - prompts/
  - agents/

## Testing & development
- Add unit tests for prompt formatting and deterministic logic.
- Use seedable randomness where appropriate.
- Keep API keys out of version control.

## Contributing
- Keep commits small and focused.
- Update README when adding new examples or public APIs.

## License
MIT — see LICENSE file.

If you need a more opinionated starter (memory, retrieval, or agents examples), say which feature to include and a short description of the use case.