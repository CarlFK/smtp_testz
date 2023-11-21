
import os

m_host=os.environ.get('m_host')
m_port=os.environ.get('m_port')
m_username=os.environ.get('m_username')
m_password=os.environ.get('m_password')
m_from=os.environ.get('m_from')
m_to=os.environ.get('m_to')

subject="da subject"
body = "da body."

# https://docs.python.org/3/library/smtplib.html#smtp-example
# https://docs.python.org/3/library/email.examples.html#email-examples

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

"""
# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())
"""

msg = EmailMessage()
msg.set_content(body)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = subject
msg['From'] = m_from
msg['To'] = m_to

# Send the message via our own SMTP server.
s = smtplib.SMTP(m_host)
s.send_message(msg)
s.quit()
