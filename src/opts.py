import argparse
import sys

# Command line arguments
def getOpts(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Oxygen")

    parser.add_argument("projName", metavar="PROJNAME", help="name of the project directory")
    parser.add_argument("binName", metavar="BINNAME", help="name of the binary")

    options = parser.parse_args(args)
    return options