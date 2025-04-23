# 🎙️ Arumdaum EM Sermon Scraper & Transcriber

An automated pipeline that scrapes the latest sermon from Arumdaum EM’s YouTube livestreams, transcribes it using AssemblyAI, organizes it into readable sections with Gemini 2.0 Flash, and stores it in a Supabase database. Includes a frontend built with Next.js for viewing.

---

# Backend

## 🧰 Stack
- `uv` (package manager)
- Python
- Docker

## ⚙️ Methodology
1. Scrapes the [YouTube livestreams page of Arumdaum EM](https://www.youtube.com/@ArumdaumEM/live) to find the latest sermon's title and YouTube link.
2. Downloads the sermon into a folder named `sermons`.
3. Sends the video file to AssemblyAI for transcription.
4. Passes the transcription to Google's Gemini 2.0 Flash model to:
   - Split into logical sections
   - Edit for readability
5. Uploads the original transcription and the sectioned version to a Supabase database via PostgREST.
6. Deletes the downloaded video file to clean up.

## 🐳 Docker
- Dockerized to run on Google Cloud with Cloud Scheduler for daily automation.
- Uses `uv` inside the Docker container for dependency installation.
- Installs Chrome in the container so Selenium can scrape properly.
- Creates a `sermons` folder in the container to store the downloaded YouTube video file.

## ▶️ Run Instructions
- Requires a `.env` file with the following credentials:
  - AssemblyAI API key
  - Gemini API key
  - Supabase database URL and key
- Can be run:
  - Locally as a Docker container
  - Directly with `uv run main.py`
- ⚠️ Google Cloud Run’s IPs are often blacklisted from downloading YouTube videos (due to being datacenter IPs). Running locally may be necessary.

---

# Frontend

## 🧰 Stack
- TypeScript
- Next.js
- React Server Components
- PostgREST (via Supabase)
- Tailwind CSS

## ⚙️ Methodology
- Deployed on [Vercel](https://sermon-transcription.vercel.app/)
- Fetches the latest sermon that has been transcribed and outlined by the backend.
- Uses React Server Components to:
  - Simplify fetching using one-liner PostgREST queries
  - Avoid extra complexity (e.g., loading spinners)
---

# Future Improvements

- Run locally on a Raspberry Pi using my local ip since it seems local ips are not flagged for downloading a video once a day, and can run a cron job to run daily
- Change Frontend UI to be more readable
