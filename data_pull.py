#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2021-05-25
Purpose: Pull data from CyVerse DS for PhenomeForce presentation
"""

import argparse
import os
import sys
import subprocess


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='PhenomeForce data downloader',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('data_path',
                        metavar='data_path',
                        help='CyVerse data path')

    parser.add_argument('-d',
                        '--download_dir',
                        help='Download directory',
                        metavar='str',
                        type=str,
                        required=True)

    return parser.parse_args()


# --------------------------------------------------
def download_tar(data_path):
    cmd = f'iget -fKPVT {data_path}'
    subprocess.call(cmd, shell=True)


# --------------------------------------------------
def uncompress_tar(filename):
    cmd = f'tar -xzvf {filename}'
    subprocess.call(cmd, shell=True)


# --------------------------------------------------
def remove_tar(filename):
    cmd = f'rm {filename}'
    subprocess.call(cmd, shell=True)

# --------------------------------------------------
def main():
    """Download, uncompress, and remove tar here"""

    args = get_args()
    os.chdir(args.download_dir)
    download_tar(args.data_path)
    file = os.path.basename(args.data_path)
    uncompress_tar(file)
    remove_tar(file)


# --------------------------------------------------
if __name__ == '__main__':
    main()
