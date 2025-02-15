# -*- coding: cp1251 -*-
count_zakazov=int(input('Введите количество заказов: '))
print('заказы записываються «Покупатель  название пиццы  количество заказанных пицц» ')
dickt_zakaz=dict()

dict_pica_colichestvo=dict()

while True:
    for i in range (count_zakazov):

        print(i+1,'й заказ',end='')
        str_zakaza=input(':')
        spisok_zakaza=str_zakaza.split()
    
        if spisok_zakaza is dickt_zakaz.keys():
            print ('такого нет ')
            dickt_zakaz[dict_pica_colichestvo]
            print (dickt_zakaz)
        else:
            print ('!!!')
            dict_pica_colichestvo.append (spisok_zakaza[1])
            dict_pica_colichestvo.append(int(spisok_zakaza[2]))
            dickt_zakaz[spisok_zakaza[0]]=dict_pica_colichestvo
       
        print (dickt_zakaz)