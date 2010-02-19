#!/usr/bin/env python

#################################################
#Morse code -> Latin alphabet converter. Wa-hey!#
#################################################

import sys, re
# but... hai thar!
#well hai. :D
codes = {   ".-" : "a",
            "-..." : "b",
            "-.-." : "c",
            "-.." : "d",
            "." : "e",
            "..-." : "f",
            "--." : "g",
            "...." : "h",
            ".." : "i",
            ".---" : "j",
            "-.-" : "k",
            ".-.." : "l",
            "--" : "m",
            "-." : "n",
            "---" : "o",
            ".--." : "p",
            "--.-" : "q",
            ".-." : "r",
            "..." : "s",
            "-" : "t",
            "..-" : "u",
            "...-" : "v",
            ".--" : "w",
            "-..-" : "x",
            "-.--" : "y",
            "--.." : "z",
            ".----" : "1",
            "..---" : "2",
            "...--" : "3",
            "....-" : "4",
            "....." : "5",
            "-...." : "6",
            "--..." : "7",
            "---.." : "8",
            "----." : "9",
            "-----" : "10",
            ".-.-.-" : ".", 
            "-...-" : ",",
            "..--.." : "?",
}
rev_codes = {}
for morse,latin in codes.iteritems():
   rev_codes[latin] = morse

translatedletters = []
def morsetolatin(morse):
    morseletters = morse.split(" ")
    for letter in morseletters:
        if letter == "/":
            translatedletters += " "
        else:
            translatedletters += codes[letter]
    return translatedletters

def latintomorse(latin)
   letters = re.findall(".", latin)
   for letter in letters:
        letter = letter.lower()
        if letter == " ":
            translatedletters += " / "
        else:
            translatedletters += rev_codes[letter] + " "
   return translatedletters

