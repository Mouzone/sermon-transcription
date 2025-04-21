from scrape_sermon_link import scrapeSermonLink
from download_sermon_audio import downloadSermonAudio


def main():
    sermon_link = scrapeSermonLink()
    downloadSermonAudio(sermon_link)


if __name__ == "__main__":
    main()
