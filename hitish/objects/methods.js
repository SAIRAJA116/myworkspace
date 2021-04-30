let me={
    name:"Raja",
    age:"17",
    gender:"Male",
    pNo:9989881554,
    capabileToVote : function(){
        if(this.age>18){
            return `Yes he is as he is ${this.age} years old! ${this.pNo}`;
        }else{
            return `No he is not capabil for that as he is just ${this.age} years old now!`;
        }
    },
    showDetails : function(){
        console.table(this.pNo);
    }
}

me.showDetails();
console.log(`Does he capabile to vote ?`);
console.log(me.capabileToVote());
