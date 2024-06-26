let st="Elzero Web School"
if((st.length*2).toString() ==="34")
{
        console.log("Good");
}
console.log(st[st.indexOf("W")].toLowerCase()==="w" ? "Good" : "Bad");
console.log(typeof st ==="string" ? "Good" : "Bad");
console.log(typeof st.length=="number" ? "Good" : "Bad");
console.log(st.slice(0,6).repeat(2) =="ElzeroElzero" ? "Good" : "Bad");