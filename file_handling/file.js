const fs=require('fs')
fs.readFile('./input.txt','utf8',(err,data)=>{
    console.log(data)
})
fs.writeFile('./input.txt',"this is the added text",(err)=>{
    console.log("success")
fs.appendFile('./input.txt','\nutf8',(err,data)=>{
    console.log("append successfully")
})
})
