document.querySelector(".getCocktail").addEventListener("click",getCocktail)

function getCocktail(){
  let drink = document.querySelector(".userInput").value
  fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita${drink}`)
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data)
      let name = data.drinks[0].strDrink //How to grab the name
      let drinkUrl = data.drinks[0].strDrinkThumb
      let drinkInstructions =data.drinks[0].strInstructions
      document.querySelector(".drinkName").innerText = name
      document.querySelector(".drinkImage").src = drinkUrl
      document.querySelector(".drinkInstructions").innerText=drinkInstructions
    })
    .catch(err => {
        console.log(`error ${err}`)
        document.querySelector(".drinkName").innerText = "Drink does not exist"
        document.querySelector(".drinkImage").src = "Drink does not exist"
        document.querySelector(".drinkInstructions").innerText="Drink does not exist"
    });
}




// document.querySelector()
// console.log(data.drinks)
// console.log(data.drinks[0])
// console.log(data.drinks[0].strDrink)
