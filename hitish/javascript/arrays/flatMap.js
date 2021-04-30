let a=[1,2,3,4,5,[[6]]];
function fun(i){
    return i*i;
}
let b=a.flatMap(fun);
console.log(a);
console.log(b);


