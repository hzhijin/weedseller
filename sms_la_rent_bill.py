# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 22:24:20 2022

@author: Golden Mars
"""


'https://www.liquisearch.com/list_of_sms_gateways'

import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import pandas as pd
from tqdm import tqdm

def sendSMS(_from,_pas,_to,_subject,_body):
	smtp = "smtp.gmail.com" 
	port = 587
	server = smtplib.SMTP(smtp,port)
	server.starttls()
	server.login(_from,_pas)
	msg = MIMEMultipart()
	msg['From'] = _from
	msg['To'] = _to
	msg['Subject'] = _subject
	body = _body
# 	msg.attach(MIMEText(body, 'plain'))
	msg.attach(MIMEText(body))
	sms = msg.as_string()
	server.sendmail(_from,_to,sms)
	server.quit()



gateways = ['@mms.att.net',
			'@messaging.sprintpcs.com',
			'@tmomail.net',
			'@vtext.com',
			'@sms.mycricket.com',]


senders = ["ok.serve.ooo@gmail.com",
		   "ok.serve.ppp@gmail.com",
		   "ok.serve.qqq@gmail.com",
		   "ok.serve.rrr@gmail.com",
		   "ok.serve.sss@gmail.com",
		   "ok.serve.ttt@gmail.com",
		   "ok.serve.uuu@gmail.com",
		   "okserve1@gmail.com",
		   ]
_pas = "3523240t&"

df = pd.read_excel('rent_la.xlsx')

_subject = '水电费地址求租\n'
with open('mail.txt',encoding="utf-8") as f:
	_body = f.read()

senderIndex = 7
_from = senders[senderIndex]

# for i in tqdm(range(senderIndex * int(len(df)/8) + 0 , (senderIndex+1) * int(len(df)/8))):
for i in tqdm(range(senderIndex * int(len(df)/8) + 0 , len(df))):
	for j in gateways:
		_to = str(df.iloc[i]['phone']) + j
		print(_to)
		try:
 			sendSMS(_from,_pas,_to,_subject,_body)
		except Exception as e:
 			print(e)
 			time.sleep(1200)
		time.sleep(60)
		
	