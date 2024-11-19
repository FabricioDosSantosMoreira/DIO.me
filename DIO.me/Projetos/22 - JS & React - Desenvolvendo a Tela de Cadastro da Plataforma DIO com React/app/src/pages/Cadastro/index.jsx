import { redirect, useNavigate  } from "react-router-dom";
import { MdEmail, MdLock, MdPerson } from 'react-icons/md';
import { Button } from '../../components/Button';
import { Header } from '../../components/Header';
import { Input } from '../../components/Input';
import { api } from '../../services/api';

import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';

import { useForm } from "react-hook-form";

import { Container, Title, Column, TitleLogin, SubtitleLogin, InfoText, GreenText, Row, Wrapper } from './styles';


const schema = yup.object({
    nome: yup.string().min(10, 'No mínimo 10 caracteres').required(),
    email: yup.string().email('E-mail inválido').required(),
    senha: yup.string().min(3, 'No mínimo 3 caracteres').required(),
}).required();


const Cadastro = () => {

    const navigate = useNavigate()

    const { control, handleSubmit, formState: { errors, isValid  } } = useForm({
        resolver: yupResolver(schema),
        reValidateMode: 'onChange',
        mode: 'onChange',
    });

    console.log(isValid, errors);

    const onSubmit = async (formData) => {
        try {
            const { data } = await api.post('/users', {
                nome: formData.nome,
                email: formData.email,
                senha: formData.senha
            });
            alert('Usuário cadastrado com sucesso!');
            navigate('/login');

        } catch (e) {
            alert("Desculpe, houve um erro ao tentar cadastrar o usuário!");
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
                <TitleLogin>Comece agora grátis</TitleLogin>
                <SubtitleLogin>Crie sua conta e make the change._</SubtitleLogin>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <Input placeholder="Nome Completo" errorMessage={errors?.nome?.message} leftIcon={<MdPerson/>} name="nome"  control={control} />
                    <Input placeholder="E-mail" errorMessage={errors?.email?.message} leftIcon={<MdEmail />} name="email"  control={control} />
                    <Input type="password" errorMessage={errors?.senha?.message} placeholder="Senha" leftIcon={<MdLock />}  name="senha" control={control} />
                    <Button title="Criar minha conta" variant="secondary" type="submit" />
                </form>
                
                <Column>
                    <InfoText>Ao clicar em "criar minha conta grátis", declaro que aceito as Políticas de Privacidade e os Termos de Uso da DIO.</InfoText>
                    <Row>
                        <InfoText><strong>Já tenho conta. </strong></InfoText>
                        <GreenText>Fazer login</GreenText>
                    </Row>
                </Column>
                </Wrapper>
            </Column>
        </Container>
    </>)
}

export { Cadastro }
