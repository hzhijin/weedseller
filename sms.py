# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:56:19 2022

@author: Billy
"""

'https://www.liquisearch.com/list_of_sms_gateways'

"""
AT&T: [number]@txt.att.net
Sprint: [number]@messaging.sprintpcs.com or [number]@pm.sprint.com
T-Mobile: [number]@tmomail.net
Verizon: [number]@vtext.com
Boost Mobile: [number]@myboostmobile.com
Cricket: [number]@sms.mycricket.com
Metro PCS: [number]@mymetropcs.com
Tracfone: [number]@mmst5.tracfone.com
U.S. Cellular: [number]@email.uscc.net
Virgin Mobile: [number]@vmobl.com

"""

import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""
def sendSMS(_from,_pas,_to,_object,_body):
	smtp = "smtp.gmail.com" 
	port = 587
	server = smtplib.SMTP(smtp,port)
	server.starttls()
	server.login(_from,_pas)
	
	msg = MIMEMultipart()
	msg['From'] = _from
	msg['To'] = _to
	
	msg['Subject'] = _object
	msg.attach(MIMEText(_body, 'plain'))
	sms = msg.as_string()
	server.sendmail(_from,_to,sms)
	server.quit()
	
gateways = ['@txt.att.net',
			'@messaging.sprintpcs.com',
			'@tmomail.net',
			'vtext.com',
			'@sms.mycricket.com',]

senders = ["okcandylau@gmail.com",
		   "okcandylau2@gmail.com",
		   "okcandylau3@gmail.com",
		   "okcandylau4@gmail.com",
		   "okcandylau5@gmail.com",
		   "okcandylau6@gmail.com",
		   "okcandylau7@gmail.com",
		   "okcandylau8@gmail.com",
		   ]
pas = 'guo654321'
	
_from = "okcandylau@gmail.com"
_pas = "guo654321"
_to = '4054122710@txt.att.net'
_object = 'This is the TITLE\n'
_body = 'This is the BODY\n'

# sendSMS(_from,_pas,_to,_object,_body)

smtp = "smtp.gmail.com" 
port = 587
server = smtplib.SMTP(smtp,port)
server.starttls()
server.login(_from,_pas)

msg = MIMEMultipart()
msg['From'] = _from
msg['To'] = _to

msg['Subject'] = _object
msg.attach(MIMEText(_body, 'plain'))
sms = msg.as_string()
server.sendmail(_from,_to,sms)
server.quit()"""
	

email = "okcandylau6@gmail.com"
pas = "guo654321"
sms_gateway = '4054122710@txt.att.net'

# def sendSMS(email,pas,sms_gateway):
	
smtp = "smtp.gmail.com" 
port = 587
server = smtplib.SMTP(smtp,port)
server.starttls()
server.login(email,pas)

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sms_gateway
msg['Subject'] = "You can insert anything\n"
body = "You can insert message here aaa\n"
msg.attach(MIMEText(body, 'plain'))
sms = msg.as_string()
server.sendmail(email,sms_gateway,sms)
server.quit()

	




# sendSMS(email,pas,sms_gateway)
