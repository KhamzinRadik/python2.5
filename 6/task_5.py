# -*- coding: cp1251 -*-





slovar_sininimov=dict()


count=int(input('������� ���������� ��� ����:'))

    

for i in range (count):
    while True:
        print(i+1,' ������� �����: ')
        str=input()
        str=''.join(str.split())
        str=str.lower()
        if '-' in str:           
            str_1=(str.split('-'))            
            slovar_sininimov[str_1[0]]=str_1[1]
            break
        else :
            print('�� ���������� ������ ����� ����������� ����������� "-" ����� ������� ����������')
while True:
    str_poisk_sinonima=input("������� ����� : ")
    str_poisk_sinonima=str_poisk_sinonima.lower()

    if str_poisk_sinonima == '�����':
        break

    if str_poisk_sinonima in slovar_sininimov.values():
      inv_dictionary = {v: k for k, v in slovar_sininimov.items()}
      print('�������:',inv_dictionary.get(str_poisk_sinonima))

    if str_poisk_sinonima in slovar_sininimov.keys():
      print('�������:',slovar_sininimov.get(str_poisk_sinonima))
    else:
        print('������ ����� � ������� ���.')

    print('��� ������ ����� "�����"')
    


