class student{
    constructor(name){
        this.name=name;
    }
    get name(){
        //return this.name, same problem as mentioned in set method
        return this._name;
    }
    set name(name){
        //this.name=name; don't write like this because it will call the set function again and again.
        this._name=name;
    }
}
const s=new student("akshai");
console.log(s.name);
s.name="ashin";
console.log(s.name);
