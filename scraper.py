import bs4 as bs
import lxml
import urllib.request
import os
import csv
list1=[]
list2=[]
list3=[]

sauce=urllib.request.urlopen('https://karki23.github.io/Weather-Data/assignment.html').read()
srccode=bs.BeautifulSoup(sauce,'lxml')
for i in srccode.find_all('a'):
    list1.append(i.get('href'))

playerdatasaved=''  
for k in list1:
    
    m='https://karki23.github.io/Weather-Data/'
    n=m+k
    
    sauce1=urllib.request.urlopen(n).read()
    srccode1=bs.BeautifulSoup(sauce1,'lxml')
    tabledata=srccode1.find_all('table')
    tableheader=srccode1.find_all('th')
    tableheaderdata=[i.text for i in tableheader]
    
  
    for row in tabledata:
        tablerow=row.find_all('tr')
        #print(tablerow)
        for data in tablerow:
           tabledata=data.find_all('td')
           rowdata=[i.text for i in tabledata]
           #print(rowdata)
           list3.append(rowdata)
           #print(list3)
    with open("data1.csv",'w') as writefile:
       writer=csv.writer(writefile)
       writer.writerow(tableheaderdata)
   
    with open("data1.csv",'a') as writefile:
       for j in list3:
          writer=csv.writer(writefile)
          writer.writerow(j)

        
           
    
    
         
    