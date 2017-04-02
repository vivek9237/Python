import openpyxl, pprint
import random
wb = openpyxl.load_workbook('vivek.xlsx')
sheet = wb.get_sheet_by_name('Page 1')
countyData = {}
rn=0
vm=0
ad=0
new=0
incidentList = ""
for row in range(2, sheet.max_row + 1):
    incident = sheet['A' + str(row)].value
    assignedTo = sheet['C' + str(row)].value
    state = sheet['F' + str(row)].value
    if(assignedTo == 'Rohan Nair'):
        rn +=1
    if(assignedTo == 'Amit Dey'):
        ad +=1 
    if(assignedTo == 'Vivek Mohanty'):
        vm +=1
    if((assignedTo is None) or (assignedTo =="")):
        new +=1
        assignedTo = ""
        incidentList += ','+incident
print("Vivek = "+str(vm))
print("Rohan = "+str(rn))
print("Amit = "+str(ad))
print("New Tickets = "+str(new))
print("\n\n")
newTotal = (vm+rn+ad+new)/3
vmNew = newTotal - vm
rnNew = newTotal - rn
adNew = newTotal - ad
output = ""
unassigned =new - (vmNew + rnNew + adNew)


print ("unassigned = "+str(unassigned))
print("\n\n")
while(not(unassigned==0)):
    who = random.randint(1, 3)
    if(who==1):
        vmNew += 1
    if(who==2):
        adNew += 1
    if(who==3):
        rnNew += 1
    unassigned -= 1
print incidentList
print("\n\n")
print("Vivek new = "+str(vmNew+vm))
print("Rohan new = "+str(rnNew+rn))
print("Amit new = "+str(adNew+ad))
incidents = incidentList.split(",")
i= new
while(i>1):
    while(vmNew>0):
        output += incidents[i]+":"+"Vivek Mohanty,"
        vmNew -= 1
        i-=1
    while(rnNew>0):
        output += incidents[i]+":"+"Rohan Nair,"
        rnNew -= 1
        i-=1
    while(adNew>0):
        output += incidents[i]+":"+"Amit Dey,"
        adNew -= 1
        i-=1
print "\n\n"+output
