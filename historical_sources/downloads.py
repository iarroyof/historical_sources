import sysconfig
import gdown
import shutil
import os

cwd = str(sysconfig.get_paths()["purelib"]) + '/historical_sources'
nuevaruta = cwd + '/results_final'
def download_datasets():
    url1 = "https://drive.google.com/drive/folders/1HAkLPz2CgVlmYAFFu8lgbqFw3w58BF7n?usp=share_link"
    gdown.download_folder(url1, quiet=True, use_cookies=False)
    shutil.move('datasets',cwd)
    

def download(default=True,link=None):
    if default is True:
        url = "https://drive.google.com/drive/folders/1VLjR9oBWR8FoyTEsQbDGqbtQS8uEJ4u_?usp=share_link"
        gdown.download_folder(url, quiet=True, use_cookies=False)
        shutil.move('results_final',cwd)
    else:
        gdown.download_folder(link, quiet=True, use_cookies=False)
        shutil.move('results_final',cwd)



