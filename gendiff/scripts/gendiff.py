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
    parser.add_argument('-f', '--format',
                        dest='format',
                        metavar='FORMAT',
                        default='plain',
                        type=str,
                        nargs=1,
                        help='set format of output')
    args = parser.parse_args()
    print(args.file_path_1)
    print(args.file_path_2)
    print(args)


if __name__ == "__main__":
    main()
