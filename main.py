import sys
from config.neoconfig import NeoConfig
from bot.neo import Neo

if __name__ == "__main__":

    if sys.version_info.major < 3 and sys.version_info.minor < 10:
        print(f"Python version must be minimum 3.10. Currently detected version: "
              f"{str(sys.version_info.major) + '.' + str(sys.version_info.minor)}")
        exit(1)


    data = NeoConfig()

    if data.token is None or len(data.token) == 0:
        print("Empty token, exiting")
        exit(1)

    neo = Neo(test_guilds=[data.guildId])

    neo.run(data.token)

    data.token = ""
