/*

hoisting é acontece automáticamente quando um programa é iniciado
o programa pega a função e escreve ela no início do programa para que 
quando for executa uma chamada àquela função, independente de onde ela for chamada
 não dar erro

*/

// add remove and ampty array
const numbers = [1,2];

numbers.push(3,4); //Add elements in the end

numbers.unshift(-1,0);//add elements in the beggining

numbers.splice(2,0, 55,10,14); //pos inicial, se quer remover algo, valores a serem inseridos


console.log(numbers);


const last = numbers.pop(); //remove do final

const firstn=numbers.shift();//remove do ínico

numbers.splice(2,2);

numbers.length=0;//truncate all values



console.log(numbers);





//getting the position of an object


console.log('O numéro na posição do index expecificado é ',numbers.indexOf(2));




//find first elements in array that mathes a condidtion

const Cursos = [
{id:1, nome : 'CC'},
{id:2, nome : 'mat'},
{id:3, nome : 'D'}
];

const curso = Cursos.find(function(callback){
    return callback.nome === 'CC';
});

console.log(curso);


const cursosss = Cursos.findIndex(function(callback){
    return callback.nome === 'CC';
});

console.log(cursosss);



//arrow functions

//mapping

//spread and rest opperator










//spread array

let a1 = [1,2,3];
let a2 = [4,5,6];
let a3 = a1.concat(a2);
console.log(a3);

let a4 = [...a1,...a2]; //spread é mais simples 

console.log(a4);



//tipo trabalho com strings mas sla

const message = 'eu gosto de comer casadas mesmo sem nunca ter tentado';
const pal = message.split(' ');
const final = pal.join('!');

console.log(final);  


 //filter an array

 const filtrado = a4.filter(function(value){
    return value<5;
 });//filtra com base na função
 
 console.log(filtrado);  




 //ex3

const num = popularArray(-10,-1);

console.log(num);


function popularArray(n,n1){
    let valor = [];
  
        for(let i = n; i<=n1;i++){
            valor.push(i);
        }
 return valor;   
}


function includes(arr,n){

    for(let ar of arr){
        if(ar === n)
        return true;
    }

 return false;   
}


console.log(includes(num,-3));


function excluir(arr,n1){
let novo =[];
    for(let ar of arr){
        if(ar!=n1)
        novo.push(ar);
    }

    return novo;
}


console.log(excluir(num,-2));



//funções que não usam parâmetros

function soma(){
    let total=0;
    for(let value of arguments){
        total +=value;
    }
    return total;
}
console.log(soma(1,2,3,4,5,6,7,8,9));




function soma2(...args){
   return args.reduce((a,b) => a+b);
    
}
console.log(soma2(1,2,3,4,5,6,7,8,9));