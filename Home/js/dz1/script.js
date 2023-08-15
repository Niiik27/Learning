
let calc = document.querySelector("#calc1");
calc.addEventListener("click",calculate1);
function calculate1(){
    let num_1 = Number(document.querySelector("#num_1").value);
    let num_2 = Number(document.querySelector("#num_2").value);
    let num_3 = Number(document.querySelector("#num_3").value);
    let sum = document.querySelector("#sum");
    let mul = document.querySelector("#mul");
    sum.innerHTML= num_1+num_2+num_3;
    mul.innerHTML= num_1*num_2*num_3;
}



