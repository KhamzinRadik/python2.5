# -*- coding: cp1251 -*-

count_zakazov=int(input('������� ���������� �������: '))
print('������ ������������� �����������  �������� �����  ���������� ���������� ����� ')

dickt_zakaz=dict()


while True:
    for i in range (count_zakazov):

        print(i+1,'� �����',end='')
        str_zakaza=input(':').split()
        
    
        if str_zakaza[0] in dickt_zakaz:
           print(f'���� { str_zakaza[0]} ������������ � ������� ')
           
           
        
           if str_zakaza[1] in dickt_zakaz[str_zakaza[0]]:
               print(f'���� { str_zakaza[1]} ������������ � ������� ')
               
               dickt_zakaz[str_zakaza[0]][str_zakaza[1]]+= int(str_zakaza[2])
            


           else :
               print(f'���� { str_zakaza[1]} �������� � ������� ')
               dickt_zakaz[str_zakaza[0]][str_zakaza[1]]=int(str_zakaza[2])
        else:
            print(f'���� { str_zakaza[0]} ����������� � ������� ')
            
            dickt_zakaz[str_zakaza[0]]={str_zakaza[1]:int(str_zakaza[2])}
           

        for clients, value in dickt_zakaz.items():
            print(f'{clients}:')
            sorted_zakaz=dict(sorted(value.items()))
            for pizza, count in sorted_zakaz.items():
                print('     ',pizza , count)
       
        
       
       