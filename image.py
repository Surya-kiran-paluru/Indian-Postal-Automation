from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog, QHBoxLayout, QFrame
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import os
from subprocess import check_output
from sys import executable
import OCR_model as ocr
import Address_parser as ap
import Knowledge_graph as kg
from spell_check import SpellCheck
import Location as loc_api

class UI(QMainWindow):
    #global fpath
    #fpath=""
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("image.ui", self)

        self.button=self.findChild(QPushButton, "pushButton")
        self.label=self.findChild(QLabel, "label")
        self.button.clicked.connect(self.clicker)
        
        self.button2=self.findChild(QPushButton, "pushButton_2")
        self.button2.clicked.connect(self.clicker2)
        
        self.ocr_out_label=self.findChild(QLabel, "label_3")
        self.addparser_label=self.findChild(QLabel, "label_4")
        self.addparser_label.setWordWrap(True)
        self.knowledge_label=self.findChild(QLabel, "label_6")
        self.latlong_label=self.findChild(QLabel, "label_9")
        
        self.show()
    
    def clicker(self):
        fname=QFileDialog.getOpenFileName(self, "Open file")
        self.pixmap=QPixmap(fname[0])
        global fpath
        fpath=fname[0]
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)

    def clicker2(self):        
        model = ocr.load_model()
        output_ocr = ocr.get_text(model, fpath)
        output_ocr = " ".join(output_ocr)
        spell_check =  SpellCheck("data\citiesname.txt")
        spell_check.check(output_ocr)
        output_ocr = spell_check.correct()
        output_ocr = output_ocr.capitalize()
        self.ocr_out_label.setText(output_ocr)
        f_output_ocr=""
        for i in output_ocr:
            if i == " ":
                f_output_ocr=f_output_ocr + ", "
            else:
                f_output_ocr = f_output_ocr + i

        print(f_output_ocr)
        output_ap = ap.parse_address(f_output_ocr)
        print(output_ap)
        parser_out=""
        for i in output_ap:
            parser_out=parser_out+"[ "
            parser_out=parser_out+i[1]+" - "
            parser_out=parser_out+i[0]+" "
            parser_out=parser_out+"] "

        self.addparser_label.setText(parser_out)

        # plt=kg.build_Kgraph(output_ap)
        # plt.savefig('knowledge graph outputs/output.png', bbox_inches='tight')
        # self.pixmap2=QPixmap("knowledge graph outputs/output.png")
        # self.knowledge_label.setPixmap(self.pixmap2)
        # self.knowledge_label.setScaledContents(True)

        Knowledgde_Graph = kg.build_Kgraph(output_ap)
        #kg.show_KG(Knowledgde_Graph)

        plt=kg.show_KG(Knowledgde_Graph)
        plt.savefig('knowledge graph outputs/output.png', bbox_inches='tight')
        self.pixmap2=QPixmap("knowledge graph outputs/output.png")
        self.knowledge_label.setPixmap(self.pixmap2)
        self.knowledge_label.setScaledContents(True)

        city = kg.get_city(Knowledgde_Graph)[0]
        s = "city: " + city + " , coordinates: "
        latlong = loc_api.get_coordinates(city)
        s+=str(latlong[0])+" "+str(latlong[1])
        self.latlong_label.setText(s)

        # plt.show()
        
        # out = check_output([executable, "main.py",fpath])
        # fout = str(out, 'UTF-8')

app=QApplication(sys.argv)
UIWindow=UI()
app.exec_()
