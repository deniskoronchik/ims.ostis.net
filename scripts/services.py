import sys, os

scripts_path = os.path.abspath(os.path.dirname(__file__))

def service(service_name, user_name, group_name, script):
	
	print "Setup sevice: " + service_name
	f = open(os.path.join('/etc/init/', service_name) + '.conf', 'w')
	
	template = 'start on runlevel [2345]\n' + \
				'stop on runlevel [016]\n' + \
				'setuid ' + user_name + '\n' + \
				'setgid ' + group_name + '\n' + \
				'respawn\n' + \
				'script\n' + \
				script + '\n' + \
				'end script'
	f.write(template)
	f.close()

if len(sys.argv) != 2:
	print "Usage: sudo python services.py <user name>"
	sys.exit(0)

user = sys.argv[1]

sctp_exec = '\texec ' + os.path.normpath(os.path.join(scripts_path, '../sc-machine/bin/sctp-server')) + ' ' + os.path.normpath(os.path.join(scripts_path, '../config/sc-web.ini'))
service('sctp', user, user, sctp_exec)

scweb_exec = '\tcd ' + os.path.normpath(os.path.join(scripts_path, '..')) + '\n' + \
		    '\t. env/bin/activate\n' + \
		    '\tpython sc-web/server/app.py --cfg=config/server.conf'
service('scweb', user, user, scweb_exec)
