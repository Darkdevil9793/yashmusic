# Power By @darkdevil898 & @ALEXBADHACKER
# Join @darkdevil979 For More Update
# Join @darkdevil898 For Hack
# Join Our Chats @darkdevil979 & @darkdevil9793 

import os
import sys
from os import listdir, mkdir

from ..logging import LOGGER


def dirr():
    if "resource" not in listdir():
        LOGGER(__name__).warning(
            f"Assets Folder not Found. Please clone repository again."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
