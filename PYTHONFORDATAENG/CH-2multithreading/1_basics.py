# import threading
from concurrent.futures import ThreadPoolExecutor

def transforming(input):

    src = input['src']
    dest = input['dest']

    print(f'copying from {src}')
    print(f'transforming data......')
    print(f'storing in {dest}')
    return f'Done {src} to {dest}'

arry = [
    {'src':'table-1','dest':'table-1'},
    {'src':'table-2','dest':'table-2'},
    {'src':'table-3','dest':'table-3'}
]

with ThreadPoolExecutor(max_workers=3) as executor:

    my_result = executor.map(transforming,arry)

print(list(my_result))