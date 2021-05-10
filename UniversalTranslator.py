from Tkinter import *
import pyaudio
import wave
import UT_play
import UT_transcribe
import UT_translate
import UT_tts
import UT_controller
import tkMessageBox
import settings

# import UT_record


def start_record():
    global stop
    stop = 1
    print('recording...')
    audio = pyaudio.PyAudio()
    # create stream with audio configurations, 16bit, 44100 frequency, one channel, default device, and 4096 buffer size
    stream = audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input_device_index=0, input=True,
                        frames_per_buffer=4096)
    frames = []
    while stop == 1:
        data = stream.read(4096)
        frames.append(data)
        gui.update()
    # stop, close and terminate stream
    stream.stop_stream()
    stream.close()
    audio.terminate()
    # create audio file, set mode, channels, resolution and frame rate
    audio_file = wave.open('inputAudio.wav', 'wb')
    audio_file.setnchannels(1)
    audio_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    audio_file.setframerate(44100)
    # join the frames collected together and write to audio
    audio_file.writeframes(b''.join(frames))
    # close audio file
    audio_file.close


def stop_record():
    global stop
    stop = 0


def main():
    status_label['text'] = 'Recording...'
    gui.update()
    # starts the recording of the user input
    start_record()
    # TODO move record function to separate file
    # UT_record.record()
    status_label['text'] = 'Transcribing...'
    gui.update()
    # transcribes user input into text
    UT_transcribe.transcribe()
    # TODO remove three lines below with object orientated classes
    input_text_file = open('inputText.txt', 'r')
    input_text = input_text_file.read()
    input_text_file.close()
    transcribe_label['text'] = input_text
    status_label['text'] = 'Translating...'
    gui.update()
    # translates the text into desired language
    UT_translate.translate()
    # TODO remove three lines below with object orientated classes
    translated_text_file = open('translatedText.txt', 'r')
    translated_text = translated_text_file.read()
    translated_text_file.close()
    translation_label['text'] = translated_text
    status_label['text'] = 'Vocalizing...'
    gui.update()
    # performs speech to text of the translation
    UT_tts.tts()
    status_label['text'] = 'Playing...'
    gui.update()
    # plays the translated audio back to the user
    UT_play.play()
    status_label['text'] = 'Finished'
    gui.update()
    tkMessageBox.showinfo('Translation', 'Success')


# GUI initialization and configuration
gui = Tk()
gui.minsize(500, 400)
gui.geometry('500x400')
gui.title('Esperanto - Universal Translator')

menu_bar = Menu(gui)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Quit', command=gui.quit)
menu_bar.add_cascade(label='Menu', menu=file_menu)
gui.config(menu=menu_bar)

# GUI label initialization and configuration
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


def retrieve_input():
    input_value = input_text_box.get()
    if len(input_value) == 2:
        text_file = open('translation.txt', 'w+')
        text_file.write(input_value)
        text_file.close()
    else:
        text_file = open('inputLang.txt', 'w+')
        text_file.write(input_value)
        text_file.close()


def retrieve_output():
    input_value = output_text_box.get()
    text_file = open('outputLang.txt', 'w+')
    text_file.write(input_value)
    text_file.close()


# GUI button for functions set input/output, start translate and stop recording
translate_button = Button(gui, text='TRANSLATE', font='Helvetica 15 bold', height=4, width=10, command=main)
translate_button.place(x=250, y=270)
stop_button = Button(gui, text='STOP REC', font='Verdana 15 bold', command=stop_record)
stop_button.place(x=250, y=20)

input_button = Button(gui, text='OK', command=retrieve_input)
input_button.place(x=170, y=115)
output_button = Button(gui, text='OK', command=retrieve_output)
output_button.place(x=170, y=265)

# GUI textbox initialization and configuration
input_text_box = Entry(gui)
input_text_box.pack(pady=10, padx=0)
input_text_box.place(x=10, y=120)
output_text_box = Entry(gui)
output_text_box.pack(pady=10, padx=0)
output_text_box.place(x=10, y=270)


gui.mainloop()
