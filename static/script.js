
// For reversing value of date
function reverseDate(date){
    var before = document.getElementById(date).value;
    return before.split('-').reverse().join('-');
}


function searchDate(){
    date = reverseDate('date-field')
    console.log(date)
    if (date) {
        window.location = '/date=' + date
    }
    else{
        alert("Please specify a date")
    }
    
}