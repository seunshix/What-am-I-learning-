let raceNumber = Math.floor(Math.random() * 1000);

const early = true;

const age = 17;

if (age > 18 && early === true) {
  raceNumber += 1000;
}

if (age > 18 && early) {
  console.log(
    "Your race number is " + raceNumber + ". You will race at 9:30am prompt!"
  );
} else if (age > 18 && !early) {
  console.log(
    "Your race number is " + raceNumber + ". You will race at 11:00am prompt!"
  );
} else if (age < 18) {
  console.log(
    "Your race number is " + raceNumber + ". You will race at 12:30pm prompt!"
  );
} else {
  console.log("Speak to someone at the registration desk.");
}
