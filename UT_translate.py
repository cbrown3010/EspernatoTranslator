"""
The UT_translate file translates the transcribed text into the desired language
@author Charlie Cho cbrown3010@gmail.com
"""
# the version 2 of translate is used instead of the version 3 as it is simpler and fits the needs of this function
from google.cloud import translate_v2


def translate():
    translate_client = translate_v2.Client()

    # open and read the input text and desired language
    input_text_file = open('inputText.txt', 'r')
    input_text = input_text_file.read()
    input_text_file.close()

    output_language_file = open('translation.txt', 'r')
    output_language = output_language_file.read()
    output_language_file.close()

    print('translating...')
    # input text and desired language to feed to API
    translation = translate_client.translate(input_text, target_language=output_language)
    print(u'-----Translation: {}'.format(translation['translatedText']))

    print('saved translation to translatedText.txt')
    translated_text_file = open('translatedText.txt', 'w+')
    # encode for utf8 for text file
    translated_text_file.write(translation['translatedText'].encode('utf8'))
    translated_text_file.close()


if __name__ == '__main__':
    translate()
