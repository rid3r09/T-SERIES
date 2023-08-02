from geopy.geocoders import Nominatim
from telethon import *
from telethon.tl import *

from AloneRobot import *
from AloneRobot import telethn as tbot
from AloneRobot.events import register

GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"


@register(pattern="^/gps (.*)")
async def _(event):
    args = event.pattern_match.group(1)

    try:
        geolocator = Nominatim(user_agent="SkittBot")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
        gm = "https://www.google.com/maps/search/{},{}".format(latitude, longitude)
        await tbot.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(float(latitude), float(longitude))
            ),
        )
        await event.reply(
            "Open with: [🌏ɢᴏᴏɢʟᴇ ᴍᴀᴘs]({})".format(gm),
            link_preview=False,
        )
    except Exception as e:
        print(e)
        await event.reply("I can't find that")


__help__ = """
sᴇɴᴅs ʏᴏᴜ ᴛʜᴇ ɢᴘs ʟᴏᴄᴀᴛɪᴏɴ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ǫᴜᴇʀʏ...

 ❍ /ɢᴘs <ʟᴏᴄᴀᴛɪᴏɴ>*:* ɢᴇᴛ ɢᴘs ʟᴏᴄᴀᴛɪᴏɴ.

☆............𝙱𝚈 » [ᴛᴏxɪᴄ](https://t.me/NOOBS_ALWAYS_OP)............☆
"""

__mod_name__ = "📍gρѕ📍"
