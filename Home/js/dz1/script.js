
let calc_sum_mul = document.querySelector("#calc-sum-mul");
calc_sum_mul.addEventListener("click",calculate_sum_mul);
function calculate_sum_mul(){
    let num_1 = Number(document.querySelector("#num_1").value);
    let num_2 = Number(document.querySelector("#num_2").value);
    let num_3 = Number(document.querySelector("#num_3").value);
    let sum = document.querySelector("#sum");
    let mul = document.querySelector("#mul");
    sum.innerHTML = num_1+num_2+num_3;
    mul.innerHTML = num_1*num_2*num_3;
}

let calc_money = document.querySelector("#calc-money");
calc_money.addEventListener("click",calculate_money);
function calculate_money(){
    let salary_input = Number(document.querySelector("#salary-input").value);
    let credit_input = Number(document.querySelector("#credit-input").value);
    let payment_input = Number(document.querySelector("#payment-input").value);
    let money_out = document.querySelector("#money-out");
    money_out.innerHTML = salary_input - credit_input - payment_input;
}

let calc_area = document.querySelector("#calc-area");
calc_area.addEventListener("click",calculate_area);
function calculate_area(){
    let d1_input = Number(document.querySelector("#d1-input").value);
    let d2_input = Number(document.querySelector("#d2-input").value);
    let area = d1_input*d2_input/2;
    let area_out = document.querySelector("#area-out");
    area_out.innerHTML = area;
}

let diff_strings_shekspir = document.querySelector("#diff-strings-shekspir");
diff_strings_shekspir.innerHTML="To be<br>or not<br>to be"

let diff_strings_lennon = document.querySelector("#diff-strings-lennon");
diff_strings_lennon.innerHTML=
'<pre>"Life is what happens\n\
    when\n\
        you’re busy making other plans”\n\
                                    John Lennon.</pre>'



let calc_miles = document.querySelector("#calc-miles");
let calc_inches = document.querySelector("#calc-inches");
let calc_yards = document.querySelector("#calc-yards");
let calc_feets = document.querySelector("#calc-feets");

calc_miles.addEventListener("click",function(){calculate_unit("miles")});
calc_inches.addEventListener("click",function(){calculate_unit("inches")});
calc_yards.addEventListener("click",function(){calculate_unit("yards")});
calc_feets.addEventListener("click",function(){calculate_unit("feets")});

function calculate_unit(units){
    let meters = Number(document.querySelector("#meters-input").value);
    let result_out = document.querySelector("#meters-out");
    let unit_out = document.querySelector("#unit-out");
    unit_out.innerHTML = units;
    switch(units){
        case "miles":
            result_out.innerHTML = meters/1609.344;
            break;
        case "inches":
            result_out.innerHTML = meters/2.54*100;
            break;
        case "yards":
            result_out.innerHTML = meters/0.9144;
            break;
        case "feets":
            result_out.innerHTML = meters/0.3048;
            break;
    }
     
}


let calc_max = document.querySelector("#calc-max");
let calc_min = document.querySelector("#calc-min");
let calc_aver = document.querySelector("#calc-aver");


calc_max.addEventListener("click",function(){calculate_max_min_aver("max")});
calc_min.addEventListener("click",function(){calculate_max_min_aver("min")});
calc_aver.addEventListener("click",function(){calculate_max_min_aver("average")});


function calculate_max_min_aver(action){
    let num_1 = Number(document.querySelector("#num_71").value);
    let num_2 = Number(document.querySelector("#num_72").value);
    let num_3 = Number(document.querySelector("#num_73").value);
    let max_min_aver_out = document.querySelector("#max-min-aver-out");

    switch(action){
        case "max":
            max_min_aver_out.innerHTML = `Максимальное число = ${Math.max(num_1,num_2,num_3)}`;
            break;
        case "min":
            max_min_aver_out.innerHTML = `Минимальное число = ${Math.min(num_1,num_2,num_3)}`;
            break;
        case "average":
            max_min_aver_out.innerHTML = `Среднее арифметическое = ${((num_1+num_2+num_3)/3).toFixed(2)}`;
            break;

    }
     
}




let define_status_btn = document.querySelector("#define-status-btn");
define_status_btn.addEventListener("click",define_status);
function define_status(){
    let user_age = Number(document.querySelector("#age-input").value);
    let status_out = document.querySelector("#status-out");

    switch(true){
        case 0 < user_age && user_age < 12:
            status_out.innerHTML = "ребенок";
            break;
        case 12 <= user_age && user_age < 18:
            status_out.innerHTML = "подросток";
            break;
        case 18 <= user_age && user_age  < 60:
            status_out.innerHTML = "взрослый";
            break;
        case 60 <= user_age:
            status_out.innerHTML = "пенсионер";
            break;
        default:
            alert("Вас нет")
    }   
}

