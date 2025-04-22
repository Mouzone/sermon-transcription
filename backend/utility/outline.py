from pydantic import BaseModel
from google import genai
import json
from typing import Dict
import os


class Sermon(BaseModel):
    anecdote: str
    opening_prayer: str
    bible_reading: str
    sermon: str
    closing_prayer: str
    conclusion: str


def outline(transcript: str) -> Dict[str, str]:
    """Process transcript with Gemini AI"""
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        if not client.api_key:
            raise ValueError("Gemini API key not found")

        prompt = f"""
            Given this sermon transcript: {transcript}. Split all the text into six
            parts: opening anecdote, first prayer, bible passage reading, sermon, final
            prayer and conclusion. Clean up the transcript removing any audio cues that
            are unnnecessary, and do your best to clean it up to be readable and
            representable without omitting too much espcially in sermon
        """

        logger.info("Sending transcript to Gemini for processing")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": Sermon,
            },
        )

        sermon = json.loads(response.text)
        logger.info("Successfully processed transcript")
        return sermon

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse Gemini response: {str(e)}")
        raise SermonProcessingError("Failed to parse AI response") from e
    except Exception as e:
        logger.error(f"Transcript processing failed: {str(e)}")
        raise SermonProcessingError("Transcript processing failed") from e
