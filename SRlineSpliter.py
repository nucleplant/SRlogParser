'''
Created on 2012. 11. 2.

@author: wonjeon ahn
'''
#-*- encoding: utf-8 -*-
from __future__ import print_function
logfile = '20121102.txt';
try:
	data = open(logfile);
	for each_line in data:
		try:
			(SRtype, requester, title, status) = each_line.split('/', 3)
			SRtype = SRtype.strip().upper()
			if (SRtype == 'SR') or (SRtype == 'OC'):
				print(SRtype, end='')
				print('\t', end='')
				requester = requester.strip()
				print(requester, end='')
				print('\t', end='')
				status = status.strip()
				print(status, end='')
				print('\t', end='')
				title = title.strip()
				print(title, end='')
				print('\n', end='')
		except ValueError:
			pass
	data.close() 
except IOError:
	print('The data file is missing!')


