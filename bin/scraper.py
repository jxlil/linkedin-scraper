#!/usr/bin/env python3

from argparse import ArgumentParser
from os import path

import sys
import time

try:
    sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), "..")))
    from scraper import __version__
    from scraper import main
except ModuleNotFoundError as e:
    print(f"[x] {e}")
    sys.exit(1)


if __name__ == "__main__":
    parser = ArgumentParser(description="Business scraper on Linkedin")
    parser.add_argument("-u", "--url", type=str, help="set URL", required="True")
    parser.add_argument(
        "-d", "--driver", type=str, help="Set path to chromedriver", required="True"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Set output file name",
        default=f"{time.strftime('%d%m%y-%H%M%S')}.csv",
    )
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s " + __version__
    )

    args = parser.parse_args()
    main.Init(args)
