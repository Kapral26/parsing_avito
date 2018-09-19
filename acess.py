#! /usr/bin/python3.5

import subprocess

link = '/etc/group'

with open(link) as file:
	file = file.read()
	file = file.split("\n")
	for row in file:
		group = row.split(":")[0]
		command = 'usermod -aG ' + group + ' kapral26'
		print(command)
		subprocess.call(command, shell=True)