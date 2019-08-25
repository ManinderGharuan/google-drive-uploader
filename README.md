# Google Drive Uploader

Automatically downloads file from link and upload to google drive.

After file uploaded, file will be removed from system.

## Getting Started

### Prerequisites

To run this app, you need following pre-installed.

- Python 3.x and pip
  - Pre-installed on most Linux and mac
  - Download from [Python website](http://www.python.org/getit/) for windows

Create Google API Credentials
  - Create a project in [Google Developers Console](https://console.cloud.google.com/)
  - Create Credentials. Press on the burger menu in the toolbar and select "APIs and Services > Credentials".

### Installing

- Clone repository

  ```
  $ git clone https://github.com/ManinderGharuan/google-drive-uploader.git
  ```

- Move to the project directory and install requirements

  ```
  $ cd google-drive-uploader
  $ pip install -r requirements.txt
  ```

- Go to directory "settings" and open file "settings.yaml" in your favorite editor
  - Find "<your_client_id>" and replace it with google api client id

  - Find "<your_secret>" and replace it with google api secret

- Run script

  ```
  $ python3 main.py
  ```

## Specs

### Use Cases

#### John

John executes the program, and terminal will ask for direct url to upload on google drive. After providing direct link a progress bar will appear.

After download completion John's default browser will opens with a page of google authentication. John will login with his account in which he want to upload and google will ask for permissions.

After a while terminal stops with message "File Uploaded successfully" and "File removed successfully.

John likes to upload another link. So he again executes the program and provide link. Terminal will ask to upload in previous account, so he will see progress bar and terminal stops with message "File Uploaded successfully" and "File removed successfully.

## TODOS

* [X] Download content from url using wget
* [X] Do authentication using Google Auth
* [X] Upload file using Google Drive
* [X] Save user credentials
* [X] When credentials already saved then ask user to re-authenticate or upload to previous account
* [X] Update readme