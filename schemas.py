
from pydantic import BaseModel, Field
from typing import List


class InterviewQuestion(BaseModel):

    question: str = Field(
        description="Practical, interview-oriented technical question"
    )

    question_type: str = Field(
        description="Scenario-based, Coding, Debugging, Conceptual, Comparison or Problem-solving"
    )

    difficulty: str = Field(
        description="Easy, Medium or Hard"
    )

    model_answer: str = Field(
        description="Detailed, technically accurate, interview-ready answer with reasoning and implementation details"
    )

    explanation: str = Field(
        description="Simple conversational explanation using relatable examples, practical situations and why the concept is useful"
    )

    practical_example: str = Field(
        description="A small real-world or code example illustrating the concept"
    )

    keywords: List[str] = Field(
        description="Important technical keywords"
    )

    follow_up: str = Field(
        description="A deeper question an interviewer might ask next"
    )


class InterviewResponse(BaseModel):

    job_role: str

    experience_level: str

    questions: List[InterviewQuestion]
