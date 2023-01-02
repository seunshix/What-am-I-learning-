const menu = {
    _meal: "",
    _price: 0,
  
    set meal(mealToCheck) {
      if (typeof mealToCheck === "string") {
        return (this._meal = mealToCheck);
      } else {
        return "Meal description must be a string";
      }
    },
    set price(priceToCheck) {
      if (typeof priceToCheck === "number") {
        return (this._price = priceToCheck);
      } else {
        return "Price of meal must be a value";
      }
    },
  
    get todaysSpecial() {
      if (this._meal && this._price) {
        return `Today's Special is ${this._meal} for ${this._price}`;
      } else {
        return "Meal or price was not set correctly!";
      }
    },
  };
  console.log(menu.todaysSpecial);


//If you want to extend your learning on this project, 
//try adding an array of meals and prices to randomly set 
//and get Today’s Special!