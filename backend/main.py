from helper_functions.scrape_recent_sermon import scrapeRecentSermon
from helper_functions.download_sermon_audio import downloadSermonAudio


def main():
    sermon_data = scrapeRecentSermon()
    downloadSermonAudio(sermon_data["link"])


if __name__ == "__main__":
    main()
