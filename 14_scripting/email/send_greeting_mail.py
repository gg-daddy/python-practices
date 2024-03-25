import smtplib
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from string import Template

import yaml


class GreetingEmailSender:
    def __init__(self, smtp_server, smtp_port, smtp_login, smtp_password, from_name):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_login = smtp_login
        self.smtp_password = smtp_password
        self.from_name = from_name

    def send_greeting_letter(self, recipients, template, subject):
        greeting_template = Template(Path(template).read_text())

        with smtplib.SMTP(host=self.smtp_server, port=self.smtp_port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(self.smtp_login, self.smtp_password)
            for recipient in recipients:
                email = EmailMessage()
                email["from"] = self.from_name
                email["to"] = recipient["address"]
                email["subject"] = subject
                kwargs = {
                    "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "name": recipient["name"],
                }
                email.set_content(greeting_template.substitute(**kwargs), "html")
                smtp.send_message(email)


if __name__ == "__main__":

    with open(".config.yaml", "r") as file:
        config = yaml.safe_load(file)

    smtp_server = config["smtp"]["server"]
    smtp_port = config["smtp"]["port"]
    smtp_login = config["smtp"]["login"]
    smtp_password = config["smtp"]["password"]
    from_name = config["smtp"]["from"]
    recipients = config["recipients"]

    sender = GreetingEmailSender(
        smtp_server, smtp_port, smtp_login, smtp_password, from_name
    )
    sender.send_greeting_letter(recipients, "greeting.html", "Greeting Letter!")
    print("Email sent successfully!")
