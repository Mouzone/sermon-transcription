import yt_dlp


def downloadSermonAudio(sermon_link: str) -> bool:
    yt_opts = {
        "verbose": True,
        "format": "bestaudio/best",
        "outtmpl": "sermons/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
    }

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download("https://www.youtube.com/watch?v=BxUS1K7xu30")
