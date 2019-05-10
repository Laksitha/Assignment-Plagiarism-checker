# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainDialog_APC.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import subprocess
import mysql.connector
import gensim
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import numpy
import pandas as pd

######################## database connector #########################################################
con = mysql.connector.connect(user='laksitha', password='1234',
                              host='localhost', port='3306', database='final_project')
######################################################################################################

class Ui_APC_MainDIalog(object):
    def setupUi(self, APC_MainDIalog):
        APC_MainDIalog.setObjectName("APC_MainDIalog")
        APC_MainDIalog.resize(834, 591)
        APC_MainDIalog.setAutoFillBackground(False)
        APC_MainDIalog.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:pad, x1:0.501, y1:0.329955, x2:0.506, y2:0, stop:0 rgba(82, 0, 0, 239), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.tabWidget = QtWidgets.QTabWidget(APC_MainDIalog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 811, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
########################################################################################################
######## input Tab ###################################################################################
########################################################################################################
        self.Subject_select_lable = QtWidgets.QLabel(self.tab_1)
        self.Subject_select_lable.setGeometry(QtCore.QRect(10, 20, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Subject_select_lable.setFont(font)
        self.Subject_select_lable.setTextFormat(QtCore.Qt.AutoText)
        self.Subject_select_lable.setObjectName("Subject_select_lable")
        self.Subject_select_combo = QtWidgets.QComboBox(self.tab_1)
        self.Subject_select_combo.setGeometry(QtCore.QRect(160, 20, 241, 22))
        self.Subject_select_combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Subject_select_combo.setCurrentText("")
        self.Subject_select_combo.setObjectName("Subject_select_combo")
        ### Get subjects from database ###
        query1 = "SELECT subjects FROM new_subject"
        mycursor1 = con.cursor()
        mycursor1.execute(query1)
        dl1 = mycursor1.fetchall()
        for item in dl1:
                self.Subject_select_combo.addItem(item[0])

        con.commit()
        mycursor1.close()

##############################################################################################
######## Select Year Label And Combo Box #####################################################
        self.Year_lable = QtWidgets.QLabel(self.tab_1)
        self.Year_lable.setGeometry(QtCore.QRect(10, 60, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Year_lable.setFont(font)
        self.Year_lable.setTextFormat(QtCore.Qt.AutoText)
        self.Year_lable.setObjectName("Year_lable")
        self.Year_select_combo = QtWidgets.QComboBox(self.tab_1)
        self.Year_select_combo.setGeometry(QtCore.QRect(160, 60, 241, 22))
        self.Year_select_combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Year_select_combo.setObjectName("Year_select_combo")
        self.Year_select_combo.addItem("")
        self.Year_select_combo.addItem("")
        self.Year_select_combo.addItem("")
        self.Year_select_combo.addItem("")
#######################################################################################
######## Select Semester Combo Box and LAbel ##########################################
        self.Semester_select_combo = QtWidgets.QComboBox(self.tab_1)
        self.Semester_select_combo.setGeometry(QtCore.QRect(160, 100, 241, 22))
        self.Semester_select_combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Semester_select_combo.setObjectName("Semester_select_combo")
        self.Semester_select_combo.addItem("")
        self.Semester_select_combo.addItem("")
        self.Semester_label = QtWidgets.QLabel(self.tab_1)
        self.Semester_label.setGeometry(QtCore.QRect(10, 100, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Semester_label.setFont(font)
        self.Semester_label.setTextFormat(QtCore.Qt.AutoText)
        self.Semester_label.setObjectName("Semester_label")
####################################################################################
        self.line_2 = QtWidgets.QFrame(self.tab_1)
        self.line_2.setGeometry(QtCore.QRect(410, 10, 21, 121))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
####################################################################################
######## Select Add new Subject LAbel , Line Edit and Save buttn ###################
        self.AddNewSub_lable = QtWidgets.QLabel(self.tab_1)
        self.AddNewSub_lable.setGeometry(QtCore.QRect(430, 20, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.AddNewSub_lable.setFont(font)
        self.AddNewSub_lable.setTextFormat(QtCore.Qt.AutoText)
        self.AddNewSub_lable.setObjectName("AddNewSub_lable")
        self.Addnew_lineedit = QtWidgets.QLineEdit(self.tab_1)
        self.Addnew_lineedit.setGeometry(QtCore.QRect(560, 20, 231, 21))
        self.Addnew_lineedit.setObjectName("Addnew_lineedit")
        self.Save_new_sub_buttton = QtWidgets.QPushButton(self.tab_1)
        self.Save_new_sub_buttton.setGeometry(QtCore.QRect(560, 50, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.Save_new_sub_buttton.setFont(font)
        self.Save_new_sub_buttton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Save_new_sub_buttton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.535, y1:0.489045, x2:0.017, y2:0.0170455, stop:0 rgba(0, 85, 127, 239), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.Save_new_sub_buttton.setAutoDefault(False)
        self.Save_new_sub_buttton.setObjectName("Save_new_sub_buttton")

        self.Save_new_sub_buttton.clicked.connect(self.Add_new_Subject)

#############################################################################################
######## Assignment Name label and Line edit ################################################
        self.Assignment_name_label = QtWidgets.QLabel(self.tab_1)
        self.Assignment_name_label.setGeometry(QtCore.QRect(10, 150, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Assignment_name_label.setFont(font)
        self.Assignment_name_label.setTextFormat(QtCore.Qt.AutoText)
        self.Assignment_name_label.setObjectName("Assignment_name_label")
        self.Assignment_name_Lineedit = QtWidgets.QLineEdit(self.tab_1)
        self.Assignment_name_Lineedit.setGeometry(QtCore.QRect(190, 150, 361, 21))
        self.Assignment_name_Lineedit.setObjectName("Assignment_name_Lineedit")
############################################################################################
######## Select files button ##############################################################
        self.Select_files_button = QtWidgets.QPushButton(self.tab_1)
        self.Select_files_button.setGeometry(QtCore.QRect(570, 190, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.Select_files_button.setFont(font)
        self.Select_files_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Select_files_button.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.535, y1:0.489045, x2:0.017, y2:0.0170455, stop:0 rgba(0, 85, 127, 239), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.Select_files_button.setAutoDefault(False)
        self.Select_files_button.setObjectName("Select_files_button")

        self.Select_files_button.clicked.connect(self.SelectFiles)

#############################################################################################
######## Save slected Assignments to the db #################################################
        self.Save_files_button = QtWidgets.QPushButton(self.tab_1)
        self.Save_files_button.setGeometry(QtCore.QRect(570, 230, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.Save_files_button.setFont(font)
        self.Save_files_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Save_files_button.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.535, y1:0.489045, x2:0.017, y2:0.0170455, stop:0 rgba(0, 85, 127, 239), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.Save_files_button.setAutoDefault(False)
        self.Save_files_button.setObjectName("Save_files_button")

        self.Save_files_button.clicked.connect(self.Save_Assignments)

###################################################################################################
######## Flie List Widget #########################################################################
        self.File_listWidget = QtWidgets.QListWidget(self.tab_1)
        self.File_listWidget.setGeometry(QtCore.QRect(10, 190, 541, 331))
        self.File_listWidget.setObjectName("File_listWidget")
#####################################################################################################
######## Submit button ##############################################################################
        self.Submit = QtWidgets.QPushButton(self.tab_1)
        self.Submit.setGeometry(QtCore.QRect(570, 150, 141, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.Submit.setFont(font)
        self.Submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Submit.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.535, y1:0.489045, x2:0.017, y2:0.0170455, stop:0 rgba(0, 85, 127, 239), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.Submit.setAutoDefault(False)
        self.Submit.setObjectName("Submit")

        self.Submit.clicked.connect(self.Submit_data_assignment)

########################################################################################################
######## Process Tab ###################################################################################
########################################################################################################
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
######## Process Select subject Label , Combo box #######################
        self.Process_SlectSub_label = QtWidgets.QLabel(self.tab_2)
        self.Process_SlectSub_label.setGeometry(QtCore.QRect(20, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Process_SlectSub_label.setFont(font)
        self.Process_SlectSub_label.setObjectName("Process_SlectSub_label")
        self.Process_SelctSub_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.Process_SelctSub_comboBox.setGeometry(QtCore.QRect(150, 20, 231, 21))
        self.Process_SelctSub_comboBox.setObjectName("Process_SelctSub_comboBox")
        ## selct subject via database ##
        query5 = "SELECT subjects FROM new_subject"
        mycursor5 = con.cursor()
        mycursor5.execute(query5)
        dl1 = mycursor5.fetchall()
        for item in dl1:
                self.Process_SelctSub_comboBox.addItem(item[0])

        con.commit()
        mycursor5.close()

#######################################################################################################
######## Process Select year combo box and label ######################################################
        self.Process_SelctYear_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.Process_SelctYear_comboBox.setGeometry(QtCore.QRect(150, 60, 231, 21))
        self.Process_SelctYear_comboBox.setObjectName("Process_SelctYear_comboBox")
        self.Process_SelctYear_comboBox.addItem("")
        self.Process_SelctYear_comboBox.addItem("")
        self.Process_SelctYear_comboBox.addItem("")
        self.Process_SelctYear_comboBox.addItem("")
        self.Process_SlectSub_label_2 = QtWidgets.QLabel(self.tab_2)
        self.Process_SlectSub_label_2.setGeometry(QtCore.QRect(20, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Process_SlectSub_label_2.setFont(font)
        self.Process_SlectSub_label_2.setObjectName("Process_SlectSub_label_2")
##################################################################################################
######## Process Select Assignment name combo box ################################################
        self.Process_SlectAssign_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.Process_SlectAssign_comboBox.setGeometry(QtCore.QRect(200, 120, 301, 21))
        self.Process_SlectAssign_comboBox.setObjectName("Process_SlectAssign_comboBox")
        self.Process_SlectSub_label_4 = QtWidgets.QLabel(self.tab_2)
        self.Process_SlectSub_label_4.setGeometry(QtCore.QRect(20, 120, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Process_SlectSub_label_4.setFont(font)
        self.Process_SlectSub_label_4.setObjectName("Process_SlectSub_label_4")
########################################################################################################
######## Process button #############################################################################
        self.Process_Button = QtWidgets.QPushButton(self.tab_2)
        self.Process_Button.setGeometry(QtCore.QRect(530, 170, 161, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.Process_Button.setFont(font)
        self.Process_Button.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.535, y1:0.489045, x2:0.017, y2:0.0170455, stop:0 rgba(0, 85, 127, 239), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.Process_Button.setAutoDefault(False)
        self.Process_Button.setObjectName("Process_Button")

        self.Process_Button.clicked.connect(self.Process)
##########################################################################################################
########### Load Assignmets names to the Assignment combobox ###########################################
        self.Process_Load_assignment_names = QtWidgets.QPushButton(self.tab_2)
        self.Process_Load_assignment_names.setGeometry(QtCore.QRect(530, 40, 161, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.Process_Load_assignment_names.setFont(font)
        self.Process_Load_assignment_names.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Process_Load_assignment_names.setToolTipDuration(-1)
        self.Process_Load_assignment_names.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.535, y1:0.489045, x2:0.017, y2:0.0170455, stop:0 rgba(0, 85, 127, 239), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.Process_Load_assignment_names.setAutoDefault(False)
        self.Process_Load_assignment_names.setObjectName("Process_Load_assignment_names")

        self.Process_Load_assignment_names.clicked.connect(self.Load_Assignment_names)

#######################################################################################################
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(410, 10, 46, 71))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.label.setFont(font)
        self.label.setObjectName("label")
########################################################################################################
################ Load Assignments to the list Widgets ##################################################
        self.Process_Load_Assignments = QtWidgets.QPushButton(self.tab_2)
        self.Process_Load_Assignments.setGeometry(QtCore.QRect(530, 120, 161, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.Process_Load_Assignments.setFont(font)
        self.Process_Load_Assignments.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0.535, y1:0.489045, x2:0.017, y2:0.0170455, stop:0 rgba(0, 85, 127, 239), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.Process_Load_Assignments.setAutoDefault(False)
        self.Process_Load_Assignments.setObjectName("Process_Load_Assignments")

        self.Process_Load_Assignments.clicked.connect(self.Load_Assignments_ListWidget)

#####################################################################################################
######## List Widget ###############################################################################
        self.Process_File_listWidget = QtWidgets.QListWidget(self.tab_2)
        self.Process_File_listWidget.setGeometry(QtCore.QRect(20, 160, 481, 371))
        self.Process_File_listWidget.setObjectName("Process_File_listWidget")
######################################################################################################
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(APC_MainDIalog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(APC_MainDIalog)

#######################################################################################################
################################ Functions of the input data tab ######################################
#######################################################################################################
## Funtions for select files and add in to the listWidgets ##

    def SelectFiles(self):
            self.getFileNames, _filter = QtWidgets.QFileDialog.getOpenFileNames(
                None, 'Open File Names', filter='Text Files(*.txt)')
            print(self.getFileNames)
            print(type(self.getFileNames))
            self.File_listWidget.addItems(self.getFileNames)

## Function for Add New Subject ##

    def Add_new_Subject(self):
            NewSubject = self.Addnew_lineedit.text()
            #print(NewSubject)
            Query2 = "INSERT INTO new_subject (subjects) VALUES('" + \
                str(NewSubject)+"')"
            mycursor2 = con.cursor()
            mycursor2.execute(Query2)
            con.commit()
            mycursor2.close()
            print("save data to database")
            self.Addnew_lineedit.clear()

## Function for add data of Assignment ##

    def Submit_data_assignment(self):
            SubCode = self.Subject_select_combo.currentText()
            SelcYear = self.Year_select_combo.currentText()
            SelcSem = self.Semester_select_combo.currentText()
            AssignName = self.Assignment_name_Lineedit.text()

            Query3 = "INSERT INTO input_data(subjects,cam_year,semester,assing_name) VALUES('"+str(
                SubCode)+"','"+str(SelcYear)+"','"+str(SelcSem)+"','"+str(AssignName)+"')"
            mycursor3 = con.cursor()
            mycursor3.execute(Query3)
            con.commit()
            mycursor3.close()
            print("save data to database")

## Function for save selected assignments ##

    def Save_Assignments(self):
            AssignNames = self.Assignment_name_Lineedit.text()
            Files = self.getFileNames
            subcode=self.Subject_select_combo.currentText()

            query4 = "INSERT INTO assignment(subjects,varassign_name,assignments) VALUES('"+str(subcode)+"','"+str(
                AssignNames)+"',%s)"
            mycursor4 = con.cursor()
            mycursor4.executemany(query4, [(r,) for r in Files])
            con.commit()
            mycursor4.close()
            print("save")
            self.File_listWidget.clear()

####################################################################################################
################################## Function of process tab #########################################
####################################################################################################

        ## Load assignment name to the assignmemt combobox ##
    def Load_Assignment_names(self):
            PSelcSub = self.Process_SelctSub_comboBox.currentText()
            PSelcYear = self.Process_SelctYear_comboBox.currentText()
            self.Process_SlectAssign_comboBox.clear()

            query6 = """SELECT assing_name FROM input_data WHERE subjects='%s' AND cam_year='%s'""" % (
                PSelcSub, PSelcYear)
            mycursor6 = con.cursor()
            mycursor6.execute(query6)
            dl2 = mycursor6.fetchall()
            for item in dl2:
                    self.Process_SlectAssign_comboBox.addItem(item[0])
            con.commit()
            mycursor6.close()
            self.Process_File_listWidget.clear()

    ## load assignments to the listwidgets ##
    def Load_Assignments_ListWidget(self):
            PrSelAssign=self.Process_SlectAssign_comboBox.currentText()
            self.Process_File_listWidget.clear()
            subcode=self.Process_SelctSub_comboBox.currentText()

            query7="""SELECT assignments from assignment WHERE varassign_name='%s' AND subjects='%s'"""%(PrSelAssign,subcode)
            mycursor7=con.cursor()
            mycursor7.execute(query7)
            self.dl3=mycursor7.fetchall()
            print(type(self.dl3))
            for item in self.dl3:
                    self.Process_File_listWidget.addItem(item[0])
            con.commit()
            mycursor7.close()

     ## process button to create the similarity matrix 
    def Process(self):
            
            items=[]## get ites as an objects
            for x in range(self.Process_File_listWidget.count()):
                    items.append(self.Process_File_listWidget.item(x))

            print(items)
            row=[i.text() for i in items] ## converted in to the
            print(row)
            out = []
            for t in row:
                file=open(t,"rb").read()
                files = file.decode("utf-8", errors="ignore").replace("\r\n","")
                out.append(files)
                #print(type(files))
            
            print(out) 
            gen_docs = [[w.lower() for w in word_tokenize(text)]
                    for text in out]
            #print(gen_docs)
            dictionary = gensim.corpora.Dictionary(gen_docs)

            corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]

            similarity_matrix = []
            index = gensim.similarities.MatrixSimilarity(corpus)
            #print(index)
            for sims in index:
                similarity_matrix.append(sims)
            similarity_array = numpy.array(similarity_matrix)
            #print(similarity_matrix)

            print(similarity_array)

            df = pd.DataFrame(similarity_array)
            #df.columns = ["file1", "file2", "file3"]
            print(df)
            print(type(df))
            


####################################################################################################
    def retranslateUi(self, APC_MainDIalog):
        _translate = QtCore.QCoreApplication.translate
        APC_MainDIalog.setWindowTitle(_translate("APC_MainDIalog", "Assignment Plagiarism Checker"))
        self.Subject_select_lable.setText(_translate("APC_MainDIalog", "Select Subject Here :"))
        self.Year_lable.setText(_translate("APC_MainDIalog", "Year :"))
        self.Year_select_combo.setItemText(0, _translate("APC_MainDIalog", "1st Year"))
        self.Year_select_combo.setItemText(1, _translate("APC_MainDIalog", "2nd Year"))
        self.Year_select_combo.setItemText(2, _translate("APC_MainDIalog", "3rd Year"))
        self.Year_select_combo.setItemText(3, _translate("APC_MainDIalog", "4th Year"))
        self.Semester_select_combo.setItemText(0, _translate("APC_MainDIalog", "1st Semester"))
        self.Semester_select_combo.setItemText(1, _translate("APC_MainDIalog", "2nd Semester"))
        self.Semester_label.setText(_translate("APC_MainDIalog", "Semester :"))
        self.AddNewSub_lable.setText(_translate("APC_MainDIalog", "Add New Subject :"))
        self.Addnew_lineedit.setPlaceholderText(_translate("APC_MainDIalog", "Input New Subject Name Here...."))
        self.Save_new_sub_buttton.setToolTip(_translate("APC_MainDIalog", "Save New Subject Code"))
        self.Save_new_sub_buttton.setText(_translate("APC_MainDIalog", "Save"))
        self.Assignment_name_label.setText(_translate("APC_MainDIalog", "Input Assignment Name :"))
        self.Assignment_name_Lineedit.setPlaceholderText(_translate("APC_MainDIalog", "Input Assignment name Here..."))
        self.Select_files_button.setToolTip(_translate("APC_MainDIalog", "Select Assignments"))
        self.Select_files_button.setText(_translate("APC_MainDIalog", "Select Files Here"))
        self.Save_files_button.setToolTip(_translate("APC_MainDIalog", "Save selected Assignments"))
        self.Save_files_button.setText(_translate("APC_MainDIalog", "Save Files"))
        self.Submit.setToolTip(_translate("APC_MainDIalog", "Save the assignment data"))
        self.Submit.setText(_translate("APC_MainDIalog", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("APC_MainDIalog", "Input Files Here"))
        self.Process_SlectSub_label.setText(_translate("APC_MainDIalog", "Select Subject :"))
        self.Process_SelctYear_comboBox.setItemText(0, _translate("APC_MainDIalog", "1st Year"))
        self.Process_SelctYear_comboBox.setItemText(1, _translate("APC_MainDIalog", "2nd Year"))
        self.Process_SelctYear_comboBox.setItemText(2, _translate("APC_MainDIalog", "3rd Year"))
        self.Process_SelctYear_comboBox.setItemText(3, _translate("APC_MainDIalog", "4th Year"))
        self.Process_SlectSub_label_2.setText(_translate("APC_MainDIalog", "Select Year :"))
        self.Process_SlectSub_label_4.setText(_translate("APC_MainDIalog", "Select Assignment Topic :"))
        self.Process_Button.setToolTip(_translate("APC_MainDIalog", "Process"))
        self.Process_Button.setText(_translate("APC_MainDIalog", "Process"))
        self.Process_Load_assignment_names.setToolTip(_translate("APC_MainDIalog", "After selecting Subject and Year"))
        self.Process_Load_assignment_names.setText(_translate("APC_MainDIalog", "Load Assignment Names"))
        self.label.setText(_translate("APC_MainDIalog", "}"))
        self.Process_Load_Assignments.setToolTip(_translate("APC_MainDIalog", "Display assignments under the assignmet name"))
        self.Process_Load_Assignments.setText(_translate("APC_MainDIalog", "Display Assignments"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("APC_MainDIalog", "Precess Here"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    APC_MainDIalog = QtWidgets.QDialog()
    ui = Ui_APC_MainDIalog()
    ui.setupUi(APC_MainDIalog)
    APC_MainDIalog.show()
    sys.exit(app.exec_())
