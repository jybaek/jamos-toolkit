#-*- coding: utf-8 -*-
import argparse
from jamos_toolkit import JamosSeparator

parser = argparse.ArgumentParser(description='Jamos toolkit')
parser.add_argument('--string', default='안녕하세요. 날씨가 좋네요.', help='Please enter the string you want to separator.')
args = parser.parse_args()

def main():
    jamos = JamosSeparator(args.string)
    jamos.run()
    print("org: \n> {0}\n".format(args.string))
    print("jamos: \n> {0}\n".format(jamos.get()))

if __name__ == '__main__':
    main()
