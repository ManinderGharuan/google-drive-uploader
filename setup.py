from setuptools import setup

setup(
    name='google-drive-uploader',
    packages=['google-drive-uploader'],
    include_package_data=True,
    install_requires=[
      'pyDrive',
      'requests',
      'wget'
    ],
)