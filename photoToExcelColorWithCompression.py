import cv2
import numpy as np
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('ColorIt.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column(0, 10000, 1)
worksheet.set_default_row(9.5)

print("Drag the image here : ")
image_name = 'dead_parrot.png'#input()
img = cv2.imread(image_name,cv2.IMREAD_COLOR)
num_of_rows = img.shape[0]
num_of_cols = img.shape[1]

row=0
col=0
sheetrow = 0
sheetcol = 0
compress_factor = 1

while(row<num_of_rows-compress_factor):
    while(col<num_of_cols-compress_factor):
        count=0
        r=0
        g=0
        b=0
        while(count<compress_factor):
            r = r + img[row+compress_factor,col+compress_factor][2]
            g = g + img[row+compress_factor,col+compress_factor][1]
            b = b + img[row+compress_factor,col+compress_factor][0]
            count=count+1
        r = r/compress_factor
        g = g/compress_factor
        b = b/compress_factor
        hex_color_code = '#'+str('%02x%02x%02x' % (int(r), int(g), int(b)))
        cell_format = workbook.add_format({'bg_color': hex_color_code})
        worksheet.write_blank (sheetrow, sheetcol, '', cell_format)
        sheetcol = sheetcol+1
        col=col+compress_factor
    row=row+compress_factor
    sheetrow=sheetrow+1
    sheetcol =0
    col=0
workbook.close()
