import os
import argparse
from pathlib import Path

def parse_args() -> tuple:
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path",
                    default="/home/barry/Documents/Coding/2022", help="path to the folder that needs organizing")
    ap.add_argument("-d", "--delimiter", default=" ", help="delimiter of file names")
    return ap.parse_args()

args = parse_args()

for filename in os.listdir(args.path):
    file_path = os.path.join(args.path, filename)
    if not os.path.isfile(file_path):
        continue
    subfolder_name = Path(filename).stem.split(args.delimiter)[0]
    subfolder_path = os.path.join(args.path,subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)
    os.rename(file_path, os.path.join(subfolder_path, filename))

