from pyfcm import FCMNotification


class PushNotifications():

    def __init__(self, db):
        self.db = db

    def send_push_notification(self, trip_id, stop_id):
        push_service = FCMNotification(api_key='AIzaSyBbs3cP4o7hJGwbJ51Rhf6zBdAsqnw2-nM')
        #TYÖN ALLA, toistaiseksi käytetään kovakoodattua registration_id:tä. #devices = self.db.get_device_ids(trip_id, stop_id)
        registration_ids = ['e60w7vyvSrY:APA91bGMqp8VNOinW4fD61CbS9_HI6Ty1aZc98jl7fZhoJWh3JGnIAn7IimN7fUB8r9bKhB8V7vua-pArr8CsChxNDFC46lhCsj8fHoIsMTm2CFDarFxeGrFA69o-JfnJIg4WVDPYr4b']#json.dumps([devices])
        data_message = {
            "title": "Kulkuneuvo saapuu!",
            "message": "Tilaamasi kulkuneuvo on pysäkilläsi hetken kuluttua"
        }
        result = push_service.notify_multiple_devices(registration_ids=registration_ids,
                                                      data_message=data_message)