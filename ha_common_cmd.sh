#重启ha
sudo systemctl restart hass.service 
#查看日志
journalctl -u hass -n 100
#重启ra
sudo systemctl stop room-assistant && sleep 5 && sudo systemctl restart bluetooth.service && sleep 10 && sudo systemctl restart room-assistant
#查看蓝牙情况
hciconfig hci0
#查看ra的写入数据
mosquitto_sub -h 127.0.0.1 -p 1883 -u weishao -P xingxuan -t 'room-assistant/#' -v