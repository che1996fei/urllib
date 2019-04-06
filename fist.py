import urllib.parse
import urllib.request
import socket
import urllib.error
#在命名名称时不要用库的名，会导致库无效化

#urlopen
# response = urllib.request.urlopen('https://www.python.org/')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# print(type(response))
# print(response.read().decode('utf-8'))

#urlopen+data
# data = bytes(urllib.parse.urlencode({'word': 'hello'}).encode('utf8'))
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

#urlopen+timeout
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
    print(response.read())
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
