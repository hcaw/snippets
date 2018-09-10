# Prints information on all open tabs in brave. Only works in MacOS.

import json, os, sys

# args = sys.argv[1:]

# if len(args) == 0 or args[0] == "-h":
#     print("### brave-tabs help ###")
#     print("Save Tabs:")
#     print("\t$ brave-tabs save")
#     print("Print Tabs:")
#     print("\t$ brave-tabs print")
#     sys.exit()

user_name = os.environ.get('USER')
all_windows = json.load(open("/Users/" + user_name + "/Library/Application Support/brave/session-store-1"))['perWindowState']


def save_tabs():
	print("saving tabs to ...")

def print_tabs():
    for i, window in enumerate(all_windows):
	    print("Window: ", i)
	    all_tabs_in_window = window['frames']
	    for j, tab in enumerate(all_tabs_in_window):
		    print("\tTab: ", j)
		    if 'title' in tab:
			    print("\t\ttitle: ", tab['title'])
		    if 'src' in tab:
			    print("\t\turl: ", tab['src'])


print_tabs()