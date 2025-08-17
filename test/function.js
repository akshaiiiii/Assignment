//currying function
//takes one agrument at a time
function curryfunc(a){
    return function inner(b){
        return a+b
    }
}
//currying function using arrow function
const func= (a)=>{
    return (b)=>{
        return a+b
    }
}
const add=curryfunc(5)
console.log(add(4))
const x=func(5)
console.log(x(3))

//partial application 
function partial(fn, ...fixedArgs) {
  return function(...remainingArgs) {
    return fn(...fixedArgs, ...remainingArgs);
  };
}
function multiply(a,b,c){
    return a*b*c
}
const multiplyby2and3=partial(multiply,2,3)//it will fix a=2 and b=3
console.log(multiplyby2and3(5))//this will sets c=5 and calls the multiply function

