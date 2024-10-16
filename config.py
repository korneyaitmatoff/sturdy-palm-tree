from os.path import abspath

from dotenv import dotenv_values

env = dotenv_values(abspath(".env").replace("tests\\", ""))

db_config = {key.replace("PG_", "").lower(): env[key] for key in env if "PG_" in key}
