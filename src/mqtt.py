import json
import paho.mqtt.client as mqtt


class MQTT:
    def __init__(self, db):
        self.db = db
        client = mqtt.Client()

        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect("epsilon.fixme.fi", 1883, 60)
        client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to the MQTT server with result code " + str(rc))
        client.subscribe("subscriptions")

    def on_message(self, client, userdata, msg):
        message = json.loads(msg.payload.decode('UTF-8'))
        if message.get('status') == 'start':
            self.db.add_vehicle(message.get('veh_id'), message.get('gtfsId'))
        elif message.get('status') == 'stop':
            self.db.remove_vehicle(message.get('veh_id'), message.get('gtfsId'))
