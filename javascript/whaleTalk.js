const input = "turpentine and turtles";
const vowels = ["a", "e", "i", "o", "u"];
const resultArray = [];

for (let i = 0; i < input.length; i++) {
  ///console.log(`inputIndex is ${i}`)
  if (input[i] === "e" || input[i] === "u") {
    resultArray.push(input[i]);
  }
  for (let j = 0; j < vowels.length; j++) {
    ///console.log(`vowelIndex is ${j}`)
    if (input[i] === vowels[j]) {
      resultArray.push(input[i]);
    }
  }
}
const resultString = resultArray.join("");

console.log(resultString.toUpperCase());
