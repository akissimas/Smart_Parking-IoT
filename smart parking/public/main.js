const refreshRate = 1000;
const apiUrl = "/api";

const element = document.getElementById("is_parked");
const parkingId = document.getElementById("parking_id");


const getApiResponse = async () => {
    const response = await fetch(apiUrl);
    const responseAsJson = await response.json();
    const { parking_id, parked } = responseAsJson;

    parkingId.innerText = `Parking Number: ${parking_id}`;

    if(parked){
        element.innerHTML = '<img src="images/parked-car-w.svg" width="300" height="300"/>';
    }
    else{
        element.innerHTML = '<img src="images/parking-space-w.svg" width="300" height="300"/>';
    }
    
}

getApiResponse();

const updateInterval = setInterval(getApiResponse, refreshRate);