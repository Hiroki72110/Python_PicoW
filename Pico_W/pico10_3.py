import network
import time

ssid = 'Love iPhone'
password = '29541231'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.disconnect() 
wlan.connect(ssid,password)


#等待連線或失敗
#status=0,1,2正在連線
#status=3連線成功
#<0,>3失敗的連線

max_wait = 10
while max_wait > 0:
    status = wlan.status()
    if status < 0 or status >= 3:
        break
    max_wait -= 1
    print("等待連線")
    time.sleep(1)

#檢查目前連線狀態
    
if wlan.status() != 3:
    raise RuntimeError('連線失敗')

else:
    print('連線成功')
    configure = wlan.ifconfig()
    print(f'ip={configure[0]}')