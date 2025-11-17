function getUserNameOrLoginCTA(user){
    return user.name || "<a href='/login'>Entrar</a>";
}

console.log(getUserNameOrLoginCTA({name: ""})); //exemplo com falsy

//Operador ||:
// Retorna o primeiro valor truthy encontrado. Se o primeiro for falsy, ele continua e retorna o próximo.

// Operador &&:
// Retorna o primeiro valor falsy. Se todos forem truthy, retorna o último.
