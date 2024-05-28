import os
import subprocess

import requests


# 定义要调用的curl命令
curl_command = '''
curl 'https://chatglm.cn/chatglm/backend-api/assistant/stream' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZTUxNGU4MDg4NmY0OWMwOTI5MGI0ZjZhYzdkZGVmNSIsImV4cCI6MTcxNjYzMTk3NywibmJmIjoxNzE2NTQ1NTc3LCJpYXQiOjE3MTY1NDU1NzcsImp0aSI6ImNlYTUxODk1MTI5NzRjZGZhNTFiYzgxY2FmOGU1NjVjIiwidWlkIjoiNjYwMTcyNDZlN2UxZTAxNWYzNDY4MDIyIiwidHlwZSI6ImFjY2VzcyJ9.UWdMSQHLcLCNt5rk-7EAXjKXrh9ar8569Xn8NOddHxY' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: chatglm_refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNTg1NjE1MSwianRpIjoiYjdlOWJjYzgtNmZiYi00MzkzLTg4ZGMtMzUyMWFjMWVjZThkIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiJlZTUxNGU4MDg4NmY0OWMwOTI5MGI0ZjZhYzdkZGVmNSIsIm5iZiI6MTcxNTg1NjE1MSwiZXhwIjoxNzMxNDA4MTUxLCJ1aWQiOiI2NjAxNzI0NmU3ZTFlMDE1ZjM0NjgwMjIiLCJ1cGxhdGZvcm0iOiJpT1MiLCJyb2xlcyI6WyJ1bmF1dGhlZF91c2VyIl19.iuKQp8HjB2srG_h6xTKk8Ho5tCWIIn1yo8EzhgcGfWc; chatglm_user_id=66017246e7e1e015f3468022; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2266017246e7e1e015f3468022%22%2C%22first_id%22%3A%2218f86a57b50271d-0d610ff16439078-1b525637-1484784-18f86a57b5128a6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22_latest_wx_ad_click_id%22%3A%22%22%2C%22_latest_wx_ad_hash_key%22%3A%22%22%2C%22_latest_wx_ad_callbacks%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmODZhNTdiNTAyNzFkLTBkNjEwZmYxNjQzOTA3OC0xYjUyNTYzNy0xNDg0Nzg0LTE4Zjg2YTU3YjUxMjhhNiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjY2MDE3MjQ2ZTdlMWUwMTVmMzQ2ODAyMiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2266017246e7e1e015f3468022%22%7D%2C%22%24device_id%22%3A%2218f86a57b50271d-0d610ff16439078-1b525637-1484784-18f86a57b5128a6%22%7D; _ga=GA1.1.226690994.1715950943; chatglm_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZTUxNGU4MDg4NmY0OWMwOTI5MGI0ZjZhYzdkZGVmNSIsImV4cCI6MTcxNjU0NTMwNSwibmJmIjoxNzE2NDU4OTA1LCJpYXQiOjE3MTY0NTg5MDUsImp0aSI6IjhjM2I1ZjIwOWE4YTRmNGY5NWU0ZGUzNmFlMjgxODVkIiwidWlkIjoiNjYwMTcyNDZlN2UxZTAxNWYzNDY4MDIyIiwidHlwZSI6ImFjY2VzcyJ9.-mmJW63Cy6QcYLwDbsM_atxsOVxYrUENlPWJf6rzNR0; chatglm_token_expires=2024-05-23%2020:08:25; _ga_PMD05MS2V9=GS1.1.1716530302.6.0.1716530302.0.0.0; acw_tc=2760775017165401401086098e394a73933a75fe9942497c48edb493236d83' \
  -H 'Origin: https://chatglm.cn' \
  -H 'Referer: https://chatglm.cn/main/alltoolsdetail' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' \
  -H 'accept: text/event-stream' \
  -H 'sec-ch-ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw '{"assistant_id":"65940acff94777010aa6b796","conversation_id":"66502c865cc0b0919f1fa1ff","meta_data":{"mention_conversation_id":"","is_test":false,"input_question_type":"xxxx","channel":"","draft_id":"","quote":""},"messages":[{"role":"user","content":[{"type":"text","text":"1+1"}]}]}'
'''

# 使用subprocess运行curl命令
result = subprocess.run(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 输出结果
print(result.stdout)
