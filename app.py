from flask import Flask, render_template, request
import os
from modules.bulk_extension_fix import run as bulk_run
from flask import send_from_directory
from modules.bulk_rename import run as rename_run
from modules.video_downloader import run as video_run
import json
from datetime import datetime
from modules.file_share import save_files

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

SHARE_FOLDER = "shared_files"
os.makedirs(SHARE_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/bulk", methods=["GET", "POST"])
def bulk():
    zip_file = None

    if request.method == "POST":
        files = request.files.getlist("files")
        target_ext = request.form.get("ext")

        zip_file = bulk_run(files, target_ext, UPLOAD_FOLDER)

    return render_template("bulk.html", zip_file=zip_file)

@app.route("/rename", methods=["GET", "POST"])
def rename():
    zip_file = None

    if request.method == "POST":
        files = request.files.getlist("files")
        prefix = request.form.get("prefix", "")
        suffix = request.form.get("suffix", "")
        numbering = True if request.form.get("numbering") else False

        zip_file = rename_run(files, prefix, suffix, numbering, UPLOAD_FOLDER)

    return render_template("rename.html", zip_file=zip_file)


DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/video", methods=["GET", "POST"])
def video():
    file = None

    if request.method == "POST":
        url = request.form.get("url")
        file = video_run(url, DOWNLOAD_FOLDER)

    return render_template("video.html", file=file)


@app.route("/download-video/<filename>")
def download_video(filename):
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        return "File not found", 404

    return send_from_directory(
        DOWNLOAD_FOLDER,
        filename,
        as_attachment=True
    )



@app.route("/get/<filename>")
def get_shared_file(filename):
    file_path = os.path.join(SHARE_FOLDER, filename)
    meta_path = os.path.join(SHARE_FOLDER, filename + ".json")

    if not os.path.exists(file_path) or not os.path.exists(meta_path):
        return "File not found or expired", 404

    with open(meta_path) as m:
        meta = json.load(m)

    expires_at = datetime.fromisoformat(meta["expires_at"])

    if datetime.now() > expires_at:
        return "This link has expired", 410

    return send_from_directory(
        SHARE_FOLDER,
        filename,
        as_attachment=True
    )

@app.route("/share", methods=["GET", "POST"])
def share():
    link = None
    expiry = None

    if request.method == "POST":
        files = request.files.getlist("files")

        if not files or files[0].filename == "":
            return render_template("share.html", error="No files selected")

        filename, expiry = save_files(files, SHARE_FOLDER)
        link = request.host_url + "get/" + filename

    return render_template("share.html", link=link, expiry=expiry)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

