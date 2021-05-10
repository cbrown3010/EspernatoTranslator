"""
The UT model contains the model part of the MVC structure
Currently unused
@author Charlie Cho
"""

from Tkinter import *
import UT_controller
from UniversalTranslator import stop_record
from UniversalTranslator import main


# class model:
#
#     def __init__(self):
#         pass
#
#     def model:
#         status_label['text'] = 'Recording...'
#         gui.update()
#         start_record()
#         # TODO move record function to separate file
#         # UT_record.record()
#         status_label['text'] = 'Transcribing...'
#         gui.update()
#         UT_transcribe.transcribe()
#         # TODO REMOVE BOTTOM 3
#         input_text_file = open('inputText.txt', 'r')
#         input_text = input_text_file.read()
#         input_text_file.close()
#         transcribe_label['text'] = input_text
#         status_label['text'] = 'Translating...'
#         gui.update()
#         UT_translate.translate()
#         # TODO REMOVE BOTTOM 3
#         translated_text_file = open('translatedText.txt', 'r')
#         translated_text = translated_text_file.read()
#         translated_text_file.close()
#         translation_label['text'] = translated_text
#         status_label['text'] = 'Vocalizing...'
#         gui.update()
#         UT_tts.tts()
#         status_label['text'] = 'Playing...'
#         gui.update()
#         UT_play.play()
#         status_label['text'] = 'Finished'
#         gui.update()
#         tkMessageBox.showinfo('Translation', 'Success')
