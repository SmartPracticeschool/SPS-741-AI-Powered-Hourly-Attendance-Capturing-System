const api_url =
      "https://6oxglfodp6.execute-api.us-east-1.amazonaws.com/test_sample1/data";
// Defining async function
async function getapi(url) {

	// Storing response
        console.log(url)
	const response = await fetch(url);
        console.log(response);
	// Storing data in form of JSON
	var data = await response.json();
	console.log(data);
	data.sort(function(a, b){
    return a.Name - b.Name;
    });
	if (response) {
		hideloader();
	}
	show(data);
}
// Calling that async function
getapi(api_url);

// Function to hide the loader
function hideloader() {
	document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(data) {
	let tab =
		`<tr>
		<th>Name</th>
                <th>count</th>
		</tr>`;


    for (var i = 0; i < data.length; i++){
    var obj = data[i];
    for (var key in obj){
        var attrName = key;
        var attrValue = obj[key];
            tab += `
    	<td><center>${attrValue}</center></td>
       `;
    }
    tab += `<tr></tr>`;
}

	// Setting innerHTML as tab variable
	document.getElementById("Name").innerHTML = tab;
}