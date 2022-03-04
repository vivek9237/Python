import xlsxwriter



# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Openit.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.

# Start from the first cell. Rows and columns are zero indexed.
rowi = 0
coli = 0
col= 0
row = 0

char_dict = {
   "A":"1,2|1,3|1,4|1,5|2,1|2,3|3,1|3,3|4,2|4,3|4,4|4,5",
   "B":"1,1|1,2|1,3|1,4|1,5|2,1|2,3|2,5|3,1|3,3|3,5|4,2|4,4",
   "C":"1,2|1,3|1,4|2,1|2,5|3,1|3,5|4,1|4,5",
   "D":"1,1|1,2|1,3|1,4|1,5|2,1|2,5|3,1|3,5|4,2|4,3|4,4",
   "E":"1,1|1,2|1,3|1,4|1,5|2,1|2,3|2,5|3,1|3,3|3,5",
   "F":"1,1|1,2|1,3|1,4|1,5|2,1|2,3|3,1|3,3",
   "G":"1,2|1,3|1,4|2,1|2,5|3,1|3,3|3,5|4,1|4,3|4,4|4,5",
   "H":"1,1|1,2|1,3|1,4|1,5|2,3|3,3|4,1|4,2|4,3|4,4|4,5",
   "I":"1,1|1,2|1,3|1,4|1,5",
   "J":"1,4|2,5|3,5|4,1|4,2|4,3|4,4",
   "K":"1,1|1,2|1,3|1,4|1,5|2,3|3,2|3,4|4,1|4,5",
   "L":"1,1|1,2|1,3|1,4|1,5|2,5|3,5",
   "M":"1,1|1,2|1,3|1,4|1,5|2,2|3,3|4,2|5,1|5,2|5,3|5,4|5,5",
   "N":"1,1|1,2|1,3|1,4|1,5|2,2|3,3|4,1|4,2|4,3|4,4|4,5",
   "O":"1,2|1,3|1,4|2,1|2,5|3,1|3,5|4,2|4,3|4,4",
   "P":"1,1|1,2|1,3|1,4|1,5|2,1|2,3|3,1|3,3|4,2",
   "Q":"1,2|1,3|1,4|2,1|2,5|3,1|3,4|4,2|4,3|4,5",
   "R":"1,1|1,2|1,3|1,4|1,5|2,1|2,3|3,1|3,3|3,4|4,2|4,5",
   "S":"1,2|1,5|2,1|2,3|2,5|3,1|3,3|3,5|4,1|4,4",
   "T":"1,1|2,1|3,1|3,2|3,3|3,4|3,5|4,1|5,1",
   "U":"1,1|1,2|1,3|1,4|2,5|3,5|4,1|4,2|4,3|4,4",
   "V":"1,1|1,2|1,3|2,4|3,5|4,4|5,3|5,2|5,1",
   "W":"1,1|1,2|1,3|2,4|2,5|3,1|3,2|3,3|4,4|4,5|5,1|5,2|5,3",
   "X":"1,1|1,2|1,4|1,5|2,3|3,3|4,1|4,2|4,4|4,5",
   "Y":"1,1|1,2|1,3|1,5|2,3|2,5|3,3|3,5|4,1|4,2|4,3|4,4",
   "Z":"1,1|1,4|1,5|2,1|2,3|2,5|3,1|3,3|3,5|4,1|4,2|4,5",
   "_":"1,5|2,5|3,5|4,5|5,5",
   ".":"1,5|1,5"
}


print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

for text in contents:
    #text = input("Enter Text = ")
    text = text.upper()
    item = "0"
    # Iterate over the data and write it out row by row.
    for ch in text:
        coll=0
        if(ch == ' '):
            coli = coli+3
            continue
        elif (char_dict.get(ch) is not None):
            cells = char_dict.get(ch).split("|") 
        else:
            continue
        for cell in cells:
            code1 = cell.split(",")
            count = 0
            print (code1)
            for num in code1:
                if (count == 0):
                    col = coli + int(num)
                    #print col
                if (count == 1):
                    row = rowi + int(num)
                    #print row
                count += 1
                coll = col
            worksheet.write(row, col, item)
            print (str(row)+","+str(col))
        coli = coll+1
    # going to next line
    rowi = rowi + 7
    coli = 0
format1 = workbook.add_format({'bg_color': '#000000','font_color': '#000000'})
worksheet.set_column(0, 1000, 2.2)

worksheet.conditional_format('A1:ZZ1000', {'type': 'cell','criteria': '>=','value': '1', 'format': format1})

workbook.close()