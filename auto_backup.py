import os
import zipfile
import glob
import shutil
import subprocess


DOWNLOADS_FOLDER = "C:/Users/pande/Downloads"
EXTRACT_FOLDER = "C:/Users/pande/OneDrive/Desktop/Photo_backup_automation/Photos-001"


zip_files = glob.glob(os.path.join(DOWNLOADS_FOLDER, "takeout*.zip"))  
if not zip_files:
    print("No Google Takeout ZIP files found. Exiting.")
    exit()

latest_zip = max(zip_files, key=os.path.getctime)  
print(f"Found latest ZIP: {latest_zip}")


if not os.path.exists(EXTRACT_FOLDER):
    os.makedirs(EXTRACT_FOLDER)

with zipfile.ZipFile(latest_zip, 'r') as zip_ref:
    zip_ref.extractall(EXTRACT_FOLDER)

print(f"Extracted to: {EXTRACT_FOLDER}")


organizer_script = "C:/Users/pande/OneDrive/Desktop/Photo_backup_automation/organize_photos.py"
subprocess.run(["python", organizer_script])

print("✅ Photos have been organized!")
