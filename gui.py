from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import os

import file
import utils
from main import getData

font=("Helvetica",15)
backColor = "#423F3E"
textBoxColor = "#272121"
textColor= "white"
borderlineColor = "#E4E4E4"
btnBg = "#EDEDED"
global fieldList
global imgIndex
global dataDict
global formImg
global label

#global formImage
imgIndex = 0
fieldList = []
formList = os.listdir('forms')

def convert_to_image(frame):
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	image = Image.fromarray(frame)

	return image
def showloading():
	loading = Toplevel()
	x = int((screen_width / 2) - (250 / 2))
	y = int((screen_height / 2) - (150 / 2))
	loading.geometry(f'250x150+{x}+{y}')
	loading.wm_attributes('-topmost','true')
	#loading.overrideredirect(1)
	progess = ttk.Progressbar(loading,orient=HORIZONTAL,
							  length=100,mode='indeterminate')
	progess.grid(row=0,column=0,padx=5,pady=5)
	progess.start()
	#loading.update_idletasks()
	loadLabel = Label(loading,text="Analyzing Data",font=("Helvetica",20))
	loadLabel.grid(row=1,column=0)
# def hideLoading():
# 	#global loading

# 	loading.destroy()
# 	loading.update()
def saveValue():
	d = {}
	for field in fieldList:

		if field['type'] == 'sbox':
			value = ''
			boxes = field['boxes']
			for box in boxes:
				value += str(box.get()).strip()
			d[field['name']]=value
		if field['type'] == 'cbox':
			cbox = field['cbox'][0]
			if(cbox.state()):
				d[field['name']] = 1
			else:
				d[field['name']] = 0

	file.insertIntoCSV(d)
	messagebox.showinfo("Saved","Form Data Saved To CSV File")
def clearEntryBoxes():
    for widget in dataFrame.winfo_children():
        if(widget.winfo_class()=="Label"):
            pass
        else:
            widget.destroy()
def next():
	global imgIndex
	global formImg
	global label
	if(imgIndex<len(formList)-1):
		#root.update_idletasks()

		imgIndex +=1
		#showloading()
		label.grid_forget()
		clearEntryBoxes()
		setData()
		loadImage(formImg)
		dataTraverse()

	else:
		messagebox.showerror("Error","No More Image")

def prev():
	global imgIndex
	global formImg
	global label
	if(imgIndex>0):
		imgIndex -=1
		label.grid_forget()
		clearEntryBoxes()
		setData()
		loadImage(formImg)
		dataTraverse()
	else:
		messagebox.showerror("Error","No More Image")

def loadImage(img):
	img = utils.resize(img, 4)
	#utils.show(imgShow,1)
	img = convert_to_image(img)
	global label
	global imgShow
	imgShow = ImageTk.PhotoImage(img)
	label = Label(imageFrame, image=imgShow)
	label.grid(row=0, column=0, sticky=NW, padx=2, pady=5, columnspan=3)
# form = cv2.imread('forms/F1.jpg')
# formImg,dict = getData(form)
# print(dict)
dic = [{'type': 'sbox', 'segments': 17, 'name': 'bcn', 'value': '২০০৯৪৫২৩০৫৬৮৯১২৭৯'}, {'type': 'sbox', 'segments': 8, 'name': 'dob', 'value': '১০১২১৯৯৮'}, {'type': 'cbox', 'name': 'male', 'value': 1}, {'type': 'cbox', 'name': 'female', 'value': 0}, {'type': 'sbox', 'segments': 17, 'name': 'nid', 'value': '১৫৬৭৯৭৮৯১৩৫৬৭৬৯৯৩'}, {'type': 'sbox', 'segments': 11, 'name': 'mobile', 'value': '০৯৭৭৬৭৬৭৭২৬'}, {'type': 'sbox', 'segments': 10, 'name': 'reg', 'value': '২০১৭৩৩১০৪৮'}, {'type': 'sbox', 'segments': 8, 'name': 'date', 'value': '৯৮০৯২০২২'}]
# cv2.imwrite('im.jpg',formImg)
#formImg = cv2.imread(f'forms/{formList[imgIndex]}')
def setData():
	global dataDict
	global formImg
	#showloading()
	form = cv2.imread(f'forms/{formList[imgIndex]}')
	formImg, dataDict = getData(form)
