#Music file must be in program folder.
#Conversion of .wav files to mp3 stepwise
# import os, pydub and glob
# list all wave files using glob.glob('./*.wav') in the programs folder
# for each wavefile in wavefiles list create an mp3 file using the wave file's name(firstpart - [0] + '.mp3').
# See syntax os.path.splitext(file)[0]
# Note: Extension part has value of 1. (os.path.splitext(file)[1])
# extract sound from the wavefile using pydub.AudioSegment.from_wav(wav_file)
# export this sound into the corresponding mp3 file created for the wave file using sound.export() method
# print completed message

import os
import pydub
import glob


#---------------------------------------------------------------------------------------------------------
# CONVERT SINGLE FILE AND PLAY
#---------------------------------------------------------------------------------------------------------
#FILE 1:
greatness_wav_file = os.path.splitext('J.Wiley - Greatness.mp3')[0] + '.wav'
sound = pydub.AudioSegment.from_mp3('J.Wiley - Greatness.mp3')
sound.export(greatness_wav_file, format="wav")
print("Converted")
from playsound import playsound
playsound(greatness_wav_file)
# FILE 2:
greatness_wav_file = os.path.splitext('Thank_You_Pentatonix.mp3')[0] + '.wav'
sound = pydub.AudioSegment.from_mp3('Thank_You_Pentatonix.mp3')
sound.export(greatness_wav_file, format="wav")
print("Converted")
from playsound import playsound
playsound(greatness_wav_file)

# FILE 3:
greatness_wav_file = os.path.splitext('Happy Now.mp3')[0] + '.wav'
sound = pydub.AudioSegment.from_mp3('Happy Now.mp3')
sound.export(greatness_wav_file, format="wav")
print("Converted")
from playsound import playsound
playsound(greatness_wav_file)
#----------------------------------------------------------------------------------------------------------

# Code begins here

#----------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------
# CONVERT MULTIPLE FILES
#---------------------------------------------------------------------------------------------------------
wav_files = glob.glob('./*.wav')
print(wav_files)
for wav_file in wav_files:
    mp3_file = os.path.splitext(wav_file)[0] + '.mp3'
    sound = pydub.AudioSegment.from_wav(wav_file)
    sound.export(mp3_file, format="mp3")
print("Conversion complete")












