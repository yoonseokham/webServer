import urllib
from urllib.request import urlopen
from urllib.parse import urlencode
data=urllib.parse.urlencode({"query":"python"}).encode("utf-8")
f= urlopen("http://www.example.com",data)
print(f.read(500))
