document.querySelector('.getPokemon').addEventListener('click', getFetch)

async function getFetch() {
    const pokemon = document.querySelector('.userInput').value.toLowerCase()
    const url = `https://pokeapi.co/api/v2/pokemon/${pokemon}`

    let data = await fetch(url)
    let pokemonInfo = await data.json()
    const pokemonName= document.querySelector(".pokemonName").innerText = pokemonInfo.species.name
    if (document.querySelector(".shinyImage").checked){
        const pokemonShiny= document.querySelector(".pokemonImage").src = pokemonInfo.sprites.front_shiny
    } else {
        const pokemonImage= document.querySelector(".pokemonImage").src = pokemonInfo.sprites.front_default
    
    }
    if (pokemonInfo.types[1]) {
        const pokemonType = document.querySelector(".pokemonType").innerText = pokemonInfo.types[0].type.name + " & "+ pokemonInfo.types[1].type.name 
    } else {
        const pokemonType = document.querySelector(".pokemonType").innerText = pokemonInfo.types[0].type.name
    }
    console.log(pokemonInfo)
    console.log(pokemonName)
    console.log(pokemonImage)
    console.log(pokemonShiny)
    console.log(pokemonType)
}


//https://pokeapi.co/docs/v2

/**
 *  let pokemon = .userInput
 *  const pokemonName= document.querySelector(".pokemonName").innerText = pokemon.species.name
 *  const pokemonImage= document.querySelector(".pokemonImage").src =
 *  const pokemonShinynName= document.querySelector(".pokemonShiny").innerText =
 *  const pokemonType= document.querySelector(".pokemonType").innerText =
 *  
 * 
 * pokemonInfo.results[6].name 
*/




