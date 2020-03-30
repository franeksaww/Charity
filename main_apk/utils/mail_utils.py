import smtplib, ssl
from email.mime.text import MIMEText as text


def send_email(pass_password, recivers, message, subject):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "franeksawwdevelopment@gmail.com"
    password = pass_password
    context = ssl.create_default_context()
    m = text(message)
    m['subject'] = subject
    m['from'] = sender_email
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, recivers, m.as_string().encode('utf8'))

if __name__ == '__main__':
    send_email('Gh8mck9w', 'franeksaww@gmail.com', 'To ma być wiadomość', 'Temat zagadnienia')