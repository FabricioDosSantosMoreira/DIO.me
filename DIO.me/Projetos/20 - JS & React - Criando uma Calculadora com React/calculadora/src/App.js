import Input from './components/Input'
import Button from './components/Button'

import { Container, Content, Row, Column } from './styles';
import { useState } from 'react';


const App = () => {
  const [currentNumber, setCurrentNumber] = useState('0');
  const [firstNumber, setFirstNumber] = useState('0');
  const [operation, setOperation] = useState('');


  const handleOnClear = () => {
    setCurrentNumber('0');
    setFirstNumber('0');
    setOperation('');
  };

  const handleOnRemove = () => {
    setCurrentNumber(prev => `${prev.slice(0, -1)}`)
  }
 
  const handleAppendNumber = (number) => {
    setCurrentNumber(prev => `${prev === '0' ? '' : prev}${number}`)
  }

  const handleSumNumber = () => {
    if(firstNumber === '0')  {
      setFirstNumber(String(currentNumber));
      setCurrentNumber('0');
      setOperation('+');
    } else {
      const res = Number(firstNumber) + Number(currentNumber);
      setCurrentNumber(String(res)); 
      setOperation('');
    }
  }

  const handleSubtractNumber = () => {
    if(firstNumber === '0')  {
      setFirstNumber(String(currentNumber));
      setCurrentNumber('0');
      setOperation('-');
    } else {
      const res = Number(firstNumber) - Number(currentNumber);
      setCurrentNumber(String(res)); 
      setOperation('');
    }
  }

  const handleMultiplyNumber = () => {
    if(firstNumber === '0')  {
      setFirstNumber(String(currentNumber));
      setCurrentNumber('0');
      setOperation('*');
    } else {
      const res = Number(firstNumber) * Number(currentNumber);
      setCurrentNumber(String(res)); 
      setOperation('');
    }
  }

  const handleDivideNumber = () => {
    if(firstNumber === '0')  {
      setFirstNumber(String(currentNumber));
      setCurrentNumber('0');
      setOperation('/');
    } else {
      const res = Number(firstNumber) / Number(currentNumber);
      setCurrentNumber(String(res)); 
      setOperation('');
    }
  }

  const handleModuleOfNumber = () => {
    if(firstNumber === '0')  {
      setFirstNumber(String(currentNumber));
      setCurrentNumber('0');
      setOperation('%');
    } else {
      const res = Number(firstNumber) % Number(currentNumber);
      setCurrentNumber(String(res)); 
      setOperation('');
    }
  }
  

  const HandleEquals = () => {
    if(firstNumber !== '0' && operation !== '' && currentNumber !== '0')  {
      switch (operation) {
        case '+':
          handleSumNumber();
          break;
        case '-':
          handleSubtractNumber();
          break;
        case '*':
          handleMultiplyNumber();
          break;
        case '/':
          handleDivideNumber();
          break;
        case '%':
          handleModuleOfNumber();
          break;
      
        default:
          break;
      }

      setFirstNumber('0');
    }
  }


  return (
    <Container>
      <Content>
        <Input value={currentNumber}/>
        
        <Row> 
          <Button label="C" onClick={() => handleOnClear()}/>
          <Button label="X" onClick={() => handleOnRemove()}/>
          <Button label="%" onClick={() => handleModuleOfNumber('%')}/>
          <Button label="/" onClick={() => handleDivideNumber()}/>
        </Row>
        <Row> 
          <Button label="7" onClick={() => handleAppendNumber('7')}/>
          <Button label="8" onClick={() => handleAppendNumber('8')}/>
          <Button label="9" onClick={() => handleAppendNumber('9')}/>
          <Button label="*" onClick={() => handleMultiplyNumber('*')}/>
        </Row>
        <Row> 
          <Button label="4" onClick={() => handleAppendNumber('4')}/>
          <Button label="5" onClick={() => handleAppendNumber('5')}/>
          <Button label="6" onClick={() => handleAppendNumber('6')}/>
          <Button label="-" onClick={() => handleSubtractNumber('-')}/>
        </Row>
        <Row> 
          <Button label="1" onClick={() => handleAppendNumber('1')}/>
          <Button label="2" onClick={() => handleAppendNumber('2')}/>
          <Button label="3" onClick={() => handleAppendNumber('3')}/>
          <Button label="+" onClick={() => handleSumNumber()}/>
        </Row>
        <Row> 
          <Button label="@" onClick={() => handleAppendNumber('')}/>
          <Button label="0" onClick={() => handleAppendNumber('0')}/>
          <Button label="," onClick={() => handleAppendNumber('.')}/>
          <Button label="=" onClick={() => HandleEquals()}/>
        </Row>
        
      </Content>
    </Container>
  );
}

export default App;
