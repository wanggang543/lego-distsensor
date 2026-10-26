from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

# 1. 初始化 Hub 與插在 Port A 的超音波感測器
hub = PrimeHub()
sensor = UltrasonicSensor(Port.A)

# 音頻設定為 440 Hz (標準音 A4)
NOTE_FREQ = 440

# 建立兩個計時器，分別追蹤印出時間與發音間隔
print_watch = StopWatch()
beep_watch = StopWatch()

while True:
    # 讀取感測器距離（Pybricks 回傳 mm，除以 10 換算為 cm）
    dist_mm = sensor.distance()
    dist_cm = dist_mm / 10 if dist_mm is not None else 999

    # 2. 每 0.2 秒 (500 毫秒) 印出一次純數字，利於自訂網頁解析
    if print_watch.time() >= 500:
        print("{:.1f}".format(dist_cm))
        print_watch.reset()

    # 蜂鳴器警示邏輯判斷
    if dist_cm <= 5:
        # 當距離 <= 5cm 時：440 Hz 長音不間斷
        hub.speaker.beep(frequency=NOTE_FREQ, duration=-1)
    elif dist_cm <= 10:
        # 當距離 <= 10cm 時：發出聲音，週期 0.2 秒 (200 ms)
        if beep_watch.time() >= 200:
            hub.speaker.beep(frequency=NOTE_FREQ, duration=80)
            beep_watch.reset()
    elif dist_cm <= 20:
        # 當距離 <= 20cm 時：發出聲音，週期 0.5 秒 (500 ms)
        if beep_watch.time() >= 500:
            hub.speaker.beep(frequency=NOTE_FREQ, duration=100)
            beep_watch.reset()
    else:
        # 距離 > 20cm：停止發聲
        hub.speaker.beep(frequency=NOTE_FREQ, duration=0)

    wait(10)