#!/usr/bin/env python
import subprocess

import sys, re, os

class Base(object):
	'''
	send command and internal helper
	'''
	def __init__(self,url):
		self.url=url

	def _call(self,command):
		if subprocess.Popen(command, stderr=subprocess.PIPE).stderr.read(): # command output is from oc stderr 
			return subprocess.Popen(command, stderr=subprocess.PIPE).stderr.read()
		else:
			return subprocess.Popen(command, stdout=subprocess.PIPE).stdout.read()  # command output is from oc stdout
	
	def _return_random_name(self,length):
	    number = '0123456789'
	    alpha = 'abcdefghijklmnopqrstuvwxyz'
	    name = ''
	    for i in range(0,length,2):
	        name += random.choice(number)
	        name += random.choice(alpha)
	    return name
	
	def call_commands(self, *args):
		command = [x.encode('UTF8') for x in args]
		print command
		return self._call(command)

	def check_output_keyword(self,**args):
		if args['keyword'] in args['source']: return "OK"
		else: 
			error = "%s is not in %s !!"%(args['keyword'],args['source'])
			raise Exception(error)



if __name__ == '__main__':
	pass
	# url="https://host-8-241-25.host.centralci.eng.rdu2.redhat.com:8443"
	# l=["oc","login",url,"-u xiaocwan","-p p"]
 # 	cli = Base(url)
 # 	command = cli.get_command_list(l)
 # 	print cli._call(command)

 # 	print cli.call(["oc","whoami","-c"])