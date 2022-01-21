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


senders = ["okcandylau@gmail.com",
# 		   "okcandylau2@gmail.com",
		   "okcandylau3@gmail.com",
		   "okcandylau4@gmail.com",
		   "okcandylau5@gmail.com",
		   "okcandylau6@gmail.com",
		   "okcandylau7@gmail.com",
		   "okcandylau8@gmail.com",
		   ]
_pas = "guo654321"

df = pd.read_excel('dispensary list from weedmap.xls')
df['telephone'] = df.telephone.str.replace('(','')
df['telephone'] = df.telephone.str.replace(')','')
df['telephone'] = df.telephone.str.replace(' ','')
df['telephone'] = df.telephone.str.replace('-','')


_subject = 'Updated Quality Flowers Wholesale\n'
with open('mail.txt') as f:
	_body = f.read()

senderIndex = 6
_from = senders[senderIndex]

# for i in tqdm(range(senderIndex * int(len(df)/8) + 30 , (senderIndex+1) * int(len(df)/8))):
for i in tqdm(range(senderIndex * int(len(df)/8) + 30 , len(df))):
	for j in gateways:
		_to = df.iloc[i]['telephone'][-10:] + j
		print(_to)
		try:
			sendSMS(_from,_pas,_to,_subject,_body)
		except Exception as e:
			print(e)
			time.sleep(1200)
		time.sleep(60)
	
	