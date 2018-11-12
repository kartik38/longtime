from tkinter import *
import tkinter.ttk as ttk
import psycopg2

connection = psycopg2.connect(user='kartik', password='0111', database='origin')
cursor = connection.cursor()

mainWindow = Tk()
mainWindow.geometry('300x200')
mainWindow.resizable(0,0)
mainWindow.title('Project Management')
# mainWindow.mainloop()

# loginFrame = Frame(mainWindow)
viewFrame   = Frame(mainWindow)
insertFrame = Frame(mainWindow)
updateFrame = Frame(mainWindow)
updateFrame2 = Frame(mainWindow)
deleteFrame = Frame(mainWindow)



def openViewFrame   () :
	if (insertFrame) :
		insertFrame.grid_forget()
	if (updateFrame) :
		updateFrame.grid_forget()
	if (deleteFrame) :
		deleteFrame.grid_forget()
	if (updateFrame2) :
		updateFrame2.grid_forget()

	classNameViewLabel= ttk.Label(viewFrame, text='Class')
	classNameViewLabel.grid(row='2', column='0')
	classNameViewEntry = ttk.Entry(viewFrame)
	classNameViewEntry.grid(row='2', column='1')

	rollNumberViewLabel= ttk.Label(viewFrame, text='Roll No')
	rollNumberViewLabel.grid(row='3', column='0')
	rollNumberViewEntry = ttk.Entry(viewFrame)
	rollNumberViewEntry.grid(row='3', column='1')


	def viewing () :
		if (classNameViewEntry.get()!='' and rollNumberViewEntry.get()!='') :
			classNameViewFrameValue = classNameViewEntry.get().lower()
			rollNumberViewFrameValue = rollNumberViewEntry.get()

			cursor.execute("""SELECT *
												FROM ORIGIN
												WHERE CLASS=%s AND ROLLNO=%s;""",
												(classNameViewFrameValue, rollNumberViewFrameValue))

			data = cursor.fetchone()
			# for i in data:
			# 	print(i)
			viewWindow = Tk()

			fnameViewWindowLabel = ttk.Label(viewWindow, text='First Name')
			fnameViewWindowLabel.grid(row='0', column='0')
			fnameViewWindowLabel = ttk.Label(viewWindow, text=data[1])
			fnameViewWindowLabel.grid(row='0', column='1')

			lnameViewWindowLabel = ttk.Label(viewWindow, text='Last Name')
			lnameViewWindowLabel.grid(row='1', column='0')
			lnameViewWindowLabel = ttk.Label(viewWindow, text=data[2])
			lnameViewWindowLabel.grid(row='1', column='1')

			classNameViewWindowLabel = ttk.Label(viewWindow, text='Class Name')
			classNameViewWindowLabel.grid(row='2', column='0')
			classNameViewWindowLabel = ttk.Label(viewWindow, text=data[3])
			classNameViewWindowLabel.grid(row='2', column='1')

			rollNumberViewWindowLabel = ttk.Label(viewWindow, text='Roll No.')
			rollNumberViewWindowLabel.grid(row='3', column='0')
			rollNumberViewWindowLabel = ttk.Label(viewWindow, text=data[4])
			rollNumberViewWindowLabel.grid(row='3', column='1')

			projectNameViewWindowLabel = ttk.Label(viewWindow, text='Project Name')
			projectNameViewWindowLabel.grid(row='4', column='0')
			projectNameViewWindowLabel = ttk.Label(viewWindow, text=data[5])
			projectNameViewWindowLabel.grid(row='4', column='1')

			contactNumberViewWindowLabel = ttk.Label(viewWindow, text='Contact No.')
			contactNumberViewWindowLabel.grid(row='5', column='0')
			contactNumberViewWindowLabel = ttk.Label(viewWindow, text=data[6])
			contactNumberViewWindowLabel.grid(row='5', column='1')

			emailIdViewWindowLabel = ttk.Label(viewWindow, text='Email ID')
			emailIdViewWindowLabel.grid(row='6', column='0')
			emailIdViewWindowLabel = ttk.Label(viewWindow, text=data[7])
			emailIdViewWindowLabel.grid(row='6', column='1')


			viewWindow.mainloop()
			if (mainWindow.destroy()) :
				viewWindow.destroy()


	viewViewButton = ttk.Button(viewFrame, text='View', command=viewing)
	viewViewButton.grid(row='7', columnspan='2')
	viewFrame.grid()



