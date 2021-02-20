# ex_download_pic.py
# write a func that receives a url and downloads
# pic to computer.
import random
import urllib.request

# urellib is a library in the request module
"""urlretrieve takes the pic that the url
leads to and copies it to a local file in my
computer.
!!! Retrieve a URL into a temporary location on disk.
urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)
1. url is required in the func - tmp file location
2. filename (defaults none)
3. ?
4. ?
if filename isnt passed it is saved in tmp location
if filename is passed and url points to a local file,
it is copied to a new file.
returns a tuple containing path to new file +
result of httpMessage object

returns (filename -- path to url in my comp, headers -- all data linked to url)
"""

def download_image(url):
    rand = random.randint(1, 1000)
    full_name = str(rand) + '.png'
    # randomises a pic name with number and png suffix
    urllib.request.urlretrieve(url, full_name)

download_image()

# find http download



