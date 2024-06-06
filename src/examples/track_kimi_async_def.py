import asyncio
import json

import aiohttp
import gradio as gr

from src.infra.token_mapper import select

url = 'https://kimi.moonshot.cn/api/chat/cp2vkrivk6g1dk1na440/completion/stream'

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTcxNjk4NzkzNywiaWF0IjoxNzE2OTg3MDM3LCJqdGkiOiJjcGJpOTdlNzY4ajVhNGpvdWlkZyIsInR5cCI6ImFjY2VzcyIsInN1YiI6ImNvYWhhbXFsbmw5M21mczJzbDQwIiwic3BhY2VfaWQiOiJjb2FoYW1xbG5sOTNtZnMyc2wzZyIsImFic3RyYWN0X3VzZXJfaWQiOiJjb2FoYW1xbG5sOTNtZnMyc2wzMCJ9.EMUjyqw_xG5qBRWFM26BDeSGDgztiRtqKXceVCF4gH-CL-aMyvKKPS0694KcQNc-pqMXccOtrUX3PE6rsrFx9Q',
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


async def sse_client(input):
    payload['messages'][0]['content'] = input
    token = select('kimi')
    headers['authorization'] = f'Bearer {token}'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers,
                                data=json.dumps(payload)) as response:
            result = ''
            while True:  # 可以在这里添加逻辑来处理接收到的数据
                try:
                    line = await response.content.readline()
                    if not line:
                        break
                    # 解析JSON数据
                    # print(line)
                    data_str = line.decode('utf-8').strip()
                    try:
                        if "auth.token.invalid" in data_str:
                            print("您的授权已过期，请重新登录")
                            return
                        line_json = data_str.split("data: ")[1]
                        data = json.loads(line_json)
                        if data['event'] == 'cmpl':
                            text_ = data['text']
                            print(text_, end='')
                            result = result + text_
                            yield result
                    except Exception as err:
                        continue
                except asyncio.CancelledError as err:
                    print(err)
                    break

iface = gr.Interface(fn=sse_client, inputs="text", outputs=gr.Textbox(),
                     # live=True,
                     theme="soft",
                     title="ChengChat GPT",
                     description="利用gradio库做页面，抓包kimi返回数据")
iface.launch(share=True)
