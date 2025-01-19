# Automatic Image Uploader

This project automatically uploads images from a specified directory to a remote server. 
It monitors the directory for new image files, waits for 30 seconds after each image is added, uploads it to a remote server, and then moves the file to an "uploaded" folder to avoid re-uploading.

## Features

Monitors a directory for new images (.png, .jpg, .jpeg).
Waits 30 seconds before uploading each image.
Uploads images to a remote server using the curl command.
Moves successfully uploaded images to an "uploaded" folder.


## Requirements
you should have  atleast Python 3.x
=> curl installed on your system

## Setup
Clone or download the repository.

Modify the SOURCE_DIR and DEST_DIR in the script to match your local directories.
Update the UPLOAD_ENDPOINT with the correct URL for your server.

Run the script:
=>python3 upload_images.py

## Notes
The script only uploads images with .png, .jpg, or .jpeg extensions.
Ensure the destination folder for uploaded files exists or will be automatically created.


## License
This project is licensed under the MIT License.

