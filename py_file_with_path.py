import os

count = 0
item = os.listdir(r'C:\Users\Shree\PycharmProjects\Comprehenssion_FileHandling\First_Project\Program')

for each in item:
    if '.py' in each:
        print(os.path.abspath(item[count]))
    count += 1

