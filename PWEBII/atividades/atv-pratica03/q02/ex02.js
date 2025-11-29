const dispositivo1 = { info: { bateria: { nivel: 85 } } };
const dispositivo2 = { info: null };
const dispositivo3 = { info: { bateria: { nivel: 0 } } };

function obterNivel(dispositivo) {
    const nivel = dispositivo.info?.bateria?.nivel ?? -1;
    return nivel;
  }
  
  console.log(obterNivel(dispositivo1)); 
  console.log(obterNivel(dispositivo2)); 
  console.log(obterNivel(dispositivo3)); 

//O dispositivo 2 retorna -1 por conta do valor padrão definido na função caso nivel seja null ou undefined. Já o dispositivo 3, retorna 0 por conta que é um valor válido, e que foi atribuido no objeto.  