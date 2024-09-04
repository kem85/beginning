let remove= ["s","@","a","@","@","@","r","@","@@","i","@@@@@","m"];
let neww = remove.map(function (acc, current){
    return current[0] !=="@"? acc+current : acc;
}).join('')
console.log(neww);