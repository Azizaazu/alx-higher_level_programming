#!/usr/bin/node
const noArgumentsMessage = "Insufficient arguments.";
if (process.argv.length >= 4)
{
	const arg1 = process.argv[2];
	const arg2 = process.argv[3];
	console.log(`${arg1} is ${arg}`);
}
else
{
	console.log(noArgumentsMessage);
}
