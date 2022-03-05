import cv2
import numpy as np
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('ColorIt.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column(0, 10000, 1)
worksheet.set_default_row(9.5)

print("Drag the image here : ")
image_name = input()
img = cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)
num_of_rows = img.shape[0]
num_of_cols = img.shape[1]

row=0
col=0
while(row<num_of_rows):
    while(col<num_of_cols):
        grey_scale_intensity = img[row,col]
        hex_color_code = '#'+str('%02x%02x%02x' % (grey_scale_intensity, grey_scale_intensity, grey_scale_intensity))
        cell_format = workbook.add_format({'bg_color': hex_color_code})
        worksheet.write_blank (row, col, '', cell_format)
        col=col+1
    row=row+1
    col=0

workbook.close()
