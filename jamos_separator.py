#-*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(description='Jamos separator')
parser.add_argument('--string', default='안녕하세요. 날씨가 좋네요.', help='Please enter the string you want to separator.')
args = parser.parse_args()

class JamosSeparator():
    def __init__(self, string):
        self.string = string
        self.result = []
        self.choseong_list = [char for char in "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"]
        self.jungseong_list = [char for char in "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"]
        self.jongseong_list = [char for char in " ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"]

    def run(self):
        for char in self.string:

            character_code = ord(char)

            # Do not process unless it is in Hangul syllables range.
            if 0xD7A3 < character_code or character_code < 0xAC00:
                continue

            choseong_index = (character_code - 0xAC00) // 21 // 28
            jungseong_index = (character_code - 0xAC00 - (choseong_index * 21 * 28)) // 28
            jongseong_index = character_code - 0xAC00 - (choseong_index * 21 * 28) - (jungseong_index * 28)

            self.result.append(self.choseong_list[choseong_index])
            self.result.append(self.jungseong_list[jungseong_index])
            self.result.append(self.jongseong_list[jongseong_index])
            self.result.append("_")

    def get(self):
        return self.result

def main():
    jamos = JamosSeparator(args.string)
    jamos.run()
    print("org: \n> {0}\n".format(args.string))
    print("jamos: \n> {0}\n".format(jamos.get()))

if __name__ == '__main__':
    main()
