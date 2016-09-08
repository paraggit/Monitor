#!/opt/VRTSpython/bin/python3

import testlib
import setuplib

def install(testobj):
	"""
		INstall build on host
		@args:
			testobject
		@return:
			True: if build is install
			False: if build is not installed
	
		1. check if test is already running on setup.
		2. check cfsstatus.
		4. copy pkgs and fsqa.tar in testroot
		5. remove older packages if any
		7. return
	"""

	if testlib.teststatus(nodelist) == True:
		""" Test is already running on setup intimate user """
		return False

	if setuplib.clusterstatus == False:
		""" Cluster is Down intimate user and exit """
		return False

	#if buildlib.mountbuildlocation == False:
	#	""" Error mounting build directory """
	#	return False

	#testroot = utils.createbuilddir(testroot)
	#testroot = buildlib.createbuilddir(testroot)
	packages = buildlib.copybuild(testroot, platfrom, osname, buildname)
	#packages = buildlib.packages(testroot,platfrom,buildname=None,buildlocation=None)

	if packages is None:
		""" packages copy not sucessfull """
		return False
	
	if setuplib.stopcluster == False:
		""" unable to stop cluster """
		return False

	if pkglib.uninstallpkgs(packages,nodes) == False:
		""" Unable to uninstall package from system """
		return False

	if pkglib.installpkgs(packages,nodes) == False:
		""" Error installing packages """
		retun False

	return True	
	
