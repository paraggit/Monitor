#!/opt/VRTSpython/bin/python3


def start(testobject):
	"""
		starting test on test machine
		@args:
			testobject
		@return:
			True: if test started successfully
			False: if test not started sucessfully.

		1. check cluster status.
		##################################### Do we need to download fsqa tar first before extract
		2. extract fsqa tar in testroot
		##################################### We need to NFS mount fsqa iand odmqa tar in case of CFS 
		3. extract odmqa tar on testroot 
		4. set run.devices.
		5. set run.env
		6. start cachevolume.
		7. start test.
	"""

	if system.clusterstatus == False:
		""" Cluster is not up  """
		return False

	if pkglib.extractfsqatar() == False:
		""" Fsqa tar extract Fails """
		return False

	if pkglib.extractodmqatar(odmqatarlocation,location) == False:
		""" odmqa tar extract fails """
		return False
	
	if testlib.setrundevices() == False:
		""" unable to set run.devices for set """
		return False

	if testlib.setrunenv() == False:
		""" Setting run.env fails """

	""" in some condition set test run """
	if testlib.settestrun(tests) == False:
		""" Error adding test in run file """
		return False

	if testlib.prerequisitesetup() == False:
		""" test  prerequisite setup fails"""
		return False

	if testlib.starttest(host) == False:
		""" test starting fails """
		return False

	""" Update test status to In Progress """

	if result.uploadresult() == False:
		""" upload test result Fails """
		return False
	
	return True


def update(testobj):
	"""
		Updating test status.
		@args:
			testobject
		@return:
			True: if update done successfully.
			False : if update not done successfully.

		1. check test status.
		2. mount resuld dir.
		3. copy resultfile.
		4. update time.
		5. return 
	"""

	if testlib.teststatus() == False:
		"""
			if test is not running update test status and return
		"""
		""" TODO: update  test status """
		return False

	if result.uploadresult() == False:
		""" error uploading result """
		return False

	""" Update test updation time """

	return True
	
		


def complet(testobj):
	"""
		Complete test and update final status.
		@args:
			testobj
		@return:
			True: if test updated successfully.
			False: if test not updated successfully.

		1. collest all test results.
		2. update test time.  ######## we will need config cycle as well
		3. update test status.
		4. return
	"""

	if result.uploadresult() == False:
		""" Return  """
		return False

	""" update test status """

	"""   """
	return True
