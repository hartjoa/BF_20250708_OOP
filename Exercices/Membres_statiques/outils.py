from os import system
import time

class Outils:
    @staticmethod
    def clear_console():
        system("cls")

    @staticmethod
    def pause(seconds):
        time.sleep(seconds)