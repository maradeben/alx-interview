const fetch = require('node-fetch');

// Get the movie ID from the first positional argument
const movieId = process.argv[1];

// Make a request to the Star Wars API to get the movie data
async function fetchStarWarsMovieData(movieId) {
  const response = await fetch(`https://swapi.dev/api/films/${movieId}`);
  const movieData = await response.json();
  return movieData;
}

// Print each character name on a new line
async function printStarWarsCharacterNames(movieId) {
  const movieData = await fetchStarWarsMovieData(movieId);
  const characters = movieData.characters;

  for (const character of characters) {
    console.log(character);
  }
}

// Call the printStarWarsCharacterNames function with the movie ID
printStarWarsCharacterNames(movieId);
