// For reversing value of date
var method = document.getElementById("place-field");
var pinField = document.getElementById("pin-field");
var districtField = document.getElementById("district-field");


function reverseDate(date) {
  // Reversing date
  var before = document.getElementById(date).value;
  return before.split("-").reverse().join("-");
}


// For alert messages

var msgBox = document.getElementById("msg-box");
var holder = document.getElementById("msg-holder");

function warn(msg, color) {
  msgBox.style.animation = "slideIn 1s";
  msgBox.style.display = "block";
  msgBox.style.right = "0";
  msgBox.style.opacity = "1";
  holder.innerHTML = msg;
  msgBox.style.backgroundColor = "var(" + color + ")";
  clean();
}

function cleaner() {
  msgBox.style.opacity = "0";
  msgBox.style.animation = "slideOut 2s";
}

function clean() {
  setTimeout(function () {
    cleaner();
  }, 4000);
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
        warn("Please wait while the server fetch data for " + distr , '--success')
        window.location = "/district/id=" + distr + "&date=" + date;
      }

      // Checking if district in input valid or not
      else {
        warn("Not a valid option", "--danger");
      }
    } else if (method.value == "pin-opt") {
      var pincode = pinField.value;

      if (pincode) {
        // If pincode
        warn("Please wait while the server fetch data for " + pincode , '--success')
        window.location = "/pincode/pin=" + pincode + "&date=" + date;
      } else {
        warn("No Pin code specified? Trying to trick my website :(", "--warn");
      }
    }
  } else {
    // For no date
    warn("Please specify a date", "--warn");
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

function load(){
  getMethod()
  districtField.value = ""
  pinField.value=""
}


window.onload = load()