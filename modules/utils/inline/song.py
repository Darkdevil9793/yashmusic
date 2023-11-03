# Power By @darkdevil898 & @ALEXBADHACKER
# Join @darkdevil979 For More Update
# Join @darkdevil898 For Hack
# Join Our Chats @darkdevil979 & @darkdevil9793 

from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons



# Power By @darkdevil898 & @ALEXBADHACKER
# Join @darkdevil979 For More Update
# Join @darkdevil898 For Hack
# Join Our Chats @darkdevil979 & @darkdevil9793 