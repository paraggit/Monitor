#!/opt/VRTSpython3/bin/python3


def checkpackges(package,host,platfrom):
	"""
		@args
			package name,
			hostname,
			platfrom,
		@return 
			True if package is installed.
			False if package is not installed.

		check given package installed on system or not
		1. check package installed or not 
		2. if package is installed return True
		3. if package is not installed on system return False.

	"""

	

	

def installpkgs(pkgname,host):
	""" 
		install vxfs pkgs 
		@args:
			pkgname as dict()
			hostname
		@return:
			True: if pkgs installed successfully
			False: if pkgs not installed successfully.

		TODO: create thread per host for installing packages 
	"""

	if type(pkgs) is dict:
		pass

	if type(host) is list:
		pass

	
	

def uninstallpkgs(pkgname,host,platfrom):
	""" 
		Uninstalling pkgs.
		@args:
			pkgname
			host
			platfrom
		@return:
			True: if pkg uninstalled successfully.
			False: if pkgs not uninstalled successfully.

		1. first check package is installed or not.
		2. then proceed for removing packages.
	"""
	
	if checkpackges(package,host,platfrom) == False:
		return True

	

	
	
	
	

def extractfsqatar(tarlocation,testroot):
	"""
		Extracting fsqa tar on given location.
		@args:
			fsqa tar location,
			testroot

		@return:
			True: if tar extracted successfully.
			False: if tar not extracted successfully.
	"""

def extractodmqatar(odmqatarlocation,location):
	"""
		Extraction odmqa tar on given location.
		@args:
			odmqatarlocation,
			destination
		@return:
			True: if tar extracted successfully.
                        False: if tar not extracted successfully.
	"""

