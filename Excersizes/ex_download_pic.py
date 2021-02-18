#ex_download_pic.py
#write a func that receives a url and downloads
#pic to computer.
import random
import urllib.request
#urellib is a library in the request module
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




def pic_name():
	"""randomises a pic name with number and png suffix"""
	rand = random.randint(1,1000)
	name = str(rand) + '.png'
	return name

print(pic_name())
#https problem
urllib.request.urlretrieve('http://she-codes.org/wp-content/uploads/2019/07/banner_she_con2019_center-01-1-1-1024x576.png', filename = pic_name)













