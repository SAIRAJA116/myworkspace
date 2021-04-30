function func(name,role){
    switch (role) {
        case "admin":
            return `${name} is admin he as all the capbility to change every thing on the database`;
        case "faculty":
            return `${name} is faculty he has only capbility of pushing the things on to the database but cant manuplate them`;
        case "student":
            return `${name} is student he has only capbility of retriving from the database`;
        
    
        default: 
            return `${name} is nothing he is just playing the visitor role he willnot liked to the database in anyway.`;
            
    }
}

console.log(func("sairaja","admin"));
console.log(func("keerthi","faculty"));
console.log(func("sandeep","faculty"));
console.log(func("swamy","student"));
console.log(func("rekha","nothing"));