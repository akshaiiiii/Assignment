const R=require("ramda");
num=[1,2,3,4,5];
console.log(num.map(x=>x*x));
console.log(num.filter(x=>x<=4));
console.log(num.reduce((acc,curr)=>acc+curr));
const double = x=>x+x;
const square = x=>x*x;
const incr= x=>x+1;
//in built pipe function
//const pipe=(...func)=>input=>func.reduce((acc,curr)=>curr(acc),input)
//pipe function using ramda library
console.log(R.pipe(double,square,incr)(4));
