import os
import uuid
import yt_dlp

def run(video_url, download_folder):
    os.makedirs(download_folder, exist_ok=True)

    video_id = str(uuid.uuid4())
    output_template = os.path.join(download_folder, f"{video_id}.%(ext)s")

    ydl_opts = {
        "outtmpl": output_template,
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": True,   # logs dikhenge (debug ke liye)
        "js_runtimes": {
            "node": {
                "path": "/usr/local/nodejs/bin/node"
            }
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(video_url, download=True)

    # actual downloaded file detect
    for f in os.listdir(download_folder):
        if f.startswith(video_id):
            return f

    raise Exception("Downloaded file not found")