let shft_digit_btn = document.querySelector("#shft-digit-btn");
shft_digit_btn.addEventListener("click",shft_digit);
function shft_digit(){
    let shift_digit_input = document.querySelector("#shift-digit-input").value;
    let shift_digit_out = document.querySelector("#shift-dig-out");

    switch (shift_digit_input){
            case "!":
                shift_digit_out.innerHTML = 1;
                break;
            case "@":
            case "\"":
                shift_digit_out.innerHTML = 2;
                break;
            case "#":
            case "№":
                shift_digit_out.innerHTML = 3;
                break;
            case "$":
            case ";":
                shift_digit_out.innerHTML = 4;
                break;
            case "%":
                shift_digit_out.innerHTML = 5;
                break;
            case "^":
            case ":":
                shift_digit_out.innerHTML = 6;
                break;
            case "&":
            case "?":
                shift_digit_out.innerHTML = 7;
                break;
            case "*":
                shift_digit_out.innerHTML = 8;
                break;
            case "(":
                shift_digit_out.innerHTML = 9;
                break;
            case ")":
                shift_digit_out.innerHTML = 0;
                break;
            default:
                alert("Не та кнопка");
                break;
            }
        
}

let digit3_btn = document.querySelector("#digit3-btn");
digit3_btn.addEventListener("click",digit3_define);
function digit3_define(){
    let digit3_input = document.querySelector("#digit3-input").value;
    let num = Number(digit3_input);
    let dig3_out = document.querySelector("#dig3-out");
    let order = digit3_input.length-1;
    let first = Math.floor(num/(10**order));
    num = num%(10**order);

    order = order-1;
    let second = Math.floor(num/(10**order));
    num = num%(10**order);

    order = order-1;
    let third = Math.floor(num/(10**order));
    num = num%(10**order);
    dig3_out.innerHTML = first == second || second == third || first == third? "Есть повторения":"Нет повторяющихся цифр";
}

let year_btn = document.querySelector("#year-btn");
year_btn.addEventListener("click",leap_year_define);
function leap_year_define(){
    let year_input = Number(document.querySelector("#year-input").value);
    let year_out = document.querySelector("#year-out");
    switch(true){
        case year_input%400==0:
            year_out.innerHTML = "Високосный";
            break;
        case year_input%100==0:
            year_out.innerHTML = "Обычный";
            break;
        case year_input%4==0:
            year_out.innerHTML = "Високосный";
            break;
        default:
            year_out.innerHTML = "Обычный";
    }  
}

let palindrome_btn = document.querySelector("#palindrome-btn");
palindrome_btn.addEventListener("click",palindrome_define);
function palindrome_define(){
    let palindrome_input = document.querySelector("#palindrome-input").value;
    let num = Number(palindrome_input);
    let palindrome_out = document.querySelector("#palindrome-out");
    let order = palindrome_input.length-1;
    let first_right = num - Math.floor(num/10)*10
    let first_left = Math.floor(num/(10**order))
    let result = "Это не плалиндром!"
    num = Math.floor(num%(10**order)/10)
    order = order-1
    if (first_right == first_left)
    {
        order = order-1
        first_right = num - Math.floor(num/10)*10
        first_left = Math.floor(num/(10**order))
        num = Math.floor(num%(10**order)/10)
        order = order-1//Теперь число теряет по 2 цифры
        if (first_right == first_left){
            order = order-1
            first_right = num - Math.floor(num/10)*10
            first_left = Math.floor(num/(10**order))
            num = Math.floor(num%(10**order)/10)
            order = order-1
            if (first_right == first_left){
                result = "Это ПАЛИНДРОМ!"}
            }
    }
    palindrome_out.innerHTML = result
}

let eur_btn = document.querySelector("#eur-btn");
let uan_btn = document.querySelector("#uan-btn");
let azn_btn = document.querySelector("#azn-btn");
let ru_btn = document.querySelector("#ru-btn");

eur_btn.addEventListener("click",function(){convert_money("eur")});
uan_btn.addEventListener("click",function(){convert_money("uan")});
azn_btn.addEventListener("click",function(){convert_money("azn")});
ru_btn.addEventListener("click",function(){convert_money("ru")});

