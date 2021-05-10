"""
The UT_record file records the users input and saves it for translation
Currently it is unused as it is embedded in the main
@author Charlie Cho cbrown3010@gmail.com
"""
import pyaudio
import wave
import UniversalTranslator


def record():
    print('recording...')
    audio = pyaudio.PyAudio()
    # create stream with audio configurations, 16bit, 44100 frequency, one channel, default device, and 4096 buffer size
    stream = audio.open(format=pyaudio.paInt16, rate=44100, channels=1, input_device_index=0, input=True,
                        frames_per_buffer=4096)
    frames = []
    global stop
    while stop == 1:
        data = stream.read(4096)
        frames.append(data)
        UniversalTranslator.GUI.update()
    # stop, close and terminate stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # create audio file, set mode, channels, resolution and frame rate
    audio_file = wave.open('input_audio.wav', 'wb')
    audio_file.setnchannels(1)
    audio_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    audio_file.setframerate(44100)
    # join the frames collected together and write to audio
    audio_file.writeframes(b''.join(frames))
    # close audio file
    audio_file.close()


if __name__ == '__main__':
    record()
