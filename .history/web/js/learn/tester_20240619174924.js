let st="Elzero Web School"
console.log(st[st.indexOf("W")].toLowerCase()==="w" ? "Good1" : "Bad");
console.log(typeof st ==="string" ? "Good2" : "Bad");
console.log(typeof st.length=="number" ? "Good3" : "Bad");
console.log(st.slice(0,6).repeat(2) =="ElzeroElzero" ? "Good4" : "Bad");
console.log((st.length*2).toString() ==="34" ? "Good5" : "Bad");