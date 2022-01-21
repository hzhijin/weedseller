# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 21:00:27 2021

@author: Administrator
"""

import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import glob
import pandas as pd
import time
from tqdm import tqdm
def addAttachment(message,filename):

#	filename = "f944.pdf"  # In same directory as script
	# Open PDF file in binary mode
	with open(filename, "rb") as attachment:
	    # Add file as application/octet-stream
	    # Email client can usually download this automatically as attachment
	    part = MIMEBase("application", "octet-stream")
	    part.set_payload(attachment.read())
	
	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)
	
	# Add header as key/value pair to attachment part
	part.add_header(
	    "Content-Disposition",
	    f"attachment; filename= {filename}",
	)
	
	# Add attachment to message and convert message to string
	message.attach(part)
	return message



def sendGmail(sender,receiver,subject,text,files):

	password = '3523240t&'
	message = MIMEMultipart("alternative")
	message["Subject"] = subject
	message["From"] = sender
	message["To"] = receiver

	# Turn these into plain/html MIMEText objects
	#part1 = MIMEText(text, "plain")
	part2 = MIMEText(text, "html")
	
	# Add HTML/plain-text parts to MIMEMultipart message
	# The email client will try to render the last part first
#	message.attach(part1)
	message.attach(part2)
	
	for file in files:
		addAttachment(message,file)
	
	# Create secure connection with server and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender, password)
		server.sendmail(
			sender, receiver, message.as_string()
		)
	
	

text0 = """
	We got some new flowers in stock shown below.
	Feel free to contact us about which strains and how much do you like 
	We are glad to deliver and work with you.
	
	Yours
	Billy
	4054122710
"""

files = glob.glob('a2/*.*')
subject = "Quality and price competitve flowers wholesale"
sender = "okcqqq@gmail.com"

dfs = pd.read_excel('dispensary list from weedmap.xls')
for i in tqdm(range(3,len(dfs))):
#for i in range(5):
	shop = dfs.iloc[i]['name']
	text = text0

#	shop = 'Kush'
	receiver = dfs.iloc[i]['email']
#	receiver = "qqqlby@gmail.com"
	
	sendGmail(sender,receiver,subject,text,files)
	print('email sent successfully for ')
	print(shop,receiver)
	sleep = 10
	print('have a '+str(sleep)+' seconds gap')
	time.sleep(sleep)
	
	
	