function convert_money(units){
    let usd = Number(document.querySelector("#usd-input").value);
    let usd_out = document.querySelector("#usd-out");
    let convert_out = document.querySelector("#convert-out");
    let unit_out = document.querySelector("#ue-name-out");
    usd_out.innerHTML = usd;
    unit_out.innerHTML = units;
    switch(units){
        case "eur":
            convert_out.innerHTML = usd*0.92764;
            break;
        case "uan":
            convert_out.innerHTML = usd*7.06;
            break;
        case "azn":
            convert_out.innerHTML = usd*1.7;
            break;
        case "ru":
            convert_out.innerHTML = usd*80.17;
            break;
    }
     
}

let check_acquisition_value_btn = document.querySelector("#check-acquisition-value-btn");
check_acquisition_value_btn.addEventListener("click",check_acquisition_value);
function check_acquisition_value(){
    let money = Number(document.querySelector("#acquisition-value-input").value);
    let discount_out = document.querySelector("#discount-price-out");

    if(money < 0){
        alert(`Введите положительное число. Вы ввели ${money}`);
    }
    else{
        let discount = 0;
        switch(true) {
            case money >= 200 && money < 300:
                discount = 3;
                break;
            case money >= 300 && money < 500:
                discount = 5;
                break;
            case money >= 500:
                discount = 7;
                break;
        }
        money = money - (money/100*discount);       
        discount_out.innerHTML =`Цена со скидкой ${discount}% = ${money} рублей`;    
    }
}

let check_round_btn = document.querySelector("#check-round-btn");
check_round_btn.addEventListener("click",check_round);
function check_round(){
    let round_input = Number(document.querySelector("#round-input").value);
    let rectangle_input = Number(document.querySelector("#rectangle-input").value);
    let d = round_input/(2*3.141592) 
    let side = rectangle_input/4
    let round_out = document.querySelector("#round-out");
    round_out.innerHTML = `${d<=side?"помещается": "слишком большая!"}`

}


let answer_1_btn = document.querySelector("#answer-1-btn");
let answer_2_btn = document.querySelector("#answer-2-btn");
let answer_3_btn = document.querySelector("#answer-3-btn");
let num_question = 1

answer_1_btn.addEventListener("click",function(){check_answer(answer_1_btn.innerHTML)});
answer_2_btn.addEventListener("click",function(){check_answer(answer_2_btn.innerHTML)});
answer_3_btn.addEventListener("click",function(){check_answer(answer_3_btn.innerHTML)});

get_question()


function get_question(){
    let question_out = document.querySelector("#question-out");

    switch(num_question){
        case 1:
            question_out.innerHTML = "Сколько грамм в килограмме?"
            answer_1_btn.innerHTML = 100
            answer_2_btn.innerHTML = 1000
            answer_3_btn.innerHTML = 900
            break;
        case 2:
            question_out.innerHTML = "Спутник Земли?"
            answer_1_btn.innerHTML = "Луна"
            answer_2_btn.innerHTML = "Марс"
            answer_3_btn.innerHTML = "Юпитер"
            break;
        case 3:
            question_out.innerHTML = "Драгоценный метал?"
            answer_1_btn.innerHTML = "Медь"
            answer_2_btn.innerHTML = "Аллюминий"
            answer_3_btn.innerHTML = "Серебро"
            break;

    }

}

function check_answer(answer){

    let score_out = document.querySelector("#score-out");
    let congratulations_out = document.querySelector("#congratulations-out");
    switch(num_question){
        case 1:
            if(answer.toLowerCase()=="1000"){
                score_out.innerHTML = 2
                alert("Молодец! Вам 2 очка")
            }
            else{
                alert("Ответ неверный!")
            }
            num_question = 2
            get_question()
            break;
        case 2:
            if(answer.toLowerCase()=="луна"){
                score_out.innerHTML = Number(score_out.innerHTML)+2
                alert("Молодец! Вам еще 2 очка")    
            }
            else{
                alert("Ответ неверный!")
            }
            num_question = 3
            get_question()
            break;
        case 3:
            if(answer.toLowerCase()=="серебро"){
                score_out.innerHTML = Number(score_out.innerHTML)+2
                alert(`Молодец! Вам еще 2 очка. Итого ${score_out.innerHTML}`)
                congratulations_out.innerHTML = `Поздравляем! Вы набрали ${score_out.innerHTML}`  
            }
            else{
                alert("Ответ неверный!")
            }
            num_question = 1
            get_question()
            break;
    }  
}

