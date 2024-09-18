//Initialize variables
let total = 0;

//current display 
let display = document.querySelector(".boxdisplay")

//assign eventlisteners to all buttons
const button1 = document.querySelector(".button1").addEventListener('click', one);
const button2 = document.querySelector(".button2").addEventListener('click', two);
const button3 = document.querySelector(".button3").addEventListener('click', three);
const button4 = document.querySelector(".button4").addEventListener('click', four);
const button5 = document.querySelector(".button5").addEventListener('click', five);
const button6 = document.querySelector(".button6").addEventListener('click', six);
const button7 = document.querySelector(".button7").addEventListener('click', seven);
const button8 = document.querySelector(".button8").addEventListener('click', eight);
const button9 = document.querySelector(".button9").addEventListener('click', nine);
const button0 = document.querySelector(".button0").addEventListener('click', zero);


//provide a function for all buttons
//provide a function for the equal button
//provide an update display function
// Add event listeners for operator buttons



/*
* When #button1.clicked -> will push the number to an empty arraw -> number1=[]. 
* num1 = Number(numbers1.join("")) will convert each press from string to number
* after #buttonplus.clicked -> will push the next set of numbers to an empty array->numbers2=[]
* num2 = Number(number2.join(""))
* sum = num1 + num2
*/

//document.querySelectorAll('.button1').addEventListener('click', add)

// function add() {
//   total = total + 1
//   document.querySelector('.box1').value = total
// }