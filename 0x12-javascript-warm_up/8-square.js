#!/usr/bin/node
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num))
	console.log('Missing size');
else
{
	for (let i = 0; i < num; i++)
	{
		let sp = '';
		for (let j = 0; j < num; j++)
			sp += 'X';
		console.log(sp);
	}
}

