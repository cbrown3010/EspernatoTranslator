"""
The UT_play file plays the audio that has been translated
@author Charlie Cho cbrown3010@gmail.com
"""
from playsound import playsound
import os

def play():
    print('playing speech...')
    playsound('outputAudio.mp3')
    os.remove('outputAudio.mp3')

def repeat():
    playsound('outputAudio.mp3')


# The below is used for Python
# import os
#
# def play():
#     print('playing translated text...')
#     os.system("omxplayer --display=5 /home/pi/Desktop/UT/output.mp3")
#

if __name__ == '__main__':
    play()
