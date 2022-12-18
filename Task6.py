print('Введите Ваш номер проездного билета')
Num = int(input())
Figure1 = Num//1000
Figure2 = Num % 1000
print(Figure1, Figure2)

figure1 = Figure1 // 100
figure2 = Figure1 % 100
figure3 = figure2 // 10
figure4 = figure2 % 10
print(figure1, figure2, figure3, figure4) 
Total_figure1 = (figure1 + figure3 + figure4)
print(Total_figure1)

figure5 = Figure2 // 100
figure6 = Figure2 % 100
figure7 = figure6 // 10
figure8 = figure6 % 10
print(figure5, figure6, figure7, figure8) 
Total_figure2 = (figure5 + figure7 + figure8)
print(Total_figure2)

if (Total_figure1 == Total_figure2):
    print('Ваш билетик- счастливый!!! Ура, ура')
else:
    print('Не унывайте, повезет в следующей поездке=)')