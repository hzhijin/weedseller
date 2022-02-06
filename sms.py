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


senders = ["usseller0001@gmail.com",
 		   "usseller0002@gmail.com",
		   "usseller0003@gmail.com",
		   "usseller0004@gmail.com",
		   "usseller0005@gmail.com",
		   "usseller0006@gmail.com",
		   "usseller0007@gmail.com",
		   "usseller0008@gmail.com",
           "usseller0009@gmail.com",
           "usseller0010@gmail.com",
           "usseller0011@gmail.com",
		   ]
_pas = "spring1708"

df = pd.read_excel('omma_growers_list.xlsx')
df['phone'] = df.phone.apply(str)
df['phone'] = df.phone.str.replace('(','')
df['phone'] = df.phone.str.replace(')','')
df['phone'] = df.phone.str.replace(' ','')
df['phone'] = df.phone.str.replace('-','')


_subject = 'Phantom grow lights available'
with open('mail.txt') as f:
	_body = f.read()

senderIndex = 10
_from = senders[senderIndex]

# for i in tqdm(range(senderIndex * int(len(df)/11)  , (senderIndex+1) * int(len(df)/11))):
for i in tqdm(range(senderIndex * int(len(df)/11) , len(df))):
# for i in range(1):
	for j in gateways:
		_to = df.iloc[i]['phone'][-10:] + j
		print(_to)
		try:
			sendSMS(_from,_pas,_to,_subject,_body)
		except Exception as e:
			print(e)
			time.sleep(1200)
		time.sleep(60)
	
	