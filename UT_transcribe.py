"""
The UT_transcribe file transcribes the audio from the user
@author Charlie Cho cbrown3010@gmail.com
"""
import io
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def transcribe():
    print('transcribing...')
    input_lang_file = open('inputLang.txt', 'r')
    input_language = input_lang_file.read()
    input_lang_file.close()
    client = speech.SpeechClient()

    # open the input audio file as reading/binary mode
    with io.open('inputAudio.wav', 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    # set encoding configuration to same as recording configurations, insert input language
    config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
                                     sample_rate_hertz=44100, language_code=input_language)
    # transcribe with Google API by inserting the configuration and audio
    response = client.recognize(config, audio)

    # print transcript, the alternatives[0] indicate the highest probable match, coded in utf8
    for result in response.results:
        print('-----Transcript: {}'.format((result.alternatives[0].transcript).encode('utf8')))

    input_lang_file = open('inputText.txt', 'w+')
    input_lang_file.write((result.alternatives[0].transcript).encode('utf8'))
    print ('saved transcript to inputText.txt')


if __name__ == '__main__':
    transcribe()
