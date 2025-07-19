import sys
sys.path.append('./src')
from device.core import core
import json
import time
from statistic.statistic import *

class AISpeaker:
    def __init__(self, core, conf):
        self.core = core
        self.speaker_e = conf["speaker"]
        self.cmd_e = conf["cmd"]
        self.volume_e = conf["volume"]
        self.unique_name = conf["unique_name"]
        self.area = conf['area']
        self.status()
        
    def set_volume(self, value=None, pct=None):
        if value is not None:
            self.core.call_service("set_value", entity_id = self.volume_e, value = value)
        elif pct is not None:
            self.core.call_service("set_value", entity_id = self.volume_e, value = pct)
    
    def set_volume_relative(self, value=None, pct=None):
        self.status()
        cur_volume = self.volume
        max_volume = self.max_volume
        min_volume = self.min_volume
        if value is not None:
            self.core.call_service("set_value", entity_id = self.volume_e, value = max(min_volume,min(max_volume,cur_volume+value)))
        elif pct is not None:
            self.core.call_service("set_value", entity_id = self.volume_e, value = max(min_volume,min(max_volume,cur_volume+pct*max_volume)))
        
    def use_speaker_to_command(self, cmd, need_response=False):
        need_silence = not need_response
        self.core.call_service('send_message', entity_id=self.cmd_e, message=json.dumps([cmd, need_silence]))
        
    def speak(self, sentence):
        core.call_service('send_message', entity_id=self.speaker_e, message=sentence)
        
    def status(self):
        try:
            status = self.core.get_state(self.volume_e)
            self.volume = int(status.state)
            self.max_volume = int(status.attributes['max'])
            self.min_volume = int(status.attributes['min'])
            self.on_work = True
        except Exception as e:
            self.volume = -1
            self.max_volume = -1
            self.min_volume = -1
            self.on_work = False
        res = {
            "volume": self.volume,
            "max_volume": self.max_volume,
            "min_volume": self.min_volume,
            "on_work": self.on_work
        }
        self.volume_s = submit_statistic(self.unique_name+'_volume', self.volume)
        self.on_work_s = submit_statistic(self.unique_name+'_on_work', self.on_work)
        return res

if __name__ == "__main__":
    from conf.ai_speaker_conf import conf
    test = AISpeaker(core, conf[0])
    test.speak("你好")
    print(test.status())
    test.set_volume_relative(pct = 0.3)
    time.sleep(5)
    print(test.status())
    # test.set_volume(10)
    # test.speak("你好")
    # time.sleep(5)
    # print(test.status())
    # test.set_volume(35)
    # test.speak("你好")
    # time.sleep(5)
    # test.use_speaker_to_command("打开卫生间灯",True)
    # time.sleep(5)
    # test.use_speaker_to_command("关闭卫生间灯",False)

