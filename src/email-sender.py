import os
import smtplib
import csv

# Set port number and server
port = 587  # Port number for gmail
smtp_server = "smtp.gmail.com"

# Set credentials
user_email = os.environ.get("EMAIL_USER")
password = os.environ.get("PASSWORD")

# Set message, replace message below
message = """Subject: {recipient}, how are you?

Hey {recipient},

This is a test message. 

Bye

- {sender}

"""
sender = user_email

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user_email, password)
    with open("csv-file-here.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)    # add this to skip the header row
        for sender_name, recipient_name, email in csv_reader:
            server.sendmail(
                sender_name,
                email,
                message.format(sender_name=sender, recipient_name=recipient_name)
            )
            print(f'Sent to {recipient_name}')
