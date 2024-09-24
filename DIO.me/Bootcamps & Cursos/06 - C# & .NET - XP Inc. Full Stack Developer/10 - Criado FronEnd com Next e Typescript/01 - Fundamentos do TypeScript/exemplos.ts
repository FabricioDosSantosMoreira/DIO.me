// Tipagem
const nome: string = 'string';
const idade: number = 24;
const ativo: boolean = false;


// Interfaces
interface IUsuario {
    nome: string;
    idade: Number;
    ativo: boolean;
}
const usuario: IUsuario = {
    nome: 'teste',
    idade: 22,
    ativo: true
}


// Type
type IUsuarioType = {
    nome: string;
    idade?: Number;
    ativo?: boolean;
}

const usuarioType: IUsuarioType = {
    nome: 'teste',
}


// Enums
enum CARGO {
    DESENVOLVEDOR = 'desenvolvedor'
}

const usuarioEnum = {
    nome: 'teste',
    cargo: CARGO.DESENVOLVEDOR,
}