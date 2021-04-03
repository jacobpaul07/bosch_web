import time
import paho.mqtt.client as paho

# broker="broker.hivemq.com"
broker = "broker.mqttdashboard.com"  #########################################


# define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))


client = paho.Client("clientid-jacob001")  #################################################
# create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message = on_message
#####
print("connecting to broker ", broker)
client.connect(broker)  # connect
# client.loop_start() #start loop to process received messages
print("subscribing ")
topic = "data/Bosch"  #################################################
client.subscribe(topic)  # subscribe
time.sleep(2)
# print("publishing ")
# client.publish("house/bulb1","on")#publish
# time.sleep(2)
# client.disconnect() #disconnect
client.loop_forever()  # stop loop
