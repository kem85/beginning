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
    path := "pythonw C:\Users\kem7\Documents\GitHub\beginning\python\clipboard.py "
    clip := string(A_Clipboard)
    all1 := path . clip
   runwait(all1)
}