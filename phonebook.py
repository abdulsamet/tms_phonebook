# -*- coding: utf-8 -*-

import requests

requests.packages.urllib3.disable_warnings()
from xml.etree import ElementTree as ET

headers = {'content-type': 'text/xml'}
body = """
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetPhonebooks xmlns="http://www.tandberg.net/2004/06/PhoneBookSearch/">
      <SystemIdentifier>
        <SystemName>Endpoint1</SystemName>
        <MACAddress>FF:FF:FF:FF:FF:FF</MACAddress>
        <SerialNumber>string</SerialNumber>
        <IPAddress>10.10.10.10</IPAddress>
        <SWVersion>string</SWVersion>
      </SystemIdentifier>
    </GetPhonebooks>
  </soap:Body>
</soap:Envelope>
"""
phonebook_url = "http://tms.domain.com/tms/public/external/phonebook/phonebookservice.asmx"

response = requests.post(phonebook_url, data=body, headers=headers)
ext = response.text.encode('utf-8')

parse = ET.fromstring(ext)
for i in range(2, 200):
    print parse[0][0][0][i][0].text # System Name
	# parse[0][0][0][i][0].text # H323 Alias
