from discord.ext import commands
import requests
import asyncio
import discord
import json
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

client1 = commands.Bot(command_prefix='!')
client2 = commands.Bot(command_prefix='!')
client3 = commands.Bot(command_prefix='!')

url = 'https://api.scpslgame.com/serverinfo.php?format=json'
ids = [18257, 17909, 18289]
keys = ['CENSORED :/', 'CENSORED :/', 'CENSORED :/']
client_list = [client1, client2, client3]

time_now = None


def set_time():
    global time_now
    now_local = datetime.now().astimezone()
    time_normal = f"{now_local.isoformat(timespec='seconds')}"
    time_temp = time_normal[11:]
    time_now = time_temp[:-6]


@client1.event
async def on_ready():
    print("Ready!\n======================")

    while True:

        set_time()

        for i in range(0, 3):

            response = requests.get(url=url, params={'id': ids[i], 'key': keys[i], 'players': True,
                                                     'online': True}).content.decode("utf-8")  # decoded response
            jsonresp = json.loads(response)  # json response

            success, player_count, error = None, None, None
            success = jsonresp["Success"]

            if jsonresp["Success"]:  # if Server Online

                try:

                    player_count = jsonresp.get("Servers")[0].get("Players")
                    print("Players:", player_count)
                    await client_list[i].change_presence(
                        activity=discord.Activity(type=discord.ActivityType.watching, name=player_count))
                except:
                    print("Something went wrong!\n")
                    print(jsonresp)

            else:

                try:
                    error = jsonresp.get("Error")
                    print("Error:", error)
                    await client_list[i].change_presence(status=discord.Status.offline)
                except:
                    print("Something went wrong!\n")
                    print(jsonresp)

            i += 1

        print("\nAt:", time_now)
        print("==============================================")

        await asyncio.sleep(15)


loop = asyncio.get_event_loop()

loop.create_task(client1.start('CENSORED :/'))  # <- SCP Bot1
loop.create_task(client2.start('CENSORED :/'))  # <- SCP Bot1
loop.create_task(client3.start('CENSORED :/'))  # <- SCP Bot3