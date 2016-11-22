from pyfcm import FCMNotification
import os


class PushNotificationService():

    def send_push_notification(self, registration_ids):
        push_service = FCMNotification(api_key=os.getenv('FCM_API_KEY'))
        #registration_ids = ['e60w7vyvSrY:APA91bGMqp8VNOinW4fD61CbS9_HI6Ty1aZc98jl7fZhoJWh3JGnIAn7IimN7fUB8r9bKhB8V7vua-pArr8CsChxNDFC46lhCsj8fHoIsMTm2CFDarFxeGrFA69o-JfnJIg4WVDPYr4b'] #([devices])
        data_message = {
            "title": "Kulkuneuvo saapuu!",
            "message": "Tilaamasi kulkuneuvo on pysäkilläsi hetken kuluttua"
        }
        return push_service.notify_multiple_devices(registration_ids=registration_ids,
                                                      data_message=data_message)
    