import os
import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)


message = Mail(
    from_email='roshanshrestha01@gmail.com',
    to_emails='roshanshrestha@whitehatengineering.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>'
)

with open('downloads/t.xlsx', 'rb') as f:
    data = f.read()
    f.close()
encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('today.xlsx'),
    FileType('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
    Disposition('attachment')
)
message.attachment = attachedFile

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.send(message)
print(response.status_code, response.body, response.headers)
