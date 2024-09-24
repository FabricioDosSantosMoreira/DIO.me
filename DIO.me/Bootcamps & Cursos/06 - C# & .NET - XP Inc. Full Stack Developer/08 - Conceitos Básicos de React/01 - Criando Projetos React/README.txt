
npm init -y

-D especifica uma dependencia de desenvolvimento
npm add @babel/core @babel/preset-env @babel/preset-react babel-loader -D

Criar o .babelrc

npm add html-loader html-webpack-plugin webpack webpack-cli webpack-dev-server style-loader css-loader file-loader -D

Criar o webpack.config.js

npm add react react-dom -D

npm start

// Configurando o ESLint
npm install eslint -D
npm init @eslint/config

ir até o eslint.config.mjs e mudar rules["react-in-jsx-scope"],


// Adicionando o Prettier
npm add eslint-config-prettier eslint-plugin-prettier prettier -D
eslintPluginPrettier.configs.recommended,


// Adicionando o Editor Config
.editorconfig 