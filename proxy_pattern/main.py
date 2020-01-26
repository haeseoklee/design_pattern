from abc import ABCMeta, abstractmethod
import aiohttp
import asyncio
import time


class ProxyExample(metaclass=ABCMeta):

    @abstractmethod
    def fetch(self, url):
        pass


class HttpProxy(ProxyExample):

    def __init__(self):
        self.instance = None
        self.retrieving = False

    async def fetch(self, url):
        if self.instance:
            return self.instance.fetch(url)
        else:
            print('데이터를 가져오는 중입니다')
            if not self.retrieving:
                self.retrieving = True

                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as res:
                        assert res.status == 200, 'Error!!'
                        self.instance = HttpRequest()
                        text = await res.text()
                        self.instance.data[url] = text
                        return text


class HttpRequest(ProxyExample):

    def __init__(self):
        self.data = dict()

    def fetch(self, url):
        print('이미 가져온 데이터를 보여드립니다')
        return self.data[url]


async def main():
    urls = ['https://python.flowdas.com/library/asyncio-dev.html' for _ in range(15)]
    proxy = HttpProxy()
    data = await asyncio.gather(*[proxy.fetch(url) for url in urls])
    # print(data)
    print(len(data))
    data = await asyncio.gather(*[proxy.fetch(url) for url in urls])
    # print(data)
    print(len(data))



if __name__ == '__main__':
    asyncio.run(main())
