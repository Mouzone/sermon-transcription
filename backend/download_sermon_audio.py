import yt_dlp


def downloadSermonAudio(sermon_link: str) -> bool:
    yt_opts = {"verbose": True, "force_keyframes_at_cuts": True, "audio": True}

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download("https://www.youtube.com/watch?v=BxUS1K7xu30")
