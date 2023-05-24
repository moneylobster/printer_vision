from ffpp.Network import Network
import time
import asyncio
import urllib.request

async def main():
    # sol
    #pr=Network("192.168.0.189")
    # sag
    pr=Network("192.168.0.167")

    await pr.connect()
    await pr.sendAbortRequest()
    await pr.disconnect()


asyncio.run(main())