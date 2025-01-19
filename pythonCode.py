import os
import time
import subprocess
from shutil import move

SOURCE_DIR = "/home/ashrafu/Documents/EMBEDDED_SYS"
DEST_DIR = os.path.join(SOURCE_DIR, "uploaded")
UPLOAD_ENDPOINT = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

os.makedirs(os.path.normpath(DEST_DIR), exist_ok=True)

def upload_image(image_path):
    try:
        result = subprocess.run(
            ["curl", "-X", "POST", "-F", f"imageFile=@{image_path}", UPLOAD_ENDPOINT],
            capture_output=True,
            text=True
        )
        print(f"stdout: {result.stdout}")
        print(f"stderr: {result.stderr}")
        print(f"Return code: {result.returncode}")
        
        if result.returncode == 0 and "200" in result.stdout:
            print(f"Upload successful: {image_path}")
            return True
        else:
            print(f"Upload failed for {image_path}.")
            return False
    except Exception as e:
        print(f"Error during upload for {image_path}: {e}")
        return False

def watch_directory():
    print(f"Watching directory: {SOURCE_DIR}")
    while True:
        try:
            files_to_upload = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            for file_name in files_to_upload:
                image_path = os.path.join(SOURCE_DIR, file_name)
                if time.time() - os.path.getmtime(image_path) >= 30:
                    if upload_image(image_path):
                        move(image_path, os.path.join(DEST_DIR, file_name))
                        print(f"Moved file to uploaded folder: {file_name}")
        except Exception as e:
            print(f"Error in monitoring loop: {e}")
        time.sleep(10)

if __name__ == "__main__":
    watch_directory()
