class autherror extends Error{
    constructor(message){
        super(message);
        this.name="authentication Error";
    }    
}
function test(num){
    try{
        if (parseInt(num)<18){
            throw new autherror("age should be greater than 18");
        }
        else{
            return "voting can be done";
        }
    }
    catch(err){
        console.log(err.name);
        console.log(err.message);

    }
    finally{
        console.log("finally i am here");
    }
}
console.log(test(12));