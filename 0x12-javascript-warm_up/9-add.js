#!/usr/bin/node
const missingArgumentsMessage = "Missing arguments";
const add = (a, b) => a + b;

if (process.argv[2] && process.argv[3])
{
	const num1 = parseInt(process.argv[2]);
	const num2 = parseInt(process.argv[3]);
	if (!isNaN(num1) && !isNaN(num2))
	{
		console.log(add(num1, num2));
	}else
	{
		console.log(missingArgumentsMessage);
	}
}
else
{
  console.log(missingArgumentsMessage);
}
