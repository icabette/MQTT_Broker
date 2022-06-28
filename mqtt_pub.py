from time import sleep
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected. Return Code is " + str(rc))

def on_publish(client, userdata, mid):
    print("Publish #" + str(mid))

broker_address = "192.168.0.9"
broker_port = 1883

# 새로운 클라이언트 생성
client = mqtt.Client()

# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

# address : localhost, port: 1883 에 연결
client.username_pw_set(username="",password="")
client.connect(broker_address, broker_port)
client.loop_start()

msgCount = 0
try:
    # message 반복 실행
    while (1):
        client.publish('test/test','UriBag1 from Python: '+ str(msgCount))
        msgCount = msgCount + 1
        sleep(1)
except KeyboardInterrupt:
    client.loop_stop()
    # 연결 종료
    client.disconnect()