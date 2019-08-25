#!/usr/bin/env python

from Downloader import RootDownloader
from GoogleAPI import GoogleDrive

url = input("Give me file link to upload on google drive and make sure it is an direct link: \n")

try:
  gdrive = GoogleDrive()
  gauth = gdrive.authentication()

  downloader = RootDownloader(url)

  file_path = downloader.download()

  if not file_path:
    print("Error while downloading file...")
  else:
    gdrive.upload_file(gauth=gauth, fileMetadata=file_path)

    downloader.delete_file(file_path)
except Exception as error:
  print("There is an error while processing.")
  print(error)