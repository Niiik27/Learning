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


alert("Упражнение №2 - вывести символ shif+цифра - подходит match/case")
pressed_key = prompt("Нажмити цифру на клавиатуре ");
switch (pressed_key){
    case "1":
        alert("!");
    case "2":
        alert("@");
    case "3":
        alert("#");
    case "4":
        alert("$");
    case "5":
        alert("%");
    case "6":
        alert("^");
    case "7":
        alert("&");
    case "8":
        alert("*");
    case "9":
        alert("(");
    case "0":
        alert("0");
    default:
        alert("Не та кнопка");
    }
