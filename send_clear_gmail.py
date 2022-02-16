# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:56:36 2022

@author: golde
"""

import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import pandas as pd
from tqdm import tqdm
from imapclient import IMAPClient

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

def clearGmail(_from,_pas):
	obj = IMAPClient('imap.gmail.com', ssl=True)
	obj.login(_from,_pas)
	obj.list_folders()
	
	obj.select_folder('[Gmail]/Sent Mail')
	msg_ids = obj.search('ALL')
	obj.delete_messages(msg_ids)
	obj.expunge()
	obj.close_folder()
	
	obj.select_folder('[Gmail]/Spam')
	msg_ids = obj.search('ALL')
	obj.delete_messages(msg_ids)
	obj.expunge()
	obj.close_folder()
	
	obj.select_folder('[Gmail]/Trash')
	msg_ids = obj.search('ALL')
	obj.delete_messages(msg_ids)
	obj.expunge()
	obj.close_folder()
	
	obj.select_folder('[Gmail]/All Mail')
	msg_ids = obj.search(['FROM', _from])
	obj.delete_messages(msg_ids)
	obj.expunge()
	obj.close_folder()
	
	obj.logout()


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
		   "usseller0012@gmail.com",
		   ]


_pas = "spring1708"
_from = 'usseller0011'
_to = '9183062046@vtext.com'
_to = '4054122710@mms.att.net'
_subject = 'test subject'
_body = 'test body'

sendSMS(_from,_pas,_to,_subject,_body)
clearGmail(_from,_pas)








