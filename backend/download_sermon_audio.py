import yt_dlp


def downloadSermonAudio(sermon_link: str) -> bool:
    """
    1. Takes link to youtube video
    2. Downloads video as .webm file
    3. Processes as mp3 audio file
    4. Deletes .webm file
    """
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
        ydl.download(sermon_link)
