
import smtplib, ssl
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = None
sender_address = None
sender_name = None
def init_client(server_address:str, user_email:str, user_name:str, password:str, port:int =465 ):
    global server
    global sender_address
    global sender_name
    sender_address = user_email
    sender_name = user_name
    # Create a secure SSL context
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(server_address, port, context=context)
    server.login(sender_address, password)

def send_email(receiver, html_content: str= "", plain_content: str= "", subject="", receiver_name: str=None)-> None:
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = formataddr((sender_name, sender_address))
    message["To"] = formataddr((receiver_name or receiver, receiver))

    message.attach(MIMEText(plain_content, "plain"))
    message.attach(MIMEText(html_content, "html"))

    server.sendmail(sender_address, receiver, message.as_string())
