import asyncio
import time

import aiohttp
import requests
import json

#
# curl 'https://kimi.moonshot.cn/api/auth/token/refresh' \
#   -H 'accept: */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTcyNDc2MTc0NSwiaWF0IjoxNzE2OTg1NzQ1LCJqdGkiOiJjcGJodjRiM2Flc3Vob2JrNDlpMCIsInR5cCI6InJlZnJlc2giLCJzdWIiOiJjb2FoYW1xbG5sOTNtZnMyc2w0MCIsInNwYWNlX2lkIjoiY29haGFtcWxubDkzbWZzMnNsM2ciLCJhYnN0cmFjdF91c2VyX2lkIjoiY29haGFtcWxubDkzbWZzMnNsMzAifQ.9S1AF787iwlA819MoN8xeexJQZvnXdtNyyiUXLKgeEXcaEA68_Cj9Kf6cFQOyZYOZ6hh88mIVi7LV9mSwZu7Yw' \
#   -H 'cookie: Hm_lvt_358cae4815e85d48f7e8ab7f3680a74b=1716262953; _ga=GA1.1.392308330.1716262954; _gcl_au=1.1.661196205.1716262954; _clck=sf05ux%7C2%7Cfm5%7C0%7C1591; _ga_YXD8W70SZP=GS1.1.1716880055.5.1.1716880388.0.0.0; Hm_lpvt_358cae4815e85d48f7e8ab7f3680a74b=1716880389' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://kimi.moonshot.cn/chat/cp80mntvbf6p2f1q2900' \
#   -H 'sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'

url = 'https://kimi.moonshot.cn/api/chat/cp2vkrivk6g1dk1na440/completion/stream'

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTcxNjk4NzkzNywiaWF0IjoxNzE2OTg3MDM3LCJqdGkiOiJjcGJpOTdlNzY4ajVhNGpvdWlkZyIsInR5cCI6ImFjY2VzcyIsInN1YiI6ImNvYWhhbXFsbmw5M21mczJzbDQwIiwic3BhY2VfaWQiOiJjb2FoYW1xbG5sOTNtZnMyc2wzZyIsImFic3RyYWN0X3VzZXJfaWQiOiJjb2FoYW1xbG5sOTNtZnMyc2wzMCJ9.EMUjyqw_xG5qBRWFM26BDeSGDgztiRtqKXceVCF4gH-CL-aMyvKKPS0694KcQNc-pqMXccOtrUX3PE6rsrFx9Q',
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

question = "你能做点什么"
payload = {
    "messages": [
        {"role": "user", "content": question}],
    "refs": [],
    "use_search": False,
    "kimiplus_id": "kimi"
}

print(question)


async def sse_client():
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers,
                                data=json.dumps(payload)) as response:
            while True:  # 可以在这里添加逻辑来处理接收到的数据
                try:
                    line = await response.content.readline()
                    if line:
                        # 解析JSON数据
                        # print(line)
                        data_str = line.decode('utf-8').strip()
                        try:
                            if "auth.token.invalid" in data_str:
                                print("您的授权已过期，请重新登录")
                                return
                            line_json = data_str.split("data: ")[1]
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
                                correctly_encoded_str = wrong_encoded_bytes.decode(
                                    'utf-8')
                                print(correctly_encoded_str, end='')
                            except Exception as err:
                                print(text_, end='')

                except asyncio.CancelledError as err:
                    print(err)
                    break

asyncio.run(sse_client())