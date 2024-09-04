#Requires AutoHotkey v2.0
MButton::
{
    click
    send "f"
    send "^l"
    loop 5
    {
        Send "^c"
        sleep 20
    }
    pythonn := "C:\Users\kem7\AppData\Local\Programs\Python\Python312\pythonw.exe "
    path := "C:\Users\kem7\Documents\GitHub\beginning\python\clipboard.py "
    file := FileOpen("C:\Users\kem7\Documents\GitHub\beginning\output.txt", "w") 
    file.write("")
    file.close()
    clip := string(A_Clipboard)
    FileAppend clip, "C:\Users\kem7\Documents\GitHub\beginning\output.txt"
    all1 := pythonn . path . clip
    link := runwait(all1)
    sleep 80
    buff :=FileRead("C:\Users\kem7\Documents\GitHub\beginning\output.txt")
    A_Clipboard := buff
    send "^v"
    Send('{Enter}')
    loop 5
        {
        send ('{PgUp}')
        }
    color := PixelGetColor(700, 408)
    while (color != "0X00ACC1" and color!= "0X18C1DB")
        {
            color := PixelGetColor(700, 408)
        }
    click(700,408,1)
    color := PixelGetColor(100, 716)
    color2 := PixelGetColor(103,714)
    while (color2 != "0xCCCCCC")
        {
             color2 := PixelGetColor(103,714)
        }
    click(1300,718,1)
    click(700,408,0)
}
