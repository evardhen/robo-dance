# -*- coding: utf-8 -*-

###########################################################
# Retrieve robot audio buffer
# Syntaxe:
#    python scriptname --pip <ip> --pport <port>
#
#    --pip <ip>: specify the ip of your robot (without specification it will use the NAO_IP defined some line below
#
# Author: Alexandre Mazel
###########################################################

NAO_IP = "10.0.7.101"

from optparse import OptionParser
import naoqi
import numpy as np
import time
import sys
import os
import wave
from audio_recognition_system_py27.libs.reader_file import FileReader
from danceroom import DanceRoom
import speech_recognition as asr

sys.path.insert(0, './audio_recognition_system_py27/libs')

class SoundReceiverModule(naoqi.ALModule):
    """
    Use this object to get call back from the ALMemory of the naoqi world.
    Your callback needs to be a method with two parameter (variable name, value).
    """

    def __init__(self, strModuleName, strNaoIp, naoPort):
        try:
            naoqi.ALModule.__init__(self, strModuleName)
            self.BIND_PYTHON(self.getName(), "callback")
            self.strNaoIp = strNaoIp
            self.naoPort = naoPort
            self.danceRoom = DanceRoom()
            self.outfile = None
            self.seconds = 5
        except BaseException, err:
            print("ERR: abcdk.naoqitools.SoundReceiverModule: loading error: %s" % str(err))

    # __init__ - end
    def __del__(self):
        print("INF: abcdk.SoundReceiverModule.__del__: cleaning everything")
        self.stop()

    def start(self):
        audio = naoqi.ALProxy("ALAudioDevice", self.strNaoIp, self.naoPort)
        nNbrChannelFlag = 3  # ALL_Channels: 0,  AL::LEFTCHANNEL: 1, AL::RIGHTCHANNEL: 2; AL::FRONTCHANNEL: 3  or AL::REARCHANNEL: 4.
        nDeinterleave = 0
        nSampleRate = 16000
        audio.setClientPreferences(self.getName(), nSampleRate, nNbrChannelFlag,
                                   nDeinterleave)  # setting same as default generate a bug !?!
        tts = naoqi.ALProxy("ALTextToSpeech", self.strNaoIp, self.naoPort)
        tts.say("Hit me!")
        time.sleep(2)
        audio.subscribe(self.getName())
        print("INF: SoundReceiver: started!")


    def stop(self):
        print("INF: SoundReceiver: recognizing song...")
        audio = naoqi.ALProxy("ALAudioDevice", self.strNaoIp, 9559)
        audio.unsubscribe(self.getName())
        self.write_outfile(self)
        self.dance(self)
            #  ALMotion's angleInterpolationBezier function is a blocking call, so hopefully the loop should not continue until the dance is done
            # TODO: start dancing the correct dance for the song
        print("INF: SoundReceiver: stopped!")

    def write_outfile(self):
        if (self.outfile != None):
            self.outfile.close()
            strFilenameOutChanWav = self.strFilenameOut.replace(".raw", ".wav")
            with open("./out.raw", "rb") as inp_f:
                data = inp_f.read()
                out_f = wave.open(strFilenameOutChanWav, "wb")
                out_f.setnchannels(1)
                out_f.setsampwidth(2)  # number of bytes
                out_f.setframerate(16000)
                out_f.writeframesraw(data)
                out_f.close()

    def dance(self):
        tts = naoqi.ALProxy("ALTextToSpeech", self.strNaoIp, self.naoPort)
        song_info = self.recognize_from_file()
        song_name = song_info.get('songname')
        tts.say("Song recognized, dancing to " + song_name)
        time.sleep(1)
        if (song_name == "Disco_Disco"):
            self.danceRoom.disco_dance()
        elif (song_name == "Yoga"):
            self.danceRoom.yoga_dance()
        elif (song_name == "Metal"):
            self.danceRoom.headbang_dance()
        elif (song_name == "Waltzer"):
            self.danceRoom.headbang_dance()
        elif (song_name == "Hey ya"):
            self.danceRoom.headbang_dance()
        elif (song_name == "Feeling Good"):
            self.danceRoom.headbang_dance()

    def processRemote(self, nbOfChannels, nbrOfSamplesByChannel, aTimeStamp, buffer):
        """
        This is THE method that receives all the sound buffers from the "ALAudioDevice" module
        """
        aSoundDataInterlaced = np.fromstring(str(buffer), dtype=np.int16)
        aSoundData = np.reshape(aSoundDataInterlaced, (1, nbrOfSamplesByChannel), 'F') # nbOfChannels hardcoded to 1

        # save to file
        self.strFilenameOut = "./out.raw"
        if (self.outfile == None):
            print("INF: Writing sound to '%s'" % self.strFilenameOut)
            self.outfile = open(self.strFilenameOut, "wb")

        aSoundData[0].tofile(self.outfile)  # wrote only one channel

    # processRemote - end

    def recognize_from_file(self, fileName="out.wav"):

        directory = os.getcwd()
        filePath = directory + '/' + fileName
        print(filePath)

        r = FileReader(filePath)
        song_info = r.parse_audio(self.seconds)
        r.recognize()

        print(song_info.get('songname'))
        return song_info

    def version(self):
        return "0.6"


# SoundReceiver - end


def main():
    """ Main entry point

    """
    parser = OptionParser()
    parser.add_option("--pip",
                      help="Parent broker port. The IP address or your robot",
                      dest="pip")
    parser.add_option("--pport",
                      help="Parent broker port. The port NAOqi is listening to",
                      dest="pport",
                      type="int")
    parser.add_option("--seconds",
                      help="Number of seconds that should be recorded by Nao",
                      dest="seconds",
                      type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559,
        seconds = 7)

    (opts, args_) = parser.parse_args()
    pip = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = naoqi.ALBroker("myBroker",
                              "0.0.0.0",  # listen to anyone
                              0,  # find a free port and use it
                              pip,  # parent broker IP
                              pport)  # parent broker port

    # Warning: SoundReceiver must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global SoundReceiver
    SoundReceiver = SoundReceiverModule("SoundReceiver", pip, pport)
    SoundReceiver.start()
    time.sleep(opts.seconds)
    print("%i seconds recorded...", opts.seconds)
    myBroker.shutdown()
    sys.exit(0)


if __name__ == "__main__":
    main()
