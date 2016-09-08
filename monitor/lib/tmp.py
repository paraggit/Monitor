#!/opt/VRTSpython3/bin/python3

import utils

builserver = "fswebpun"
sourcemountpoint = "/mnt_davidson"
targetmountpoint="/mnt1"
host = None
#out =  utils.checknfsmount(builserver,mountpoint,host=host)
out =  utils.nfsmount(builserver,sourcemountpoint,targetmountpoint,host=host)
print(out)
