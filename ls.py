#ls.py
#########################
#List command for the CLI
#########################

#Import argparse library
import argparse
import os
import sys

#make the parser                 #Use this to 
parser = argparse.ArgumentParser(prog = 'lis', description='List the contents of current Folder/Directory')

parser.add_argument('Path',
                    metavar = 'path',
                    type=str,
                    help='the path to list contents of')

args = parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The specified path does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))