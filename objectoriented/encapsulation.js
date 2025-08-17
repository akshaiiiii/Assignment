class section {
    #balance;
    constructor(balance){
        this.#balance=balance;
    }
    get Balance(){
        return this.#balance;
    }
    set Balance(balance){
        this.#balance=balance;
    }
}
const s=new section(30);
console.log(s.Balance);
s.Balance=20;
console.log(s.Balance);
//console.log(s.#balance);
//this will cause an error because private field is accessable only within the class only;