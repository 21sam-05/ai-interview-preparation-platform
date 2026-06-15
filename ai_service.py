import os

from dotenv import load_dotenv

import google.generativeai as genai


load_dotenv()

genai.configure(
    api_key=os.getenv("AIzaSyBoEPoqIVW23lPs05dZq8Xi3tTzSnXbh60")
)

model = genai.GenerativeModel(
    "models/gemini-2.0-flash"
)


def evaluate_answer(question, answer):

    prompt = f"""
    You are a technical interviewer.

    Evaluate the candidate answer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Give response in this format:

    Score: X/10

    Strengths:
    - ...

    Weaknesses:
    - ...
    """

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        print("Gemini Error:", e)

        return """
Score: 5/10

Strengths:
- Answer submitted successfully

Weaknesses:
- AI evaluation temporarily unavailable
"""