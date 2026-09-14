# OCP means that any software entity like class, modules or functions should be open for extension and closed for modification.
from abc import ABC, abstractmethod

# Bad Example
# the notification service

class BadNotification:
    def send_SMS(self, message: str):
        print(f"sending SMS: {message}")

    def send_Mail(self, message: str):
        print(f"sending mail: {message}")

    def send_Whatsapp(self, message: str):
        print(f"sending on whatsapp: {message}")

class SendNotification:
    def send_message(self, type: str):
        notification = BadNotification()
        if type == "SMS":
            notification.send_SMS("sending message")
        elif type == "Email":
            notification.send_Mail("sending email")
        elif type == "whatsapp":
            notification.send_Whatsapp("sending message")

# Good Example
# using abstraction to write better code

class Notification(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

class SMSNotification(Notification):
    def send_notification(self, message: str):
        print(f"send sms: {message}")

class MailNotification(Notification):
    def send_notification(self, message: str):
        print(f"send email: {message}")

class WhatsappNotification(Notification):
    def send_notification(self, message: str):
        print(f"send Whatsapp notification: {message}")

class InformUser:
    def send_message(self, notification: Notification, message: str):
        notification.send_notification(message)

inform_user = InformUser()
inform_user.send_message(SMSNotification(), "Hey there")
inform_user.send_message(MailNotification(), "Hey there")
inform_user.send_message(WhatsappNotification(), "Hey there")

