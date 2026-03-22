from plyer import notification

def send_notification(message):
    notification.notify(
        title="Crypto Alert",
        message=message,
        timeout=10
    )#type:ignore