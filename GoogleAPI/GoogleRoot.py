from pydrive.auth import GoogleAuth

class GoogleRoot():
  """
  Root methods of google api
  e.g Authentication with google api
  """
  def authentication(self):
    """
    Do google authentication using pydrive
    Returns gauth
    """
    gauth = GoogleAuth()

    return gauth