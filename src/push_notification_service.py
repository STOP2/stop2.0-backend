from pyfcm import FCMNotification
import os


class PushNotificationService():

    def send_push_notifications(self, registration_ids):
        push_service = FCMNotification(api_key=os.getenv('FCM_API_KEY'))
        data_message = {
            "title": "Kulkuneuvo saapuu!",
            "message": "Tilaamasi kulkuneuvo on pysäkilläsi hetken kuluttua"
        }
        return push_service.notify_multiple_devices(registration_ids=registration_ids,
                                                      data_message=data_message)

    def send_error_push_notifications(self, registration_ids, error_message):
        push_service = FCMNotification(api_key=os.getenv('FCM_API_KEY'))

        data_message = {
            "title": "Error",
            "message": error_message
        }