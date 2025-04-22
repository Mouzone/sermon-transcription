from helper_functions.scrape_recent_sermon import scrapeRecentSermon
from helper_functions.download_sermon_audio import downloadSermonAudio
from helper_functions.get_transcript import getTranscript
from backend.helper_functions.get_summary import getSummary
import asyncio


async def main():
    sermon_data = await scrapeRecentSermon()
    downloadSermonAudio(sermon_data["link"])
    transcript = getTranscript()
    summary = getSummary(transcript)


if __name__ == "__main__":
    asyncio.run(main())
