const fs=require('fs').promises

async function read(){
    const data=await fs.readFile('./input.txt','utf8')
    console.log(data)
    await fs.appendFile('./input.txt','\nthis is the file appended')

};
read()

