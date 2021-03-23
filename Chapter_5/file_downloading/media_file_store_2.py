import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

download_directory = 'downloaded'
base_url = 'http://pythonscraping.com'

def get_absolute_url(base_url, source):
    if source.startswith('http://www.') or source.startswith('https://'):
        url = 'http://' + source[11:]
    elif source.startswith('http://') or source.startswith('https://'):
        url = source
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://' + source
    else:
        url = base_url + '/' + source

    if base_url not in url:
        return None

    return url

def get_download_path(base_url, absolute_url, download_directory):
    path = absolute_url.replace('www.', '')
    path = path.replace(base_url, '')
    path = download_directory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return path

html = urlopen('http://www.pythonscraping.com')
bs_obj = BeautifulSoup(html)
download_list = bs_obj.find_all('img', src=True)

for download in download_list:
    file_url = get_absolute_url(base_url, download['src'])

    if file_url is not None:
        print(file_url)
        urlretrieve(file_url, get_download_path(base_url, file_url, download_directory))
