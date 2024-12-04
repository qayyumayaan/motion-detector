import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

# Load environment variables from cred.env
load_dotenv("cred.env")

# Read credentials from the environment
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")

def send_email(subject, body, attachment_path):
    """
    Sends an email with an attachment.
    Args:
        subject (str): Email subject.
        body (str): Email body content.
        attachment_path (str): Path to the attachment file.
        RECIPIENT_EMAIL (str): Recipient's email address.
    """
    if not os.path.exists(attachment_path):
        print(f"Attachment not found: {attachment_path}")
        return False

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
    msg.attach(part)

    # Send the email
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server: 
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {RECIPIENT_EMAIL} with attachment {attachment_path}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
