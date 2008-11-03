#!/usr/bin/env python
import sys

import command
from util.exceptions import FLANNException

def print_help():
    print r"""Usage: %s [command commans_args]

Comamnds:""" % sys.argv[0]
    for c in command.__all__:
        print "     ",c
    print r"""
For command specific help type: %s <command> -h""" % sys.argv[0]
    sys.exit(1)

def main():
    if len(sys.argv)==1:
        print_help()
    elif sys.argv[1]=="-h" or sys.argv[1]=="--help":
        print_help()
    else:
        try:
            cmd = command.get_command(sys.argv[1])
            cmd.execute_command(sys.argv[2:])
        except KeyError:
            print "Invalid command specified"
            print_help()
        except FLANNException, ex:
            print ex


if __name__ == "__main__":
    main()