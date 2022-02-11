//hard-coded local URL, replace once Python API is hosted
fetch("http://localhost:3000/")
    .then(response => response.json())
    //just displaying the data from the JSON object
    .then(obj => {
        console.log(obj);

        obj.data.forEach(record => {
            document.querySelector("body").innerHTML += `<strong>Name:</strong> ${record.name}<br><strong>User ID:</strong> ${record.userId}<hr>`    
        });
         
    })