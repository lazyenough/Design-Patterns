# We use this design pattern to separate the logic of object creation and it usage.

class Notification:
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Email notification sent: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS notification sent: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Push notification sent: {message}")

# Without this design pattern client code would look like this
# notification_type = ""
# if notification_type == "email":
#     notifier = EmailNotification()
# elif notification_type == "sms":
#     notifier = SMSNotification()
# elif notification_type == "push":
#     notifier = PushNotification()
# else:
#     raise ValueError("Error")


# Using Factory design pattern 
class FactoryMethod:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError("Error")
        

# Now the client code would look like this

if __name__ == "__main__":

    notifier1 = FactoryMethod.create_notification("email")
    notifier2 = FactoryMethod.create_notification("sms")
    notifier3 = FactoryMethod.create_notification("push")

    notifier1.send("message 1")
    notifier2.send("message 2")
    notifier3.send("message 3")