let name = 'puta';
let name2, name3 = 'puta';
const pi = 3.1415;


//objects

let person = {
    name: 'mamaco',
    age: 11
};
//dot notation
person.name = 'aranha';


//bracket notation
let selector = 'name';

person[selector] = 'mamawebo';


//arrays  ele aloca dinâmicamente os valores e caso aloquemos valores não sequenciais, os valores intermédios ficam a null

let colors = ['red', 'blue'];

colors[5] = 'amarelo'


//functions

function hello() {
    console.log('vai tomar no suco de caju, água minera, ula ula é 1 real');
}


function concatena(nome, sobrenome, fraseOfensiva) {
    console.log('o ' + nome + ' ' + sobrenome + ' é ' + fraseOfensiva);
}


function quadrado(numero) {
    return numero * numero;
}

//hello();
//concatena('marcelo','crivela','um arrombadinho de merda');
//console.log(quadrado(4));




//operators
let numero = 10;
console.log(++numero); //incrementa antes
console.log(numero++); //incrementa depois
console.log(numero);



//ternary

let points = 100;
let type = points > 100 ? 'gold' : 'silver';
console.log(type);


//if else

if (points < 100) {
    console.log('menor');

} else if (points > 100) {
    console.log('maior');
} else {
    console.log('igual');
}

//switch case
let coisa='o ' ;

switch (coisa) {
    case 'o coisa':
        console.log('o coisa');
        break;

    case 'a coisa':
        console.log('a coisa');
        break;


    default:
        console.log('coisa sem gênero');
        break;
}

//for

for(let i = 0; i<10;i++){
console.log(i);
}


//while
let i=0;
while(i<50){
    //console.log('dentro do loop' + i);
    i++;
}


do{
    console.log('dentro do loop' + i);
    i--;
}
while(i!=0);




//for in: iterar sobre propriedades de uma lista!!!!!!!!!!!!!!!!!

for(let pessoa in person){
    console.log(pessoa,person[pessoa]);
}

//for of: iterar sobre elementos de uma lista!!!!!!!!!!!!
let letras = ['a','b','b','d']
for(let letra of letras){
    console.log(letra);
}

















function max(numero1, numero2){
    if(numero1>numero2)
    console.log(numero1 ,' é o maior');
    else
    console.log(numero2,' é o maior');
}


max(5,10);



function fizzbuzz(argumento){
    if(typeof(argumento) != 'number')
    return 'valor inválido'
    else{
        if(argumento % 3== 0 && argumento % 5== 0 ){
            return 'fizz buzz';
        }
        else if(argumento % 3 == 0){
            return 'fizz';
        }
        else if(argumento % 5 == 0){
            return 'buzz';
        }else{
            return argumento
        }

    }
}



// for(i=0;i>-1;i++){
//     const out = fizzbuzz(i);
//     console.log(out);
// }



function showProps(objects){
    for(let obj in objects){
        console.log(obj,objects[obj]);
    }

}

showProps(person);



//object oriented trash 

function Circle(radius){
    this.radius = radius;
    this.draw = function(){
        console.log('puta');
    }
}

const circle1 = new Circle(55);

console.log(circle1);



//modificando dinâmicamente um objeto
//aqui não posso dar reassign de square mas consigo adicionar dinâmicamente variáveis e funções ao objeto
const square = {
    side : 5
};

square.color = 'blue';
square.draw = function memama(){};
delete square.color;

console.log(square);


//Constructor property 

/* 
geralmente fazemos assign do tipo de variável usando  litteral, ou seja, em vez de escrever new String(), usamo '' ou "" ou até ´´ 
isso mostra que tudo é objeto em JS. as funções, as variáveis e constantes, as classes...

se executarmos batata.constructor no console do browser e executarmos circle.constructor  vamos ver que eles tem estruturas diferentes

básicamente a função create é criada belo objeto FUNCTION. caso queira se aprofundar vai estudar
*/

function createCircle(radius){
    return{
        radius,
        draw:function(){
            console.log('Draw');
        }
    }
}

const batata = createCircle(1);





//primitivos 
/*os valores das váriáveis são estáticos mas quando usamos objetos eles se tornam dinâmicos. esses são os ponteiros*/

let x = 10;
let y = x;

console.log(x,y)

x = 20; //o valor de y nºao muda pq essa merda não é um ponteiro.
console.log(x,y)


let a = {value:10}
let b = a;
console.log(a,b)

a.value = 20;
console.log(a,b);





/*esse for each (let of) só funcionaria com algo que é iteravel, e para trabalhar com 
objetos que não são iteravéis tem um hack
dessa forma conseguimos fazer a mesma coisa do IN usando o OF
*/

for(let pessoa of Object.keys(person)){
    console.log(pessoa);
}

for(let pessoa of Object.entries(person)){
    console.log(pessoa);
}

if('side' in square) console.log('yes');//verificar se existe uma parâmetro side na constante 
if('circle' in square) console.log('yes');//verificar se existe uma parâmetro circle na constante  





//clone an object : copia propriedades e métodos de um objeto

const outroObjeto = Object.assign({}, circle1)

console.log(outroObjeto);




//string litterals
const frase = ` olá ${person.name}, 
percebi que você anda com as pernas e achei TOP
o que achas de uma noite intensa de sexo e tainha ?
`


console.log(frase);





//ex2

const address ={
    street:'Rua 1',
    city:'Coimbra',
    zipCode:2220744
};


for (end in address){
    console.log(end,address[end]);
}



function Endereco(rua,cidade,cp){
    this.rua = rua;
    this.cidade = cidade;
    this.cp = cp;
}


const ende = new Endereco('rua 2', 'tainha',123123123);

console.log(ende);