let a=Array.from('foo')
let b=[1,2,3]
let c=Array.from(b,x => {
    return x * x
})
console.log(a)
console.log(c)