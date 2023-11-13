#!/usr/bin/node
const noArgumentsMessage = "No argument";
const notANumberMessage = "Not a number";
if (process.argv[2])
{
	const argumentAsInteger = parseInt(process.argv[2]);
	if (!isNaN(argumentAsInteger))
	{
		console.log(`My number: ${argumentAsInteger}`);
	}
	else
	{
		console.log(notANumberMessage);
	}
}
else
{
	console.log(noArgumentsMessage);
}
