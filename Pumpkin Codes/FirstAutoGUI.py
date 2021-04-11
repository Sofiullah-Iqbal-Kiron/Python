import pyautogui

for i in range(30):
    pyautogui.typewrite("#Boycott_France_Products")
    pyautogui.sleep(1)
    pyautogui.press("enter")
    pyautogui.sleep(2)


# pyautogui is similar to Java Robot class for automate any action(handle keyboard, mouse event).
# Describing methods of that class:-
# typewrite(string s) :
