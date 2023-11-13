#!/usr/bin/node
const noArgumentsMessage = "No argument";
const oneArgumentMessage = "Argument found";
const multipleArgumentsMessage = "Arguments found";
if (process.argv.length === 2) 
{
	console.log(noArgumentsMessage);
}
else if (process.argv.length === 3)
{
	console.log(oneArgumentMessage);
}
else
{
	console.log(multipleArgumentsMessage);
}
