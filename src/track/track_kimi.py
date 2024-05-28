import time

import requests
import json

url = 'https://kimi.moonshot.cn/api/chat/cp2vkrivk6g1dk1na440/completion/stream'

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTcxNjU0MjYyMywiaWF0IjoxNzE2NTQxNzIzLCJqdGkiOiJjcDg1aTZwcDJrMWNzNWJzZzZoMCIsInR5cCI6ImFjY2VzcyIsInN1YiI6ImNvYWhhbXFsbmw5M21mczJzbDQwIiwic3BhY2VfaWQiOiJjb2FoYW1xbG5sOTNtZnMyc2wzZyIsImFic3RyYWN0X3VzZXJfaWQiOiJjb2FoYW1xbG5sOTNtZnMyc2wzMCJ9.0ECvv11I4EMQSMezsZXyR7Wq40w1-GklMw_lvc3U1meeNeWUclJhTj-iWDfk3ff4oVY4hdZEr4nSafnloRVrUQ',
    'content-type': 'application/json',
    'cookie': 'Hm_lvt_358cae4815e85d48f7e8ab7f3680a74b=1716262953; _ga=GA1.1.392308330.1716262954; _gcl_au=1.1.661196205.1716262954; _clck=sf05ux%7C2%7Cfly%7C0%7C1591; Hm_lpvt_358cae4815e85d48f7e8ab7f3680a74b=1716281443; _ga_YXD8W70SZP=GS1.1.1716281442.2.1.1716281444.0.0.0; _clsk=16ewohd%7C1716281445297%7C2%7C0%7Ci.clarity.ms%2Fcollect',
    'origin': 'https://kimi.moonshot.cn',
    'priority': 'u=1, i',
    'r-timezone': 'Asia/Shanghai',
    'referer': 'https://kimi.moonshot.cn/chat/cp2vkrivk6g1dk1na440',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-msh-platform': 'web',
    'x-traffic-id': 'coahamqlnl93mfs2sl40'
}

data = {
    "messages": [
        {"role": "user", "content": "写一段python代码"}],
    "refs": [],
    "use_search": False,
    "kimiplus_id": "kimi"
}

response = requests.post(url, headers=headers, json=data)

# 打印响应的文本内容
# 检查请求是否成功
if response.status_code == 200:
    # 获取响应内容
    stream = response.text
    # 解析响应内容
    for line in stream.splitlines():
        if line:
            # 解析JSON数据
            # print(line)
            try:
                line_json = line.split("data: ")[1]
                data = json.loads(line_json)
            except Exception as err:
                continue
            # print(data)
            if data['event'] == 'cmpl':
                text_ = data['text']
                try:
                    # 将字符串转换为ISO-8859-1编码的字节串
                    wrong_encoded_bytes = text_.encode('latin1')

                    # 假设正确的编码是UTF-8，现在我们使用UTF-8解码
                    correctly_encoded_str = wrong_encoded_bytes.decode('utf-8')
                    print(correctly_encoded_str)
                except Exception as err:
                    print(text_, end='')

else:
    print("Error:", response)
