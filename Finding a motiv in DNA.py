
# coding: utf-8

# In[ ]:


def z_funct(s:str):
    """Вычисляет префикс-функцию строки(она же z-функция): для каждого i-го значения строки вычисляет максимальную длину
       собственного суффикса, начинающегося с i элемента, совпадающего с ее префиксом
       :param s:str - строка для которой вычисляется z-функция
       :result zf: list - список значений z-функции для каждого i-го элемента строки s
       """
    n = len(s)
    zf = [0]*n#заполняем нулями
    left = 0 #храним левую и правую границы отрезка, вначале - 0
    right = 0
    for i in range(1,n):#выполняем цикл n-1 раз 
        zf[i] = max(0, min(right-i, zf[i - left]))
        while i + zf[i] < n and s[zf[i]]== s[i + zf[i]]:
            zf[i]+=1
        if i + zf[i] > right:
            left = i
            right = i + zf[i]
    return zf

def FindSubString(Text, Pattern):
    """Функция ищет все вхождеия подстроки в строку, если таких нет - возвращает -1(нумерация с нуля)
       :param Text: str - строка, в которой будем искать подстроку
       :param Pattern: str - подстрока
       :result positions: list - список позиций вхождения подстроки в строку, если нет вхождений функция возвращает [-1]
       """
    positions = []
    UnitString = Pattern + '#' +  Text 
    zf = z_funct(UnitString)
    n = len(Pattern)
    fl = False
    for i in range(len(Pattern)+1, len(UnitString)):
        if  zf[i] == len(Pattern):
            positions.append(i-len(Pattern)-1)
            fl = True
    if fl == False:
        return [-1]
    else:
        return positions

