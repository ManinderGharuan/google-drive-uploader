from os import path, mkdir, remove
from wget import download

class RootDownloader():
  """
  Download data from given link
  """

  def __init__(self, link):
    self.link = link

  def get_link(self):
    """
    Returns User Link
    """
    return self.link

  def get_download_path(self):
    """
    Returns directory path
    """
    download_path = path.join(path.dirname(
        path.abspath('__main__')), 'Downloader', 'content')

    if not path.exists(download_path):
      mkdir(download_path)

    return download_path

  def download(self):
    """
    Download content from url 
    returns path of the files
    """
    url = self.get_link()
    download_path = self.get_download_path()
    local_url = None

    try:
      print()
      print("Downloading Content...")

      local_url = download(url, out=download_path)
    except Exception as error:
      print("Faild to download: ", url)
      print(error)

    return local_url

  def delete_file(self, path_to_file):
    """
    Deletes file from system
    Prints message after file deleted
    """
    if (path.exists(path_to_file)):
      remove(path_to_file)

    print()
    print("File removed successfully")