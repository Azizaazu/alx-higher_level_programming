#!/usr/bin/node
const noArgumentsMessage = "No argument";
if (process.argv[2])
{
	console.log(process.argv[2]);
}else
{
	console.log(noArgumentsMessage);
}
