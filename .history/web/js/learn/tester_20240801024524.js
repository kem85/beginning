let remove= ["k","@","a","@","@","@","r","@","@","i","@","m"];
let neww = remove.map(function (acc, current){
    return acc !=="@" ? acc+current : acc;
}).join('')
console.log(neww);