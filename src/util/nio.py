import aiohttp
import asyncio

async def sse_client(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            while True:
                try:
                    data = await response.content.readline()
                    if not data:
                        break
                    data_str = data.decode('utf-8').strip()
                    if data_str:
                        print(data_str)
                except asyncio.CancelledError:
                    break

async def main():
    url = 'http://example.com/events'  # 替换为您的SSE端点
    await sse_client(url)

if __name__ == '__main__':
    asyncio.run(main())


