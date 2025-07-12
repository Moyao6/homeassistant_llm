# homeassistant_llm
## Part One：关于环境
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
可以在UI中简单制作出家庭灯控系统
<img width="3834" height="1797" alt="image" src="https://github.com/user-attachments/assets/586f3a36-9bfc-4c17-9163-51bed485f04e" />
