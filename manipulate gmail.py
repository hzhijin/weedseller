# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:12:40 2022

@author: Golden Mars
"""

import imaplib
import email
from email.header import decode_header

username = "usseller0011@gmail.com"
password = "spring1708"
imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)
# imap.list()
res, messages = imap.select('"[Gmail]/Sent Mail"')
_,messages=imap.search(None,"ALL")
messages = messages[0].split(b' ')


	
for mail in messages[:3]:
	_, msg = imap.fetch(mail, "(RFC822)")
	# you can delete the for loop for performance if you have a long list of emails
	# because it is only for printing the SUBJECT of target email to delete
	for response in msg:
		if isinstance(response, tuple):
			msg = email.message_from_bytes(response[1])
			# decode the email subject
			subject = decode_header(msg["Subject"])[0][0]
			if isinstance(subject, bytes):
				# if it's a bytes type, decode to str
				subject = subject.decode()
			print("Deleting", subject,mail)
	imap.store(mail, "+FLAGS", "\\Deleted")
# imap.expunge()
	
# # 	_, msg = imap.fetch(mail, "(RFC822)")
# 	# you can delete the for loop for performance if you have a long list of emails
# 	# because it is only for printing the SUBJECT of target email to delete
# 	for response in mail:
# 		if isinstance(response, tuple):
# 			mail = email.message_from_bytes(response[1])
# 			# decode the email subject
# 			subject = decode_header(mail["Subject"])[0][0]
# 			if isinstance(subject, bytes):
# 				# if it's a bytes type, decode to str
# 				subject = subject.decode()
# 			print("Deleting", subject)
# 	# mark the mail as deleted
# 	imap.store(mail, "+FLAGS", "\\Deleted")

imap.expunge()
# close the mailbox
imap.close()
imap.logout()