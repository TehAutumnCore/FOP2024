document.querySelector("#turnBlue").addEventListener("click", turnBlueFunction);
document.querySelector("#turnGreen").addEventListener("click", turnGreenFunction);
document.querySelector("#turnRed").addEventListener("click", turnRedFunction);
document.querySelector("#turnYellow").addEventListener("click", turnYellowFunction);
document.querySelector("#turnOrange").addEventListener("click", turnOrangeFunction);
document.querySelector("#turnRandom").addEventListener("click", turnRandomFunction);
document.querySelector("#turnwhite").addEventListener("click", turnWhiteFunction);


function turnBlueFunction() {
  document.querySelector("body").style.backgroundColor = "blue";
}

function turnGreenFunction() {
  document.querySelector("body").style.backgroundColor = "green";
}

function turnRedFunction() {
  document.querySelector("body").style.backgroundColor = "red";
}
function turnYellowFunction() {
  document.querySelector("body").style.backgroundColor = "yellow";
}
function turnOrangeFunction() {
  document.querySelector("body").style.backgroundColor = "orange";
}

// hexidecimal -> #RRGGBB ->random to grab a number between 0 and 1
function turnRandomFunction() {
  const randomColor = '#' + Math.floor(Math.random() * 0xFFFFFF).toString(16);
  document.querySelector("body").style.backgroundColor = randomColor;
}
