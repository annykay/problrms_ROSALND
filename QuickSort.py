
# coding: utf-8

# In[ ]:


def quick_sort(massiv):
    """ Функция быстрой сортировки. Сортирует массив по возрастанию"""
    if len(massiv)>0:
        return quick_sort([i for i in massiv if i>massiv[0]])+[i for i in massiv if i == massiv[0]]+quick_sort([i for i in massiv  if i<massiv[0]])
    else:
        return []

if __name__ == "__main__":
    print('Enter the massiv')
    tosort = [int(i) for i in input().split()]
    print(' '.join(map(str, quick_sort(tosort))))

