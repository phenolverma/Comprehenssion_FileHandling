infile = open(r'./../Data/Capture.PNG', 'rb')
outfile = open(r'./../Data/Capture_bk.PNG', 'wb')
outfile.write((infile.read()))

