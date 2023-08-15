// alert("Задача 1 - найти сумму и произведение трех чисел")

// let num_1 = +prompt("Введите первое число");
// let num_2 = +prompt("Введите второе число");
// let num_3 = +prompt("Введите третье число");
// let vs = +prompt("1 - сумма всех чисел\n2 - произведение всех чисел");

// if (vs == 1){
//     alert(num_1+num_2+num_3)
// }
// else if (vs == 2){
//     alert(num_1*num_2*num_3);
// }
// else{
//     alert("Ошибка!");
// }

// alert("Задача 2 - сколько осталось денег");
// let salary = +prompt("Ваша зарплата:");
// let credit = +prompt("Выплата по кредиту:");
// let payment = +prompt("ЖКХ:");

// alert(`Итого в остатке  ${total} руб.\n`);


// alert("Задача 3 - найти площадь ромба по диагоналям");
// d1 = +prompt("Ваша зарплата:");
// d2 = +prompt("Выплата по кредиту:");
// area = d1*d2/2;
// alert(`Площадь ромба равна " ${area} " м.кв.\n`);

// alert("Задача 4 - вывод надписи на разных строках");
// d1 = +prompt("To be\nor not\nto be\n");

// alert("Задача 5 - вывод надписи на разных строках");
// d1 = +prompt('“Life is what happens\n\twhen\n\t\tyou’re busy making other plans”\n\t\t\t\t\tJohn Lennon.\n');

// alert("Задание №2 - максимум, минимум или среднее из трех чисел");
// let first = +prompt("Первое число ");
// let second = +prompt("Второе число ");
// let third = +prompt("Третье число ");
// max=Math.max(first,second,third);
// min=Math.max(first,second,third);
// aver=(first+second+third)/3;
// alert(`Максимум  ${max}\nМинимум${min}\nСреднее${aver}`);



// alert("Задание №3 - перевести метры в мили, дюймы, ярды");
// let meters = +prompt("Введите метры ");
// let convert = prompt("Введите m - для перевода в мили, i - в дюймы, y - ярды, f - в футы ")
// let result
// if (convert == 'm'){
//     result = meters/1609.344}
// else if (convert == 'i'){
//     result = meters/2.54*100}
// else if (convert == 'y'){
//     result = meters/0.9144}
// else if (convert == 'f'){
//     result = meters/0.3048}
// else{
//     alert("Ошибка в выборе единицы измерения")
// }
// alert(`Результат ${result}`)






// alert("Упражнение №1 - определить статус по возрасту");
// let user_age = +prompt("Сколько вам лет? ")
// if (0 < user_age && user_age < 12){
//     alert("Вы ребенок")}
// else if (12 <= user_age && user_age < 18){
//     alert("Вы подросток")}
// else if (18 <= user_age && user_age  < 60){
//     alert("Вы взрослый")}
// else if (60 <= user_age){
//     alert("Вы пенсионер")}
// else{
//     alert("Вас нет")}


// alert("Упражнение №2 - вывести символ shif+цифра")
// pressed_key = prompt("Нажмити цифру на клавиатуре ");
// switch (pressed_key){
//     case "!":
//         alert("1");
//         break;
//     case "@":
//     case "\"":
//         alert("2");
//         break;
//     case "#":
//     case "№":
//         alert("3");
//         break;
//     case "$":
//     case ";":
//         alert("4");
//         break;
//     case "%":
//         alert("5");
//         break;
//     case "^":
//     case ":":
//         alert("6");
//         break;
//     case "&":
//     case "?":
//         alert("7");
//         break;
//     case "*":
//         alert("8");
//         break;
//     case "(":
//         alert("9");
//         break;
//     case ")":
//         alert("0");
//         break;
//     default:
//         alert("Не та кнопка");
//         break;
//     }


// alert("Упражнение №3 - проверить - есть ли в трехзначном числе одинаковые цифры");

// let input_string = prompt("Введите трехзначное число ");
// let num = Number(input_string);


// let order = input_string.length-1
// let first = Math.floor(num/(10**order));
// num = num%(10**order)

// order = order-1
// let second = Math.floor(num/(10**order));
// num = num%(10**order)

// order = order-1
// let third = Math.floor(num/(10**order));
// num = num%(10**order)

// let result =  first!=second && second !=third && first!=third? "Нет повторяющихся цифр": "Есть повторения"

// alert(result)


// alert("Упражнение №4 - определить - является ли год високосным")
// let year = Number(prompt("Введите год "))
// if (year%400==0){
//     alert("Високосный")
// }
// else if (year%100==0){
//     alert("Обычный")
// }
// else if (year%4==0){
//     alert("Високосный")
// }
// else{
//     alert("Обычный")
// }

// alert("Упражнение №5 - проверить число на палиндром")
// let input_string = prompt("Введите пятизначное число ")
// let num = Number(input_string)
// let result = "Это не плалиндром!"

// let order = input_string.length-1
// let first_right = num - Math.floor(num/10)*10


// let first_left = Math.floor(num/(10**order))
// num = Math.floor(num%(10**order)/10)
// order = order-1

// if (first_right == first_left)
// {
//     order = order-1
//     first_right = num - Math.floor(num/10)*10
//     first_left = Math.floor(num/(10**order))
//     num = Math.floor(num%(10**order)/10)
//     order = order-1//Теперь число теряет по 2 цифры
//     if (first_right == first_left){
//         order = order-1
//         first_right = num - Math.floor(num/10)*10
//         first_left = Math.floor(num/(10**order))
//         num = Math.floor(num%(10**order)/10)
//         order = order-1
//         if (first_right == first_left){
//             result = "Это ПАЛИНДРОМ!"}
//         else{
//             result = "Это не плалиндром!"}
//         }
//     else{
//         result = "Это не плалиндром!"
//     }
// }
// alert(result)


