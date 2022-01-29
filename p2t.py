# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 02:42:08 2022

@author: Golden Mars
"""


import PyPDF2
import re

pdfFileObj = open('omma_growers_list.pdf', 'rb')


pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

for i in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(i)
	t = pageObj.extractText().replace('\n \n','&&&&&').replace('\n',' ')
	rr = t.split('Trade Name:')
	print(len(r))

pdfFileObj.close()

re.findall('Trade Name:[]Trade Name:',t)


r0 = r[0]

re.findall(r'COUNTY&&&&&(.*?)&&&&&',r[0])




for r in rr[1:]:
	rlist = r.split('&&&&&')
	print(len(rlist))


re.findall('&&&&&(GAAA - VJG4 - 6UJR)&&&&&',r)
re.findall('(&&&&&(\d - \d - \d)&&&&&)',r)
