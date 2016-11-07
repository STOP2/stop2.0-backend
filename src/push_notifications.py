from pyfcm import FCMNotification
import db

push_service = FCMNotification(api_key='AIzaSyD4bExMYdOyBpFOFm-S4JqJsb4vukUy1eM')

database = db.Database()
devices = database.get_device_ids()
registration_ids = [devices]
message_title = "Bussi saapuu!"
message_body = "Tilaamasi bussi saapuu pysäkillesi hetken kuluttua"
result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)