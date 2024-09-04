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
    clii := string(A_Clipboard)
     fff := runwait("C:\Usfts\GitHub\beginning\python\clipboard.py" . clii . "" )
}