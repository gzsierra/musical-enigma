import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# Send to the server
def send(subscriptions, value):
    client.publish(subscriptions, value)
    # To test if work, on server use command :
    # mosquitto_sub -d -t paho/temperature

# receives what to send
def update(cpu, ram):
    send("client/CPU", cpu)
    send("client/RAM", ram)

################### PRELOAD ###################
client = mqtt.Client()

# Host port keepalive bin_addr
client.connect("172.24.20.26", 1883, 60)
# client.connect("192.168.1.72", 1883, 60)
