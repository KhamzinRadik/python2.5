# -*- coding: cp1251 -*-
str=input("������� �����:")

list=['�','�','�','�','�','�','�','�','�','�']

list_glasnie =[i for i in str if i in list]

print("������ ������� ����:",list_glasnie)
print("����� ������:",len(list_glasnie) )


