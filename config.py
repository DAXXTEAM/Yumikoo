import os
from os import getenv


API_ID = int(getenv("API_ID", "22729446"))
API_HASH = getenv("API_HASH", "54b64d721cdcf9332921d8b1224b5fdb")
BOT_USERNAME = getenv("BOT_USERNAME", "Bot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6441904586:AAFOLaFbuly1gh-xfuPfCnVvhEtYEcFRsMs")
OWNER_ID = int(getenv("OWNER_ID", "6906607945"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6906607945").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://randi:randi@cluster0.rwqgb4m.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQC-RUMKW0CBMWCwrMU1c9kvF0os5vdUOOBYcaDKN6jsGd116SGpE4N26iZmM-zSFLRar6T7TEPb6LXgqEQqt_nZ04oIMInuxh5FYl8u5pe9zQ8c-o12iXTZ_4RT_29lHyzGB3E6D3-iacx0RBdkXcYa-cX6zqqxAM83_8qvD43TJQG5dQ6ZcUXY7tlRZiA3rQ88s6jP-kJjqMVahQSEaua35ja0t7ub4CKtbBitj-D_lvfR3RXEew6fyTNE_xO1EIfwbJTG7QLEO0ydRyHErlgBbvy94peQwTejVw84T02-wsTBJA5pthxyPahaEubC2no0PdHLQWRjI8NSsb5HiaHfAAAAAZuqeUkA")
