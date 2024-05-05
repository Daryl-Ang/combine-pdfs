import PyPDF2, os

os.chdir('C:/Users/daryl/Documents/Desktop/EE4407/Notes combined for finals/Tutorial 2 problems and solutions') # change directory (\\ or /)

# list of all files in cwd
allFiles = os.listdir() # cwd. include path if needed

# extract pdfs from list
pdfnames = []
for file in allFiles:
    if file.endswith('.pdf'):
        pdfnames.append(file)
        
print(pdfnames) # check

writer = PyPDF2.PdfWriter() # writer object (.addpage method)

for file in pdfnames:
    # open the file
    pdfFile = open(file, 'rb') # read binary mode
    # read the file
    reader = PyPDF2.PdfReader(pdfFile)

    # add all pages to the writer
    for pageNum in range(len(reader.pages)):
        page = reader.pages[pageNum]
        writer.add_page(page)


# saving the new PDF (to cwd)
outputFile = open('combined.pdf', 'wb') # specify new pdf name
writer.write(outputFile)
outputFile.close()
