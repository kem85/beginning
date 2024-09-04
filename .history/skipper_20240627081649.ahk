#Requires AutoHotkey v2.0
MButton::
{
    sleep 50
    send "f"
    send "^l"
    sleep 500
    loop 5
    {
        Send "^c"
    }
    path := "C:\Users\kem7\Documents\GitHub\beginning\python\clipboard.py"
    file := FileOpen("C:\Users\kem7\Documents\GitHub\beginning\output.txt", "w") 
    file.write("")

    file.close()
    clip := string(A_Clipboard)
    FileAppend clip, "C:\Users\kem7\Documents\GitHub\beginning\output.txt"
    pythonn := "C:\Users\kem7\AppData\Local\Programs\Python\Python312\python.exe"
    link := RunWait, "C:\Users\kem7\AppData\Local\Programs\Python\Python312\pythonw.exe" "C:\Users\kem7\Documents\GitHub\beginning\python\clipboard.py"
    sleep 1500
    buff :=FileRead("C:\Users\kem7\Documents\GitHub\beginning\output.txt")
    A_Clipboard := buff
    send "^v"
    Send('{Enter}')
}