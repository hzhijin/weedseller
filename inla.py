# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 22:30:50 2022

@author: Golden Mars
"""


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from tqdm import tqdm

pd.options.display.max_columns = 20

WEBSITE = 'https://www.chineseinla.com'

def parse_info(url):

# 	uu = WEBSITE + '/f/page_viewtopic/t_2236836.html'
	url = WEBSITE + url
	r = requests.get(url)
	b = BeautifulSoup(r.content,'lxml')
	
	c = b.find('p',{'class':'real-content'}).text
	r = re.compile(r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}')
	phone = r.findall(c)
	
	if len(phone) > 0:
		phone = re.sub(r'[ \)\(-]','',phone[0])
	else:
		phone = ''
	
	
	res = []
	ss = b.find('div',{'class':'post_body'}).findAll('span')
	for s in ss:
		st = s.text.split(':')
		slen = len(st)
		if slen > 1 and st[1] != ' ':
			res.append(st)
	
	dft = pd.DataFrame(res).T
	new_header = dft.iloc[0] #grab the first row for the header
	dft = dft[1:] #take the data less the header row
	dft.columns = new_header #set the header row as the df header
	dft['phone'] = phone
	
	if '地址' not in dft.columns:
		dft['地址'] = ''
	if '地区' not in dft.columns:
		dft['地区'] = ''
	if '类别' not in dft.columns:
		dft['类别'] = ''
	if '类型' not in dft.columns:
		dft['类型'] = ''
		
	pt = b.find('div',{'class':'post_time'}).findAll('span')[1].text[6:16]
	dft['update'] = pt
	return dft



url = 'https://www.chineseinla.com/f/page_viewforum/f_5/start_50.html'
url = 'https://www.chineseinla.com/f/page_viewforum/f_5/items_63BAA/start_25.html'

df = pd.DataFrame()
for i in tqdm(range(500)):
	u = 'https://www.chineseinla.com/f/page_viewforum/f_5/items_63BAA/start_' + str(25 * i) + '.html'
	r = requests.get(u)
	b = BeautifulSoup(r.content,'lxml')
	ts = b.findAll('div',{'class':'forum_line'})[2].findAll('a',{'class':'title'})
	for t in ts[2:]:
		url = t.attrs['href']
		title = t.text
# 		print(url,title)
		dft = parse_info(url)
		dftt = dft[['类别','地区','地址','phone']]
		dfttt = dft[['月租']].T.tail(1).T
		dft = pd.concat([dftt,dfttt],axis = 1)
		
		dft['url'] = url
		dft['title'] = title
		df = pd.concat([df,dft])
# 		print(df.shape)

	df = df[df.phone.str.len() == 10]
	df.to_excel('rent_la.xlsx')

