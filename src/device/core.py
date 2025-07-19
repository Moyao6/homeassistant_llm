from hassapi import Hass
from conf.core_conf import conf
core = Hass(hassurl=conf["ip"], token=conf["token"])
