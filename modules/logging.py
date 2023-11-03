# Power By @darkdevil898 & @ALEXBADHACKER
# Join @darkdevil979 For More Update
# Join @darkdevil898 For Hack
# Join Our Chats @darkdevil979 & @darkdevil9793 

import logging
from logging.handlers import RotatingFileHandler

from modules.config import LOG_FILE_NAME

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME, maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


# Power By @darkdevil898 & @ALEXBADHACKER
# Join @darkdevil979 For More Update
# Join @darkdevil898 For Hack
# Join Our Chats @darkdevil979 & @darkdevil9793 