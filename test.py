from argparse import ArgumentParser, FileType
from configparser import ConfigParser

parser = ArgumentParser()
parser.add_argument("--text", required=True, type=str)
args = parser.parse_args()

print(args.text)
# f = open("/folder/hello.txt", "w")
f = open("hello.txt", "w")
f.write(args.text)
f.close()

while True:
    a = 1
