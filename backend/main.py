from utility.scrape_recent_sermon import scrapeRecentSermon

from supabase import create_client, Client
from google import genai
from pydantic import BaseModel
from dotenv import load_dotenv

import assemblyai as aai
import os
import json

# import yt_dlp


class Sermon(BaseModel):
    anecdote: str
    opening_prayer: str
    bible_reading: str
    sermon: str
    closing_prayer: str
    conclusion: str


load_dotenv()


def main():
    sermon_data = scrapeRecentSermon()
    print(sermon_data)
    # yt_opts = {
    #     "verbose": True,
    #     "format": "bestaudio/best",
    #     "outtmpl": "sermons/%(title)s.%(ext)s",
    # }
    # with yt_dlp.YoutubeDL(yt_opts) as ydl:
    #     ydl.download(sermon_data["link"])

    aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
    transcriber = aai.Transcriber()

    filename = os.listdir("./sermons")[0]
    filepath = os.path.join("./sermons", filename)
    transcript_obj = transcriber.transcribe(filepath)
    transcript = transcript_obj.text

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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

    summary_json = json.loads(response.text)
    sermon = Sermon(**summary_json)

    del sermon["bible_reading"]
    sermon["title"] = sermon_data["title"]

    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    supabase.table("Sermons").insert(sermon).execute()


if __name__ == "__main__":
    main()
