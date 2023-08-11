let plus1 = document.getElementById("plus");
let plus = document.querySelector("#plus");
let minus = document.querySelector("#minus");
let out = document.querySelector("#out");

console.log(plus);
console.log(minus);
console.log(out);

// let head = document.querySelector("head");
// console.log(head);

out.innerHtml = 123231;

let h1 = document.querySelector("#h1");
h1.innerHTML = "УРОК " + 5;

let title = document.querySelector("title");
h1.innerHTML = "УРОК " + 5;

let i = 0;

function plusOut(){
    i++;
    out.innerHTML=i;
}

function minusOut(){
    i--;
    out.innerHTML=i;
}


plus.addEventListener("click",plusOut);
minus.addEventListener("click",minusOut);

let num_1 = document.querySelector("#number1");
let num_2 = document.querySelector("#number2");

let calcPlus = document.querySelector("#calcPlus");
let calcMinus = document.querySelector("#calcMinus");
let calcMul = document.querySelector("#calcMul");
let calcDiv = document.querySelector("#calcDiv");

function cPlus(){
    otvet.innerHTML=Number(num_1.value)+Number(num_2.value);
    console.log(otvet.innerHTML);
    body.style.backgroundColor = "red"
}

function cMinus(){
    otvet.innerHTML=Number(num_1.value)-Number(num_2.value); 
    console.log(otvet.innerHTML);
}

function cMul(){
    otvet.innerHTML=Number(num_1.value)*Number(num_2.value);
    console.log(otvet.innerHTML);
}

function cDiv(){
    otvet.innerHTML=Number(num_1.value)/Number(num_2.value);
    console.log(otvet.innerHTML);
}


calcPlus.addEventListener("click",cPlus);
calcMinus.addEventListener("click",cMinus);
calcMul.addEventListener("click",cMul);
calcDiv.addEventListener("click",cDiv);

let otvet = document.querySelector("#otvet");


let body =document.body;


// plusOut()
// plusOut()
// minusOut()