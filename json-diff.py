import sys
import json

def list_diff(list_one, list_two):
	diff = []
	for e in list_one:
		if e not in list_two:
			diff.append(e)
	return diff;

def diff(diff, data):
	diff_list = []
	for d in diff:
		i = 0;
		for e in data:
			if (e["groupValue"] == d):
				diff_list.append(e)
				print("['data'][", i, "] -- ", d)
			i = i + 1
	return json.dumps(diff_list)

def write_diff_json(fname_1, fname_2, dct, write_empty_json = False):
	nd = not dct
	print(fname_1, fname_2, "not dct =", nd, "write_empty_json =", write_empty_json)
	if write_empty_json == False and not dct:
		return
	fname = fname_1[0:fname_1.find(".json")] + "#" + fname_2[0:fname_2.find(".json")] + ".json"
	f = open('diff/' + fname, "w")
	f.write(dct)
	f.close()

def json_parse(filename):
	f = open('res/' + filename, "r")
	j = json.loads(f.read())
	f.close()
	return j

def json_to_list(json):
	l = []
	for e in json:
		l.append(e['groupValue'])
	return l

# The app takes the two file names are arguments
files = sys.argv[1:]

jsons = {}
lists = {}
i = 0
for f in files:
	if f.rfind('/') >= 0:
		f = f[ f.rfind('/') + 1:]
		files[i] = f
	jsons[f] = json_parse(f)
	lists[f] = json_to_list(jsons[f]['data'])
	i = i + 1

i = 0
for f in files:
	i = i + 1
	for g in files[i:]:
		print(f, "-", g, "=")
		write_diff_json(f, g, diff(list_diff(lists[f], lists[g]), jsons[f]['data']))
		write_diff_json(g, f, diff(list_diff(lists[g], lists[f]), jsons[g]['data']))