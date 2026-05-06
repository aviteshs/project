import os
import uuid
import zipfile
from datetime import datetime, timedelta
import json

def save_files(files, base_folder):
    os.makedirs(base_folder, exist_ok=True)

    file_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"shared_{timestamp}_{file_id}.zip"

    zip_path = os.path.join(base_folder, zip_name)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in files:
            z.writestr(file.filename, file.stream.read())

    expiry_date = datetime.now() + timedelta(days=7)

    meta = {
        "filename": zip_name,
        "expires_at": expiry_date.isoformat()
    }

    meta_path = os.path.join(base_folder, zip_name + ".json")
    with open(meta_path, "w") as m:
        json.dump(meta, m)

    return zip_name, expiry_date.strftime("%d %b %Y")
