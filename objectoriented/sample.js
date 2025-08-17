console.log("hai hello\n");
console.log(parseInt('11010',8));
5<6?console.log('hai'):console.log('hello');
const x=[1,2,3]
const conca=(arr1,arr2)=> arr1.concat(arr2)
console.log(conca([1,2,3],[4,5]));
const realnumbers=[-1,-2,-3,4,6,-56,3,5,6,7]
const squarelist=(arr)=>{
    const squareitem=arr.filter(num =>Number.isInteger(num) && num>0).map(num=>num*num)
    return squareitem
};
console.log(squarelist(realnumbers));