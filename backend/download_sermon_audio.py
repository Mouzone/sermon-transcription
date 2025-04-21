from pytubefix import YouTube
import os


def downloadSermonAudio(sermon_link: str) -> bool:
    try:
        yt = YouTube(sermon_link)
        audio_stream = yt.streams.filter(only_audio=True).first()

        if not audio_stream:
            print("No audio stream found for this video.")
            return False

        print(f"Downloading from {sermon_link}")
        downloaded_file = audio_stream.download("downloaded_sermons")

        # Ensure the download directory exists
        os.makedirs("downloaded_sermons", exist_ok=True)

        base, _ = os.path.splitext(downloaded_file)
        new_file = base + ".mp3"

        # Handle case where new_file already exists
        if os.path.exists(new_file):
            os.remove(new_file)

        os.rename(downloaded_file, new_file)
        print(f"Successfully converted {yt.title} to MP3: {new_file}")
        return True

    except Exception as e:
        print(f"Error downloading {sermon_link}: {str(e)}")
        return False
