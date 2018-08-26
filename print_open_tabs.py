import json
from pprint import pprint

all_windows = json.load(open("/Users/harrywright/Library/Application Support/brave/session-store-1"))['perWindowState']

for i, window in enumerate(all_windows):
	print("Window: ", i)
	all_tabs_in_window = window['frames']
	for j, tab in enumerate(all_tabs_in_window):
		print("\tTab: ", j)
		print("\t\ttitle: ", tab['title'])
		print("\t\turl: ", tab['src'])