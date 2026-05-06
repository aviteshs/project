import os
import zipfile
from datetime import datetime


def get_unique_path(path):
    base, ext = os.path.splitext(path)
    counter = 1
    new_path = path

    while os.path.exists(new_path):
        new_path = f"{base}_{counter}{ext}"
        counter += 1

    return new_path


def run(files, target_ext, upload_folder):
    converted_files = []

    for file in files:
        original_name = file.filename
        name, _ = os.path.splitext(original_name)

        new_filename = name + target_ext
        save_path = os.path.join(upload_folder, new_filename)
        save_path = get_unique_path(save_path)

        file.save(save_path)
        converted_files.append(save_path)

    # í´¥ Create ZIP with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"bulk_converted_{timestamp}.zip"
    zip_path = os.path.join(upload_folder, zip_name)

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file_path in converted_files:
            zipf.write(file_path, os.path.basename(file_path))

    return zip_name

