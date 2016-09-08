#!/opt/VRTSpython/bin/python3

import subprocess
import paramiko
import constant

def run(cmd, args=None, hosts=None, user=None, password=None):
	""" 
		Running Command on local as well as remote host 
	"""

	if args is not None:
		cmd = "{} {}".format(cmd," ".join(args))
	output = dict()
	if hosts is None:
		try:
			cmd_data = subprocess.Popen(cmd,shell=True,\
				stdout=subprocess.PIPE,\
				stderr=subprocess.STDOUT)
			cmd_status=cmd_data.wait()
		except Exception as e:
			output['stdout'] = None
			output['stderr'] = e
			output['exit'] = 1
			return output

		cmd_out=list()
		out_lines = cmd_data.stdout.readlines()

		if len(out_lines) == 0:
			output['stdout'] = None
			output['exit'] = cmd_status
		else:
			for line in out_lines:
				cmd_out.append(line.decode().strip())

			out_data = "\n".join(cmd_out)
			output['stdout'] = out_data
			output['exit'] = cmd_status		
		
	else:
		host_list = list()
        
		if type(hosts) is list:
			host_list = hosts
		else:
			host_list.append(hosts) 

		if ((user is None) and (password is None)):
			""" getting envdata """
			#envdata = utils.get_envdata()
			user = constant.SYSTEMUSER 
			password = constant.SYSTEM_PASSWORD
        
		for host in host_list:
			paramiko.util.log_to_file('ssh.log') # sets up logging
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			client.load_system_host_keys()
			try:
				client.connect(host,username=user, password=password)
				transport =  client.get_transport().open_session()
				transport.exec_command(cmd.encode())
				stdout = transport.recv(1024).strip() 
				stderr = transport.recv_stderr(1024).strip()
				extstat = transport.recv_exit_status() 
				transport.close()
				if len(stdout) == 0:
					stdout = None
				else:
					stdout = stdout.decode()

				if len(stderr) == 0:
					stderr = None
				else:
					stderr = stderr.decode()

				output['stdout']=stdout
				output['stderr']=stderr
				output['exit']=extstat
			except Exception as e:
				output['stdout']= None
				output['stderr']= e
				output['exit']= 1
	return output
