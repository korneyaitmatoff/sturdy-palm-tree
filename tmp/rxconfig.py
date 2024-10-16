from os.path import isfile, abspath

import reflex as rx
from dotenv import dotenv_values

config = rx.Config(
    app_name="sturdy_palm_tree",
)

env = dotenv_values(abspath(".env").replace("tests\\", ""))

db_config = {key.replace("PG_", "").lower(): env[key] for key in env if "PG_" in key}
