from google import genai
from pydantic import BaseModel


class Sermon(BaseModel):
    anecdote: str
    opening_prayer: str
    bible_reading: str
    sermon: str
    closing_prayer: str
    conclusion: str


def getSummary(transcript):

    client = genai.Client(api_key="YOUR_API_KEY")

    prompt = f"""
        Given this sermon transcript: {transcript}. Split all the text into six parts:
        opening anecdote, first prayer, bible passage reading, sermon, final prayer
        and conclusion. Clean up the transcript removing any audio cues that are
        unnnecessary, and do your best to clean it up to be readable and representable
        without omitting too much espcially in sermon
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": Sermon,
        },
    )

    return response.text
