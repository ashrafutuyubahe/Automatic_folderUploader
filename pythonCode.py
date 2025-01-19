import os
import time
import requests

# Folder where the camera saves the pictures
SOURCE_FOLDER = "/home/ashrafu/Documents/EMBEDDED_SYS"

# Upload endpoint
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

# Function to upload a file
def upload_file(filepath):
    try:
        with open(filepath, "rb") as file:
            files = {"imageFile": file}
            response = requests.post(UPLOAD_URL, files=files)
            if response.status_code == 200:
                print(f"Successfully uploaded: {os.path.basename(filepath)}")
                return True
            else:
                print(f"Failed to upload: {os.path.basename(filepath)}. Status Code: {response.status_code}")
                return False
    except Exception as e:
        print(f"Error uploading file {os.path.basename(filepath)}: {e}")
        return False

# Main loop
def main():
    while True:
        # List all files in the folder
        files = [os.path.join(SOURCE_FOLDER, f) for f in os.listdir(SOURCE_FOLDER) if os.path.isfile(os.path.join(SOURCE_FOLDER, f))]
        
        # Process each file
        for file in files:
            if upload_file(file):  # If upload is successful
                os.remove(file)   # Delete the file to avoid redundancy
                print(f"Deleted: {os.path.basename(file)}")
        
        # Wait for 30 seconds before checking the folder again
        time.sleep(30)

if __name__ == "__main__":
    main()
