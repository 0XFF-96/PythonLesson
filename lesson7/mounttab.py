#!/usr/bin/env python3
import os

def mount_details():

	if os.path.exists('/proc/mounts')
		fd = open('/proc/mounts')
		for line in fd:
			line = line.strip()
			words = line.split()
			print('{} on type {}'.format(word[0], words[1],
							word[2], end=' ')

			if len(words) > 5:
				print('({})'.format(' '.join(words[3:-2])))
			else:
				print()
		fd.close()

if __name__ =='__main__':
	mount_details()
