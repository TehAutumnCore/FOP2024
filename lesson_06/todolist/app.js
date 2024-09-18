//initialize variables

//---CRUD ---
//Create    createElement()

document.querySelector(".addTask").addEventListener('click',addTask)

function strikethrough(){
    if (this.style.textDecoration !=="line-through" ) {
        this.style.textDecoration = "line-through";
    } else {
        this.style.textDecoration = "none"
    }
}
// if the element isnt already strikethrough to add it, but if already striked then delete

function deleteTask(){
    if(this.style.textDecoration =="line-through") {
        this.remove()
    } else {
        this.remove()
    }
}

function addTask() {
    let userInput = document.querySelector(".userInput").value //Take the user input
    let newListTask = document.createElement('li') //create a li element for the UL element
    newListTask.innerText = userInput //assign the user input to the li element 
    newListTask.addEventListener('click',strikethrough)//
    let list = document.querySelector(".list").appendChild(newListTask) //append to ul element 
    console.log(userInput) //console log user input
}

//Remove    element.remove()   &    element.removeChild()


//Update will update a current child and strikethrough/line through it using <del></del> tags


//Delete




















// document.querySelector(".createItem").addEventListener('click',create)
//     function create(){
//         const createbutton = document.createElement("createInput")
//         const userInput = document.querySelector("input").value
//         document.querySelector("ul").innerHTML = `<li>${userInput}</li>`
//         console.log(createbutton)
//     }