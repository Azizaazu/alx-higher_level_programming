#!/usr/bin/node
const notANumberMessage = "Missing number of occurrences";
const linesToPrint = "C is fun";
if (process.argv[2])
{
	const numOccurrences = parseInt(process.argv[2]);
	if (!isNaN(numOccurrences))
	{
		for (let i = 0; i < numOccurrences; i++)
		{
			console.log(linesToPrint);
		}
	}
	else {
		console.log(notANumberMessage);
	}
}
else
{
	console.log(notANumberMessage);
}
