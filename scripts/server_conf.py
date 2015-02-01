import sys, os, ast
from colorama import init
from colorama import Fore, Back, Style

options = [
	("static_path", "../client/static", "Path to static files directory", str),
	("templates_path", "../client/templates", "Path to template files directory", str),
	("sctp_port", 55770, "Port of sctp server", int),
	("sctp_host", "localhost", "Host of sctp server. Example: 'localhost'", str),
	("event_wait_timeout", 10, "Time to wait commands processing", int),
	("idtf_serach_limit", 30, "Number of maximum results for searching by identifier", int),
	("redis_host", "localhost", "Host of redis server. Example: 'localhost'", str),
	("redis_port", 6379, "Port of redis server", int),
	("redis_db_idtf", 0, "Number of redis database to store identifiers", int),
	("redis_db_user", 1, "Number of redis database to store user info", int),
	("host", "localhost", "Nost name. Example: 'localhost'", str),
	("port", 8000, "Host port", int),
	("google_client_id", "","Client id for google auth. Example: 'xxxxxx....'", str),
	("google_client_secret", "", "Client secret for google auth. Example: 'xxxxxx.....'", str),
	("super_emails", "", "List of emails of site super administrators (maximum rights). Example: ['test@gmail.com', 'test2@gmail.com']", list),
	("db_path", "data.db", "Path to database file. Example: 'data.db'", str)
]

init()

parsed = {}

if len(sys.argv) != 2:
	print Fore.GREEN + "Usage: " + Fore.RESET + "python server_conf.py <path to server cofiguration file>"
	sys.exit(0)

if os.path.exists(sys.argv[1]):
	
	print Fore.GREEN + "Open: " + sys.argv[1] + Fore.RESET
	f = open(sys.argv[1], 'r')
	lines = f.readlines()
	f.close()

	for l in lines:
		ls = l.split('=')
		
		if len(ls) != 2:
			continue
		
		option = None
		try:
			option = ls[0].strip()
			value = ast.literal_eval(ls[1].strip())
			parsed[option] = value
		except:
			if option:
				print Fore.RED + "Can't determine value of " + Fore.WHITE + option + Fore.RESET


opts = []
for opt in options:
	name, default, hlp, tp = opt

	if parsed.has_key(name):
		default = parsed[name]

	v =	raw_input(Fore.GREEN + "*** " + Fore.WHITE + hlp + "\n" + Fore.GREEN + name + Fore.WHITE + "(" + Fore.BLUE + str(default) + Fore.WHITE + "): ")
	if v and len(v) > 0:
		try:
			v = tp(ast.literal_eval(v))
			print Fore.BLUE + str(default) + Fore.WHITE + " -> " + Fore.BLUE + str(v) + Fore.RESET
		except:
			print Fore.RED + "Can't determine value, so use default " + Fore.WHITE + str(default) + Fore.RESET
			v = default
	else:
		v = default

	if tp == str:
		v = '"' + v + '"'
	opts.append((name, v))

f = open(sys.argv[1], 'w')
for opt in opts:
	name, value = opt
	f.write(name + " = " + str(value) + "\n")
f.close()
print Fore.GREEN + "New configuration file written at " + Fore.WHITE + sys.argv[1] + Fore.RESET
