const team = {
    _players: [
      {firstName: 'Chuck', lastName: 'Bass', age: 25},
      {firstName: 'Emily', lastName: 'Paris', age: 27},
      {firstName: 'Raven', lastName: 'Brian', age: 23}
      ],
    _games: [
      {opponent: 'Chelsea', teamPoints: 27, opponentPoints: 10},
      {opponent: 'Liverpool', teamPoints: 17, opponentPoints: 5},
      {opponent: 'Barcelona', teamPoints: 47, opponentPoints: 100}
    ],
  
    get players(){
      return this._players
    },
  
    get games(){
      return this._games
    },
  
    addPlayer(newFirstName, newLastName, newAge){
      let player = {
        firstName: newFirstName,
        lastName: newLastName,
        age: newAge
      };
      this._players.push(player)
    },
  
    addGame(newOpponent, newTeamPoints, newOpponentPoints){
      let game = {
        opponent: newOpponent,
        teamPoints: newTeamPoints,
        opponentPoints: newOpponentPoints
      };
      this._games.push(game)
    }
  
  }
  
  team.addPlayer('Bugs', 'Bunny', 76)
  console.log(team.players)
  
  team.addGame('Titans', 100, 98)
  console.log(team.games)