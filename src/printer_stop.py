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
    await pr.sendControlRelease()

    try:
        while True:
            print(await pr.sendProgressRequest())
            print(await pr.sendPositionRequest())
            urllib.request.urlretrieve(f"http://{pr.ip}:8080/?action=snapshot", "camimg.jpg")
            time.sleep(5)
    finally:
        await pr.disconnect()


asyncio.run(main())