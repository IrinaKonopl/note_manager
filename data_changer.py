# Преобразование даты в дату без года

def d_w_y(d):
    if len(d)==8:
        return d[:-3]
    else:
        return d[:-5]

dat=input('Введите дату ')
print('Дата без года',d_w_y(dat))