const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;
const cors=require("cors");
const corsOptions ={
   origin:'*', 
   credentials:true,            //access-control-allow-credentials:true
   optionSuccessStatus:200,
}

app.use(cors(corsOptions)) // Use this after the variable declaration


app.use(express.static('public'));

app.get('/data', (req, res) => {
    res.sendFile(path.join(__dirname, 'leviathan_threat_model.json'));
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'leviathan_threat_model.html'));
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});