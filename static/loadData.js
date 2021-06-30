

//let api = fetch(distQuery); // request module

//api.then(function(resp){ // After making req
//    resp.json().then(function(text){ // After geting json
//        return text
//    })
//})

const tellMany = document.getElementById('how_many')

const table = document.querySelector("table");

function callCowinApi(url){ //function
    let api = fetch(url) // fetches data
    api.then(function(resp){
        resp.json().then(function(data){ //converts to json


            let sessionsLen = data['sessions'] //sessions
            tellMany.innerHTML = sessionsLen.length // tell how many centers are there

            for(let i = 0; i < sessionsLen.length; i++){ // for loop in js in range of sessions length

                var apiData = sessionsLen[i] // for simplicity

                let centerName = apiData['name']
                let totalCapacity = apiData['available_capacity']
                let age_limit = apiData['min_age_limit']
                let fee_type = apiData['fee_type']

                let row = table.insertRow() // Only one row is requeired
                let celId = row.insertCell().innerHTML = i
                let cellCenter = row.insertCell().innerHTML = centerName
                let cellAge = row.insertCell().innerHTML = age_limit
                let cellTotalCapacity  = row.insertCell().innerHTML = totalCapacity
                let cellFeeType = row.insertCell().innerHTML = fee_type
            }
        })
    })
}


document.onload = callCowinApi(url)