print('Введите Ваше число Num')
Num = int(input())
if Num !=0 and Num > 0:
    figure1 = Num//100
    figure2 = Num % 100
    figure3 = figure2 // 10
    figure4 = figure2 % 10
    print(figure1, figure2, figure3, figure4) 
    Total_figure = (figure1 + figure3 + figure4)
    print(Total_figure)
else:
    print('Ошибка ввода, введите положительное число!')