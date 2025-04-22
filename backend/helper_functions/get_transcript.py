from dotenv import load_dotenv
import assemblyai as aai
import os

load_dotenv()


def getTranscript() -> str:

    aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
    transcriber = aai.Transcriber()

    filename = os.listdir("../sermons")[0]
    filepath = os.path.join("../sermons", filename)
    transcript = transcriber.transcribe(filepath)

    return transcript.text
