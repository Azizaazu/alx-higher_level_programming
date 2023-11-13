#!/usr/bin/node
if (process.argv.length <= 2)
{
	console.log(noArgumentsMessage);
}
else
{
	const numbers = Array.from(new Set(process.argv.slice(2).map(arg => parseInt(arg))));
	const sortedNumbers = numbers.sort((a, b) => b - a);
	console.log(sortedNumbers[1] || 0);
}
