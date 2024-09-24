import React from 'react';
import { FiThumbsUp } from 'react-icons/fi';

import { CardContainer, Content, HasInfo, ImageBackground, PostInfo, UserInfo, UserPicture } from './styles';
import feedImage from '../../assets/feed-background.jpg'

const Card = () => {
  return (
    <CardContainer>
      <ImageBackground src={feedImage} alt="Imagem do Feed" />
      <Content>
        <UserInfo>
            <UserPicture src="https://avatars.githubusercontent.com/u/138410021?v=4" /> 
            <div>
                <h4>Fabrício dos Santos Moreira</h4>
                <p>Há 10 minutos</p>
            </div>
        </UserInfo>

        <PostInfo>
          <h4>Projeto da DIO</h4>
          <p>Projeto para o curso de HTML, CSS e React. <strong>Saiba Mais</strong></p>
        </PostInfo>

        <HasInfo>
            <h4>#HTML #CSS #JavaScript #React</h4>
            <p><FiThumbsUp /> 10</p>
        </HasInfo>


      </Content>
    </CardContainer>
  )
}

export { Card }
