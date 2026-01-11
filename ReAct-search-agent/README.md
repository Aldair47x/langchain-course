# ReAct Search Agent

Small LangChain agent that uses OpenAI and Tavily to search the web and return a structured summary with sources.

## Prerequisites
- Python 3.10+
- OpenAI API key
- Tavily API key

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
    ```
    pip install -U langchain langchain-openai langchain-tavily python-dotenv pydantic
    ```
3. Create a `.env` file at the project root:
    ```
    OPENAI_API_KEY=your_openai_key
    TAVILY_API_KEY=your_tavily_key
    ```

## Run
```
python main.py
```
Prints a structured response:
```
{
  "answer": "...",
  "sources": [
     {"url": "..."},
     {"url": "..."}
  ]
}
```

## Files
- main.py
  - Builds an agent with ChatOpenAI (gpt-4o) and TavilySearch.
  - Invokes the agent with a news-trend query and prints the structured response.
- schemas.py
  - Pydantic models:
     - Source: url
     - AgentResponse: answer and sources list
- prompt.py
  - ReAct-style prompt template available for customization if needed.

## Customize
- Change the query in `main.py` under `messages`.
- Switch the model via `ChatOpenAI(model="...")`.
- Add or remove tools in the `tools` list.
- Adjust the response schema in `schemas.py` and pass it as `response_format`.

## Notes
- Requires valid API keys and internet access.
- Tavily is used for search; results are summarized by the LLM.
- `.env` is loaded via `python-dotenv`.
