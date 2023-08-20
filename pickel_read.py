import pickle
infile = open('sample', 'rb')
content = pickle.load(infile) #csvObj=csv.reader(infile)
print(content)
print(content['dept'])

