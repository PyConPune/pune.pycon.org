"""
    Code taken from https://pagure.io/pagure/blob/master/f/runworker.py
"""
import argparse
import sys
import subprocess


parser = argparse.ArgumentParser(
    description='Run Celery')
parser.add_argument(
    '--debug', dest='debug', action='store_true',
    default=False,
    help='Expand the level of data returned.')
parser.add_argument(
    '--noinfo', dest='noinfo', action='store_true',
    default=False,
    help='Reduce the log level.')

args = parser.parse_args()

cmd = [
    sys.executable, '-m', 'celery', 'worker', '-A', 'pyconpune.tasks'
]

if args.debug:
    cmd.append('--loglevel=debug')
elif args.noinfo:
    pass
else:
    cmd.append('--loglevel=info')

subp = subprocess.Popen(cmd)
subp.wait()
