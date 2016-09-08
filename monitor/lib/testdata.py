#!/opt/VRTSpython/bin/python3

import sqldata

class TestData:
	""" 
		Getting all test information form database 
		and methods for setting new value to test properties.
	"""

	testid = None
	project = None
	user = None
	build = None
	platfrom = None
	osname = None
	arch = None
	dlv = None
	stack = None
	sio = None
	test = None
	status = None
	start = None
	update = None
	nodes = None
	master = None
	testroot = None
	configfile = None

	def __init__(self,testid):
		""" Constructor of the class  """
		self.testid = testid

		sql = "select prj_name,plat_name,usr_name,bld_name,os_name,\
			arch_name,test_dlv,test_stack,sio_mode,tt_name,stat_name,\
			test_start_date,test_last_update,test_nodes,test_master, \
			test_stats,test_testroot,test_config_file from fs_test_status \
			where test_id={}".format(testid)

		sqlresult = sqldata.runsql(sql)
		if sqlresult is None:
			return None

		for rec in sqlresult:
			self.project = rec[0]
			self.platfrom = rec[1]
			self.user = rec[2]
			self.build = rec[3]
			self.osname = rec[4]
			self.arch = rec[5]
			self.dlv = rec[6]
			self.stack = rec[7]
			self.sio = rec[8]
			self.test = rec[9]
			self.status = rec[10]
			self.start = rec[11]
			self.update = rec[12]
			self.nodes = rec[13]
			self.master = rec[14]
			self.testroot = rec[15]
			self.configfile = rec[16]
	

	def setPlatform(self,platformName):
		""" Setting Platfrom of Test """
		if platformName is None:
			condition = "plat_name=NULL"
		else:
			condition = "plat_name='{}'".format(platformName)
		
		sql = "update fs_test_status set {} where test_id={}".format(condition,self.testid)
		
		sqlres = sqldata.runsql(sql)
		if sqlres is None:
			return None
		else:
			self.platfrom = platformName

		return sqlres

	def setOS(self,OSname):
		""" Setting OS NAme """
		if OSname is None:
			condition = "os_name=NULL"
		else:
			condition = "os_name='{}'".format(OSname)
		sql = "update fs_test_status set {} where test_id={}".format(condition,self.testid)
		
		sqlres = sqldata.runsql(sql)
		if sqlres is None:
			return None
		else:
			self.osname = OSname
		return sqlres

	def setBuild(self,buildName):
		""" Setting build name  """
		if buildName is None:
			condition = "bld_name=NULL"
		else:
			condition = "bld_name='{}'".format(buildName)

		sql = "update fs_test_status set {} where test_id={}".format(condition,self.testid)
		
		sqlres = sqldata.runsql(sql)
	
		if sqlres is None:
			return None
		else:
			self.build = buildName
		return sqlres

	def setArch(self,archName):
		""" Setting Architecture """
		if archName is None:
			condition = "arch_name=NULL"
		else:
			condition = "arch_name='{}'".format(archName)

		sql = "update fs_test_status set {} where test_id={}".format(condition,self.testid)
		sqlres = sqldata.runsql(sql)
		
		if sqlres is None:
			return None
		else:
			self.arch = archName
		return sqlres

	def setDLV(self,DLV):
		""" Setting DLV version """
		if DLV is None:
			condition = "test_dlv=NULL"
		else:
			condition = "test_dlv='{}'".format(DLV)

		sql = "update fs_test_status set {} where test_id={}".format(condition,self.testid)
		sqlres = sqldata.runsql(sql)

		if sqlres is None:
			return None
		else:
			self.dlv = DLV
		return sqlres


	def setStack(self,stackName):
		""" Setting test stack """
		if stackName is None:
			condition = "test_stack=NULL"
		else:
			condition = "test_stack='{}'".format(stackName)

		sql = "update fs_test_status set {} where test_id={}".format(condition,self.testid)
		sqlres = sqldata.runsql(sql)

		if sqlres is None:
			return None
		else:
			self.stack = stackName
		return sqlres

	def setSIO(self,sioMode):
		""" Setting smartio Mode """
		if sioMode is None:
			condition = "sio_mode=NULL"
		else:
			condition = "sio_mode='{}'".format(sioMode)

		sql = "update fs_test_status set {} where test_id={}".format(condition,self.testid)
		sqlres = sqldata.runsql(sql)
		if sqlres is None:
			return None
		else:
			self.sio = sioMode
		return sqlres


	def setTestStart(self):
		""" Setting test start date """
		sql = "update fs_test_status set test_start_date=sysdate() where  test_id={}".foramt(self.testid)
		sqlres = sqldata.runsql(sql)
		if sqlres is None:
			return None
		else:
			""" TODO : get start date from sql """
			pass
		return sqlres

	def setTestUpdate(self):
		""" Updating test update recived time """
		sql = "update fs_test_status set test_last_update=sysdate() where  \
			test_id={}".foramt(self.testid)

		sqlres = sqldata.runsql(sql)
		if sqlres is None:
			return None
		else:
			""" TODO : get start date from sql """
			pass
		return sqlres
