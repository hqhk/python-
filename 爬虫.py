from urllib import request
import re
url =r"https://search.jd.com/Search?keyword=%E5%8F%AF%E4%B9%90&enc=utf-8&wq=%E5%8F%AF%E4%B9%90&pvid=1d8b0c759d37414cbba4b30c0b0b8fd6"
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
# 1、创建请求对象，包装ua信息
req = request.Request(url=url,headers=headers)
# 2、发送请求，获取响应对象
res = request.urlopen(req)
# 3、提取响应内容
html = res.read().decode('utf-8')
pattern=re.compile('<em>￥</em><i data-price=".*?">(.*?)</i>',re.S)
re_list=pattern.findall(html)
print(re_list)
