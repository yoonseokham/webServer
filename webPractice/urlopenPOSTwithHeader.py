import urllib
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode
req=urllib.request.Request("http://www.example.com")
req.add_header("Content-Type","text/plain")
data=urllib.parse.urlencode({"query":"python"}).encode("utf-8")
req.data=data
f= urlopen("http://www.example.com",data)

print(f.read(500))
