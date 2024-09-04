let remove= ["k","@","a","@","@","@","r","@","@","i","@","m"];
let neww = remove.map(function (acc, current){
    console.log(acc,current)
    return current !=="@"? acc+current : acc;
}).join('')
console.log(neww);