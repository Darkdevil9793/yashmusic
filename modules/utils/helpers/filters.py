# Power By @darkdevil898 & @ALEXBADHACKER
# Join @darkdevil979 For More Update
# Join @darkdevil898 For Hack
# Join Our Chats @darkdevil979 & @darkdevil9793 

from typing import Union, List
from pyrogram import filters
from modules.config import COMMAND_PREFIXES


# ╔══╗╔══╗╔══╗╔══╗╔═╦╗╔══╗╔═╗╔╗─╔══╗╔═╦╗╔═╗╔═╗
# ║╔╗║╚╗╗║╚║║╝╚╗╔╝╚╗║║║╔╗║║╬║║║─║╔╗║╚╗║║║╦╝║╬║
# ║╠╣║╔╩╝║╔║║╗─║║─╔╩╗║║╠╣║║╔╝║╚╗║╠╣║╔╩╗║║╩╗║╗╣
# ╚╝╚╝╚══╝╚══╝─╚╝─╚══╝╚╝╚╝╚╝─╚═╝╚╝╚╝╚══╝╚═╝╚╩╝

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
