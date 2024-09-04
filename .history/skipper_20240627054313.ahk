#Requires AutoHotkey v2.0
MButton::
{
    sleep 50
    send "f"
    send "^l"
    A_Clipboard := ""
    sleep 1500
    loop 5
    {
         Send "^c"
    }
    path := "C:\Users\kem7\Documents\GitHub\beginning\python\clipboard.py "
    clip := string(A_Clipboard)
    all1 := path clip
}   msgbox path