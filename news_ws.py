import aiohttp
import asyncio
import json


async def test():
    session = aiohttp.ClientSession()
    ws = await session.ws_connect('wss://realtime-prod.wallstreetcn.com/ws')
    xxx = await ws.send_str(
        json.dumps({
            "command": 'ENTER_CHANNEL',
            "data": {
                "chann_name": 'baoer-msg-pc-724',
                "cursor": ''
            }
        }))
    await ws.send_str(json.dumps({"data": 'ping'}))
    i = 0
    while i < 10:
        await ws.send_str(json.dumps({"data": 'ping'}))
        msg = await ws.receive()
        print(msg, i)
        i += 1

    # async for msg in ws:
    #     if msg.type == aiohttp.WSMsgType.TEXT:
    #         if msg.data == 'close cmd':
    #             await ws.close()
    #             break
    #         else:
    #             print(msg.data)
    #             # await ws.send_str(msg.data + '/answer')
    #     elif msg.type == aiohttp.WSMsgType.ERROR:
    #         print(msg)
    #         break


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())