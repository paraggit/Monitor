#!/opt/VRTSpython3/bin/python3

import os
import time


def createpackagedir(testroot):
	"""
		create directory under testroot for copyting build packages
		@args


		@return:
			On Success return directory location
			on fail return None
	"""

	#datestr = str(time.strftime("%d-%m-%Y"))
	datestr = "pkgs"

	if not os.path.isdir("{}/{}".format(testroot,datestr)):
		utils.makedir("{}/{}".format(testroot,datestr))

	return "{}/{}".format(testroot,datestr)

def checkbuild(buildname)
	"""
		Checking build is available or not
		@args:
		
		@return:
			True: if build is available
			False if build is not available:
	
	"""

	bld_path = "{}/fsbuild/delivery/6.2.0/".format(constant.BUILDBASE)

	for dit in os.listdir(bld_path):
		if buildname in dit:
			return True

	return False

def getpackagehash(buildname,platform,osname):
	""" 
		Create hash of package name with location
		@args:
			Buildname
			Platfrom
			osname
		@return:
			dict()

	"""

	build_base = "/{}/fsbuild/delivery/6.2.0/{}/linux/fs_{}/donotship/debug/"

	if platfrom == 'Linux':
		fspkgd = pkgmap.maphash['LINUX_FS'].format(constant.BASEDIR,)

	


def copybuild(testroot, platfrom, osname, buildname):
	""" 
		Copying build from build server
		@args

		@return:
			On success=>
			dict: package value pair
			On Failure:
			return None

		1. Mount build server
		2. check build Availiblity.
		3. create package dirtectory.
	"""

	""" Mounting build location """
	if mountbuildlocation() == False:
		""" Error mounting build location """
		return False

	""" check build availiblity  """
	if checkbuild(buildname) == False:
		""" Build is not available """
		return False

	""" Creating pkgs dir  """
	pkgdir = createpackagedir(testroot)
	if pkgdir if None:
		""" Error Creating build dir """
		return False

	""" get packages list from build location  """
	packages = getpackagehash(buildname,platform,osname)
	if packages is None:
		""" Unable to get package from buildlocation """
		return False

	""" copy build from source to destination """
	if stack == 'LM':
		pkglist = constant.LMPKGS
	elif stack == 'CFS':
		pkglist = constant.CFSPKGS

	""" copying packages in directory """
	for pkg in pkglist:
		
		
		


def mountbuildlocation():
	"""
		mounting build location 

		@return:
			True: if directory mounted successfully.
			False: if directory not mounted successfully.
	"""
	

	if os.path.exists(constant.BUILDBASE) == False:
		os.mkdir(constant.BUILDBASE)

	return utils.nfsmount(constant.BUILDSERVER,constant.BUILDMNTPT,constant.BUILDBASE)
		
