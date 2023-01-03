#!/usr/bin/env python3

import os
from termcolor import colored

os.system("sudo rm /bin/pydirman /bin/reader.out /etc/.pydirman.commands /.pydirman.config")

while True:
	try:
		ans = input(colored("Do you want to delete the configuration and profiles?[yes/no]")).lower()
	except AttributeError:
		print("Please type 'yes' or 'no'\n")
	else:
		break

		