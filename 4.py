import urllib.request
import urllib.parse

url = 'http://www.baidu.com/'

headers={
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 73.0.3683.86Safari / 537.36'
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode())