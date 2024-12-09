# словарь

dic={'username':'','title':'','content':'','status':'','created_date':'','issue_date':'','list_of_T':[]}
s=input('Введите имя пользователя  ')
dic['username']=s
s=input('Введите заголовок заметки  ')
dic['title']=s
s=input('Введите описание заметки  ')
dic['content']=s
s=input('Введите статус заметки  ')
dic['status']=s
s=input('Введите дату создания заметки в формате dd:mm:yy ')
dic['created_date']=s
s=input('Введите дату окончания в формате dd:mm:yy  ')
dic['issue_date']=s
t1,t2,t3=input('Введите название1  '), input('Введите название2  '),input('Введите название3  ')
t_list=[]
t_list.append(t1)
t_list.append(t2)
t_list.append(t3)
dic['list_of_T']=t_list

print(dic)