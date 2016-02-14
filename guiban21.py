#GUI layout basics

from Tkinter import *
from ttk import *
import rng2
import tkMessageBox


def main():
    root = Tk()
    root.geometry("640x480+400+400")
    content = Major(root)
    root.mainloop()

def gquit():
    quit()



class Major(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def openRanges(self, window):
        window.destroy()
        self.minor = Minor(self)
        self.minor.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
    def openDays(self, window):
        window.destroy()
        self.minor = RangeView1(self)
        self.minor.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
    def initUI(self):

        self.parent.title("Random Number Generator")
        self.minor = RangeView1(self)

        self.days = Button(self, text="Ranges", command=lambda: self.openDays(self.minor))

        self.rangeW = Button(self, text="Days", command=lambda: self.openRanges(self.minor))
        quitB = Button(self, text="Quit", command=gquit)


        self.grid(column=0, row=0, sticky=(N, S, E, W))

        self.days.grid(column=0, row=0, sticky=(N, W), padx=5, pady=5)
        self.rangeW.grid(column=0, row=1, sticky=(N, W), padx=5)
        quitB.grid(column=0, row=2, sticky=(N, W), padx=5, pady=5)

        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(1, weight=1)

# frame 1

        self.minor.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

class Minor(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, borderwidth=2, relief="sunken")
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.daysboxes = DaysBoxes(self)

        namelbl = Label(self, text="Choose Days of Week:")
        #name = Entry(self)

        namelbl.grid(column=0, row=0, columnspan=2, sticky=(W))
        #name.grid(column=0, row=1, columnspan=2, sticky=(N, E, W))

        self.daysboxes.sun.grid(column=0, row=3)
        self.daysboxes.mon.grid(column=1, row=3)
        self.daysboxes.tue.grid(column=2, row=3)
        self.daysboxes.wed.grid(column=3, row=3)
        self.daysboxes.thu.grid(column=4, row=3)
        self.daysboxes.fri.grid(column=5, row=3)
        self.daysboxes.sat.grid(column=6, row=3)

        for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)

class RangeView1(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, borderwidth=2, relief="sunken")
        self.parent = parent
        self.initUI()

    def initUI(self):

        self.numRlabel = Label(self, text="Number of Ranges:")
        self.numRanges = IntVar()
        self.numRanges = Entry(self)
        self.numRanges.insert(0, rng2.getnRanges())

        self.blabel = Label(self, text="Beginning of Range:")
        self.bRange = Entry(self)

        self.elabel = Label(self, text="End of Range:")
        self.eRange = Entry(self)

        self.nextB = Button(self, text="Next", command=self.nextHandler)
        self.prevB = Button(self, text="Previous", command=self.test1a)

        self.numRlabel.grid(column=0, row=0, columnspan=2, sticky=(W))
        self.numRanges.grid(column=0, row=1, columnspan=1, sticky=(N, W))
        self.blabel.grid(column=0, row=2, columnspan=2, sticky=(W))
        self.bRange.grid(column=0, row=3, columnspan=2, sticky=(N, E, W))
        self.elabel.grid(column=0, row=4, columnspan=2, sticky=(W))
        self.eRange.grid(column=0, row=5, columnspan=2, sticky=(N, E, W))
        self.nextB.grid(column=1, row=6, sticky=(S, E), padx=5, pady=5)
        self.prevB.grid(column=0, row=6, sticky = (E))

        for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)

    def test1a(self):
        tkMessageBox.showinfo("test1a", rng2.getnRanges())
        rng2.writeRanges(self.numRanges.get())

    def nextHandler(self):
        rng2.writeRanges(self.numRanges.get())
        self.parent.minor = RangeView2(self.parent)
        self.parent.minor.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

class RangeView2(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, borderwidth=2, relief="sunken")
        self.parent = parent
        self.initUI()

    #Creator for variable list of widgets
    def create_widget(self, i):
        skip = i*4
        self.blabel = Label(self, text="Beginning of Range %s:" %(i+1))
        self.blabel.grid(column=0, row=skip+1, columnspan=2, sticky=(W))
        self.widgetlist.append(self.blabel)

        self.bRange = Entry(self)
        self.bRange.grid(column=0, row=skip+2, columnspan=2, sticky=(N, E, W))
        self.widgetlist.append(self.bRange)

        self.elabel = Label(self, text="End of Range %s:" %(i+1))
        self.elabel.grid(column=0, row=skip+3, columnspan=2, sticky=(W))
        self.widgetlist.append(self.elabel)

        self.eRange = Entry(self)
        self.eRange.grid(column=0, row=skip+4, columnspan=2, sticky=(N, E, W))
        self.widgetlist.append(self.eRange)
    def initUI(self):

        #Heading of number of ranges
        self.numRlabel = Label(self, text="%s Ranges:" % rng2.getnRanges())

        #establish list of potential widgets
        self.widgetlist = []

        #loop through number of ranges creating widgets
        for i in range(int(rng2.getnRanges())):
            self.create_widget(i)

        #Movement buttons
        self.nextB = Button(self, text="Next", command=self.test1a)
        self.prevB = Button(self, text="Previous", command=self.prevHandler)

        #Positioning of widgets
        self.numRlabel.grid(column=0, row=0, columnspan=2, sticky=(W))

        self.nextB.grid(column=1, row=len(self.widgetlist)+2, sticky=(S, E), padx=5, pady=5)
        self.prevB.grid(column=0, row=len(self.widgetlist)+2, sticky = (E))

        for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)

    def test1a(self):
        tkMessageBox.showinfo("test1a", rng2.getnRanges())

    def prevHandler(self):

        self.parent.minor = RangeView1(self.parent)
        self.parent.minor.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

    def storage(self):
        popList = []
        rangeList = []

        rangeDescriptions = rng2.simpleRanges(self.getnumRanges())

        #random sample accumulator!
        stronk = rng2.sampler(popList)
        randomSample = stronk[0]
        sampleSize = stronk[1]
        extraSelections = stronk[2]
        seed = stronk[3]

        #Make sample into list
        export = rng2.sampleList(randomSample, sampleSize)

        #Write to excel
        rng2.writeExcel(getPopSize(popList), rangeList, sampleSize, extraSelections, seed, export, rangeDescriptions)


class DaysBoxes(Frame):

    def __init__(self, parent):
        self.parent = parent

        sunvar = BooleanVar()
        monvar = BooleanVar()
        tuevar = BooleanVar()
        wedvar = BooleanVar()
        thuvar = BooleanVar()
        frivar = BooleanVar()
        satvar = BooleanVar()

        sunvar.set(False)
        monvar.set(True)
        tuevar.set(True)
        wedvar.set(True)
        thuvar.set(True)
        frivar.set(True)
        satvar.set(False)

        self.sun= Checkbutton(self.parent, text="Sun", variable=sunvar, onvalue=True)
        self.mon = Checkbutton(self.parent, text="Mon", variable=monvar, onvalue=True)
        self.tue = Checkbutton(self.parent, text="Tue", variable=tuevar, onvalue=True)
        self.wed = Checkbutton(self.parent, text="Wed", variable=wedvar, onvalue=True)
        self.thu = Checkbutton(self.parent, text="Thu", variable=thuvar, onvalue=True)
        self.fri = Checkbutton(self.parent, text="Fri", variable=frivar, onvalue=True)
        self.sat = Checkbutton(self.parent, text="Sat", variable=satvar, onvalue=True)


if __name__ == '__main__':
    main()
