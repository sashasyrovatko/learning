import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendMail:
    def __init__(self, sender_email, sender_password, receiver_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email

    def send_discount_email(self, changes_models):
        subject = "Discount Alert"
        message = "The following models have a price reduction:\n\n"
        for model in changes_models:
            message += f"- {model}\n"
        self.send_email(subject, message)

    def send_email(self, subject, message):
        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = self.receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.receiver_email, msg.as_string())

