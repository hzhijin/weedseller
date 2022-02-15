# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 22:12:04 2022

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

print("Deleting mails")
count = 1
for mail in messages[:3]:
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")

    print(count, "mail(s) deleted")
    count +=1
print("All selected mails has been deleted")

# delete all the selected messages 
imap.expunge()
# close the mailbox
imap.close()

# logout from the server
imap.logout()

