document.querySelector('#check').addEventListener('click', checkDay)

daysOfWeek = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday",]
function checkDay() {
  // 1. Retrieve the user input from the input field
  const input = document.getElementById("day").value.toLowerCase().trim();
  
  // 2. Initialize a variable to store the corrected day
  let correctedDay = undefined;

  // 3. Use a for loop to check each day of the week
  for (let i = 0; i < daysOfWeek.length; i++) {
      let day = daysOfWeek[i].toLowerCase();
      if (day.startsWith(input)) {
          correctedDay = daysOfWeek[i]; // Store the correct day
          break; // Stop checking once a match is found
      }
  }
  // 4. If a match was found, suggest the correct day
  if (correctedDay) {
      console.log(document.getElementById("correctedDay").value = `Did you mean: ${correctedDay}?`);
  }
  // 5. If no match was found, show an error message
  else if (input.length > 0) {
      console.log(document.getElementById("correctedDay").textContent = "Invalid day of the week.");
  }
  // 6. If the input is empty, clear the output
  else {
      console.log(document.getElementById("correctedDay").textContent = "");
  }
  document.querySelector("#correctedDay").textContent = correctedDay
}