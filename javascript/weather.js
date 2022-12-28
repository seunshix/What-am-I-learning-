// kelvin temperature
const kelvin = 0;

// celcius temperature is 273 less than kelvin temperature
const celcius = kelvin - 273;

// fahrenheit temperature
let fahrenheit = celcius * (9 / 5) + 32;
fahrenheit = Math.floor(fahrenheit);
console.log(`The temperature is ${fahrenheit} in Fahrenheit`);

// newton temperature
let newton = celcius * (33 / 100);
newton = Math.floor(newton);

console.log(`The temperature is ${newton} degrees Newton.`);
