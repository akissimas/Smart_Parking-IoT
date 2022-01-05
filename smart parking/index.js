const express = require("express");
const {MongoClient} = require("mongodb");
const path = require('path');

function shutdown(client, server) 
{
	console.log('Closing Server.');
	client.close()
	server.close();
	process.exit(0);
}

async function getLastEntry(client)
{
	const result = await client.db("Demo").collection("Timestamp").find().sort({$natural: -1}).limit(1).next();
	return result;
} 

async function main() 
{
	const app = express();

	app.use('/', express.static(path.join(__dirname, 'public')));

	const server = app.listen(3000, () => 
	{
		console.log("Server is running on http://localhost:3000");
	});

	const uri = "mongodb+srv://IoT-Lab:iotlab@cluster0.tolfr.mongodb.net/Demo?retryWrites=true&w=majority";
	
	const client = new MongoClient(uri);
	
	process.on('SIGINT', () => shutdown(client, server));

	try
	{	
		await client.connect();
		app.get('/api', async (req, res) => {
			const result = await getLastEntry(client);
			res.status(200).json(result);
		});
	}
	catch (err)
	{
		console.error(err);
	}
}

main().catch(console.error);