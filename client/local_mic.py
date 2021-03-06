# -*- coding: utf-8-*-
"""
A drop-in replacement for the Mic class that allows for all I/O to occur
over the terminal. Useful for debugging. Unlike with the typical Mic
implementation, Dingdang is always active listening with local_mic.
"""


class Mic:
    prev = None

    def __init__(self, config, speaker, passive_stt_engine, active_stt_engine):
        return

    def passiveListen(self, PERSONA):
        return True, "DINGDANG"

    def activeListenToAllOptions(self, THRESHOLD=None, LISTEN=True,
                                 MUSIC=False):
        return [self.activeListen(THRESHOLD=THRESHOLD, LISTEN=LISTEN,
                                  MUSIC=MUSIC)]

    def activeListen(self, THRESHOLD=None, LISTEN=True, MUSIC=False):
        if not LISTEN:
            return self.prev

        input = raw_input("YOU: ")
        self.prev = input
        return input

    def say(self, phrase, OPTIONS=None):
        print("DINGDANG: %s" % phrase)

    def stop_passive(self):
        pass
