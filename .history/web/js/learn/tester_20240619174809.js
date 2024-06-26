let st="Elzero Web School"
if((st.length*2).toString() ==="34")
{
        console.log("Good");
}
console.log(st[st.indexOf("W")].toLowerCase()==="w" ? "Good" : "Bad");
if(typeof st ==="string")
    {
        console.log("Good");
    }
if(typeof st.length=="number" )
    {
        console.log("Good");
    }
if(st.slice(0,6).repeat(2) =="ElzeroElzero")
    {
        console.log("Good");
    }