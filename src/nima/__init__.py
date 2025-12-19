#!/usr/bin/env python3
"""
High-level example usage of the Nix manipulator library.
"""

import sys

from nima.cli import build_parser
from nima.expressions import NixSourceCode
from nima.manipulations import remove_value, set_value
from nima.parser import parse
from nima.serializer import serialize


def main(args=None):
    parser = build_parser()
    args = parser.parse_args(args)

    source: NixSourceCode
    match args.command:
        case "shell":
            print("Launching Nix shell...")
            # TODO
        case "set":
            source = parse(args.file.read())
            return set_value(
                source=source,
                npath=args.npath,
                value=args.value,
            )
        case "rm":
            source = parse(args.file.read())
            return remove_value(
                source=source,
                npath=args.npath,
            )
        case "test":
            original = args.file.read().strip("\n")
            source = parse(original)
            rebuild = source.rebuild().strip("\n")

            if original == rebuild:
                return "OK"
            else:
                return "Fail"
        case "serialize":
            return serialize(
                file=args.file,
                output=args.output,
            )
        case _:
            parser.print_help(sys.stderr)


if __name__ == "__main__":
    main()
