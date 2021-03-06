# Hugo - UserBot
# Copyright (C) 2021 TeamHugoX
#
# This file is a part of < https://github.com/TeamHugoX/Hugo/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamHugoX/pyHugo/blob/main/LICENSE>.

from .. import udB


def get_stuff():
    a = udB.get("NIGHT_CHATS")
    if not a:
        return {}
    try:
        return eval(a)
    except BaseException:
        udB.delete("NIGHT_CHATS")
    return {}


def add_night(chat):
    chats = get_stuff()
    if chat not in chats:
        chats.append(chat)
        udB.set("NIGHT_CHATS", str(chats))
    return


def rem_night(chat):
    chats = get_stuff()
    if chat in chats:
        chats.remove(chat)
        udB.set("NIGHT_CHATS", str(chats))
    return


def night_grps():
    return get_stuff()
