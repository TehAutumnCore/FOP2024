document.querySelector('.addTask').addEventListener('click',addTask)

function updateList(){
    if (this.style.textDecoration ==="line-through" ) {
        this.style.textDecoration = "none";
    } else {
        this.style.textDecoration = "line-through";
    }
}

function deleteTask(){
    let parent = this.parentNode;
    parent.remove()
}

function addTask(){
    let newTask = document.querySelector(".userInput").value
    
    let newListItem = document.createElement("li")
    let deleteButton = document.createElement('button')

    newListItem.innerText = newTask
    deleteButton.innerHTML = `Delete`

    newListItem.addEventListener('click',updateList)
    deleteButton.addEventListener('click',deleteTask)

    newListItem.appendChild(deleteButton)
    document.querySelector('.list').appendChild(newListItem)
}

