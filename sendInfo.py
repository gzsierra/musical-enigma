import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def send(subscriptions, value):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Host port keepalive bin_addr
    # client.connect("172.24.20.26", 1883, 60)
    client.connect("192.168.1.72", 1883, 60)

    # To test if work, on server use command :
    # mosquitto_sub -d -t paho/temperature
    client.publish(subscriptions, value)
    print("Msg sent")

def sendInfo(cpu, ram):
    send("client/CPU", cpu)
    send("client/RAM", ram)
