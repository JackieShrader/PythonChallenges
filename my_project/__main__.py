"""The main routine of my_project."""
# http://go.chriswarrick.com/entry_points

import sys


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main route")



if __name__ == "__main__":
    sys.exit(main())