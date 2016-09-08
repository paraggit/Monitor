#!/opt/VRTSpython3/bin/python3

import command

def checknfsmount(builserver,mountpoint,host=None):
	"""
		Check if directory is already mounted or not
		True if directory is mounted
	"""
	cmd_out = command.run("mount",hosts=host)
	if cmd_out['exit'] != 0:
		return False

	for line in cmd_out['stdout'].split('\n'):
		if ((builserver in line) and (mountpoint in line)):
			return True

	return False
	
	

def nfsmount(server,sourcemntpt,targetmntpt,host=None):
	"""
		Do nfs mount,
		@args:
			server,
			sourcemntpt,
			targetmntpt

		@return:
			True: if successfully mounted
			False: if not mounted
	
		1. check if already mounted or not.

		
	"""
	
	if checknfsmount(server,sourcemntpt,host=host) == True:
		return True

	systemdata = systeminfo.hostuname()
	if systemdata['platfrom'] == 'Linux':
		cmd = "mount -t vxfs {}:{} {}".format(server,sourcemntpt,targetmntpt)
	if systemdata['platfrom'] == 'AIX':
		cmd = "mount -V vxfs {}:{} {}".format(server,sourcemntpt,targetmntpt)
	if systemdata['platfrom'] == 'SunOS':
		cmd = "mount -V vxfs {}:{} {}".format(server,sourcemntpt,targetmntpt)
	if systemdata['platfrom'] == 'HP-UX':
		cmd = "mount -V vxfs {}:{} {}".format(server,sourcemntpt,targetmntpt)

	cmd_out = command.run(cmd,hosts=host)

	if cmd_out['exit'] != 0:
		return False

	return True
	
def makedir(path,host=None):
	"""
		creating directory 
		

	"""
	
	if host is None:
		os.mkdir(path)


def mountresultdir():
	"""
		Mounting resultdir
		
	"""

	return True

	
