from setuptools import setup, find_packages
import subprocess

def install_nbstripout():
  subprocess.run([
    "nbstripout",
    "--install",
    "--attributes", ".gitattributes",
    "--extra-keys", "kernelspec,metadata.language_info,widgets"
  ], check=True)

install_nbstripout()

setup(
  name='Project taml',
  version='0.1',
  packages=find_packages(),
  install_requires=[
    'geo_utils',
    'jupyter',
    'matplotlib',
    'mygene',
    'nbstripout',
    'numpy',
    'pandas',
    'pyreadr',
    'rpy2',
    'scipy',
    'seaborn',
  ],
)