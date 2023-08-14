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
//         if (money >= 200 && money < 300){
//             discount = 3;
//         }
//         else if(money >= 300 && money < 500){
//             discount = 5;
//         }
//         else if(money >= 500){
//         discount = 7;
//         }
//     money = money - (money/100*discount);       
//     alert(`Цена со скидкой ${discount}% = ${money} рублей`);
        
// }
     

