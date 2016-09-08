#!/opt/VRTSpython3/bin/python3

import mysql.connector
import re

def runsql(query,getid=False,count=False):
	"""
		@ usages
		query = "sql query statement"
		action = "rowcount,fetchone,fetchall"
	"""

	connect_args = {
		'user' : 'fsdbdemo',
		'port' : 3306,
		'password' : 'fsdbdemo!23',
		'database' : 'fsdbdemo',
		'host' : 'fswebpun.samgpunb.symantec.com'
	}

	try:
		conn = mysql.connector.connect(**connect_args)
	except Exception as e:
		return e 

	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Exception as e:
		return e


	if (re.search('^SELECT',query.upper())):
		data = cursor.fetchall()
		if count is True:
			data = cursor.rowcount
		if len(data) == 0:
			data = None

	elif (re.search('^INSERT',query.upper())):
		conn.commit()
		if getid is True:
			data = cursor.lastrowid
		else:
			data = 0
	else:
		data = cursor.rowcount
		conn.commit()

	cursor.close()
	conn.close()
	return data
