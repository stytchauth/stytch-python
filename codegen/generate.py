#!/usr/bin/env python3

import argparse
import logging
import subprocess
from typing import List, Optional

from codegen.core.generator import Generator
from codegen.core.logutils import ColoredLogFormatter


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_path",
        help="Input .yml file with an API spec or a folder container specs",
    )
    parser.add_argument(
        "output_dir", help="Output dir where the new files should be written"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite all files instead of merging them",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Use verbose logging"
    )
    return parser


def main(argv: Optional[List[str]] = None) -> None:
    parser = get_parser()
    args = parser.parse_args(argv)

    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level)
    root_logger = logging.getLogger()
    root_logger.handlers[0].setFormatter(ColoredLogFormatter())

    generator = Generator(args.input_path)

    logging.info(f"Generating APIs from {args.input_path}")
    generator.generate_all(args.output_dir, args.overwrite)

    logging.info("Running autoflake to remove unused imports")
    subprocess.Popen(["autoflake", "--in-place", "-r", args.output_dir]).wait()

    logging.info("Running formatter")
    subprocess.Popen(["black", args.output_dir]).wait()
    logging.info("All done!")


if __name__ == "__main__":
    main()
