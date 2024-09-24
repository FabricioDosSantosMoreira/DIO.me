import { Header } from '../../components/Header';
import { UserInfo } from '../../components/UserInfo';

import { Container, Column, Title, TitleHighlight } from './styles';
import { Card } from "../../components/Card";


const Feed = () => {
    return (
      <>
        <Header autenticado={true}/>
        <Container>

          <Column flex={3}>
            <Title>Feed</Title>
            <Card />
            <Card />
            <Card />
          </Column>

          <Column flex={1}>
          <TitleHighlight># RANKINGS DA SEMANA</TitleHighlight>
            <UserInfo percentual={90} nome="Fabrício" image="https://avatars.githubusercontent.com/u/138410021?v=4" />
            <UserInfo percentual={10} nome="A" image="https://avatars.githubusercontent.com/u/138410021?v=4" />
            <UserInfo percentual={30} nome="B" image="https://avatars.githubusercontent.com/u/138410021?v=4" />
            <UserInfo percentual={50} nome="C" image="https://avatars.githubusercontent.com/u/138410021?v=4" />
            <UserInfo percentual={70} nome="D" image="https://avatars.githubusercontent.com/u/138410021?v=4" />
          </Column>
        </Container>
      </>
    )
}

export { Feed }