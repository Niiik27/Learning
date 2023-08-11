console.log(2+2*2);
let int = 1;
let str = "1";
let bool = true || false;
let massiv = [1,2,3,4,5,6];
let obj = {
    "name" : "name",
    "age" : 22,
}
class Auto{
    constructor(name,age){
        this.name = name;
        this.age = age;
    }
    changeName(){
        console.log(this.name)
    }
}
class AutoV2 extends Auto{
    constructor(name,age){
        this.name = name;
        this.age = age;
    }
}

function sum(a,b){
    return a + b
}

let sum2 = (a,b) => {
    return a + b
}
console.log("5/0")
console.log(5/0)

let x = prompt("Введите ваше имя"); // строка
let y = +prompt("введите только число"); // число +
console.log(x,y)

let i = 0;

while(i < 10){
    i++;
    console.log(i)
}

for(let i = 0; i < 10; i++){
    console.log(i)
}

let z = 1;
let k = 2;

if(z < k){
    console.log("z < k")
}
else if(k < z){
    console.log("k < z")
}
else if(k == z){
    console.log("k = z")
}
else{
    console.log("ошибка")
}

let hi = "hisdasdsadsad"
console.log(`${hi} adsdsaas`)
console.log(hi + " adsdsaas")