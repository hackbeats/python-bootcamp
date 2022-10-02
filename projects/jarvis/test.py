# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:18:54 2021

@author: Yash U Hegde
"""

def speak(str):
    from win32com.client import Dispatch
    speak =Dispatch("SAPI.SpVoice")
    speak.Speak(str)
     
if __name__ =='__main__' :
    speak("hi how are you")