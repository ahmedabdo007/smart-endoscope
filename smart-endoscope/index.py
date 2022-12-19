from PyQt5 import QtCore, QtGui, QtWidgets 
#from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from xlsxwriter import *
import xlrd  
import sys
import second_design
import MySQLdb
import os
import os.path
from fpdf import FPDF


#from PyQt5.uic import loadUiType
#MainUI,_ =loadUiType('second_design.ui')

report_patient_list = []
doctor_list = []
patient_list = []

class ExampleApp(QtWidgets.QMainWindow, second_design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.DB_connection()
        self.Handle_button()
        self.UI_changes()

        self.open_login_tab()
        
        self.Show_All_patient()
        self.Show_All_patient_Archive()

        self.Show_All_Doctors()
        self.show_sepcialization()

        self.show_doctor_investigation()
        self.show_patient_investigation()

        self.show_all_admin()


        self.db_report_autocomplete('name','patient',report_patient_list)
        self.report_auto_complete_edit(report_patient_list)

        self.db_report_autocomplete('name','doctor',doctor_list)
        self.doctor_auto_complete_edit(doctor_list)

        self.db_report_autocomplete('name','patient',patient_list)
        self.patient_auto_complete_edit(patient_list)

    def UI_changes(self):
        self.tabWidget.tabBar().setVisible(False)


    def DB_connection(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='root',db='endscop')
        self.cur = self.db.cursor()

        print("connection accepted")

    def Handle_button(self):
        self.pushButton_20.clicked.connect(self.open_investegation_tab)
        self.pushButton_19.clicked.connect(self.open_patients_tab)
        self.pushButton_5.clicked.connect(self.open_doctors_tab)
        self.pushButton_39.clicked.connect(self.open_reports_tab)
        self.pushButton_6.clicked.connect(self.open_Archives_tab)
        self.pushButton_29.clicked.connect(self.open_setting_tab)

        self.pushButton_21.clicked.connect(self.log_in)
        self.pushButton_26.clicked.connect(self.open_login_tab)

        self.pushButton_12.clicked.connect(self.open_camera)

        self.pushButton_7.clicked.connect(self.Add_new_patient)
        self.pushButton_9.clicked.connect(self.Edit_patient_search)
        self.pushButton_8.clicked.connect(self.edit_patient)
        self.pushButton_10.clicked.connect(self.delete_patient)
        self.pushButton_41.clicked.connect(self.export_patient)
        self.pushButton_51.clicked.connect(self.return_patient_again)
        self.pushButton_52.clicked.connect(self.return_patient_again_search)

        self.pushButton_16.clicked.connect(self.Add_new_Doctor)
        self.pushButton_42.clicked.connect(self.Edit_Doctor_search)
        self.pushButton_14.clicked.connect(self.edit_doctor)
        self.pushButton_13.clicked.connect(self.delete_Doctor)
        self.pushButton_4.clicked.connect(self.show_patient_filter)
        self.pushButton_15.clicked.connect(self.show_doctor_filter)
        self.pushButton_18.clicked.connect(self.export_doctor)


        self.pushButton_104.clicked.connect(self.add_admin)
        self.pushButton.clicked.connect(self.add_sepcialization)

        self.pushButton_22.clicked.connect(self.add_patient_report_search)

        self.pushButton_27.clicked.connect(self.open_resetPass_tab)

        self.pushButton_11.clicked.connect(self.handle_report)

        

        
    #def openFile(self):  
     #   fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'OpenFile',"", "Excel (*.xls *.xlsx)")
      #  df = pandas.read_excel(fileName)

    
    def log_in(self):

        user_name = self.lineEdit_11.text()
        password = self.lineEdit_16.text()
        
        self.cur.execute('''
        SELECT name ,password FROM admin
        ''')
        data = self.cur.fetchall()

        for row in data:
            if row[0]==user_name and row[1]==password:
                self.groupBox_15.setEnabled(True)
                self.lineEdit_11.clear()
                self.lineEdit_16.clear()
                self.open_investegation_tab()
        
    
    def reset_password(self):
        pass

###################################################################
################auto complete######################################
    def db_report_autocomplete(self,col_name,table_name,list_name):
        list_name.clear()
        sql = 'SELECT '+col_name+' FROM '+table_name
        self.cur.execute(sql)
        names =self.cur.fetchall() 
        for name in names:
            list_name.append(name[0])
    
    def report_auto_complete(self , model ,table_list):
        model.setStringList(table_list)
    
    
    def report_auto_complete_edit(self,table_list):
        names_line_edit = self.lineEdit_15
        completer = QtWidgets.QCompleter()
        names_line_edit.setCompleter(completer)
        model = QtCore.QStringListModel()
        completer.setModel(model)
        self.report_auto_complete(model,table_list)
    ###################
    def doctor_auto_complete_edit(self,table_list):
        names_line_edit = self.lineEdit_18
        completer = QtWidgets.QCompleter()
        names_line_edit.setCompleter(completer)
        model = QtCore.QStringListModel()
        completer.setModel(model)
        self.report_auto_complete(model,table_list)
    ###################
    def patient_auto_complete_edit(self,table_list):
        names_line_edit = self.lineEdit_10
        completer = QtWidgets.QCompleter()
        names_line_edit.setCompleter(completer)
        model = QtCore.QStringListModel()
        completer.setModel(model)
        self.report_auto_complete(model,table_list)

    

    #####################Patients##########################
    def Show_All_patient(self):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        self.cur.execute('''
        SELECT National_id,name ,age,gender,phone,address,sergarydate FROM patient
        ''')

        data = self.cur.fetchall()
        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_2.setItem(row , col, QtWidgets.QTableWidgetItem(str(item)))
                col +=1
            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

    def show_patient_filter(self):
        patient_national_id = self.lineEdit_2.text()
        sql = '''SELECT  National_id,name,gender,age,phone,address,sergarydate FROM patient WHERE National_id LIKE %s'''
        self.cur.execute(sql,[("%" +patient_national_id+ "%",)])
        data = self.cur.fetchall()
        print(data)
            

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)
        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_2.setItem(row , col, QtWidgets.QTableWidgetItem(str(item)))
                col +=1
            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)


    def Show_All_patient_Archive(self):
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)
        self.cur.execute('''
        SELECT national_id,name ,age,gender,phone,address,sergarydate FROM archive
        ''')
        data = self.cur.fetchall()
        for row , form in enumerate(data):
            
            for col , item in enumerate(form):
                self.tableWidget_5.setItem(row , col, QtWidgets.QTableWidgetItem(str(item)))
                col +=1
            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

    def return_patient_again_search(self):
        pat_national_id=self.lineEdit_67.text()
        sql = ''' SELECT * FROM archive WHERE national_id  LIKE %s'''

        self.cur.execute(sql,[("%" +pat_national_id+ "%",)])
        data = self.cur.fetchone()

        self.lineEdit_66.setText(data[1])
        self.lineEdit_65.setText(data[2])
        self.dateEdit_9.setDate(data[5])
        self.lineEdit_62.setText(data[7])
        self.lineEdit_64.setText(data[6])
        self.lineEdit_63.setText(str(data[3]))
        #self.textEdit_10.setPlainText(data[8])
        self.comboBox_14.setCurrentText((data[4]))

    
    def return_patient_again(self):
        patient_name = self.lineEdit_65.text()
        patine_national_id = self.lineEdit_66.text()
        date_sergey = self.dateEdit_9.date().toString("yyyy-MM-dd")
        phone_no = self.lineEdit_62.text()
        address = self.lineEdit_64.text()
        age = self.lineEdit_63.text()
        #gender = self.comboBox_2.currentIndex()
        gender = self.comboBox_14.currentText()
        description = self.textEdit_10.toPlainText()

        self.cur.execute('''INSERT INTO patient (National_id,name , age , gender , sergarydate , address , phone , description) 
        VALUES(%s,%s , %s , %s , %s ,%s ,%s ,%s)
        ''' ,(patine_national_id,patient_name,age,gender,date_sergey,address,phone_no,description) )
        self.db.commit()
        #self.statusBar().showMessage("تم اضافه المريض بنجاح!")
        QtWidgets.QMessageBox.information(self, "Sucess" , "تم استرجاع المريض بنجاح!")
        
        sql_delete = '''DELETE FROM archive WHERE national_id =%s'''
        self.cur.execute(sql_delete,[(patine_national_id)])
        self.db.commit()

        self.Show_All_patient_Archive()
        self.Show_All_patient()

        self.db_report_autocomplete('National_id','patient',patient_list)
        self.patient_auto_complete_edit(patient_list)
        self.show_patient_investigation()   


    def Add_new_patient(self):
        patient_name = self.lineEdit_5.text()
        patine_national_id = self.lineEdit_6.text()
        date_sergey = self.dateEdit.date().toString("yyyy-MM-dd")
        phone_no = self.lineEdit_9.text()
        address = self.lineEdit_8.text()
        age = self.lineEdit_37.text()
        #gender = self.comboBox_2.currentIndex()
        gender = self.comboBox_2.currentText()
        description = self.textEdit_2.toPlainText()

        self.cur.execute('''INSERT INTO patient (National_id,name , age , gender , sergarydate , address , phone , description) 
        VALUES(%s,%s , %s , %s , %s ,%s ,%s ,%s)
        ''' ,(patine_national_id,patient_name,age,gender,date_sergey,address,phone_no,description) )
        self.db.commit()
        #self.statusBar().showMessage("تم اضافه المريض بنجاح!")
        QtWidgets.QMessageBox.information(self, "Sucess" , "تم اضافه المريض بنجاح!")
        self.Show_All_patient()

        self.db_report_autocomplete('National_id','patient',patient_list)
        self.patient_auto_complete_edit(patient_list)
        self.show_patient_investigation()

    
    def Edit_patient_search(self):
        pat_national_id=self.lineEdit_10.text()
        sql = ''' SELECT * FROM patient WHERE National_id  LIKE %s'''

        self.cur.execute(sql,[("%" +pat_national_id+ "%",)])
        data = self.cur.fetchone()
        

        self.lineEdit_12.setText(data[2])
        self.lineEdit_35.setText(data[1])
        self.dateEdit_2.setDate(data[5])
        self.lineEdit_14.setText(data[7])
        self.lineEdit_13.setText(data[6])
        self.lineEdit_39.setText(str(data[3]))
        self.textEdit.setPlainText(data[8])
        self.comboBox_4.setCurrentText((data[4]))

    def edit_patient(self):
        patient_name = self.lineEdit_12.text()
        patient_national_id = self.lineEdit_35.text()
        date_sergey = self.dateEdit_2.date().toString("yyyy-MM-dd")
        phone_no = self.lineEdit_14.text()
        address = self.lineEdit_13.text()
        age = self.lineEdit_39.text()
        gender = self.comboBox_4.currentText()
        description = self.textEdit.toPlainText()

        self.cur.execute('''
        UPDATE patient SET National_id=%s,name=%s,age=%s,gender=%s,sergarydate=%s,address=%s,phone=%s,description=%s WHERE National_id=%s
        ''',(patient_national_id,patient_name,age,gender,date_sergey,address,phone_no,description,patient_national_id))

        self.db.commit()
        #self.statusBar().showMessage("تم تعديل المعلومات بنجاح!")
        QtWidgets.QMessageBox.information(self, "Sucess" , "تم تعديل المعلومات بنجاح!")

        self.Show_All_patient()

    def delete_patient(self):
        patient_data = self.lineEdit_10.text()

        patient_name = self.lineEdit_12.text()
        patient_national_id = self.lineEdit_35.text()
        date_sergey = self.dateEdit_2.date().toString("yyyy-MM-dd")
        phone_no = self.lineEdit_14.text()
        address = self.lineEdit_13.text()
        age = self.lineEdit_39.text()
        gender = self.comboBox_4.currentText()

        self.cur.execute('''INSERT INTO archive (National_id,name , age , gender , sergarydate , address , phone ) 
        VALUES(%s,%s , %s , %s , %s ,%s ,%s )
        ''' ,(patient_national_id,patient_name,age,gender,date_sergey,address,phone_no) )
        self.db.commit()
        
        delete_message = QtWidgets.QMessageBox.warning(self,'Delete','Do you want to delete ?',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        if delete_message == QtWidgets.QMessageBox.Yes:     
            sql_delete = '''DELETE FROM patient WHERE National_id =%s'''
            self.cur.execute(sql_delete,[(patient_data)])
            self.db.commit()
            self.statusBar().showMessage("تم مسح المعلومات بنجاح!")

            self.Show_All_patient()
            self.Show_All_patient_Archive()
       
    def export_patient(self):
        self.cur.execute('''SELECT National_id,name ,age,gender,phone,address,sergarydate FROM patient''')
        data = self.cur.fetchall()

        
        excel_file = Workbook('patient_report.xlsx')
        sheet1 = excel_file.add_worksheet()

        sheet1.write(0,0,'National Id')
        sheet1.write(0,1,'Name')
        sheet1.write(0,2,'age')
        sheet1.write(0,3,'gender')
        sheet1.write(0,4,'phone')
        sheet1.write(0,5,'address')
        sheet1.write(0,6,'sergarydate')

        row_number  = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number,column_number,str(item))
                column_number +=1
            row_number +=1
        excel_file.close()

        self.statusBar().showMessage("تم الاستخراج بنجاح!")

    #####################Doctors############################
    def Show_All_Doctors(self):
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)
        self.cur.execute('''
        SELECT national_id,name ,phone,address,specialization_id FROM doctor
        ''')

        data = self.cur.fetchall()
        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_4.setItem(row , col, QtWidgets.QTableWidgetItem(str(item)))
                col +=1
            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)

    def show_doctor_filter(self):
        doctor_national_id = self.lineEdit_4.text()
        

        sql = '''SELECT national_id,name,phone,address,specialization_id FROM doctor WHERE national_id LIKE %s'''
        self.cur.execute(sql,[("%" +doctor_national_id+ "%",)])
        data = self.cur.fetchall()
        print(data)
            #print(patient_name)

        self.tableWidget_4.setRowCount(0)
        self.tableWidget_4.insertRow(0)
        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_4.setItem(row , col, QtWidgets.QTableWidgetItem(str(item)))
                col +=1
            row_position = self.tableWidget_4.rowCount()
            self.tableWidget_4.insertRow(row_position)
    
    def Add_new_Doctor(self):
        
        doctor_name = self.lineEdit_29.text()
        doctor_national_id = self.lineEdit_36.text()
        phone_no = self.lineEdit_32.text()
        address = self.lineEdit_30.text()
        doctor_special = self.comboBox.currentText()


        self.cur.execute('''INSERT INTO doctor (national_id,name , address , phone , specialization_id ) 
        VALUES(%s , %s , %s , %s ,%s)
        ''' ,(doctor_national_id,doctor_name,address,phone_no,doctor_special) )
        self.db.commit()
        #self.statusBar().showMessage("تم اضافه الدكتور بنجاح!")
        QtWidgets.QMessageBox.information(self, "Sucess" , "تم اضافه الدكتور بنجاح!")

        self.Show_All_Doctors()

        self.db_report_autocomplete('national_id','doctor',doctor_list)
        self.doctor_auto_complete_edit(doctor_list)
        self.show_doctor_investigation()

        


    def Edit_Doctor_search(self):
        doc_national_id=self.lineEdit_18.text()
        sql = ''' SELECT * FROM doctor WHERE national_id LIKE %s'''

        self.cur.execute(sql,[("%" +doc_national_id+ "%",)])
        data = self.cur.fetchone()
        

        self.lineEdit_26.setText(data[2])
        self.lineEdit_42.setText(data[1])
        self.lineEdit_28.setText(data[4])
        self.lineEdit_27.setText(data[3])
        self.comboBox_3.setCurrentText((data[5]))
        

    def edit_doctor(self):
        doctor_name = self.lineEdit_26.text()
        doctor_national_id = self.lineEdit_42.text()
        phone_no = self.lineEdit_28.text()
        address = self.lineEdit_27.text()
        doctor_special = self.comboBox_3.currentText()

        self.cur.execute('''
        UPDATE doctor SET national_id=%s,name=%s,address=%s,phone=%s,specialization_id=%s WHERE national_id=%s
        ''',(doctor_national_id,doctor_name,address,phone_no,doctor_special,doctor_national_id))

        self.db.commit()
        sql=''' SELECT * FROM doctor WHERE national_id =%s'''
        self.cur.execute(sql,[doctor_national_id,])
        data = self.cur.fetchone()
        print(data)

        self.db.commit()
        self.statusBar().showMessage("تم تعديل المعلومات بنجاح!")
        QtWidgets.QMessageBox.information(self, "Sucess" , "تم تعديل المعلومات بنجاح!")
        self.Show_All_Doctors()

        

    def delete_Doctor(self):
        doctor_data = self.lineEdit_18.text()
        delete_message = QtWidgets.QMessageBox.warning(self,'Delete','Do you want to delete ?',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        if delete_message == QtWidgets.QMessageBox.Yes:
            sql = '''DELETE FROM doctor WHERE national_id =%s'''
            self.cur.execute(sql,[(doctor_data)])
            self.db.commit()
            self.statusBar().showMessage("تم مسح المعلومات بنجاح!")

            self.Show_All_Doctors()
        

    def export_doctor(self):
        self.cur.execute('''SELECT national_id,name ,phone,address,specialization_id FROM doctor ''')
        data = self.cur.fetchall()

        
        excel_file = Workbook('doctor_report.xlsx')
        sheet1 = excel_file.add_worksheet()

        sheet1.write(0,0,'National Id')
        sheet1.write(0,1,'Name')
        sheet1.write(0,2,'phone')
        sheet1.write(0,3,'address')
        sheet1.write(0,4,'specialization_id')
        

        row_number  = 1
        for row in data:
            column_number = 0
            for item in row:
                sheet1.write(row_number,column_number,str(item))
                column_number +=1
            row_number +=1
        excel_file.close()

        self.statusBar().showMessage("تم الاستخراج بنجاح!")


    #####################investigation############################
    def show_doctor_investigation(self):
        
        self.comboBox_8.clear()
        self.cur.execute('''
        SELECT name FROM doctor
        ''')
        special = self.cur.fetchall()
        for items in special:
            self.comboBox_8.addItem(str(items[0]))

    def show_patient_investigation(self):
        
        self.comboBox_7.clear()
        self.cur.execute('''
        SELECT name FROM patient
        ''')
        special = self.cur.fetchall()
        for items in special:
            self.comboBox_7.addItem(str(items[0]))

        

##########################Reports##############################
###############################################################
    def add_patient_report_search(self):
        pat_national_id=self.lineEdit_15.text()
        sql = ''' SELECT * FROM patient WHERE National_id  LIKE %s'''

        self.cur.execute(sql,[("%" +pat_national_id+ "%",)])
        data = self.cur.fetchone()

        print(data)
        self.lineEdit_43.setText(data[2])
        self.lineEdit_21.setText(data[7])
        self.dateEdit_3.setDate(data[5])
        self.lineEdit_22.setText(data[6])
        self.lineEdit_40.setText(str(data[3]))
        self.comboBox_6.setCurrentText((data[4]))
        

    def handle_report(self):
        pat_name=self.lineEdit_43.text()
        pat_national_id=self.lineEdit_15.text()
        pat_phone=self.lineEdit_21.text()
        pat_address=self.lineEdit_22.text()
        pat_age=self.lineEdit_40.text()
        pat_gender=self.comboBox_6.currentText()
        pat_investigate_dat=self.dateEdit_3.date().toString("yyyy-MM-dd")
        pat_Noification=self.textEdit_3.toPlainText()

        pdf = FPDF()
        pdf.add_page()
        ######header
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 15)    
        pdf.cell(80)
            
        #pdf.line(10, 290, 200, 290)
        #pdf.set_xy(6.0,6.0)
        #pdf.set_line_width(0.0)
        #pdf.set_fill_color(0, 255, 0)
        pdf.set_fill_color(255, 255, 255)
        pdf.rect(5.0, 5.0, 200.0,287.0,'DF')

        pdf.set_fill_color(255, 255, 255)
        pdf.rect(8.0, 8.0, 194.0,282.0,'FD')

        pdf.set_fill_color(255, 255, 255)
        pdf.rect(10.0, 35.0, 190.0,65.0,'FD')
        pdf.set_fill_color(255, 255, 255)
        pdf.rect(10.0, 105.0, 190.0,182.0,'DF')
        
        pdf.set_font("Arial", size=12)
        pdf.image(name='C:/Users/ahmed/OneDrive/Desktop/last_test/imag/itar.png', x=177, y=8, w=25, h=25, type = 'PNG')
        pdf.image(name='C:/Users/ahmed/OneDrive/Desktop/last_test/imag/itar2.png', x=8, y=8, w=25, h=25, type = 'PNG')
        pdf.set_x(80.0)
        pdf.cell(50, 10, 'Patient Report', 1, 0, 'C')
        
        pdf.ln(20)
        pdf.cell(200,10, txt= "     patient Name :" +pat_name, ln=2, align="L")
        pdf.cell(200,10, txt= "     National Id :" +pat_national_id, ln=2, align="L")
        pdf.cell(200,10, txt= "     phone No :" +pat_phone, ln=2, align="L")
        pdf.cell(200, 10, txt="     Address:"+pat_address, ln=2,align="L" )
        pdf.ln(5)
        pdf.cell(200, 0, txt="     Age:"+pat_age, ln=2, align="L")
        pdf.cell(200, 0, txt="     gender:"+pat_gender, ln=2, align="C")
        pdf.ln(5)
        pdf.cell(200, 10, txt="     Date of Investigation:"+pat_investigate_dat, ln=2, align="L")
        #pdf.ln(5)
        pdf.set_xy(80,107.0)
        pdf.cell(50, 10, 'Description', 1, 0, 'C')
        pdf.set_xy(15.0,105.0)
        pdf.multi_cell(180, 10, txt=pat_Noification, align="L")
        ##########footer
        
            # Select Arial italic 8
        pdf.set_font('Arial', 'I', 8)
            # Print centered page number
        pdf.set_y(275)
        pdf.cell(0, 0, 'Page %s' % pdf.page_no(), 0, 0, 'C')
        
        #pdf.output(pat_name+"_report.pdf",'D')
        
        pdf.output("C:/Users/ahmed/OneDrive/Desktop/last_test/Report/"+pat_name+"_report.pdf",'D')

        pdf = FPDF(orientation='P', unit='mm', format='A4')

    
    #####################setting##############################
    def show_sepcialization(self):
        self.comboBox.clear()
        self.comboBox_3.clear()
        self.cur.execute('''
        SELECT name FROM specialization
        ''')
        special = self.cur.fetchall()
        for items in special:
            #print(items[0])

            self.comboBox.addItem(str(items[0]))
            self.comboBox_3.addItem(str(items[0]))

    def add_sepcialization(self):
        special_name = self.lineEdit_31.text()
        
        self.cur.execute('''INSERT INTO specialization (name ) 
        VALUES(%s)
        ''' ,(special_name,))
        self.db.commit()
        #print("Add new special")
        QtWidgets.QMessageBox.information(self, "Sucess" , "تم الاضافه  بنجاح!")

        self.show_sepcialization()
        self.lineEdit_31.clear()


    def add_admin(self):
        user_name = self.lineEdit_83.text()
        password = self.lineEdit_82.text()
        
        self.cur.execute('''INSERT INTO admin (name,password ) 
        VALUES(%s,%s)
        ''' ,(user_name,password,))
        self.db.commit()
        #print("Add new special")
        QtWidgets.QMessageBox.information(self, "Sucess" , "تم الاضافه  بنجاح!")

        
        self.lineEdit_83.clear()
        self.lineEdit_82.clear()

        self.show_all_admin()
    def show_all_admin(self):
        self.cur.execute('''SELECT name,password FROM admin''')
        data = self.cur.fetchall()
        #print(data)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_6.insertRow(0)
        for row , form in enumerate(data):
            for col , item in enumerate(form):
                self.tableWidget_6.setItem(row , col, QtWidgets.QTableWidgetItem(str(item)))
                col +=1
            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)

    ############################################################
    #################open-tabs##################################
    
    def open_login_tab(self):
        self.tabWidget.setCurrentIndex(0)
        self.groupBox_15.setEnabled(False)

    def open_resetPass_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def open_investegation_tab(self):
        self.tabWidget.setCurrentIndex(2)
     
        

    def open_patients_tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_3.setCurrentIndex(0)
    
    def open_doctors_tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_4.setCurrentIndex(0)

    def open_reports_tab(self):
        self.tabWidget.setCurrentIndex(5)
    
    def open_Archives_tab(self):
        self.tabWidget.setCurrentIndex(6)
        self.tabWidget_6.setCurrentIndex(0)
    
    def open_setting_tab(self):
        self.tabWidget.setCurrentIndex(7)
        self.tabWidget_5.setCurrentIndex(0)



    ############################################################
    #################open Camera################################

    def open_camera(self):
        
        dir = "C:\Program Files (x86)\ManyCam\ManyCam.exe"
        os.startfile(dir)

    ############################################################
    ################ specialization#########################

    


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
