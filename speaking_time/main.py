from gtts import gTTS
import os
import tempfile
import time


def number_to_words(num):
    if num % 10 == 1 and num % 100 != 11:
        return f'{num} минута'
    elif num % 10 in {2,3,4} and num % 100 not in {12,13,14}:
        return f'{num} минуты'
    else:
        return f'{num} минут'


while True:
    ti = time.localtime()
    time_str = time.strftime('%H:%M', ti).split(':')

    if '0' in time_str[-1][0]:
        rez = f'{time_str[0]} chasov ,{number_to_words(int(time_str[-1][-1]))} '
    else:
        rez = f'  {time_str[0]} chasov , {number_to_words(int(time_str[-1]))} '
    tts = gTTS(text=rez, lang='ru')
    # Create a temporary file to save the speech audio
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        tmp_file_path = tmp_file.name
        tts.save(tmp_file_path)

    # Play the saved audio file
    os.system(f'afplay {tmp_file_path}')

    # Clean up the temporary file after playback
    os.remove(tmp_file_path)
    time.sleep(1200)
