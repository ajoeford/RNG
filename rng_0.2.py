import xlsxwriter
import random

#initiate excel workbook
workbook = xlsxwriter.Workbook('random02.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})

#Classes for population
class unit(object):
    '''An individual unit of the population
    Holds numbering and range description'''
    def __init__(self, number, description):
        self.number = number
        self.description = description
        
    def getNumber(self):
        return self.number
        
    def getDescription(self):
        return self.description    

#Classes for rows and lines
class multiunit(unit):
    def __init__(self, number, description, row):
        unit.__init__(self, number, description)
        self.row = row

    def getRow(self):
        return self.row 
        

#Create ranges
def createRange(i):
    while True:
        try:
            begRange = input('Beginning Range ' + str(i+1) +': ')
            endRange = input('Ending Range ' + str(i+1) +': ')
            description = raw_input('Range Description ' + str(i+1) +': ')
            for n in range(begRange, endRange+1):
                popList.append(unit(n, description))
    
            #write beg and end range back to main
            rangeList.append([begRange, endRange])
            return description
            
        except NameError:
            print ('Error: Invalid number')

##
###random sample parameters
##

#Ranges - establish number of ranges

def simpleRanges():
    
    numRanges = input('Number of Ranges: ')
    rangeDescriptions = []

    for i in range(numRanges):
        rangeDescriptions.append(createRange(i))
    
    return rangeDescriptions

#random sampler

def sampler(poplist):
    while True:
        try:
            #establish sample parameters
            sampleSize = input('Sample Size: ')
            extraSelections = input('Extra Selection: ')
            seed = 1
            break
        except NameError:
            print 'Please enter a valid integer.'
    random.seed(seed)
    randomSamp = random.sample(poplist,sampleSize+extraSelections)
    return [randomSamp, sampleSize, extraSelections, seed]

       
#create numbered list of sample

def sampleList(randomSample, sampleSize):
    
    export = []
    count = 1
    extra = 1
    for i in randomSample:
        if count <= sampleSize:
            export.append([count, i.getNumber(), i.getDescription()])
            count += 1
        else:
            export.append(['e'+str(extra), i.getNumber(), i.getDescription()])
            extra += 1
    return export

##
###write random sample to excel workbook
##

def writeExcel(popSize, rangeList, sampleSize, extraSelections, seed, export, rangeDescriptions):

    #write summary header
    row = 1
    col = 0

    worksheet.write(row, col,'Population Size', bold)
    worksheet.write(row, col+1,popSize)
    k = 0
    for i in rangeList:
        row += 1
        worksheet.write(row, col,'Range: ' + rangeDescriptions[k], bold)
        worksheet.write(row, col+1,str(i[0]) + ' - ' + str(i[1]))
        k += 1
    worksheet.write(row+1, col,'Sample Size', bold)
    worksheet.write(row+1, col+1,sampleSize)
    worksheet.write(row+2, col,'Extra Selections', bold)
    worksheet.write(row+2, col+1,extraSelections)
    worksheet.write(row+3, col,'Seed #', bold)
    worksheet.write(row+3, col+1,seed)


    #write data headers
    worksheet.write(row+6, col,'#', bold)
    worksheet.write(row+6, col+1,'Selection', bold)
    worksheet.write(row+6, col+2,'Description', bold)
    
    row += 7
    
    #write body
    for k in export:
        worksheet.write(row, col, k[0])
        worksheet.write(row, col+1, k[1])
        worksheet.write(row, col+2, k[2])
        row += 1
    
    workbook.close()

def getPopSize(popList):
    popSize = len(popList)
    return popSize

##
###Runtime
##

#Create ranges
popList = []

#Choose type of sampling
rangeList = []

while True:
    sampleType = raw_input('Choose a sample type. \'r\' for ranges. \'l\' for lines and rows. \'d\' for days of the week.: ')
    if sampleType == 'r':
        rangeDescriptions = simpleRanges()
        break
    elif sampleType == 'l':
        ## Complete
        break
    elif sampleType == 'd':
        ## Complete
        break
    else:
        print 'Please provide a proper input.'

#random sample accumulator!
stronk = sampler(popList)
randomSample = stronk[0]
sampleSize = stronk[1]
extraSelections = stronk[2]
seed = stronk[3]

#Make sample into list
export = sampleList(randomSample, sampleSize)

#Write to excel
writeExcel(getPopSize(popList), rangeList, sampleSize, extraSelections, seed, export, rangeDescriptions)