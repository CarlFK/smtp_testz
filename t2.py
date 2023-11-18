
import os
import smtplib

from email.message import EmailMessage

m_host=os.environ.get('m_host')
m_port=os.environ.get('m_port')
m_port=int(m_port)
m_username=os.environ.get('m_username')
m_username="foo"
m_password=os.environ.get('m_password')
m_from=os.environ.get('m_from')
m_to=os.environ.get('m_to')

subject="da subject v3"
body = "da body."

msg = EmailMessage()

msg['From'] = m_from
msg['To'] = m_to
msg['Subject'] = subject
msg.set_content(body)

# server = smtplib.SMTP_SSL(host=m_host, port=m_port)
server = smtplib.SMTP_SSL(m_host)

r1=server.noop()
print(f"{r1=}")

r2=server.login(m_username, m_password)
print(f"{r2=}")
try:
    r3=server.sendmail(msg.get('From'),msg["To"],msg.as_string())
    print(f"{r3=}")
except smtplib.SMTPServerDisconnected as e:
    print(f"smtplib.SMTPServerDisconnected {e=}")
except Exception as e:
    print(f"Exception {e=}")

r4=server.quit()
print(f"{r4=}")

