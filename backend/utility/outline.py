import json
import os
from typing import Dict

from google import genai
from pydantic import BaseModel

from utility.logging import SermonProcessingError, setup_logger


class Sermon(BaseModel):
    anecdote: list[str]
    opening_prayer: list[str]
    bible_reading: list[str]
    sermon: list[str]
    closing_prayer: list[str]
    conclusion: list[str]


logger = setup_logger(__name__)


def outline(transcript: str) -> Dict[str, list[str]]:
    """Process transcript with Gemini AI"""
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        prompt = f"""
           Given this sermon transcript: {transcript}, segment it 
           into these six parts: opening anecdote, first prayer, bible 
           passage reading, sermon, final prayer, and conclusion. 
           For each segment, clean the text for readability as in a book: 
           add paragraphs, remove unnecessary audio cues (like 'uh'). 
           Throughout each section feel free to add punctuation, paragraphs,
           and edit it so the point is spoken concisely without omitting much
           of the original thought. For each section, return an array storing 
           each paragraph as its own string. If there are three paragraphs in sermon,
           return an array of three strings.
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
