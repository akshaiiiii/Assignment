const { log } = require('console')
const EventEmitter=require('events')
const emitter=new EventEmitter()
function greet(name){
    console.log(`inside the callback function: ${name}`)
}
//here the first parameter is the function name in which the event should triggerd
//the second parameter is the call back function that should be executed 
emitter.on("greet",greet)
emitter.emit('greet','akshai')
