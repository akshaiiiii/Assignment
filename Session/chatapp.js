const { Socket } = require('dgram')
const http= require('http')
const WebSocket=require('ws')

const clients=new Set()
const server=http.createServer()
const wss=new WebSocket.Server({server})
wss.on('connection',(ws)=>{
    console.log("connected to the server");
    clients.add(ws)
    ws.on('message',(message)=>{
        console.log("message from client",message.toString())
        clients.forEach(client=>{
            if(client!==ws && client.readyState===WebSocket.OPEN){
                client.send(`${message}`)

            }
        })

    })
    ws.on('close',()=>{
        console.log("client disconnected")
        clients.delete(ws)
    })
    ws.send("you are connected to the server")

    
})
server.listen(3000,()=>{
    console.log('Server running on ws://localhost:3000')
})


