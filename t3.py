
import os
import smtplib

from email.message import EmailMessage

m_host=os.environ.get('m_host')
m_port=os.environ.get('m_port')
m_port=int(m_port)
m_username=os.environ.get('m_username')
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

rr,ctr,sd,lc=0,0,0,0

server = smtplib.SMTP(m_host)

while True:

    ctr+=1
    lc+=1
    print(lc, end=" ", flush=True)

    try:

        r1=server.noop()
        # r1=(250, b'2.0.0 Ok')

        assert r1[0]==250, print(f"{r1=}")
        r3=server.sendmail(msg.get('From'),msg["To"],msg.as_string())
        print(f"{r3=}")

    except ConnectionResetError as e: # [Errno 104] Connection reset by peer
        # ConnectionResetError: [Errno 104] Connection reset by peer

        print(f"ConnectionResetError {e=}")
        print("import sys;sys.exit()"); import code; code.interact(local=locals())


    except smtplib.SMTPRecipientsRefused as e:
        rr+=1
        # print(f"smtplib.SMTPRecipientsRefused {e=}")

    except smtplib.SMTPServerDisconnected as e:
        # e=SMTPServerDisconnected('Connection unexpectedly closed: [Errno 104] Connection reset by peer')
        # e=SMTPServerDisconnected('Server not connected')

        lc=0
        sd+=1
        r5=server.connect(host=m_host)
        print(f"\n")
        print(f"{r5=}")
        print(f"smtplib.SMTPServerDisconnected {e=}")
        # print("import sys;sys.exit()"); import code; code.interact(local=locals())
        print(f"{ctr=} {rr=} {sd=}", end=". ", flush=True)

    except Exception as e:
        print(f"Exception {e=}")
        print("import sys;sys.exit()"); import code; code.interact(local=locals())

r4=server.quit()
print(f"{r4=}")
r4=(221, b'2.0.0 Bye')
assert r4[0]==221, print(f"{r4=}")

