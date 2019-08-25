from .GoogleRoot import GoogleRoot

class GoogleDrive(GoogleRoot):
  """
  Use google drive api
  e.g Upload file
  """
  def upload_file(self, gauth=None, fileMetadata=None):
    """
    Upload file to google drive
    Prints message after file uploaded
    """
    if fileMetadata is None:
      return
    
    if gauth is None:
      gauth = self.authentication()

    # TODO
    # Process to upload file

    print()
    print("File Uploaded successfully")