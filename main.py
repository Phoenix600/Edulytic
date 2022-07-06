# import your modules here 
import pandas as pd
import smtplib as smt
from tkinter import *
import subprocess as sp
from replit import clear
import matplotlib.pyplot as plt

# define class here 

class DataBase():
	# def __init__(self):
	# 	print("List of Data base files : ")
	# 	sp.call("ls | grep .csv",shell=True)
	# 	self.filename = input("[+]Select the DataBase : ")
	# 	self.DataBase = pd.read_csv(self.filename)	
	

	def intro(self):
		clear()
		self.logo = r"""
=========================================================
██████╗░██████╗░░██████╗░░░██╗░░░██╗██████╗░
██╔══██╗██╔══██╗██╔════╝░░░██║░░░██║╚════██╗
██║░░██║██████╦╝╚█████╗░░░░╚██╗░██╔╝░░███╔═╝
██║░░██║██╔══██╗░╚═══██╗░░░░╚████╔╝░██╔══╝░░
██████╔╝██████╦╝██████╔╝██╗░░╚██╔╝░░███████╗
╚═════╝░╚═════╝░╚═════╝░╚═╝░░░╚═╝░░░╚══════╝
=========================================================
Welcome to DBS program analize your data base : 
=========================================================
		"""
		print(self.logo)

	def PrintDataBase(self,dataFrame):
		self.dataFrame = dataFrame
		print(self.dataFrame)


	def OpenDataBase(self):
		print("Listing the available database files")
		sp.call("ls | grep .csv",shell=True)
		self.filename  = input("[+]Select the database to open and analize : ")
		self.dataFrame = pd.read_csv(self.filename)
		self.PrintDataBase(self.dataFrame)


		def DataVisualize(self):
			OpenDataBase()
			print(self.dataFrame)

	def Menu(self):
		self.intro()

		self.choice = int(0)
		print("""
=========================================================
[+]Enter the key to do the following oprations :
========================================================= 
[01]	Open Data Base
[02]	Visualize the DataBase
[03]	Update Tool
[04]	System Check 
[05]	Exit
=========================================================
			""")
		self.choice = input("[+]Select the following key :")

		if self.choice == 1 :
			self.OpenDataBase()
		elif self.choice == 2 :
			self.DataVisualize()
		else :
			pass

# write main code here 
if __name__ == "__main__":
	
	# Creating the DataBase object 
	Employee = DataBase()
	# Testing the methods 
	Employee.intro()
	Employee.OpenDataBase()
	Employee.Menu()

	# DataBase = getDataBase
	# DataBase = DataBase()
	# DataBase.intro()
	# Database.getDataBase() 

