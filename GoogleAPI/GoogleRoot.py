from os.path import join, dirname, abspath, exists
from os import remove
from sys import stdout
from pydrive.auth import GoogleAuth

class GoogleRoot():
  """
  Root methods of google api
  e.g Authentication with google api
  """
  def get_settings_file(self):
    """
    Returns settings file
    """
    return join(dirname(abspath('__main__')), 'settings', 'settings.yaml')
  
  def get_client_secret_file(self):
    """
    Returns user secret file
    """
    return join(dirname(abspath('__main__')), 'client_secret.json')

  def query_yes_no(self, question, default="yes"):
    """
    Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}

    if default is None:
      prompt = " [y/n] "
    elif default == "yes":
      prompt = " [Y/n] "
    elif default == "no":
      prompt = " [y/N] "
    else:
      raise ValueError("invalid default answer: '%s'" % default)

    while True:
      stdout.write(question + prompt)

      choice = input().lower()

      if default is not None and choice == '':
        return valid[default]
      elif choice in valid:
        return valid[choice]
      else:
        stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")
    
  def ask_for_reAuthentication(self):
    """
    Ask user to delete old secret and add new
    """
    if exists(self.get_client_secret_file()):
      re_auth = self.query_yes_no("Do you want to upload in previous account?")

      if not re_auth:
        remove(self.get_client_secret_file())

  def authentication(self):
    """
    Do google authentication using pydrive
    Returns gauth
    """
    self.ask_for_reAuthentication()

    gauth = GoogleAuth(settings_file=self.get_settings_file())

    return gauth
