

class MockPushService():
    def send_push_notifications(self, registration_ids):
        return [{'canonical_ids': 0, 'multicast_id': 8049279068692141908,
                 'results': [{'message_id': '0:1479802488914353c8bc1d27f9fd7ecd'},
                             {'message_id': '0:1479802488914973c8bc1d27f9fd7ecd'},
                             {'message_id': '0:1479802488915364c8bc1d27f9fd7ecd'}],
                 'failure': 0,
                 'success': len(registration_ids)}]
