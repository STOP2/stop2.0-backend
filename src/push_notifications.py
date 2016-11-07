from pyfcm import FCMNotification


class PushNotifications():

    def __init__(self, db):
        self.db = db

    def get_push_notification(self):
        push_service = FCMNotification(api_key='AIzaSyDzuwUdIs5sog6UAv1dTzx2JJuCG2yOkcA')
        #lisättävä ehto, joka rajaa notifikaation saajat
        devices = self.db.get_device_ids(trip_id, stop_id)
        registration_ids = [devices]
        message_title = "Bussi saapuu!"
        message_body = "Tilaamasi bussi saapuu pysäkillesi hetken kuluttua"
        result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)