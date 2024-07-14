#!/usr/bin/python3
from bs4 import BeautifulSoup as bs
import requests
import sys

class AAU:
      def __init__(self,firstname,fathername,idno) -> None:
         self.firstname=firstname
         self.fathername=fathername
         self.idno=idno
         global payload
         global r
         global html
         payload={'firstName':self.firstname, 'fatherName': self.fathername,'studentidno':'ugr/'+self.idno}
         r=requests.post("https://portal.aau.edu.et/NewStudents/Welcome/Login" , data=payload)
         html=bs(r.text, 'lxml')
      def phone(self):
        
          try:
              part=html.find('input', id='Telephone')
              part_str=str(part)
              value=part_str.split()[-1]
              if value[7]== '+':
                getit=value[7:20]
              else:
                getit=value[7:17]
              return getit 
          except:
             print("Please make sure you entered correct name and id \nor check you internet connection ")
      def email(self):
          try:
              part=html.find('input', id='Email')
              part_str=str(part)
              value=part_str.split()[-1]
              
              return value.split("\"")[1]
          except:
              print("Please make sure you entered correct name and id \nor check you internet connection ")
      def birth(self):
          try:
              part=html.find('input', class_='k-input')
              part_str=str(part)
              
              if part_str:
                  return part_str
              else:
                  return "make sure you entered correct input "
          except Exception as e: 
              print(e)
              return 'no'

                      
      
      def photo(self,filename):
          part=html.find('img', id='output')
          part_str=str(part).split()
          src=part_str[8]
          img_link="https://portal.aau.edu.et/"+src[6:-1]
          pic=requests.get(img_link)
          file = open(f"{filename}", "wb")
          file. write(pic.content)
          file. close()
          return ""

