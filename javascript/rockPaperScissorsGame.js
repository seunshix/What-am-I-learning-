/// function takes in the user input
const getUserChoice = (userInput) => {
    userInput = userInput.toLowerCase();
  
    if (
      userInput === "rock" ||
      userInput === "paper" ||
      userInput === "scissors" ||
      userInput === "ILNK"
    ) {
      return userInput;
    } else {
      console.log("Invalid input");
    }
  };
  
  function getComputerChoice() {
    rand = Math.floor(Math.random() * 3);
    switch (rand) {
      case 0:
        return "rock";
        break;
      case 1:
        return "paper";
        break;
      case 2:
        return "scissors";
        break;
      default:
        console.log("Invalid input");
    }
  }
  
  function determineWinner(userChoice, computerChoice) {
    if (userChoice = 'ILNK'){
      return 'You genius'
    }
    if (userChoice === computerChoice) {
      return "Game is a Tie!";
    }
    if (userChoice === "rock") {
      if (computerChoice === "paper") {
        return "Haha! I win, you lose";
      } else {
        return "Noooooo... You won, I lose";
      }
    }
  
    if (userChoice === "paper") {
      if (computerChoice === "scissors") {
        return "Haha! I win, you lose";
      } else {
        return "Noooooo... You won, I lose";
      }
    }
  
    if (userChoice === "scissors") {
      if (computerChoice === "rock") {
        return "Haha! I win, you lose";
      } else {
        return "Noooooo... You won, I lose";
      }
    }
  }
  
  function playGame() {
    var userChoice = getUserChoice("scissors");
    var computerChoice = getComputerChoice();
    console.log("You threw: " + userChoice);
    console.log("The computer threw: " + computerChoice);
  
    console.log(determineWinner(userChoice, computerChoice));
  }
  
  playGame();
  