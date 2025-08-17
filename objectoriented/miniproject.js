class user{
    constructor(name){
        if (new.target==user){
            throw new error("it is not possible\n");
        }
        this.name=name;
    }
    edit() {
        return false;  
    }
    view(){
        return false;
    }
    delete(){
        return false;
    }
}
class admin extends user{
    constructor(name){
        super(name)
    }
    edit(){
        return true;
    }
     view(){
        return true;
    }
    delete(){
        return true;
    }
}
class editor extends user{
     constructor(name){
        super(name)
    }
    edit(){
        return true;
    }
}
class viewer extends user{
    constructor(name){
        super(name)
    }
}
x=new viewer("akshai");
y=new editor("ashin");
z=new admin("gigi");
console.log(x.name);
console.log(x.edit());
console.log(x.view());
console.log(x.delete());
console.log("_".repeat(30));
console.log(y.name);
console.log(y.edit());
console.log(y.view());
console.log(y.delete());
console.log("_".repeat(30));
console.log(z.name);
console.log(z.edit());
console.log(z.view());
console.log(z.delete());
c=new user("chahchacha");


