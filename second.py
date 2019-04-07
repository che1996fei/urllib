import urllib.request
import urllib.parse

# 最基本的请求
request = urllib.request.Request('https://www.python.org/')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

# 传入多个参数构建
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Host': 'httpbin.org'
        }
dict = {
    'name': 'Germey'
        }
data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))



