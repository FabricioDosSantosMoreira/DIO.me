import { useEffect, useState } from "react"

const AppOld = () => {
    const arr = [1, 2, 3, 4, 5, 6, ,7, 8, 9]

    return (
        // Fragment
        <> 
        <div className="App">
            <h1>Hello World!</h1>
        </div>

        <div className="App">
            {arr.map(item => {
                return (
                    <p>Item: {item}</p>
                )
            })}
        </div>
        </>
    )
}


// Componente Funcional
const App = () => {
    const [letra, setLetra] = useState("");
    const [count, setCount] = useState(0);
    const [letras, setLetras] = useState(["A", "B", "C"]);

    const handleAddLetra = () => {
        if(letra !== "") {
            setLetras([...letras, letra])
            setLetra("");
        }
    };

    useEffect(() => {
        setCount(letras.length)
        
    }, [letras]);


    return(
        <div className="App">
            <h1>Lista de Letras:</h1>
            <h2>Total de Letras: {count}</h2>

            <div>
                <input value={letra} onChange={(event) => setLetra(event.target.value)}/>
                <button onClick={handleAddLetra}>Adicionar</button>
            </div>

            <hr />
            {letras.map(letra => {
                return (
                    <p>Letra: {letra}</p>
                )
            })}
        </div>
    )
}


export default App;
