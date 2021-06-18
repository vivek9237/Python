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

A = "1,2|1,3|1,4|1,5|2,1|2,3|3,1|3,3|4,2|4,3|4,4|4,5"
B = "1,1|1,2|1,3|1,4|1,5|2,1|2,3|2,5|3,1|3,3|3,5|4,2|4,4"
C = "1,2|1,3|1,4|2,1|2,5|3,1|3,5|4,1|4,5"
D = "1,1|1,2|1,3|1,4|1,5|2,1|2,5|3,1|3,5|4,2|4,3|4,4"
E = "1,1|1,2|1,3|1,4|1,5|2,1|2,3|2,5|3,1|3,3|3,5"
F = "1,1|1,2|1,3|1,4|1,5|2,1|2,3|3,1|3,3"
G = "1,2|1,3|1,4|2,1|2,5|3,1|3,3|3,5|4,1|4,3|4,4|4,5"
H = "1,1|1,2|1,3|1,4|1,5|2,3|3,3|4,1|4,2|4,3|4,4|4,5"
I = "1,1|1,2|1,3|1,4|1,5"
J = "1,4|2,5|3,5|4,1|4,2|4,3|4,4"
K = "1,1|1,2|1,3|1,4|1,5|2,3|3,2|3,4|4,1|4,5"
L = "1,1|1,2|1,3|1,4|1,5|2,5|3,5"
M = "1,1|1,2|1,3|1,4|1,5|2,2|3,3|4,2|5,1|5,2|5,3|5,4|5,5"
N = "1,1|1,2|1,3|1,4|1,5|2,2|3,3|4,1|4,2|4,3|4,4|4,5"
O = "1,2|1,3|1,4|2,1|2,5|3,1|3,5|4,2|4,3|4,4"
P = "1,1|1,2|1,3|1,4|1,5|2,1|2,3|3,1|3,3|4,2"
Q = "1,2|1,3|1,4|2,1|2,5|3,1|3,4|4,2|4,3|4,5"
R = "1,1|1,2|1,3|1,4|1,5|2,1|2,3|3,1|3,3|3,4|4,2|4,5"
S = "1,2|1,5|2,1|2,3|2,5|3,1|3,3|3,5|4,1|4,4"
T = "1,1|2,1|3,1|3,2|3,3|3,4|3,5|4,1|5,1"
U = "1,1|1,2|1,3|1,4|2,5|3,5|4,1|4,2|4,3|4,4"
V = "1,1|1,2|1,3|2,4|3,5|4,4|5,3|5,2|5,1"
W = "1,1|1,2|1,3|2,4|2,5|3,1|3,2|3,3|4,4|4,5|5,1|5,2|5,3"
X = "1,1|1,2|1,4|1,5|2,3|3,3|4,1|4,2|4,4|4,5"
Y = "1,1|1,2|1,3|1,5|2,3|2,5|3,3|3,5|4,1|4,2|4,3|4,4"
Z = "1,1|1,4|1,5|2,1|2,3|2,5|3,1|3,3|3,5|4,1|4,2|4,5"
space = "1,5|2,5|3,5|4,5|5,5"
text = input("Enter Text = ")
text = text.upper()
item = "0"
# Iterate over the data and write it out row by row.
for ch in text:
    coll=0
    if (ch == 'A'):
        cells = A.split("|")
        print ('a')
    if (ch == 'B'):
        cells = B.split("|")
        print ('b')
    if (ch == 'C'):
        cells = C.split("|")
        print ('c')
    if (ch == 'D'):
        cells = D.split("|")
        print ('d')
    if (ch == 'E'):
        cells = E.split("|")
        print ('e')
    if (ch == 'F'):
        cells = F.split("|")
        print ('f')
    if (ch == 'G'):
        cells = G.split("|")
        print ('g')
    if (ch == 'H'):
        cells = H.split("|")
        print ('h')
    if (ch == 'I'):
        cells = I.split("|")
        print ('i')
    if (ch == 'J'):
        cells = J.split("|")
        print ('j')
    if (ch == 'K'):
        cells = K.split("|")
        print ('k')
    if (ch == 'L'):
        cells = L.split("|")
        print ('l')
    if (ch == 'M'):
        cells = M.split("|")
        print ('m')
    if (ch == 'N'):
        cells = N.split("|")
        print ('n')
    if (ch == 'O'):
        cells = O.split("|")
        print ('o') 
    if (ch == 'P'):
        cells = P.split("|")
        print ('p')
    if (ch == 'Q'):
        cells = Q.split("|")
        print ('q')
    if (ch == 'R'):
        cells = R.split("|")
        print ('r')
    if (ch == 'S'):
        cells = S.split("|")
        print ('s')
    if (ch == 'T'):
        cells = T.split("|")
        print ('t')
    if (ch == 'U'):
        cells = U.split("|")
        print ('u')
    if (ch == 'V'):
        cells = V.split("|")
        print ('v')
    if (ch == 'W'):
        cells = W.split("|")
        print ('w')
    if (ch == 'X'):
        cells = X.split("|")
        print ('x')
    if (ch == 'Y'):
        cells = Y.split("|")
        print ('y')
    if (ch == 'Z'):
        cells = Z.split("|")
        print ('z')
    if (ch == ' '):
        cells = space.split("|")
        print (' ')
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
format1 = workbook.add_format({'bg_color': '#000000','font_color': '#000000'})
worksheet.set_column(0, 1000, 2.2)

worksheet.conditional_format('A1:ZZ10', {'type': 'cell','criteria': '>=','value': '1', 'format': format1})

workbook.close()
