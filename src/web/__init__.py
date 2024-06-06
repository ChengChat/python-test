import aiohttp
import asyncio


async def fetch_events(session, url):
    async with session.get(url, headers={
        'Accept': 'text/event-stream',
        # 添加其他必要的 headers
    }) as response:
        if response.status != 200:
            print('Server returned an error:', response.status)
            return

        print('Server is sending events...')
        async for event in response.content:
            if event:
                data = event.decode()
                print('Received event:', data)


async def main():
    url = 'http://127.0.0.1:5000/api/text_stream'
    async with aiohttp.ClientSession() as session:
        await fetch_events(session, url)


# 运行事件循环
asyncio.run(main())