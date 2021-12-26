# Hugo - UserBot
# Copyright (C) 2021 TeamHugoX
#
# This file is a part of < https://github.com/TeamHugoX/Hugo/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamHugoX/pyHugo/blob/main/LICENSE>.

from .. import udB


def get_stuff(key="USERNAME_DB"):
    kk = udB.get(key)
    if not kk:
        return {}
    try:
        return eval(kk)
    except BaseException:
        udB.delete(key)
    return {}


def update_username(id, uname):
    ok = get_stuff()
    ok.update({id: uname})
    udB.set("USERNAME_DB", str(ok))


def get_username(id):
    ok = get_stuff()
    if ok.get(id):
        return ok[id]
    return None
