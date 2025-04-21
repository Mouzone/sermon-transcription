from scrape_sermon_link import scrapeSermonData
from download_sermon_audio import downloadSermonAudio


def main():
    sermon_data = scrapeSermonData()
    print(sermon_data)
    downloadSermonAudio(sermon_data["link"])


if __name__ == "__main__":
    main()
