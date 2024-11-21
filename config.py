from os.path import abspath

from dotenv import dotenv_values

env = dotenv_values(abspath(".env").replace("tests\\", ""))

db_config = {
    "user": "user",
    "password": "user",
    "database": "test",
    "host": "127.0.0.1",
    "port": "5432"
}
