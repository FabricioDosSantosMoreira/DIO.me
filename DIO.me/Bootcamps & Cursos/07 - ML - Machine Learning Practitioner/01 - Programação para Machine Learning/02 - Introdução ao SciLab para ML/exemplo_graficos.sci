x = [-3, -2, -1, 0, 1, 2, 3];
y = [9, 4, 1, 0, 1, 4, 9];

plot(x, y);

clf
x = [0:0.1:4*%pi];
y1 = sin(x);
y2 = cos(x);

plot(x, y1, '-*b');
plot(x, y2, '-dr');

xtitle('Funções de seno e cosseno');
xlabel('Eixo X');
ylabel('Eixo Y');
legend('Seno', 'Cosseno');
