# homeassistant_llm
## Part One: 基于UI控制的智能家居Homeassistant
> * homeassistant version： Core ≥ 2024.4.4
> * Operating System ≥ 13.0
### xiaomi_home 安装
假设homeassistant的配置目录为/config
```bash 
cd config
git clone https://github.com/XiaoMi/ha_xiaomi_home.git
cd ha_xiaomi_home
git checkout v0.3.2
./install.sh /config
```
### xiaomi_home Login
Settings > Devices & services > ADD INTEGRATION > Search Xiaomi Home > NEXT > Click here to login > Sign in with Xiaomi account
![image](https://github.com/user-attachments/assets/57ece23c-7c1f-4985-a978-2166d6130fe1)
![image](https://github.com/user-attachments/assets/aed5580a-d1ee-4239-afc6-2f2d8ce3b1cf)
完成之后能在主页看到所有从米家添加的设备
<img width="3818" height="1811" alt="image" src="https://github.com/user-attachments/assets/e709ed9a-35e7-4f5a-87ec-298d845281b3" />
### homeassistant 接入所有智能家居
可以在UI中简单制作出家庭灯控系统，也可以将家庭传感器、空调、扫地机器人、洗碗机、洗衣机等等接入进来。
<img width="3827" height="1759" alt="image" src="https://github.com/user-attachments/assets/2b5c862d-582e-45b5-9e5c-2e4eb9279737" />
<img width="3789" height="1773" alt="image" src="https://github.com/user-attachments/assets/dabf11a3-1a9f-417f-b101-b80fac1d189d" />
<img width="3834" height="1780" alt="image" src="https://github.com/user-attachments/assets/77acc018-54a4-45c7-a187-0cd28b4678bb" />
<img width="3775" height="1791" alt="image" src="https://github.com/user-attachments/assets/15f0cb5a-6b5c-4cbd-8344-f3ecd74c978e" />
<img width="3829" height="1784" alt="image" src="https://github.com/user-attachments/assets/b35c0f65-9118-4715-bc74-416f279ff3fd" />
## Part Two: 基于代码控制的智能家居系统
## Part Three: 基于LLM控制的智能家居系统
## Part Four: 基于agent控制的智能家居系统