// alert("Упражнение №6 - Сконвертировать доллар в другую валюту")
// let usd = +prompt("Введите сумму в долларах ")
// let money = prompt("Во что конвертировать - EUR, UAN, AZN, RU(По умолчанию)? ")
// let result =  0.0
// switch (money.toLowerCase())
// {   case "":
//         money= "ru"
//     case "ru":
//         result =  usd*80.17;
//         break;
//     case "eur":
//         result =  usd*0.92764;
//         break;
//     case "uan":
//         result =  usd*7.06;
//         break;
//     case "azn":
//         result =  usd*1.7;
//         break;
//     default:
//         alert(`В ${money} не конвертирую`);
//         result =  usd;
//         money = "USD";
//         }
// alert(`${usd} USD = ${result} ${money.toUpperCase()}`)


// alert("Упражнение №7 - Сделать скидку")
// let money = +prompt("Введите сумму покупки ");
// if(money < 0){
//     alert(`Введите положительное число. Вы ввели ${money}`);
// }
// else{
//     let discount = 0;
//     switch(true) {
//         case money >= 200 && money < 300:
//             discount = 3;
//             break;
//         case money >= 300 && money < 500:
//             discount = 5;
//             break;
//         case money >= 500:
//             discount = 7
//             break;
//     }
//     money = money - (money/100*discount);       
//     alert(`Цена со скидкой ${discount}% = ${money} рублей`);    
// }
     
// alert("Упражнение №8 - Узнать впишется ли окружность в квадрат ")
// let ring_len = +prompt("Введите длину окружности ")
// let perimeter = +prompt("Введите периметр квадрата ")
// let d = ring_len/(2*3.141592) 
// let side = perimeter/4
// alert(`Окружность ${d<=side?"помещается": "слишком большая!"}`)



// alert("Упражнение №9 - Спросить пользователя и наградить за верный ответ ")
// let q_1 = +prompt("Сколько грамм в килограмме - 100, 1000, 900? ")

// let score = 0
// let nxt=' '
// if (q_1=="1000"){
//     score+=2
//     alert("Молодец! Вам 2 очка")
//     nxt=' еще '}
// else{
//     alert("Ответ неверный!")
//     alert(`У вас ${score} очк.`)}



// let q_2 = prompt("Спутник Земли - Луна, Марс, Юпитер? ")
// if (q_2=="Луна" || q_2=="луна"){
//     score+=2
//     alert(`Молодец! Вам${nxt}2 очка`)
//     nxt=' еще '}
// else{
// alert("Ответ неверный!")
// alert(`У вас ${score} очк.`)}


// let q_3 = input("Драгоценный метал - Медь, Аллюминий, Серебро? ")
// if (q_3=="Серебро" || q_3=="серебро") {
//     score+=2
//     alert(`Молодец! Вам${nxt}2 очка`)
// }
// else{
// alert("Ответ неверный!")}

// alert(`Вы набрали ${score} очк.`)

alert("Упражнение №10 - Показать следующий день ")
let current_day = +prompt("Введите день ")
let current_month = +prompt("Введите месяц ")
if (current_month > 12){
    current_month=12    }

switch (current_month){
    case "январь":
        current_month = 1
        break;
    case "февраль":
        current_month = 2 
        break;   
    case "март":
        current_month = 3
        break;
    case "апрель":
        current_month = 4
        break;
    case "май":
        current_month = 5
        break;
    case "июнь":
        current_month = 6  
        break;  
    case "июль":
        current_month = 7
        break;
    case "август":
        current_month = 8 
        break;
    case "сентябрь":
        current_month = 9
        break;
    case "октябрь":
        current_month = 10  
        break;  
    case "ноябрь":
        current_month = 11
        break;
    case "декабрь":
        current_month = 12  
        break; 

      }
        
let current_yaer = +prompt("Введите год ")

let month_31 = ((current_month%2!=0) && current_month < 8) || ((current_month%2==0) && current_month > 7)


if (month_31){
    if (current_month == 12){
        if (current_day>30){
            current_yaer+=1
            current_month=1
            current_day=1}
        else{
            current_day+=1}}
    else if (current_day>30){
        current_month+=1
        current_day=1}
    else{
        current_day+=1}}
else{
    if (current_month==2){

        if (current_yaer %400==0){
            leap=1}
        else if (current_yaer %100==0){
            leap=0}
        else if (current_yaer %4==0){
            leap=1}
        else{
            leap=0}

        if (current_day>27+leap){
            current_month+=1
            current_day=1}
        else{
            current_day++}}
    else if (current_day>29){
            current_month+=1
            current_day=1}
    else{
        current_day+=1}}




switch (current_month){
    case 1:
        current_month = "Январь"
        break;  
    case 2:
        current_month = "Февраль"   
        break;   
    case 3:
        current_month = "Март"
        break;  
    case 4:
        current_month = "Апрель"
        break;  
    case 5:
        current_month = "Май"
        break;  
    case 6:
        current_month = "Июнь"  
        break;  
    case 7:
        current_month = "Июль"
        break;  
    case 8:
        current_month = "Август" 
        break;  
    case 9:
        current_month = "Сентябрь"
        break;  
    case 10:
        current_month = "Октябрь"  
        break;   
    case 11:
        current_month = "Ноябрь"
        break;  
    case 12:
        current_month = "Декабрь" 
        break;  
     } 


     alert(`Следующий день будет: ${current_day}, ${current_month}, ${current_yaer} г.`)