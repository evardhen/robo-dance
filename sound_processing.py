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

sys.path.insert(0, './audio_recognition_system_py27/libs')


class SoundReceiverModule(naoqi.ALModule):
    """
    Use this object to get call back from the ALMemory of the naoqi world.
    Your callback needs to be a method with two parameter (variable name, value).
    """

    def __init__(self, strModuleName, strNaoIp):
        try:
            naoqi.ALModule.__init__(self, strModuleName)
            self.BIND_PYTHON(self.getName(), "callback")
            self.strNaoIp = strNaoIp
            self.outfile = None
            self.aOutfile = [None] * (4 - 1)  # ASSUME max nbr channels = 4
        except BaseException, err:
            print("ERR: abcdk.naoqitools.SoundReceiverModule: loading error: %s" % str(err))

    # __init__ - end
    def __del__(self):
        print("INF: abcdk.SoundReceiverModule.__del__: cleaning everything")
        self.stop()

    def start(self):
        audio = naoqi.ALProxy("ALAudioDevice", self.strNaoIp, 9559)
        nNbrChannelFlag = 0  # ALL_Channels: 0,  AL::LEFTCHANNEL: 1, AL::RIGHTCHANNEL: 2; AL::FRONTCHANNEL: 3  or AL::REARCHANNEL: 4.
        nDeinterleave = 0
        nSampleRate = 48000
        audio.setClientPreferences(self.getName(), nSampleRate, nNbrChannelFlag,
                                   nDeinterleave)  # setting same as default generate a bug !?!
        audio.subscribe(self.getName())
        print("INF: SoundReceiver: started!")
        # self.processRemote( 4, 128, [18,0], "A"*128*4*2 ); # for local test

        # on romeo, here's the current order:
        # 0: right;  1: rear;   2: left;   3: front,

    def stop(self):
        print("INF: SoundReceiver: stopping...")
        audio = naoqi.ALProxy("ALAudioDevice", self.strNaoIp, 9559)
        audio.unsubscribe(self.getName())
        # self.convert_raw_to_wav()
        print("INF: SoundReceiver: stopped!")
        if (self.outfile != None):
            self.outfile.close()

    def processRemote(self, nbOfChannels, nbrOfSamplesByChannel, aTimeStamp, buffer):
        """
        This is THE method that receives all the sound buffers from the "ALAudioDevice" module
        """
        aSoundDataInterlaced = np.fromstring(str(buffer), dtype=np.int16)
        aSoundData = np.reshape(aSoundDataInterlaced, (nbOfChannels, nbrOfSamplesByChannel), 'F')

        # save to file
        fileNameFinal = ""
        self.nbOfChannels = nbOfChannels
        self.strFilenameOut = "./out.raw"
        if (self.outfile == None):
            print("INF: Writing sound to '%s'" % self.strFilenameOut)
            self.outfile = open(self.strFilenameOut, "wb")
            for nNumChannel in range(1, nbOfChannels):
                strFilenameOutChan = self.strFilenameOut.replace(".raw", "_%d.raw" % nNumChannel)
                self.aOutfile[nNumChannel - 1] = open(strFilenameOutChan, "wb")
                print("INF: Writing other channel sound to '%s'" % strFilenameOutChan)

        aSoundData[0].tofile(self.outfile)  # wrote only one channel
        self.aSoundData = aSoundData

    def convert_raw_to_wav(self):
        for nNumChannel in range(1, self.nbOfChannels):
            self.aSoundData[nNumChannel].tofile(self.aOutfile[nNumChannel - 1])
            # convert to wav???
            strFilenameOutChan = self.strFilenameOut.replace(".raw", "_%d.raw" % nNumChannel)
            strFilenameOutChanWav = strFilenameOutChan.replace(".raw", ".wav")
            fileNameFinal = strFilenameOutChanWav
            with open(strFilenameOutChan, "rb") as inp_f:
                data = inp_f.read()
                with wave.open(strFilenameOutChanWav, "wb") as out_f:
                    out_f.setnchannels(1)
                    out_f.setsampwidth(2)  # number of bytes
                    out_f.setframerate(44100)
                    out_f.writeframesraw(data)

    # song_info = self.recognize_from_file(fileNameFinal)
    # processRemote - end

    def recognize_from_file(fileName="awaken-136824.mp3"):
        seconds = 5
        # fileName = "awaken-136824.mp3"

        directory = os.getcwd()
        filePath = directory + '/mp3/' + fileName
        print(filePath)

        r = FileReader(filePath)
        song_info = r.parse_audio(seconds)
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
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

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
    SoundReceiver = SoundReceiverModule("SoundReceiver", pip)
    SoundReceiver.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)


if __name__ == "__main__":
    main()
