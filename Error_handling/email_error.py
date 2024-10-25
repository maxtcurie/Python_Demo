import smtplib
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'sender@gmail.com'
EMAIL_PASSWORD = getpass.getpass(f"Enter email password for {EMAIL_ADDRESS}: ")

RECIPIENT_ADDRESS = 'reader@gmail.com'

def send_error_email(error_message):
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_ADDRESS
    msg['Subject'] = 'Error Occurred in Script'

    # Attach the error message to the email
    msg.attach(MIMEText(error_message, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, RECIPIENT_ADDRESS, msg.as_string())
        server.quit()
        print('Error email sent successfully.')
    except Exception as e:
        print('Failed to send email. Error:', e)

def main():
    try:
        # Your script logic here
        # For demonstration, let's raise an exception
        raise ValueError('An example error occurred!')
    except Exception as e:
        error_message = ''.join(traceback.format_exception(None, e, e.__traceback__))
        send_error_email(error_message)

if __name__ == '__main__':
    main()
