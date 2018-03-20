import json
import os
import subprocess
import sys

def escape_parameter(parameter):
	if type(parameter) != type(''):
		return False
	need_escape=['"', '[', ']', ' ', '?', '*', ',', '+']
	for c in need_escape:
		if parameter.find(c) >= 0:
			return True
	return False

def build_parameter(config):
	param_enabled = ['--' + x for x in config['enabled']]
	param_parameter = ' '.join(param_enabled) +' '
	param_dict = config['parameter']
	for key in [x for x in param_dict]:
		val = param_dict[key]
		#print(key, val)
		if type(val) != type(''):
			param_parameter = param_parameter + '--{0} {1} '.format(key, val)
		elif escape_parameter(val):
			param_parameter = param_parameter + '--{0} "{1}" '.format(key, val)
		else:
			param_parameter = param_parameter + '--{0} {1} '.format(key, val)
	return param_parameter

def extract_title(url):
	return os.path.split(url)[1]

def build_command(url, config):
	cmd = '"{0}" {1} {2} {3}.pdf'.format(config['bin'], build_parameter(config), url, extract_title(url))
	return cmd

if __name__ == '__main__':
	with open('config.json', 'r', encoding='utf-8') as f:
		config = json.load(f)
	#print(config)
	#parameter = build_parameter(config)
	#print(parameter)
	#print(build_command('https://en.wikipedia.org/wiki/Rectifier', config))
	#subprocess.call(build_command('https://en.wikipedia.org/wiki/Rectifier', config))
	subprocess.call(build_command(sys.argv[1], config))
