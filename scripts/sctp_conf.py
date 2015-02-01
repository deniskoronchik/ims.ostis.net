import os, sys, ConfigParser
from colorama import init
from colorama import Fore, Back, Style

options = {
	"Network": {
		"Port": (55770, int, "Port number that will be used by sctp server")
	},
	"Repo": {
		"Path": ("../kb.bin", str, "Path to repository")
	},
	"Extensions": {
		"Directory": ("../sc-machine/bin/extensions", str, "Path to directory with memory extensions")
	},
	"Stat": {
		"UpdatePeriod": (1800, int, "Time period in seconds to save statistics"),
		"Path": ("../stat", str, "Path to directory, where to save statistics")
	},
	"memory": {
		"max_loaded_segments": (100, int, "Number of maximum loaded segments"),
		"save_period": (3600, int, "Memory state save period")
	},
	"filememory": {
		"engine": ("redis", str, "Name of filememory engine. Possible values: redis, filesystem")
	}
}

init()

if len(sys.argv) < 2:
	print Fore.GREEN + "Usage:" + Fore.RESET + " python sctp_config.py <path to config file>"
	sys.exit(0)

if os.path.exists(sys.argv[1]):

	print Fore.GREEN + " Open " + Fore.WHITE + sys.argv[1] + Fore.RESET
	config = ConfigParser.ConfigParser()
	config.read([sys.argv[1]])

	for section, opt in options.items():
		for option, data in opt.items():
			value, tp, hp = data
			if config.has_option(section, option):
				try:
					options[section][option] = (tp(config.get(section, option)), tp, hp)
				except ValueError:
					pass

config = ConfigParser.ConfigParser()
for section, opt in options.items():
	added_section = False
	print Fore.BLUE + section + Fore.RESET
	for option, data in opt.items():

		value, tp, hp = data
		v = raw_input("\t" + Fore.GREEN + hp +"\n\t" + Fore.WHITE + option + "(" + Fore.BLUE + str(value) + Fore.WHITE + "): " + Fore.RESET)
		try:
			if v and len(v) > 0:
				v = tp(v)
				print "\t" + Fore.BLUE + str(value) + Fore.WHITE + " -> " + Fore.BLUE + str(v) + Fore.RESET
			else:
				v = value
		except ValueError:
			print "\t\tInvalid data value: " + Fore.RED + str(v) + ". " + Fore.RESET + "Value: " + Fore.BLUE + str(value) + Fore.RESET + " will be used"
			v = value

		if not added_section:
			added_section = True
			config.add_section(section)
		config.set(section, option, v)

with open(sys.argv[1], 'w') as f:
	config.write(f)
