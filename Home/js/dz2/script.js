
let calc = document.querySelector("#calc");
calc.addEventListener("click",calculate);

function calculate(){
    let a = Number(document.querySelector("#A").value);
    let b = Number(document.querySelector("#B").value);
    let c = Number(document.querySelector("#C").value);
    
    let D = document.querySelector("#D");
    let X1 = document.querySelector("#X1");
    let X2 = document.querySelector("#X2");

    let d = b**2-4*a*c
    D.innerHTML= `D = ${d}`;
    console.log(D.innerHTML);
    if (d>0){
        X1.innerHTML = `X1 = ${(-b+Math.sqrt(d))/(2*a)}`
        X2.innerHTML = `X2 = ${(-b-Math.sqrt(d))/(2*a)}`
    }
    else if (d==0){
        X1.innerHTML = `X1 = ${-b/(2*a)}`
        X2.innerHTML = 'Нет корня'
    }
    else{
        X1.innerHTML = 'Нет корня'
        X2.innerHTML = 'Нет корня'
    }
}



