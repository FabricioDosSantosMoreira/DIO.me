import React, { useState, useEffect, useMemo, useCallback } from 'react';

const App = () => {

  // useState - Usado para definir e atualizar o estado de componentes funcionais
  // Aqui, criamos um estado `count` com valor inicial de 0
  const [count, setCount] = useState(0);
  const [text, setText] = useState('');



  // useEffect - Executa código após o componente ser montado ou atualizado
  // Neste exemplo, o useEffect roda toda vez que o `count` é alterado
  useEffect(() => {
    console.log('useEffect - O count foi alterado:', count);

    // Podemos retornar uma função de "limpeza" que é chamada quando o componente é desmontado ou antes de uma nova execução do useEffect
    return () => {
      console.log('Limpeza de useEffect');
    };
  }, [count]); // O useEffect será chamado sempre que o `count` mudar



  // useMemo - Memoriza o resultado de uma função cara de cálculo até que suas dependências mudem
  // Aqui, apenas recalculamos o valor quando o `count` mudar
  const computedValue = useMemo(() => {
    console.log('Executando cálculo caro...');
    return count * 2;
  }, [count]); // Recalcula `computedValue` apenas quando `count` muda



  // useCallback - Memoriza uma função para evitar que ela seja recriada em cada renderização
  // Útil ao passar funções para componentes filhos que dependem de props ou estado
  const incrementCount = useCallback(() => {
    setCount((prevCount) => prevCount + 1);
  }, []); // `incrementCount` só será recriada se as dependências (nenhuma no caso) mudarem


  
  return (
    <div>
      <h1>React Hooks: useState, useEffect, useMemo, useCallback</h1>

      {/* Exemplo de useState */}
      <div>
        <h2>useState</h2>
        <p>Contador: {count}</p>
        <button onClick={incrementCount}>Incrementar</button>
      </div>

      {/* Exemplo de useEffect */}
      <div>
        <h2>useEffect</h2>
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Digite algo"
        />
        <p>Você digitou: {text}</p>
      </div>

      {/* Exemplo de useMemo */}
      <div>
        <h2>useMemo</h2>
        <p>Valor computado (count * 2): {computedValue}</p>
      </div>

      {/* Exemplo de useCallback */}
      <div>
        <h2>useCallback</h2>
        <p>
          Este exemplo utiliza useCallback para memorizar a função
          `incrementCount`, evitando sua recriação em cada renderização.
        </p>
      </div>
    </div>
  );
};

export { App }
