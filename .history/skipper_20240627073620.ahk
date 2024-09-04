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
    clip := string(A_Clipboard)
    FileAppend clip, "C:\Users\kem7\Documents\GitHub\beginning\output.txt"
    all1 := pythonn . path . clip
    link := runwait, (pythonw %path%)
    sleep 1500
    buff :=FileRead("C:\Users\kem7\Documents\GitHub\beginning\output.txt")
    A_Clipboard := buff
    send "^v"
    Send('{Enter}')
}