const express=require('express')
const fs=require('fs')

const app=express();


app.get('/' , (req , res)=>{
//    res.sendFile('index.html')
   fs.readFile('index.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    res.end();
   })
 
})


app.post('/' , (req , res)=>{

    fs.readFile('index.html', function(err, data) {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        res.end();
       })

})


app.listen(1234)