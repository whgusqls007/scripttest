from argparse import ArgumentParser, FileType
from configparser import ConfigParser

parser = ArgumentParser()
parser.add_argument("--text", required=True)
args = parser.parse_args()

config_parser = ConfigParser()

print(args.text)
# f = open("/folder/hello.txt", "w")
f = open("hello.txt", "w")
f.write(args.text)
f.close()

while True:
    a = 1
