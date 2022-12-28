const getSleepHours = (day) => {
    /// Manually enter hours slept for each day and call in next function
  };
  
  const getActualSleepHours = () => 8 + 8 + 9 + 15 + 7 + 8 + 3;
    /// Using function above
    // getSleepHours("Monday") +
    //   getSleepHours("Tuesday") +
    //   getSleepHours("Wednesday") +
    //   getSleepHours("Thursday") +
    //   getSleepHours("Friday") +
    //   getSleepHours("Saturday") +
    //   getSleepHours("Sunday");
  
  const getIdealSleepHours = idealHours => idealHours * 7;
  
  const calculateSleepDebt = () => {
    var actualSleepHours = getActualSleepHours();
    var idealSleepHours = getIdealSleepHours(8);
    hoursNeeded = Math.abs(idealSleepHours - actualSleepHours);
    if (actualSleepHours === idealSleepHours) {
      console.log("You got the right amount of sleep");
    } else if (actualSleepHours > idealSleepHours) {
      console.log("You got " + hoursNeeded + " hour(s) more sleep this week.");
    } else {
      console.log("You should get " + hoursNeeded + " hour(s) more rest");
    }
  };
  
  calculateSleepDebt();
  