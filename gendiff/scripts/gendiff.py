#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        'file_path_1',
        metavar='first_file',
        type=str,
        nargs=1,
    )
    parser.add_argument(
        'file_path_2',
        metavar='second_file',
        type=str,
        nargs=1,
    )
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()
    print(args.file_path_1)
    print(args.file_path_2)
    print(args)


if __name__ == "__main__":
    main()