let next_day_btn = document.querySelector("#next-day-btn");
next_day_btn.addEventListener("click",next_day);
function next_day(){
    let current_day_input = String(document.querySelector("#current-day-input").value);
    let date = current_day_input.split("-");
    let next_day_out = document.querySelector("#next-day-out");
    let current_year = Number(date[0]);
    let current_month = Number(date[1]);
    let current_day = Number(date[2]);
    let month_31 = ((current_month%2!=0) && current_month < 8) || ((current_month%2==0) && current_month > 7);

    if (month_31){
    if (current_month == 12){
        if (current_day>30){
            current_year+=1;
            current_month=1;
            current_day=1;}
        else{
            current_day+=1;}}
    else if (current_day>30){
        current_month+=1;
        current_day=1;}
    else{
        current_day+=1;}}
    else{
        if (current_month==2){

            if (current_year %400==0){
                leap=1;}
            else if (current_year %100==0){
                leap=0;}
            else if (current_year %4==0){
                leap=1;}
            else{
                leap=0;}

            if (current_day>27+leap){
                current_month+=1;
                current_day=1;}
            else{
                current_day++}}
        else if (current_day>29){
                current_month+=1;
                current_day=1;}
        else{
            current_day+=1}}
switch (current_month){
    case 1:
        current_month = "Январь";
        break;  
    case 2:
        current_month = "Февраль"  ; 
        break;   
    case 3:
        current_month = "Март";
        break;  
    case 4:
        current_month = "Апрель";
        break;  
    case 5:
        current_month = "Май";
        break;  
    case 6:
        current_month = "Июнь" ; 
        break;  
    case 7:
        current_month = "Июль";
        break;  
    case 8:
        current_month = "Август" ;
        break;  
    case 9:
        current_month = "Сентябрь";
        break;  
    case 10:
        current_month = "Октябрь" ; 
        break;   
    case 11:
        current_month = "Ноябрь";
        break;  
    case 12:
        current_month = "Декабрь" ;
        break;  
     } 


     next_day_out.innerHTML = `Следующий день будет: ${current_day}, ${current_month}, ${current_year} г.`;  
}

let numerator_btn = document.querySelector("#numerator-btn");
let back_numerator_btn = document.querySelector("#back-numerator-btn");

numerator_btn.addEventListener("click",function(){find_numerators(false)});
back_numerator_btn.addEventListener("click",function(){find_numerators(true)});

function find_numerators(back_order){
    let start= Number(document.querySelector("#start-div-input").value);
    let end = Number(document.querySelector("#end-div-input").value);
    let denominator = Number(document.querySelector("#denominator-input").value);
    let numerator_out = document.querySelector("#numerator-out");
    let multiple5_out = document.querySelector("#multiple5-out");
    let count5 = 0;
    let res="[";
    if(back_order){
        for (i=end;i>=start;i--){
            if (i % denominator == 0){
                    res+=`${i}, `;
                }
            if (i % 5 == 0){
                count5++;
                }
        }
        let tmp=start;
        start=end;
        end=tmp;

    }else{
        for (i=start;i<=end;i++){
            if (i % denominator == 0){
                    res+=`${i}, `;
                }
            if (i % 5 == 0){
                count5++;
                }
        }}

        if (res.length>2){
            res = res.substring(0,res.length-2);
    }
    res +="]"   
    numerator_out.innerHTML =(`Числа кратные ${denominator} в диапазоне от ${start} до ${end}: ${res}`)
    multiple5_out.innerHTML = count5
}


let fizz_buzz_btn = document.querySelector("#fizz-buzz-btn");
fizz_buzz_btn.addEventListener("click",fizz_buzz);


function fizz_buzz(){
    let start= Number(document.querySelector("#start-fizz-buzz-input").value);
    let end = Number(document.querySelector("#end-fizz-buzz-input").value);
    let fizz_buzz_out = document.querySelector("#fizz-buzz-out");
    let res="";

    for (i=start;i<=end;i++){
        if (i % 3 == 0 || i % 5 == 0){
            if (i % 3 == 0){
                    res+="Fizz";
                }
            else{
                res+="Buzz";
                }     
        }
        else{
            res+=i;
        }
        res+="\n";
    }

    fizz_buzz_out.innerHTML = `<pre>${res}</pre>`

}


let calc_diff = document.querySelector("#calc-diff");
calc_diff.addEventListener("click",calculate_diff);

function calculate_diff(){
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