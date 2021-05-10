"""
The UT controller file contains the controller part of the MVC structure
@author Charlie Cho
Currently in use but under development
"""


def input_english():
    text_file = open('inputLang.txt', 'w+')
    text_file.write('en-US')
    text_file.close()


def input_korean():
    text_file = open('inputLang.txt', 'w+')
    text_file.write('ko-KR')
    text_file.close()


def input_japanese():
    text_file = open('inputLang.txt', 'w+')
    text_file.write('ja-JP')
    text_file.close()


def output_japanese():
    text_file = open('outputLang.txt', 'w+')
    text_file.write('ja-JP')
    text_file.close()
    text_file2 = open('translation.txt', 'w+')
    text_file2.write('ja')
    text_file2.close()


def output_english():
    text_file = open('outputLang.txt', 'w+')
    text_file.write('en-US')
    text_file.close()
    text_file2 = open('translation.txt', 'w+')
    text_file2.write('en')
    text_file2.close()


def output_korean():
    text_file = open('outputLang.txt', 'w+')
    text_file.write('ko-KR')
    text_file.close()
    text_file2 = open('translation.txt', 'w+')
    text_file2.write('ko')
    text_file2.close()


def output_male():
    text_file = open('gender.txt', 'w+')
    text_file.write('MALE')
    text_file.close()


def output_female():
    text_file = open('outputLang.txt', 'w+')
    text_file.write('FEMALE')
    text_file.close()
