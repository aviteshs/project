import os
import zipfile
from datetime import datetime

def run(files, prefix, suffix, numbering, upload_folder):
    renamed_files = []
    counter = 1

    for file in files:
        original_name = file.filename
        name, ext = os.path.splitext(original_name)

        number = f"{counter:03d}_" if numbering else ""
        new_name = f"{prefix}{number}{name}{suffix}{ext}"

        save_path = os.path.join(upload_folder, new_name)

        # Avoid overwrite
        i = 1
        base, ext2 = os.path.splitext(save_path)
        while os.path.exists(save_path):
            save_path = f"{base}_{i}{ext2}"
            i += 1

        file.save(save_path)
        renamed_files.append(save_path)
        counter += 1

    # ZIP create
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"bulk_renamed_{timestamp}.zip"
    zip_path = os.path.join(upload_folder, zip_name)

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for f in renamed_files:
            zipf.write(f, os.path.basename(f))

    return zip_name
