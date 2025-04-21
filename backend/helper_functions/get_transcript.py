from dotenv import load_dotenv
import assemblyai as aai
import os

load_dotenv()


def getTranscript() -> str:
    aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
        "./sermons/Mon 4.21.25 Numbers 14： 1-10 The Limits of Leadership.webm"
    )

    return transcript.text
