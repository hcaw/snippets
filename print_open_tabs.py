# Prints information on all open tabs in brave. Only works in MacOS.

import json, os
from pprint import pprint

user_name = os.environ.get('USER')

all_windows = json.load(open("/Users/" + user_name + "/Library/Application Support/brave/session-store-1"))['perWindowState']

for i, window in enumerate(all_windows):
	print("Window: ", i)
	all_tabs_in_window = window['frames']
	for j, tab in enumerate(all_tabs_in_window):
		print("\tTab: ", j)
		print("\t\ttitle: ", tab['title'])
		print("\t\turl: ", tab['src'])