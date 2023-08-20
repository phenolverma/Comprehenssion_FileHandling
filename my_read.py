read_file = open(r'./../Data/Hello.txt', 'r')
print(read_file.read())
read_file.seek(0)
print(read_file.readline())
read_file.seek(0)
print(read_file.readlines())
read_file.seek(0)
for each in read_file:
    print(each)