def openInsertFrame () :
	if (viewFrame) :
		viewFrame.grid_forget()
	if (updateFrame) :
		updateFrame.grid_forget()
	if (updateFrame2) :
		updateFrame2.grid_forget()
	if (deleteFrame) :
		deleteFrame.grid_forget()
	# insertFrame = Frame(mainWindow)
	fnameInsertLabel= ttk.Label(insertFrame, text='First Name')
	fnameInsertLabel.grid(row='0', column='0')
	fnameInsertEntry = ttk.Entry(insertFrame)
	fnameInsertEntry.grid(row='0', column='1')

	lnameInsertLabel= ttk.Label(insertFrame, text='Last Name')
	lnameInsertLabel.grid(row='1', column='0')
	lnameInsertEntry = ttk.Entry(insertFrame)
	lnameInsertEntry.grid(row='1', column='1')

	classNameInsertLabel= ttk.Label(insertFrame, text='Class')
	classNameInsertLabel.grid(row='2', column='0')
	classNameInsertEntry = ttk.Entry(insertFrame)
	classNameInsertEntry.grid(row='2', column='1')

	rollNumberInsertLabel= ttk.Label(insertFrame, text='Roll No')
	rollNumberInsertLabel.grid(row='3', column='0')
	rollNumberInsertEntry = ttk.Entry(insertFrame)
	rollNumberInsertEntry.grid(row='3', column='1')

	projectNameInsertLabel= ttk.Label(insertFrame, text='Project Name')
	projectNameInsertLabel.grid(row='4', column='0')
	projectNameInsertEntry = ttk.Entry(insertFrame)
	projectNameInsertEntry.grid(row='4', column='1')

	contactNumberInsertLabel= ttk.Label(insertFrame, text='Contact No')
	contactNumberInsertLabel.grid(row='5', column='0')
	contactNumberInsertEntry = ttk.Entry(insertFrame)
	contactNumberInsertEntry.grid(row='5', column='1')

	emailIdInsertLabel= ttk.Label(insertFrame, text='Email ID')
	emailIdInsertLabel.grid(row='6', column='0')
	emailIdInsertEntry = ttk.Entry(insertFrame)
	emailIdInsertEntry.grid(row='6', column='1')


	def insertIntoDB () :
		fnameInsertFrameValue = fnameInsertEntry.get().lower()
		lnameInsertFrameValue = lnameInsertEntry.get().lower()
		classNameInsertFrameValue = classNameInsertEntry.get().lower()
		rollNumberInsertFrameValue = rollNumberInsertEntry.get()
		projectNameInsertFrameValue = projectNameInsertEntry.get().lower()
		contactNumberInsertFrameValue = contactNumberInsertEntry.get()
		emailIdInsertFrameValue = emailIdInsertEntry.get().lower()
		

		if (fnameInsertFrameValue!='' and lnameInsertFrameValue!='' and classNameInsertFrameValue!='' and
				rollNumberInsertFrameValue!='' and projectNameInsertFrameValue!='' and contactNumberInsertFrameValue!=''
				and emailIdInsertFrameValue!=''  ) :
			cursor.execute('INSERT INTO ORIGIN (FNAME, LNAME, CLASS, ROLLNO, PROJECTNAME, MOBILENUMBER, EMAILID) VALUES (%s,%s,%s,%s,%s,%s,%s)',
											(fnameInsertFrameValue, lnameInsertFrameValue, classNameInsertFrameValue, 
										   rollNumberInsertFrameValue, projectNameInsertFrameValue, contactNumberInsertFrameValue, emailIdInsertFrameValue))
			connection.commit()
			fnameInsertEntry.delete(0, 'end')
			lnameInsertEntry.delete(0, 'end')
			classNameInsertEntry.delete(0, 'end')
			rollNumberInsertEntry.delete(0, 'end')
			projectNameInsertEntry.delete(0, 'end')
			contactNumberInsertEntry.delete(0, 'end')
			emailIdInsertEntry.delete(0, 'end')
		else:
			connection.rollback()


	insertInsertButton = ttk.Button(insertFrame, text='Insert', command=insertIntoDB)
	insertInsertButton.grid(row='7', columnspan='2')
	insertFrame.grid()



