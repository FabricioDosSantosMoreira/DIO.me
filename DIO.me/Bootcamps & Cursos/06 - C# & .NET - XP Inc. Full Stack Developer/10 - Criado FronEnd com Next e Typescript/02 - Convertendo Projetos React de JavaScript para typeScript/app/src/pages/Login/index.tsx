import { useNavigate  } from "react-router-dom";
import { MdEmail, MdLock } from 'react-icons/md';
import { Button } from '../../components/Button';
import { Header } from '../../components/Header';
import { Input } from '../../components/Input';
import { api } from '../../services/api';

import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';

import { useForm } from "react-hook-form";

import { Container, Title, Column, TitleLogin, SubtitleLogin, EsqueciText, CriarText, Row, Wrapper } from './styles';
import { IFormData } from "./types";


const schema = yup.object({
    email: yup.string().email('E-mail inválido').required(),
    senha: yup.string().min(3, 'No mínimo 3 caracteres').required(),
}).required();


const Login = () => {

    const navigate = useNavigate()

    const { control, handleSubmit, formState: { errors, isValid  } } = useForm<IFormData>({
        resolver: yupResolver(schema),
        reValidateMode: 'onChange',
        mode: 'onChange',
    });

    console.log(isValid, errors);

    const onSubmit = async (formData: IFormData) => {
        try{
            const {data} = await api.get(`/users?email=${formData.email}&senha=${formData.senha}`);
            if(data.length && data[0].id){
                navigate('/feed') 
                return
            }
            alert('Usuário ou senha inválido')
        }catch(e){
            alert("Desculpe, Houve um erro!")
        }
    };

    console.log('errors', errors);

    return (<>
        <Header />
        <Container>
            <Column>
                <Title>
                    A plataforma para você aprender com experts, dominar as principais tecnologias
                    e entrar mais rápido nas empresas mais desejadas.
                </Title>
            </Column>

            <Column>
                <Wrapper>
                <TitleLogin>Faça seu Login</TitleLogin>
                <SubtitleLogin>Faça seu login e make the change._</SubtitleLogin>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <Input placeholder="E-mail" errorMessage={errors?.email?.message} leftIcon={<MdEmail />} name="email"  control={control} />
                    <Input type="password" errorMessage={errors?.senha?.message} placeholder="Senha" leftIcon={<MdLock />}  name="senha" control={control} />
                    <Button title="Entrar" variant="secondary" type="submit" />
                </form>
                
                <Row>
                    <EsqueciText>Esqueci minha senha</EsqueciText>
                    <CriarText>Criar Conta</CriarText>
                </Row>
                </Wrapper>
            </Column>
        </Container>
    </>)
}

export { Login }
