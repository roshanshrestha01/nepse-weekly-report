import os
import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)


class SendgridMail:
    def __init__(self, filename, receivers):
        self.filename = filename
        self.receivers = receivers
        self.attached_file = None

    def set_attachment(self, path):
        with open(path, 'rb') as f:
            data = f.read()
            f.close()

        encoded_file = base64.b64encode(data).decode()

        attached_file = Attachment(
            FileContent(encoded_file),
            FileName(self.filename),
            FileType('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
            Disposition('attachment')
        )

        self.attached_file = attached_file

    def send_mail(self):
        if not self.attached_file:
            raise Exception("Sorry, no attached file found.")
        message = Mail(
            from_email=os.environ.get('FROM_EMAIL'),
            to_emails=self.receivers,
            subject='Sending weekly report {}.'.format(self.filename),
            html_content='<strong>Please find in attachment.</strong>'
        )
        message.attachment = self.attached_file
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code, "{} sent.".format(self.filename))
