const fs = require('fs')

const fileLookup = fs.readFile('./project1/sampletext.txt', 'utf-8', (err,file) => {
	
	if(file){
	        //I only want to see part of the list of words not all.
		//I will figure out how to be more specific when calling a string.
		const words = file.slice(10,40);
		console.log(words);
		return; }
		
	else
		console.log(err);
		console.log("No File Found.")
});

//I used w3schools.com/js/js_string_methods.asp to look up all functions I could potentially use.
//I also watched "How to Read and write to text files in Javascript" youtube.com/watch?v=zMX3gqs3Y7l to get an idea of how to set up my code. 

