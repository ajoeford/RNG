import xlsxwriter
import random

#initiate excel workbook
workbook = xlsxwriter.Workbook('random02.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

##
###random sample parameters
##

#establish number of ranges
numRanges = input('Number of Ranges: ')
rangeList = []

if numRanges > 10:
    print 'fukoff mate.'
else:
    for i in range(numRanges):
        rangeList.append([input('Beginning Range ' + str(i+1) +': '), input('Ending Range ' + str(i+1) +': ')])

#make big list of population
popList = []
for k in rangeList:
    for n in range(k[0],k[1]+1):
        popList.append(n)

#establish sample parameters
sampleSize = input('Sample Size: ')
extraSelections = input('Extra Selection: ')
popSize = len(popList)
seed = 1

#random sampler
def sampler(poplist, seed):
    random.seed(seed)
    return random.sample(poplist,sampleSize+extraSelections)

#random sample accumulator!
randomSample = sampler(popList, seed)
       
#create numbered list of sample
export = []
count = 1
extra = 1
for i in randomSample:
    if count <= sampleSize:
        export.append([count, i])
        count += 1
    else:
        export.append(['e'+str(extra), i])
        extra += 1
##
###write random sample to excel workbook
##

#write summary header
row = 1
col = 0

worksheet.write(row, col,'Population Size', bold)
worksheet.write(row, col+1,popSize)
for i in rangeList:
    worksheet.write(row+1, col,'Range', bold)
    worksheet.write(row+1, col+1,str(i[0]) + ' - ' + str(i[1]))
    row += 1
worksheet.write(row+1, col,'Sample Size', bold)
worksheet.write(row+1, col+1,sampleSize)
worksheet.write(row+1, col,'Extra Selections', bold)
worksheet.write(row+1, col+1,extraSelections)
worksheet.write(row+3, col,'Seed #', bold)
worksheet.write(row+3, col+1,seed)


#write data headers
worksheet.write(row+6, col,'#', bold)
worksheet.write(row+6, col+1,'Selection', bold)

row += 7

#write body
for k in export:
    worksheet.write(row, col, k[0])
    worksheet.write(row, col+1, k[1])
    row += 1

workbook.close()
