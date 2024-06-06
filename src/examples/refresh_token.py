import time

import requests

from src.infra.token_mapper import update

# 刷新token的API地址
REFRESH_TOKEN_URL = 'https://kimi.moonshot.cn/api/auth/token/refresh'

# 旧的Bearer token
OLD_BEARER_TOKEN = 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTcyNDc2MTc0NSwiaWF0IjoxNzE2OTg1NzQ1LCJqdGkiOiJjcGJodjRiM2Flc3Vob2JrNDlpMCIsInR5cCI6InJlZnJlc2giLCJzdWIiOiJjb2FoYW1xbG5sOTNtZnMyc2w0MCIsInNwYWNlX2lkIjoiY29haGFtcWxubDkzbWZzMnNsM2ciLCJhYnN0cmFjdF91c2VyX2lkIjoiY29haGFtcWxubDkzbWZzMnNsMzAifQ.9S1AF787iwlA819MoN8xeexJQZvnXdtNyyiUXLKgeEXcaEA68_Cj9Kf6cFQOyZYOZ6hh88mIVi7LV9mSwZu7Yw'

# 请求头
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': f'Bearer {OLD_BEARER_TOKEN}',
    'cookie': 'Hm_lvt_358cae4815e85d48f7e8ab7f3680a74b=1716262953; _ga=GA1.1.392308330.1716262954; _gcl_au=1.1.661196205.1716262954; _clck=sf05ux%7C2%7Cfm5%7C0%7C1591; _ga_YXD8W70SZP=GS1.1.1716880055.5.1.1716880388.0.0.0; Hm_lpvt_358cae4815e85d48f7e8ab7f3680a74b=1716880389',
    'priority': 'u=1, i',
    'referer': 'https://kimi.moonshot.cn/chat/cp80mntvbf6p2f1q2900',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}



def refresh_token():
    # 发送请求来获取新的token

    # 发送POST请求来刷新token
    response = requests.get(REFRESH_TOKEN_URL, headers=headers)

    # 检查响应状态码
    if response.status_code == 200:
        # 如果响应成功，打印新的token
        access_token = response.json().get('access_token')
        refresh_token = response.json().get('refresh_token')
        print(f'新的token是: {access_token}')
        update('kimi', access_token, refresh_token)
    else:
        print(f'刷新token失败，状态码: {response.status_code}')

# 每隔10分钟调用一次refresh_token函数
while True:
    refresh_token()
    time.sleep(10 * 60)  # 10分钟间隔
