let remove= ["k","@","a","@","@","@","r","@","@","i","@","m"];
let neww = remove.map(function (acc, current){
    return acc !=="@" ? acc : null;
}).join('')
console.log(neww);