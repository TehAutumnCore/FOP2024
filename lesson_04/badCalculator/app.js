let numbers=[]
let total = 0

let display = document.querySelector(".boxdisplay")

document.querySelector('.button1').addEventListener('click', add1)

function add1() {
  total = total + 1
  document.querySelector('.box1').innerText = total
}

/**
 * When #button1.clicked -> will push the number to an empty arraw -> number1=[]. 
 * num1 = Number(numbers1.join("")) will convert each press from string to number
 * after #buttonplus.clicked -> will push the next set of numbers to an empty array->numbers2=[]
 * num2 = Number(number2.join(""))
 * sum = num1 + num2
 */