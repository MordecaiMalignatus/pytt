#!/usr/bin/env python3.5

import sys

from reconstruct import get_current_project
from serialise import replace_current_project


def add_handler(input: str):
    current_project = get_current_project()
    current_project.add_task(input)

    print(current_project.stringify())

    replace_current_project(current_project)


def do_handler(input_str):
    current_project = get_current_project()
    current_project.do_task(int(input_str))

    print(current_project.stringify())

    replace_current_project(current_project)


def parse_command(argv: str):
    if argv.startswith("add"):
        add_handler(argv[4:])

    if argv.startswith("do"):
        do_handler(argv[3:])


if __name__ == '__main__':
    args = " ".join(sys.argv[1:])
    parse_command(args)
