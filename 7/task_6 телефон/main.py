# -*- coding: cp1251 -*-
import msvcrt
import os



def add_contackt(contackt_l):

     print("������� ��� � ������� ������ �������� (����� ������): ")
     while True:

         str_name= input().split()
         name=(str_name[0], str_name[1])
     

         if name in contackt_l:
              
              print('����� ������� ��� ���� � ���������.')
         else:
          
              phone_namber=int(input('������� ����� ��������: '))
              contackt_l[name]=phone_namber
              
         print('��� ������ ������� Esc ')
         key=msvcrt.getch()
         if key==b'\x1b':
             break
     return contackt_l
def poisk (contackt_list):
    shared_name={}
    print (contackt_list)
    f_l_name= input("������� ������� ��� ������: ").lower()
    for i in contackt_list:
        if f_l_name == i[1] or f_l_name==i[0] :
            clear()
            print(*i,'����� �������� :',contackt_list[i])
        else:
            clear()
            print('����� ������� �� ������')




contackt_list={}

while True:
        clear = lambda: os.system('cls')
        
        print('\t\t\t\t������� ����� ��������:\n\t\t\t\t',
              '1 �������� �������.\n\t\t\t\t',
              '2 ����� ��������.\n\t\t\t\t',
              '3 �����\n\t\t\t\t ')
    
        key=msvcrt.getch()
        

        if (key == b'1'):
            add_contackt(contackt_list)   
            
        if (key == b'2'):
            poisk(contackt_list)
            
               
                
        
   

