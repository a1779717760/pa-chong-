import urllib.parse

url = 'http://www.baidu.conm/index.html'

name = 'goudan'
age = 18
sex = 'nv'
height = '180'

data ={
    'name' : name,
    'age' : age,
    'sex' : sex,
    'height' : height,
}
lt =[]
for k,v in data.items():
    lt.append(k + '=' + str(v))
query_string = '&'.join(lt)

url = url +'?' + query_string

print(url)


