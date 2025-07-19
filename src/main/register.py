#在此注册新设备，如果设备不能很好的兼容，需要新增设备py
import sys
sys.path.append("/home/weis/daemon/homecopilot/device")
from light import *
from lyj import *
from pc import *
from conditioner import *
from player import *
from person import *
from tv import *
def regist():
    return {
        "客厅电视": TV(short_id = 0, area = ["客厅东侧"], nickname = ["TCL"], entity_id = "media_player.android_tv_192_168_3_11"),
        "客厅电视灯": Light(short_id = 1, area = ["客厅东侧", "电视上方"], nickname = ["射灯"], entity_id = "light.ke_ting_dian_shi_deng_zu"),
        "客厅移门灯": Light(short_id = 2, area = ["客厅南侧", "移门上方", "靠近次卧"], nickname = ["筒灯"], entity_id = "light.ke_ting_yi_men_deng_zu"),
        "客厅沙发灯": Light(short_id = 3, area = ["客厅西侧", "沙发上方"], nickname = ["射灯"], entity_id = "light.ke_ting_sha_fa_deng_zu"),
        "客厅灯带": Light(short_id = 4, area = ["客厅一周"], nickname = ["灯带"], entity_id = "light.ccb5d1ec01dd_light"),
        "客厅小爱": Player(short_id = 9, area = ["客厅"], nickname = ["小爱同学"], entity_id = "media_player.xiaomi_l05c_3092_play_control"),
        "客厅空调": Conditioner(short_id = 6, area = ["客厅"], nickname = [], entity_id = "climate.ab70013296_climate"),
        "主卧吸顶灯": Light(short_id = 7, area = ["主卧中央"], nickname = ["吸顶灯","主灯","大灯"], entity_id = "light.mismartledceilinglight450_4c07_mi_smart_led_ceiling_light_sw_2"),
        "主卧灯带": Light(short_id = 8, area = ["主卧东", "床边", "衣柜里", "壁龛里"], nickname = ["灯带"], entity_id = "switch.ccb5d1d191da_switch"),
        "主卧小爱": Player(short_id = 5, area = ["主卧"], nickname = ["小爱同学"], entity_id = "media_player.xiaomi_l05b_b528_play_control"),
        "次卧吸顶灯": Light(short_id = 10, area = ["次卧"], nickname = [], entity_id = "light.mismartledceilinglight350_46c9_mi_smart_led_ceiling_light_sw_2"),
        "次卧电脑": PC(short_id = 11, area = ["次卧"], nickname = [], entity_id = "switch.pc"),
        # "次卧小爱": Player(short_id = 12, area = ["次卧"], nickname = ["小爱同学"], entity_id = "media_player.xiaomi_l05d_3092_play_control"),
        "次卧空调": Conditioner(short_id = 13, area = ["次卧"], nickname = [], entity_id = "climate.ab70013295_climate"),
        "主卧空调": Conditioner(short_id = 14, area = ["主卧"], nickname = [], entity_id = "climate.ab70013297_climate"),
        "阳台晾衣架": LYJ(short_id = 15, area = ["主卧阳台"], nickname = [], entity_id = "cover.hyd_znlyj5_c8df_airer_3"),
        "阳台灯": Light(short_id = 16, area = ["主卧阳台"], nickname = [], entity_id = "light.hyd_znlyj5_c8df_light_3"),
        "厨房灯": Light(short_id = 17, area = ["厨房"], nickname = [], entity_id = "light.dced836e7c2e_chu_fang_deng"),
        "玄关灯": Light(short_id = 18, area = ["玄关"], nickname = ["青空灯"], entity_id = "light.dced8386426f_light"),
        "干区灯": Light(short_id = 19, area = ["干区","镜柜"], nickname = ["射灯"], entity_id = "light.gan_qu_deng_zu"),
        "干区灯带": Light(short_id = 20, area = ["干区"], nickname = ["灯带"], entity_id = "light.ccb5d1e0913f_gan_qu_deng_dai"),
        "湿区灯": Light(short_id = 21, area = ["湿区"], nickname = [], entity_id = "light.ccb5d1e0913f_ce_suo_deng"),
        "鞋柜灯": Light(short_id = 22, area = ["玄关", "鞋柜"], nickname = ["灯带"], entity_id = "light.dced836e7c2e_xie_ju_deng")
    }

#客厅电视
DEVICES = regist()
PERSONS =  {
        "邵伟": Person(0,"邵伟", ["老公"], "person.weis", "2210132c"),
        "王卫": Person(1,"王卫", ["老婆"], "person.wang_wei", "iphone")
}
for k, v in DEVICES.items():
    v.print_name = k
# with open("/home/weis/daemon/homecopilot/device/op.json", "w") as f:
#     json.dump({
#         "灯": DEVICES["客厅电视灯"].op,
#         "电视": DEVICES["客厅电视"].op,
#         "空调": DEVICES["客厅空调"].op,
#         "晾衣架": DEVICES["阳台晾衣架"].op,
#         "电脑": DEVICES["次卧电脑"].op,
#         "音箱": DEVICES["客厅小爱"].op
#     },f,ensure_ascii=False)

# with open("/home/weis/daemon/homecopilot/device/devices.json", 'w') as f:
#     json.dump([json.loads(str(DEVICES[i])) for i in DEVICES],f,ensure_ascii=False)