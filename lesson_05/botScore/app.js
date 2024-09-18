localStorage.setItem('count', 1)
const getStr = localStorage.getItem('count')
console.log(getStr)


document.querySelector(".localStorageCount").innerText = getStr

document.querySelector("add1").addEventListener('click',plusOne())
function plusOne() {
    localStorage.setItem('count',parseInt(getStr)+1)
    getStr = localStorage.getItem('count')
    console.log(getStr)
    document.querySelector(".numCount").innerText = getStr
}

document.querySelector("sub1").addEventListener('click',subtractOne())
function subtractOne() {
    localStorage.setItem('count',parseInt(getStr)-1)
    getStr = localStorage.getItem('count')
    console.log(getStr)
    document.querySelector(".numCount").innerText = getStr
}

document.querySelector("resetCount").addEventListener('click',zero())
function zero() {
    localStorage.removeItem('count')
    getStr = 0
    console.log(getStr)
    document.querySelector(".numCount").innerText = getStr
}
document.querySelector(".numCount").innerText = getStr
// localStorage.setItem()
// localStorage.getItem()
// localStorage.removeItem()
// localStorage.clear()
