# создание списка

username=input('Введите имя пользователя  ')
title=input('Введите заголовок заметки  ')
content=input('Введите описание заметки  ')
status=input('Введите статус заметки  ')
created_date=input('Введите дату создания заметки в формате dd:mm:yy ')
issue_date=input('Введите дату окончания в формате dd:mm:yy  ')
t1,t2,t3=input('Введите название1  '), input('Введите название2  '),input('Введите название3  ')
t_list=[]
t_list.append(t1)
t_list.append(t2)
t_list.append(t3)
print('Список названий: ',t_list)
print ("Имя пользователя ",username,"Название ", title,"Содержание ", content,"Статус", status,"Дата создания ", created_date,"Дата окончания ", issue_date)