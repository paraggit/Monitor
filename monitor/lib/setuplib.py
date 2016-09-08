#!/opt/VRTSpython3/bin/python3


def clusterstatus(host,nodes=None,testobj):
	""" 
		Checking cluster status:
 
		1. run "cfscluster status" command on test machines
		2. if it get's succeed on any of the node 
		   then verify whether CVM and FS status is running or not

		@return:
			True if cluster is running
			False if cluster is down
	"""
	status = 0
	if 'LM' in testobj.stack:
		return True

	for node in testobj.nodes:
		cmd_stat = command.run(constant.CFSCLUSTER, args=["status","|grep -i running"], hosts=node)
		exit_stat = cmd_stat['exit']
		if exit_stat == 0:
			cmd_out = cmd_stat['stdout'].split('\n')
			for line in cmd_out:
				if 'not-running' in line:
					status = 1

	if status == 1:
		print("CLUSTER IS DOWN")
		return False

	print("CLUSTER IS UP")
	return True


def startcluster(nodes):
	"""
		Start cluster 
		@args:
			nodelist
		@return:
			True: if cluster start sucessfully
			False: if cluster is not started successfully.
	"""
	
	if 'LM' in testobj.stack:
		return True
	


def stopcluster(host,nodes=None,testobj):
	"""
		Stoping cluster process.
		1. process the nodeslist and perform "hastop -local"
		    on all the nodes to stop the cluster
		2. disable the odm on all the nodes
		
		@args:
			nodelist
		@return:
			True : if cluster stop successfully.
			False: if cluster not stop successfully.
	"""

	if 'LM' in testobj.stack:
		return True
        
	for node in testobj.nodes:
                mount_cmd = command.run(constant.MOUNT, args=["-p"], hosts=[node])
                mount_out = mount_cmd['stdout'].split('\n')
                for line in mount_out:
                        if 'vxfs' in line:
                                return 1

                stop_cfs = command.run(constant.HASTOP, args=["-local"], hosts=node)
                if stop_cfs['exit'] != 0:
                        return 1
                gab_stat = command.run(constant.GABCONFIG, args=["-a"], hosts=node)
                gab_out = gab_stat['stdout'].split('\n')
                for line in gab_out:
                        if 'd' in line:
                                if 'Linux' in osname:
                                        odm_stat = command.run(constant.LINUXODM, args=['stop'], hosts=node)
                                        if odm_stat['exit'] != 0:
                                                return 1
                                elif 'SunOS' in osname:
					odm_stat = command.run(constant.SUNOSODM, args=['disable','vxodm'], hosts=node)
					if odm_stat['exit'] != 0:
						return 1
                                elif 'AIX' in osname:
                                        odm_stat = command.run(constant.AIXODM, args=['stop'], hosts=node)
                                        if odm_stat['exit'] != 0:
                                                return 1
                                elif 'HP-UX' in osname:
                                        odm_stat = command.run(constant.HPUXODM, args=['stop'], hosts=node)
                                        if odm_stat['exit'] != 0:
                                                return 1

        return True


def reboothost(host):
	"""
		Rebooting host
		@args:
			hostname,

	"""
