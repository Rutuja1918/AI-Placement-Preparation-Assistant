
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.exceptions import OutputParserException

from prompts import interview_prompt
from schemas import InterviewResponse

load_dotenv()

parser = PydanticOutputParser(
    pydantic_object=InterviewResponse
)


def get_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("Groq API key not found.")

    return ChatGroq(
        model="openai/gpt-oss-20b",
        api_key=api_key,
        temperature=0.3,
        max_tokens=12000
    )


def generate_interview(
    job_role,
    experience_level,
    difficulty,
    num_questions
):

    llm = get_llm()

    chain = llm | parser

    prompt = interview_prompt.format(
        job_role=job_role,
        experience_level=experience_level,
        difficulty=difficulty,
        num_questions=num_questions
    )

    for attempt in range(3):

        retry_instruction = ""

        if attempt > 0:
            retry_instruction = (
                f"\nIMPORTANT: Your previous response was incomplete. "
                f"Generate exactly {num_questions} complete questions. "
                "Include every required field for every question."
            )

        try:
            response = chain.invoke(
                prompt + retry_instruction
            )

            if len(response.questions) == num_questions:
                return response

        except OutputParserException:
            continue

    raise ValueError(
        "Unable to generate the requested number of valid questions. "
        "Please try again."
    )
