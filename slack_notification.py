import os
import requests

slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']


def send_slack_notification(status):
    if status == 'success':
        color = 'good'
        message = 'La construction a réussi'
    else:
        color = 'danger'
        message = 'La construction a échoué'

    payload = {
        "attachments": [
            {
                "fallback": message,
                "color": color,
                "text": message
            }
        ]
    }

    requests.post(slack_webhook_url, json=payload)