def dataTraverse():
	row = 1
	global fieldList
	global dataDict
	fieldList = []
	for field in dataDict:
		dict = {}
		dict['name'] = field["name"]
		dict['type'] = field['type']
		fieldFrame = Frame(dataFrame, bg=backColor, highlightcolor=borderlineColor, highlightthickness=1,
							   highlightbackground="#222831")
		fieldFrame.grid(row=row, column=0, sticky=NW, padx=2, pady=5)
		if field['type'] == 'sbox':
			boxList = []
			labelName = Label(fieldFrame, text=f'{field["name"]}:', font=font, bg=backColor, fg=textColor)
			labelName.grid(row=0, column=0,sticky=NW)
			for s in range(len(field["value"])):
				entryBox = Entry(fieldFrame, font=font, width=3, bg=textBoxColor, fg=textColor, relief=FLAT,
								   highlightcolor=borderlineColor, highlightthickness=1, highlightbackground=backColor,
								   insertbackground=textColor)
				entryBox.grid(row=1, column=s, pady=5, padx=1)
				entryBox.insert(0,f'{field["value"][s]}')
				boxList.append(entryBox)
			dict['boxes'] = boxList

		if field['type'] == 'cbox':
			checkList = []
			s = ttk.Style()
			s.configure('TCheckbutton', font=font, background=backColor, foreground=textColor)
			chk = ttk.Checkbutton(fieldFrame, text=f'{field["name"]}',state=s)
			#chk.config(state=tkinter.SELECTED)
			#chk['state']='selected'
			chk.state(['!alternate'])
			if field['value'] == 1:
				chk.state(['selected'])
			#print(chk.state())
			#labelName = Label(fieldFrame, text=f'{field["name"]} : ', font=font, bg=backColor, fg=textColor)
			chk.grid(row=0, column=0, sticky=NW)
			checkList.append(chk)
			dict['cbox']= checkList
		fieldList.append(dict)
		row += 1

root = Tk()
#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.title("Form Data Extractor")
root.configure(bg='#423F3E')
imageFrame = Frame(root,width = int(screen_width/2.5),height=int(screen_height),bg=backColor,highlightcolor=borderlineColor,highlightthickness=1,highlightbackground="#222831")
imageFrame.grid(row=0,column=0,sticky=NW,padx=2,pady=5,columnspan=3)
imageFrame.grid_propagate(False)
# setData()
# loadImage(formImg)
#showloading()
#imgShow = ImageTk.PhotoImage(imgShow)

#loadImage(formImg)
dataFrame= Frame(root,width = int(screen_width/2.1),height=int(screen_height),bg=backColor,highlightcolor=borderlineColor,highlightthickness=1,highlightbackground="#222831")
dataFrame.grid(row=0,column=3,sticky=NW,padx=5,pady=5,columnspan=3)
dataFrame.grid_propagate(False)
# dataTraverse()
buttonFrame= Frame(root,width = int(screen_width/10),height=int(screen_height),bg=backColor,highlightcolor=borderlineColor,highlightthickness=1,highlightbackground="#222831")
buttonFrame.grid(row=0,column=6,sticky=NW,padx=5,pady=5,columnspan=3)
buttonFrame.grid_propagate(False)
btnSave = Button(buttonFrame,font=("Helvetica",25,'bold'),text="Save",bg="#52c5a9",fg="black",command = saveValue)
btnSave.grid(row=0,column=0,padx=2,pady=5)
btnNext = Button(buttonFrame,font=("Helvetica",25,'bold'),text="Next",bg="#52c5a9",fg="black",command = next)
btnNext.grid(row=1,column=0,padx=2,pady=5)
btnPrev = Button(buttonFrame,font=("Helvetica",20,'bold'),text="Previous",bg="#52c5a9",fg="black",command = prev)
btnPrev.grid(row=2,column=0,padx=2,pady=5)
setData()
loadImage(formImg)
dataTraverse()
root.mainloop()
