
# coding: utf-8

# In[ ]:


def qsort(massiv):
    """ Функция быстрой сортировки. Сортирует массив по возрастанию"""
    if len(massiv)>0:
        return qsort([i for i in massiv if i>massiv[0]])+[i for i in massiv if i == massiv[0]]+qsort([i for i in massiv  if i<massiv[0]])
    return []

