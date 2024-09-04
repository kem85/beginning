#Requires AutoHotkey v2.0
MButton::
{
    ; sleep 50
    ; send "f"
    ; send "^l"
    ; sleep 500
    ; loop 5
    ; {
    ;     Send "^c"
    ; }
    pythonn := "C:\Users\kem7\AppData\Local\Programs\Python\Python312\pythonw.exe "
    ; path := "C:\Users\kem7\Documents\GitHub\beginning\python\clipboard.py "
    ; file := FileOpen("C:\Users\kem7\Documents\GitHub\beginning\output.txt", "w") 
    ; file.write("")
    ; file.close()
    ; clip := string(A_Clipboard)
    ; FileAppend clip, "C:\Users\kem7\Documents\GitHub\beginning\output.txt"
    ; all1 := pythonn . path . clip
    ; link := runwait(all1)
    ; sleep 150
    ; buff :=FileRead("C:\Users\kem7\Documents\GitHub\beginning\output.txt")
    ; A_Clipboard := buff
    ; send "^v"
    ; Send('{Enter}')
    color := PixelGetColor(700, 408)
    while color != "0X00ACC1"
        {
            color := PixelGetColor(700, 408)
        }
    click(700,408,1)
}
