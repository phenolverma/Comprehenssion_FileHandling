import pickle
data1 = {'name': 'Amit', 'sal': 40000, 'dept': 'IT','designation': 'TechLead'}
outfile = open(r'sample', 'wb')
pickle.dump(data1, outfile) #csv.writer
outfile.close()