def openUpdateFrame () :
	if (viewFrame) :
		viewFrame.grid_forget()
	if (insertFrame) :
		insertFrame.grid_forget()
	if (deleteFrame) :
		deleteFrame.grid_forget()
	if (updateFrame2) :
		updateFrame2.grid_forget()
	classNameUpdateLabel= ttk.Label(updateFrame, text='Class')
	classNameUpdateLabel.grid(row='2', column='0')
	classNameUpdateEntry = ttk.Entry(updateFrame)
	classNameUpdateEntry.grid(row='2', column='1')

	rollNumberUpdateLabel= ttk.Label(updateFrame, text='Roll No')
	rollNumberUpdateLabel.grid(row='3', column='0')
	rollNumberUpdateEntry = ttk.Entry(updateFrame)
	rollNumberUpdateEntry.grid(row='3', column='1')

	classNameUpdateFrameValue = classNameUpdateEntry.get().lower()
	rollNumberUpdateFrameValue = rollNumberUpdateEntry.get()

	def openUpdateFrame3 ():
		if (classNameUpdateEntry.get()!='' and rollNumberUpdateEntry.get()!='') :
			if (updateFrame) :
				updateFrame.grid_forget()

			def openFnameUpdateWindow () :
				fnameUpdateWindow = Tk()
				fnameUpdateWindow.title('Update First Name')
				# fnameUpdateWindow.geometry('400x100')
				fnameUpdateLabel = ttk.Label(fnameUpdateWindow, text='First Name')
				fnameUpdateLabel.grid()
				fnameUpdateEntry = ttk.Entry(fnameUpdateWindow)
				fnameUpdateEntry.grid()
				def fnameUpdate ():
					classNameUpdateFrameValue = classNameUpdateEntry.get().lower()
					rollNumberUpdateFrameValue = rollNumberUpdateEntry.get()
					fnameUpdateValue = fnameUpdateEntry.get().lower()
					if (fnameUpdateEntry.get()!='') :
						cursor.execute("""UPDATE ORIGIN 
															SET FNAME=%s
															WHERE CLASS=%s AND ROLLNO=%s;
															""",
															(fnameUpdateValue, classNameUpdateFrameValue, rollNumberUpdateFrameValue))
						connection.commit()
						fnameUpdateEntry.delete(0, 'end')

						fnameUpdateWindow.destroy()


				fnameUpdateButton = ttk.Button(fnameUpdateWindow, text='Update', command=fnameUpdate)
				fnameUpdateButton.grid()
				fnameUpdateWindow.mainloop()

			def openLnameUpdateWindow () :
				lnameUpdateWindow = Tk()
				lnameUpdateWindow.title('Update Last Name')
				lnameUpdateLabel = ttk.Label(lnameUpdateWindow, text='Last Name')
				lnameUpdateLabel.grid()
				lnameUpdateEntry = ttk.Entry(lnameUpdateWindow)
				lnameUpdateEntry.grid()
				def lnameUpdate ():
					classNameUpdateFrameValue = classNameUpdateEntry.get().lower()
					rollNumberUpdateFrameValue = rollNumberUpdateEntry.get()
					lnameUpdateValue = lnameUpdateEntry.get().lower()
					if (lnameUpdateEntry.get()!='') :
						cursor.execute("""UPDATE ORIGIN 
															SET LNAME=%s
															WHERE CLASS=%s AND ROLLNO=%s;
															""",
															(lnameUpdateValue, classNameUpdateFrameValue, rollNumberUpdateFrameValue))
						connection.commit()
						lnameUpdateEntry.delete(0, 'end')
						
						lnameUpdateWindow.destroy()
				lnameUpdateButton = ttk.Button(lnameUpdateWindow, text='Update', command=lnameUpdate)
				lnameUpdateButton.grid()
				lnameUpdateWindow.mainloop()

			def openClassNameUpdateWindow () :
				classNameUpdateWindow = Tk()
				classNameUpdateWindow.title('Update Class Name')
				classNameUpdateLabel = ttk.Label(classNameUpdateWindow, text='Class Name')
				classNameUpdateLabel.grid()
				classNameUpdateEntry = ttk.Entry(classNameUpdateWindow)
				classNameUpdateEntry.grid()
				def classNameUpdate ():
					classNameUpdateFrameValue = classNameUpdateEntry.get().lower()
					rollNumberUpdateFrameValue = rollNumberUpdateEntry.get()
					classNameUpdateValue = classNameUpdateEntry.get().lower()
					if (classNameUpdateEntry.get()!='') :
						cursor.execute("""UPDATE ORIGIN 
															SET CLASS=%s
															WHERE CLASS=%s AND ROLLNO=%s;
															""",
															(classNameUpdateValue, classNameUpdateFrameValue, rollNumberUpdateFrameValue))
						connection.commit()
						classNameUpdateEntry.delete(0, 'end')
						
						classNameUpdateWindow.destroy()
				classNameUpdateButton = ttk.Button(classNameUpdateWindow, text='Update', command=classNameUpdate)
				classNameUpdateButton.grid()
				classNameUpdateWindow.mainloop()

			def openRollNumberUpdateWindow () :
				rollNumberUpdateWindow = Tk()
				rollNumberUpdateWindow.title('Update RDll Number')
				rollNumberUpdateLabel = ttk.Label(rollNumberUpdateWindow, text='Roll Number Name')
				rollNumberUpdateLabel.grid()
				rollNumberUpdateEntry = ttk.Entry(rollNumberUpdateWindow)
				rollNumberUpdateEntry.grid()
				def rollNumberUpdate ():
					classNameUpdateFrameValue = classNameUpdateEntry.get().lower()
					rollNumberUpdateFrameValue = rollNumberUpdateEntry.get()
					rollNumberUpdateValue = rollNumberUpdateEntry.get().lower()
					if (rollNumberUpdateEntry.get()!='') :
						cursor.execute("""UPDATE ORIGIN 
															SET ROLLNO=%s
															WHERE CLASS=%s AND ROLLNO=%s;
															""",
															(rollNumberUpdateValue, classNameUpdateFrameValue, rollNumberUpdateFrameValue))
						connection.commit()
						rollNumberUpdateEntry.delete(0, 'end')
						
						rollNumberUpdateWindow.destroy()
				rollNumberUpdateButton = ttk.Button(rollNumberUpdateWindow, text='Update', command=rollNumberUpdate)
				rollNumberUpdateButton.grid()
				rollNumberUpdateWindow.mainloop()

			def openProjectNameUpdateWindow () :
				projectNameUpdateWindow = Tk()
				projectNameUpdateWindow.title('Update Project Name')
				projectNameUpdateLabel = ttk.Label(projectNameUpdateWindow, text='Project Name')
				projectNameUpdateLabel.grid()
				projectNameUpdateEntry = ttk.Entry(projectNameUpdateWindow)
				projectNameUpdateEntry.grid()
				def projectNameUpdate ():
					classNameUpdateFrameValue = classNameUpdateEntry.get().lower()
					rollNumberUpdateFrameValue = rollNumberUpdateEntry.get()
					projectNameUpdateValue = projectNameUpdateEntry.get().lower()
					if (projectNameUpdateEntry.get()!='') :
						cursor.execute("""UPDATE ORIGIN 
															SET PROJECTNAME=%s
															WHERE CLASS=%s AND ROLLNO=%s;
															""",
															(projectNameUpdateValue, classNameUpdateFrameValue, rollNumberUpdateFrameValue))
						connection.commit()
						projectNameUpdateEntry.delete(0, 'end')
						
						projectNameUpdateWindow.destroy()
				projectNameUpdateButton = ttk.Button(projectNameUpdateWindow, text='Update', command=projectNameUpdate)
				projectNameUpdateButton.grid()
				projectNameUpdateWindow.mainloop()

			def openContactNumberUpdateWindow () :
				contactNumberUpdateWindow = Tk()
				contactNumberUpdateWindow.title('Update Contact Number')
				contactNumberUpdateLabel = ttk.Label(contactNumberUpdateWindow, text='Contact Number')
				contactNumberUpdateLabel.grid()
				contactNumberUpdateEntry = ttk.Entry(contactNumberUpdateWindow)
				contactNumberUpdateEntry.grid()
				def contactNumberUpdate ():
					classNameUpdateFrameValue = classNameUpdateEntry.get().lower()
					rollNumberUpdateFrameValue = rollNumberUpdateEntry.get()
					contactNumberUpdateValue = contactNumberUpdateEntry.get().lower()
					if (contactNumberUpdateEntry.get()!='') :
						cursor.execute("""UPDATE ORIGIN 
															SET MOBILENUMBER=%s
															WHERE CLASS=%s AND ROLLNO=%s;
															""",
															(contactNumberUpdateValue, classNameUpdateFrameValue, rollNumberUpdateFrameValue))
						connection.commit()
						contactNumberUpdateEntry.delete(0, 'end')
						
						contactNumberUpdateWindow.destroy()
				contactNumberUpdateButton = ttk.Button(contactNumberUpdateWindow, text='Update', command=contactNumberUpdate)
				contactNumberUpdateButton.grid()
				contactNumberUpdateWindow.mainloop()

			def openEmailIdUpdateWindow () :
				emailIdUpdateWindow = Tk()
				emailIdUpdateWindow.title('Update Email ID')
				emailIdUpdateLabel = ttk.Label(emailIdUpdateWindow, text='Email ID')
				emailIdUpdateLabel.grid()
				emailIdUpdateEntry = ttk.Entry(emailIdUpdateWindow)
				emailIdUpdateEntry.grid()
				def emailIdUpdate ():
					classNameUpdateFrameValue = classNameUpdateEntry.get().lower()
					rollNumberUpdateFrameValue = rollNumberUpdateEntry.get()
					emailIdUpdateValue = emailIdUpdateEntry.get().lower()
					if (emailIdUpdateEntry.get()!='') :
						cursor.execute("""UPDATE ORIGIN 
															SET EMAILID=%s
															WHERE CLASS=%s AND ROLLNO=%s;
															""",
															(emailIdUpdateValue, classNameUpdateFrameValue, rollNumberUpdateFrameValue))
						connection.commit()
						emailIdUpdateEntry.delete(0, 'end')
						
						emailIdUpdateWindow.destroy()
				emailIdUpdateButton = ttk.Button(emailIdUpdateWindow, text='Update', command=emailIdUpdate)
				emailIdUpdateButton.grid()
				emailIdUpdateWindow.mainloop()

			fnameUpdate2Button = ttk.Button(updateFrame2, text='First Name', command=openFnameUpdateWindow)
			fnameUpdate2Button.grid()
			lnameUpdate2Button = ttk.Button(updateFrame2, text='Last Name', command=openLnameUpdateWindow)
			lnameUpdate2Button.grid()
			classNameUpdate2Button = ttk.Button(updateFrame2, text='Class Name', command=openClassNameUpdateWindow)
			classNameUpdate2Button.grid()
			rollNumberUpdate2Button = ttk.Button(updateFrame2, text='Roll no.', command=openRollNumberUpdateWindow)
			rollNumberUpdate2Button.grid()
			projectNameUpdate2Button = ttk.Button(updateFrame2, text='Project Name', command=openProjectNameUpdateWindow)
			projectNameUpdate2Button.grid()
			contactNumberUpdate2Button = ttk.Button(updateFrame2, text='Contact no.', command=openContactNumberUpdateWindow)
			contactNumberUpdate2Button.grid()
			emailIdUpdate2Button = ttk.Button(updateFrame2, text='Email ID', command=openEmailIdUpdateWindow)
			emailIdUpdate2Button.grid()
			updateFrame2.grid()

	def openUpdateFrame2 () :
		if (classNameUpdateEntry.get()!='' and rollNumberUpdateEntry.get()!=''):
			if (updateFrame) :
				updateFrame.grid_forget()
			def openFnameUpdateWindow () :
				fnameUpdateWindow = Tk()
				fnameUpdateWindow.title('Update First Name')
				# fnameUpdateWindow.geometry('400x100')
				fnameUpdateLabel = ttk.Label(fnameUpdateWindow, text='First Name')
				fnameUpdateLabel.grid()
				fnameUpdateEntry = ttk.Entry(fnameUpdateWindow)
				fnameUpdateEntry.grid()
				def fnameUpdate ():
					classNameUpdateFrameValue = classNameUpdateEntry.get().lower()
					rollNumberUpdateFrameValue = rollNumberUpdateEntry.get()
					fnameUpdateValue = fnameUpdateEntry.get().lower()	

				fnameUpdateButton = ttk.Button(fnameUpdateWindow, text='Update')
				fnameUpdateButton.grid()
				fnameUpdateWindow.mainloop()

			def openLnameUpdateWindow () :
				lnameUpdateWindow = Tk()
				lnameUpdateWindow.title('Update Last Name')
				lnameUpdateLabel = ttk.Label(lnameUpdateWindow, text='Last Name')
				lnameUpdateLabel.grid()
				lnameUpdateEntry = ttk.Entry(lnameUpdateWindow)
				lnameUpdateEntry.grid()
				lnameUpdateButton = ttk.Button(lnameUpdateWindow, text='Update')
				lnameUpdateButton.grid()
				lnameUpdateWindow.mainloop()

			def openClassNameUpdateWindow () :
				classNameUpdateWindow = Tk()
				classNameUpdateWindow.title('Update Class Name')
				classNameameUpdateLabel = ttk.Label(classNameUpdateWindow, text='Class Name')
				classNameameUpdateLabel.grid()
				classNameameUpdateEntry = ttk.Entry(classNameUpdateWindow)
				classNameameUpdateEntry.grid()
				classNameameUpdateButton = ttk.Button(classNameUpdateWindow, text='Update')
				classNameameUpdateButton.grid()
				classNameUpdateWindow.mainloop()

			def openRollNumberUpdateWindow () :
				rollNumberUpdateWindow = Tk()
				rollNumberUpdateWindow.title('Update RDll Number')
				rollNumberUpdateLabel = ttk.Label(rollNumberUpdateWindow, text='Roll Number Name')
				rollNumberUpdateLabel.grid()
				rollNumberUpdateEntry = ttk.Entry(rollNumberUpdateWindow)
				rollNumberUpdateEntry.grid()
				rollNumberUpdateButton = ttk.Button(rollNumberUpdateWindow, text='Update')
				rollNumberUpdateButton.grid()
				rollNumberUpdateWindow.mainloop()

			def openProjectNameUpdateWindow () :
				projectNameUpdateWindow = Tk()
				projectNameUpdateWindow.title('Update Project Name')
				projectNameUpdateLabel = ttk.Label(projectNameUpdateWindow, text='Project Name')
				projectNameUpdateLabel.grid()
				projectNameUpdateEntry = ttk.Entry(projectNameUpdateWindow)
				projectNameUpdateEntry.grid()
				projectNameUpdateButton = ttk.Button(projectNameUpdateWindow, text='Update')
				projectNameUpdateButton.grid()
				projectNameUpdateWindow.mainloop()

			def openContactNumberUpdateWindow () :
				contactNumberUpdateWindow = Tk()
				contactNumberUpdateWindow.title('Update Contact Number')
				contactNumberUpdateLabel = ttk.Label(contactNumberUpdateWindow, text='Contact Number')
				contactNumberUpdateLabel.grid()
				contactNumberUpdateEntry = ttk.Entry(contactNumberUpdateWindow)
				contactNumberUpdateEntry.grid()
				contactNumberUpdateButton = ttk.Button(contactNumberUpdateWindow, text='Update')
				contactNumberUpdateButton.grid()
				contactNumberUpdateWindow.mainloop()

			def openEmailIdUpdateWindow () :
				emailIdUpdateWindow = Tk()
				emailIdUpdateWindow.title('Update Email ID')
				emailIdUpdateLabel = ttk.Label(emailIdUpdateWindow, text='Email ID')
				emailIdUpdateLabel.grid()
				emailIdUpdateEntry = ttk.Entry(emailIdUpdateWindow)
				emailIdUpdateEntry.grid()
				emailIdUpdateButton = ttk.Button(emailIdUpdateWindow, text='Update')
				emailIdUpdateButton.grid()
				emailIdUpdateWindow.mainloop()

			fnameUpdate2Button = ttk.Button(updateFrame2, text='First Name', command=openFnameUpdateWindow)
			fnameUpdate2Button.grid()
			lnameUpdate2Button = ttk.Button(updateFrame2, text='Last Name', command=openLnameUpdateWindow)
			lnameUpdate2Button.grid()
			classNameUpdate2Button = ttk.Button(updateFrame2, text='Class Name', command=openClassNameUpdateWindow)
			classNameUpdate2Button.grid()
			rollNumberUpdate2Button = ttk.Button(updateFrame2, text='Roll no.', command=openRollNumberUpdateWindow)
			rollNumberUpdate2Button.grid()
			projectNameUpdate2Button = ttk.Button(updateFrame2, text='Project Name', command=openProjectNameUpdateWindow)
			projectNameUpdate2Button.grid()
			contactNumberUpdate2Button = ttk.Button(updateFrame2, text='Contact no.', command=openContactNumberUpdateWindow)
			contactNumberUpdate2Button.grid()
			emailIdUpdate2Button = ttk.Button(updateFrame2, text='Email ID', command=openEmailIdUpdateWindow)
			emailIdUpdate2Button.grid()

		updateFrame2.grid()


	okkkkkUpdateButton = ttk.Button(updateFrame, text='Okkkkk', command=openUpdateFrame3)
	okkkkkUpdateButton.grid(row='7', columnspan='2')
	updateFrame.grid()



