from os.path import join, dirname, abspath
from pydrive.auth import GoogleAuth

class GoogleRoot():
  """
  Root methods of google api
  e.g Authentication with google api
  """
  def __init__(self):
    self.settings_file = join(dirname(abspath('__main__')), 'settings', 'settings.yaml')

  def authentication(self):
    """
    Do google authentication using pydrive
    Returns gauth
    """
    gauth = GoogleAuth(settings_file=self.settings_file)

    return gauth