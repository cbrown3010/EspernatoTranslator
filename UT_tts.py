"""
The UT_tts file text-to-speech converts the translated output into an audio file
@author Charlie Cho cbrown3010@gmail.com
"""
from google.cloud import texttospeech


def tts():
    print ('vocalizing...')

    # open and read output language, output gender and translated text
    output_language_file = open('outputLang.txt', 'r')
    output_language = output_language_file.read()
    output_language_file.close()

    gender_file = open('gender.txt', 'r')
    gender = gender_file.read()
    gender_file.close()

    translated_text_file = open('translatedText.txt', 'r')
    translated_text = translated_text_file.read()
    translated_text_file.close()

    client = texttospeech.TextToSpeechClient()

    print('performing text-to-speech...')
    # synthesizes and parses the text to be vocalized
    synthesis_input = texttospeech.types.SynthesisInput(text=translated_text)
    # check if desired gender is male or female
    if gender == 'MALE':
        voice = texttospeech.types.VoiceSelectionParams(language_code=output_language,
                                                        ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
    else:
        voice = texttospeech.types.VoiceSelectionParams(language_code=output_language,
                                                        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
    # set the configuration and encoding for output audio
    audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    # input voice based on gender, configurations and synthesized text
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open('outputAudio.mp3', 'wb') as out:
        out.write(response.audio_content)
        out.close()
    print('saved speech as outputAudio.mp3')



if __name__ == '__main__':
    tts()
