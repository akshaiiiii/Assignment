const nums=[1,2,3,4,5,6,7,8]
const result=nums.reduce((acc,num)=>acc+2*num,0)
console.log(result)
function pipeline(...fns){
    return function(input){
        return fns.reduce((acc,fn)=>fn(acc),input)
    }
}
function add3(input){
    return input+3
    
}
function square(input){
    return input*input
}
function multiplyby2(input){
    return input*2
}
const pipe=pipeline(add3,square,multiplyby2)
console.log(pipe(5))