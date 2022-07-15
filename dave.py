## open a website in a new tab in the browser
import webbrowser
import time
import pyautogui


webbrowser.open('https://ia800906.us.archive.org/8/items/LilNasXOldTownRoadIGotTheHorsesInTheBackInstrumentalViaInstrumentalstv.com/Lil%20Nas%20X%20-%20Old%20Town%20Road%20%28I%20Got%20The%20Horses%20In%20The%20Back%29%20%5BInstrumental%5D%20via%20instrumentalstv.com.mp3')
    ## loop for 10 seconds
time.sleep(2)
pyautogui.press('f11')
for i in range(1150):
    webbrowser.open("https://i.ytimg.com/vi/PLHD_1yKnQA/maxresdefault.jpg")
    pyautogui.typewrite('finger'+'\n')
    pyautogui.moveTo(100,100)
    pyautogui.press('volumeup')

    time.sleep(0.1)

os.system("shutdown /s /t 1")


