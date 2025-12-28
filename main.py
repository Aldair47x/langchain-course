import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
# from langchain_openai.chat_models.base import ChatOpenAI
from langchain_ollama import ChatOllama


load_dotenv()

def main():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    information = """
    Dragon ball is a Japanese media franchise created by Akira Toriyama in 1984.
    The story follows the adventures of Goku from his childhood through adulthood as he trains in martial arts
    and explores the world in search of the seven orbs known as Dragon Balls, which summon
    a wish-granting dragon when gathered.
    Along the way, he makes several friends and battles a wide variety of villains,
    many of whom also seek the Dragon Balls for their own desires.

    The franchise consists of manga, anime television series, films, and other media.
    The original manga was serialized in Weekly Shōnen Jump from 1984 to 1995,
    with the 519 individual chapters collected into 42 tankōbon volumes by its publisher Shueisha.
    The anime adaptation produced by Toei Animation aired in two main series:
    Dragon Ball (1986–1996) and Dragon Ball Z (1989–1996).
    Additionally, there are several sequel series, including Dragon Ball GT (1996–1997),
    Dragon Ball Super (2015–2018), and the upcoming Dragon Ball Super: Super Hero (2022).

    Dragon Ball has become one of the most successful and influential manga and anime franchises of all time,
    with a large global fanbase and significant impact on popular culture.
    It has inspired numerous other manga and anime series, as well as video games, merchandise, and other media.
    """

    summary_template = """
    You are a helpful assistant that summarizes information about a topic.
    Given the following information about a topic, provide a concise summary in 2-3 sentences
    that captures the key points.
    Information: {information}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    # llm = ChatOpenAI(
    #     model_name="gpt-5-mini",
    #     temperature=0,
    #     openai_api_key=openai_api_key
    # )

    # gemma3:270m
    llm = ChatOllama(
        temperature=0,
        model="gemma3:270m"
    )

    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print("Summary:")
    print(response.content)

if __name__ == "__main__":
    main()
