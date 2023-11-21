import datetime
import json
import os
import requests

m_tos=os.environ.get('m_tos')
m_from=os.environ.get('m_from')

m_endpoint=os.environ.get('m_endpoint')
m_apikey=os.environ.get('m_apikey')

subject="da subject v3"

msg = {}

msg['to'] = m_tos
msg['from'] = m_from
msg['subject'] = "da subject v4 " + datetime.datetime.now().strftime("%m:%S")
msg['text'] = "%recipient.body%"

rvs = {}
for t in m_tos.split(','):
    k=t.strip()
    v = {'body':f"hello {k[0]}"}
    rvs[k] = v
msg['recipient-variables'] = json.dumps(rvs)

mailing = requests.post(
            m_endpoint,
            auth=('api', m_apikey),
            data=msg
        )

print(f"{mailing.status_code=}")
# mailing.status_code=200

print(f"{mailing.content=}")
# mailing.content=b'{"id":"<20231120050924.821da8a904fe7ca3@sandbox0c7ed6bf35a74ed7b00fccdc3099ed88.mailgun.org>","message":"Queued. Thank you."}\n'

