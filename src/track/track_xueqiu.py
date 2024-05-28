import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Cookie': 'xq_a_token=ea6ef3abf0b64fa4ec4343c5608361ed54114204; xqat=ea6ef3abf0b64fa4ec4343c5608361ed54114204; xq_r_token=38fbe8417b7b1b21f8f4c0a40a8e75e1f538990a; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxNzU0ODcxMCwiY3RtIjoxNzE1ODU1MDYwMTk4LCJjaWQiOiJkOWQwbjRBWnVwIn0.rKAaJp2zqZfST0-LtZhAwAiNh4Et2beNsriVq8DHZsuSc_UD1GWPvQbEBgPanfDYVL9E1L6wbTsDNgdhNtQTkayeHgaSKPFqFw5SyUO4YSg54qLNiWcMTAHhRXomJKvVUCJPuEBiC9CXB-e6wnF4ACiudxs0TZn-BxdAaltYwKnLksxwY3Ugb0uGb1aTN7pDN5KFWKwT5_ZrxjUKw6eNNA-aXoQ5SdGUBBlgNJnVKiXU3y6ni0Rh2UScjXMlHvK8qwyVD4_A0h0lKVsYoZMlYQK0-ghYijhNdfeVj-y7ML1feLlIsHrj1G9Q7gmIv5pqOL6C7SaOnvwizjjKk-TGvg; cookiesu=571715855062650; u=571715855062650; Hm_lvt_1db88642e346389874251b5a1eded6e3=1715855063; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1715855063; device_id=2eed57e4cf7a8417b83ed8cf299e2d05',
}
url = 'https://xueqiu.com/query/v1/search/web/stock.json'


def track(symbol):
    params = {
        "q": symbol, "size": 1, "page": 1
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        # 打印返回的结果
        print(response.text)
        print(response.json()['list'][0])
        print(response.json()['list'][0]['current'])


track("AAPL")
