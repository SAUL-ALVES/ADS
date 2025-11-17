// Estado global exposto (vaza para todo o app)


function contador() {
  let count = 0;  
  
  return {
    increment(){
    count++;
  },
  getCount() {
    return count;
   }
 };

}



const contador1 = contador();
contador1.increment();
console.log(contador1.getCount());

//R:
//Quando uma função é criada, ela captura as variáveis que estavam disponíveis no momento da criação, de acordo com onde ela está escrita no código — não quando ela é executada.

//Esse conjunto de variáveis é chamado ambiente léxico. E o closure garante que esse ambiente continua existindo mesmo depois da função externa já ter terminado de executar