def openDeleteFrame () :
	if (viewFrame) :
		viewFrame.grid_forget()
	if (insertFrame) :
		insertFrame.grid_forget()
	if (updateFrame) :
		updateFrame.grid_forget()
	if (updateFrame2) :
		updateFrame2.grid_forget()
	fnameDeleteLabel= ttk.Label(deleteFrame, text='First Name')
	fnameDeleteLabel.grid(row='0', column='0')
	fnameDeleteEntry = ttk.Entry(deleteFrame)
	fnameDeleteEntry.grid(row='0', column='1')

	lnameDeleteLabel= ttk.Label(deleteFrame, text='Last Name')
	lnameDeleteLabel.grid(row='1', column='0')
	lnameDeleteEntry = ttk.Entry(deleteFrame)
	lnameDeleteEntry.grid(row='1', column='1')

	classNameDeleteLabel= ttk.Label(deleteFrame, text='Class Name')
	classNameDeleteLabel.grid(row='2', column='0')
	classNameDeleteEntry = ttk.Entry(deleteFrame)
	classNameDeleteEntry.grid(row='2', column='1')

	rollNumberDeleteLabel= ttk.Label(deleteFrame, text='Roll No')
	rollNumberDeleteLabel.grid(row='3', column='0')
	rollNumberDeleteEntry = ttk.Entry(deleteFrame)
	rollNumberDeleteEntry.grid(row='3', column='1')


	def deleteFromDB () :
		fnameDeleteFrameValue = fnameDeleteEntry.get().lower()
		lnameDeleteFrameValue = lnameDeleteEntry.get().lower()
		classNameDeleteFrameValue = classNameDeleteEntry.get().lower()
		rollNumberDeleteFrameValue = rollNumberDeleteEntry.get()

		if (fnameDeleteFrameValue!='' and lnameDeleteFrameValue!='' and
				classNameDeleteFrameValue!='' and rollNumberDeleteFrameValue!='') :
			cursor.execute (""" DELETE
													FROM ORIGIN
													WHERE FNAME=%s AND
																LNAME=%s AND
																CLASS=%s AND
																ROLLNO=%s """,
												(fnameDeleteFrameValue, lnameDeleteFrameValue, classNameDeleteFrameValue, rollNumberDeleteFrameValue))
			connection.commit()
			fnameDeleteEntry.delete(0, 'end')
			lnameDeleteEntry.delete(0, 'end')
			classNameDeleteEntry.delete(0, 'end')
			rollNumberDeleteEntry.delete(0, 'end')
		else:
			connection.rollback()

	deleteDeleteButton = ttk.Button(deleteFrame, text='Delete', command=deleteFromDB)
	deleteDeleteButton.grid(row='4', columnspan='2')
	deleteFrame.grid()



menubar = Menu(mainWindow)
menubar.add_command(label='View', command=openViewFrame)
menubar.add_command(label='Insert', command=openInsertFrame)
menubar.add_command(label='Update', command=openUpdateFrame)
menubar.add_command(label='Delete', command=openDeleteFrame)
mainWindow.config(menu=menubar)
 


mainWindow.mainloop()
connection.close()