import PyPDF2, os
import sys
#program for finding relevant pdf pages in a directory
Writer = PyPDF2.PdfFileWriter()

solutions = open('/home/max/Desktop/solutions.pdf', 'wb')
keys = []
pdfFiles = []

#make a list with PDFs of directory
for filename in os.listdir('/home/max/PastTI'):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)

#make list of keywords(commandline arguments)
for i in range(1, len(sys.argv)):
    keys.append(sys.argv[i])
match = 0
for key in keys:
    for filename in pdfFiles:
    
        target = open(filename, 'rb')
        targetReader = PyPDF2.PdfFileReader(target)
        text = None

        for x in range(targetReader.numPages):
            text = targetReader.getPage(x).extractText()
            if key in text:
                match += 1
                Writer.addPage(targetReader.getPage(x))
                #line 26
            
                for z in range(x+1, targetReader.numPages):
                    if "Aufgabe" not in targetReader.getPage(z).extractText():
                        Writer.addPage(targetReader.getPage(z))
                        
                    else:
                        Writer.addPage(targetReader.getPage(z))
                        break
                break

        if key in text:
            break
           
if match == 0:
    print("No matches found: ", match)
Writer.write(solutions)
solutions.close()


    
        
    





    
