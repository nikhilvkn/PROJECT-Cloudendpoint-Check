#!/usr/bin/python

from version import __version__
import argparse
import sys
import os


def main(arguments):

	scripts = {
			'service-check' : '/home/tivo/bin/service-check.py',
			'server' : '/home/tivo/bin/server.py',
			'service' : '/home/tivo/bin/service.py',
		}

	parse = argparse.ArgumentParser()
	parse.add_argument('command', 
						help='command to query inception\n: {}'.format(', '.join(sorted(scripts.keys()))))
	parse.add_argument('args', nargs=argparse.REMAINDER,
						help='The arguments to the command')
	parse.add_argument('--version', action='version',
                    version='Inception Scripts: {version}'.format(version=__version__))
	parse_arguments = parse.parse_args(arguments)

	if parse_arguments.command not in scripts:
		print('These are the available scripts to run:')
		print('\n'.join(sorted(scripts.keys())))
	else:
	 	os.execv(scripts.get(parse_arguments.command), [scripts.get(parse_arguments.command)] + parse_arguments.args)


if __name__ == '__main__':
	try:
		main(sys.argv[1:])
	except KeyboardInterrupt:
		pass








