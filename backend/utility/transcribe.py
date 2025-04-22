import assemblyai as aai
import os


def transcribe_audio(filepath: str) -> str:
    """Transcribe audio file with AssemblyAI"""
    try:
        aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
        if not aai.settings.api_key:
            raise ValueError("AssemblyAI API key not found")

        logger.info(f"Starting transcription for {filepath}")
        transcriber = aai.Transcriber()
        transcript_obj = transcriber.transcribe(filepath)

        if transcript_obj.error:
            logger.error(f"Transcription failed: {transcript_obj.error}")
            raise SermonProcessingError(f"Transcription failed: {transcript_obj.error}")

        logger.info("Transcription completed successfully")
        return transcript_obj.text

    except Exception as e:
        logger.error(f"Transcription error: {str(e)}")
        raise SermonProcessingError("Transcription failed") from e
