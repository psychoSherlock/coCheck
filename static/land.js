// For reversing value of date
var method = document.getElementById("place-field");
var pinField = document.getElementById("pin-field");
var districtField = document.getElementById("district-field");

function reverseDate(date) {
  // Reversing date
  var before = document.getElementById(date).value;
  return before.split("-").reverse().join("-");
}

function search() {
  // Validate inputs
  date = reverseDate("date-field");

  if (date) {
    // Checking for date presence
    if (method.value == "dis-opt") {
      // iF district
      var distr = districtField.value;

      if (is_valid_datalist_value("district-id", districtField.value)) {
        window.location = "/district/id=" + distr + "&date=" + date;
      }

      // Checking if district in input valid or not
      else {
        alert("Not a valid option");
      }
    } else if (method.value == "pin-opt") {
      var pincode = pinField.value;

      if (pincode) {
        // If pincode
        window.location = "/pincode/pin=" + pincode + "&date=" + date;
      } else {
        alert("No Pin code specified? Trying to trick my website :(");
      }
    }
  } else {
    // For no date
    alert("Please specify a date");
  }
}

function is_valid_datalist_value(idDataList, inputValue) {
  // Validate options
  var option = document.querySelector(
    "#" + idDataList + " option[value='" + inputValue + "']"
  );
  if (option != null) {
    return option.value.length > 0;
  }
  return false;
}

function getMethod() {
  if (method.value == "dis-opt") {
    pinField.style.display = "none";
    districtField.style.display = "inline";
  } else if (method.value == "pin-opt") {
    pinField.style.display = "inline";
    districtField.style.display = "none";
  }
}
