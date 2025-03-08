import os
import shutil
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS


SOURCE_FOLDER = "C:/Users/pande/OneDrive/Desktop/Photo_backup_automation/Photos-001"
DESTINATION_FOLDER = "C:/Users/pande/OneDrive/Desktop/OrganisedPhotos"

def get_photo_date(photo_path):
    """Extracts the date taken from photo metadata."""
    try:
        image = Image.open(photo_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Error reading {photo_path}: {e}")
    return None  

def organize_photos():
    """Organizes photos into Year/Month folders."""
    if not os.path.exists(DESTINATION_FOLDER):
        os.makedirs(DESTINATION_FOLDER)

    for file_name in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file_name)

  
        if not file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

    
        date_taken = get_photo_date(file_path)
        if not date_taken:
            print(f"Skipping {file_name} (No date found)")
            continue

 
        year_folder = os.path.join(DESTINATION_FOLDER, str(date_taken.year))
        month_folder = os.path.join(year_folder, f"{date_taken.month:02d}_{date_taken.strftime('%B')}")

        os.makedirs(month_folder, exist_ok=True)

  
        shutil.move(file_path, os.path.join(month_folder, file_name))
        print(f"Moved {file_name} to {month_folder}")

organize_photos()
print("✅ Photos organized successfully!")
