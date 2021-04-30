var i=10

function fun(){
    console.log(i);
}

var obj = {
    j : 20,
    fun : function (){
        fun()
        console.log(i,this.j,this);
    }
}

// fun()
obj.fun()