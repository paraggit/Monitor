#!/opt/VRTSpython3/bin/python3

import platform

def hostuname(host=None):
	"""
		Get system uname of given host
		@args:
			host
		@return:
			dict()
			{
				platfrom : <platfrom>,
				arch	 : <architecture>
				hostname : <hostname>
				os       : <Operating System>
			}
	"""
	data = dict()
	if host is None:
		hostdata = platform.uname()
		data['platfrom'] = hostdata[0]
		data['host'] = hostdata[1]
		data['arch'] = hostdata[1]
		
	
	return data


def volumes(host):
	"""
		Get all system volumes
		@args
			host
		@return
			list() : all volumes list
	"""

	return data

def dg(host):
	"""
		Get DG name
		@args:
			host
		@return:
			list() :  all available dg name
	"""

	return data


def volumesize(volname,host,unit=None):
	"""
		Get volumesize of given volume
		@args:
			volumename
			host
			[unit] : MB,GB,KB
		@return:
			volumesize 

	"""

	return data


	
