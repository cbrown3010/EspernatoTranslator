"""
The UT view file contains the view part of the MVC structure
Currently unused
@author Charlie Cho
"""

from Tkinter import *
import UT_controller
from UniversalTranslator import stop_record
from UniversalTranslator import main
translation_label = Label(gui)
translation_label.place(x=250, y=200)
transcribe_label = Label(gui)
transcribe_label.place(x=250, y=150)
status_label = Label(gui, text='', font='Verdana 15 bold')
status_label.place(x=250, y=100)
input_label = Label(gui, text='Language Input', font='Helvetica 15 bold')
input_label.place(x=10, y=0)
output_label = Label(gui, text='Language Output', font='Helvetica 15 bold')
output_label.place(x=10, y=150)
gender_label = Label(gui, text='Gender', font='Helvetica 15 bold')
gender_label.place(x=10, y=290)

# GUI button initialization and configuration for language/gender selection
english_input_button = Button(gui, text='English', command=UT_controller.input_english)
korean_input_button = Button(gui, text='Korean', command=UT_controller.input_korean)
japanese_input_button = Button(gui, text='Japanese', command=UT_controller.input_japanese)
english_input_button.place(x=10, y=30)
korean_input_button.place(x=10, y=60)
japanese_input_button.place(x=10, y=90)
english_output_button = Button(gui, text='English', command=UT_controller.output_english)
korean_output_button = Button(gui, text='Korean', command=UT_controller.output_korean)
japanese_output_button = Button(gui, text='Japanese', command=UT_controller.output_japanese)
english_output_button.place(x=10, y=180)
korean_output_button.place(x=10, y=210)
japanese_output_button.place(x=10, y=240)
male_button = Button(gui, text='Male')
female_button = Button(gui, text='Female')
male_button.place(x=10, y=320)
female_button.place(x=10, y=350)

# GUI button for functions set input/output, start translate and stop recording
translate_button = Button(gui, text='TRANSLATE', font='Helvetica 15 bold', height=4, width=10, command=main)
translate_button.place(x=250, y=270)
stop_button = Button(gui, text='STOP REC', font='Verdana 15 bold', command=stop_record)
stop_button.place(x=250, y=20)
input_button = Button(gui, text='OK', command=UT_controller.retrieve_input)
input_button.place(x=170, y=115)
output_button = Button(gui, text='OK', command=UT_controller.retrieve_output)
output_button.place(x=170, y=265)

# GUI textbox initialization and configuration
input_text_box = Entry(gui)
input_text_box.pack(pady=10, padx=0)
input_text_box.place(x=10, y=120)
output_text_box = Entry(gui)
output_text_box.pack(pady=10, padx=0)
output_text_box.place(x=10, y=270)
