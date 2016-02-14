import Tkinter
#inherits from Tkinter.Tk
class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		#create and then add to layout manager
		self.entryVariable = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self, textvariable = self.entryVariable)
		self.entry.grid(column=0, row=0, sticky = 'EW')
		self.entry.bind("<Return>", self.OnPressEnter) 
		self.entryVariable.set("Enter text here.") #defaults
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)
		
		button = Tkinter.Button(self,text ="GoOGOGOGOGOGO!", command = self.OnButtonClick)
		button.grid(column = 1, row = 0)

		self.labelVariable = Tkinter.StringVar()
		label = Tkinter.Label(self, textvariable = self.labelVariable, anchor = "w", fg = "white", bg="blue")
		label.grid(column = 0, row = 1, columnspan = 2, sticky = 'EW')
		self.labelVariable.set('Hello') #defaults
		self.grid_columnconfigure(0, weight = 1)
		self.resizable(True, False)
		self.update()
		self.geometry(self.geometry());

		

	def OnButtonClick(self):
		self.labelVariable.set(self.entryVariable.get()+ "button" )
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)
		#this is why we need self on event

	def OnPressEnter(self,event):
		self.labelVariable.set(self.entryVariable.get()+ "enter" )
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title("My app")
	app.mainloop()