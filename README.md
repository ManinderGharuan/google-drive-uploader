# Google Drive Uploader

Automatically downloads file from link and upload to google drive.
After file uploaded file will be removed from system.

## Setup

```
$ pip install -r ./requirements.txt
```

## Specs

### Use Cases

#### John

John executes the program, and terminal will ask for direct url to upload on google drive. After providing direct link a progress bar will appear.

After download completion John's default browser will opens with a page of google authentication. He will login with his account in which he want to upload and google will ask for permissions.

After a while terminal stops with message "File Uploaded successfully" and "File removed successfully.

John likes to upload another link. So he again executes the program and provide link. His authentication is already completed, so he will see progress bar and terminal stops with message "File Uploaded successfully" and "File removed successfully.

## TODOS

* [X] Download content from url using wget
* [X] Do authentication using Google Auth
* [X] Upload file using Google Drive
* [ ] Save user credentials
* [ ] When credentials already saved then ask user to re-authenticate or upload to previous account
* [ ] Update readme