#Requires AutoHotkey v2.0
MButton::
{
    sleep 50
    send "f"
    send "^l"
    A_Clipboard := ""
    sleep 150
    loop 5
    {
         Send "^c"
    }
    path := "C:\Users\kem7\Documents\GitHub\beginning\python\clipboard.py {path}",string(A_Clipboard)
    msgbox path
}