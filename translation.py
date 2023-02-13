#........................TRAMA....................

'''
The goal of the program:
           words Translator of Text with just one click on text work in python sheel.
            (in sheel of python)
            
   Programmer :
               Ahmadali Jamali

                   11.03.2021
                   Teheran
'''
#Start.....


#libraries
import pyautogui as pya
import pyperclip
import time
from googletrans import Translator, constants
from pprint import pprint
import pyautogui as pya


#class
translator = Translator()

#functions:
def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

# double clicks on a position of the cursor

#********************************API***********************************#
    
#***.........................Input/Output...........................***# 

#the Input output of the cmd:
if __name__ == '__main__':
    
    while True:
        
        #fw=open('Text_Translatore.txt','a')
        #input('press enter any key')
        pya.doubleClick(pya.position())
        var = copy_clipboard()
         

        #string = str(input('Write your comment:\n'))
            
        translation = translator.translate(str(var),dest="fa")
        
        y = f"{translation.origin} ({translation.src})  : {translation.text} ({translation.dest})"
        
        print(y)
        print('\n')
        
        #fw.write(str(y))
        #fw.write("\n")
        #fw.write("=========================================\n")
        #fw.close()
        
        input('Press enter to serach next text:\n')    
            

input()

#End
