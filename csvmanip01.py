import csv
import re
import numpy
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses.xlsx')
worksheet = workbook.add_worksheet()

f = open('mdRC_2015_t1.csv')

csv_f = csv.reader(f, delimiter = ';')

file_split = [[]]
temp_row = []
temp2_row = []
i = 0
j = 0
row = 0

for rowq in csv_f:
        k =  re.split('1.|2.|3.|4.|5.|6.|7.|8.|9.|10.|11.|12.|13.|14.|15.|16.|17.|18.|19.|20.|21.|22.|23.|24.|25.|26.|27.|28.|29.|30.|31.|32.|33.|34.|35.|36.|37.|38.|39.|40.|41.|42.|43.|44.|45.|46.|47.|48.|49.|50.|51.|52.|53.|54.|55.|56.|57.|58.|59.|60.|61.|62.|63.|64.|65.|66.|67.|68.|69.|70.|71.|72.|73.|74.|75.|76.|77.|78.|79.|80.', rowq[3])
        i = 0
        col = 0
        for data in k:
            row = row + 1
            temp_row = rowq    
           # if row[2] == " ":
            #     temp_row = temp2_row
            if rowq[3] != " " :
                 file_split.append([])
                 temp_row[3] = data
                 i = i + 1
                # print temp_row[3]
                # print temp_row
               
                # for  rec in (temp_row):
                 worksheet.write_string (j, col, temp_row[0])
                 worksheet.write_string (j, col + 1, temp_row[1] )
                 worksheet.write_string (j, col + 2, temp_row[2] )
                 worksheet.write_string (j, col + 3, temp_row[3] )
                   #  worksheet.write_string (row, col + 4, rec[4] )
                   #  worksheet.write_string (row, col + 5, rec[5] )
                   #  worksheet.write_string (row, col + 6, rec[6] )
                   #  worksheet.write_string (row, col + 7, rec[7] )
                   #  worksheet.write_string (row, col + 8, rec[8] ) 
                   # row += 1   
           
        j = j + i
        #if row[2] != " ":
         #       temp2_row = row
    # print row[4]
#print file_split      
f.close()




#worksheet.write(0, 0, 'Hello Excel')


#row = 1
#col = 0
#for key in (file_split):
   #     col = 0
    #    print key
     #   for  rec in (key):
     # Convert the date string into a datetime object.
            # print rec[3]
      #       worksheet.write (row, col, rec[3])
            
           #  worksheet.write_string (row, col + 1, rec[1] )
            # worksheet.write_string (row, col + 2, rec[2] )
            # worksheet.write_string (row, col + 3, rec[3] )
            # worksheet.write_string (row, col + 4, rec[4] )
            # worksheet.write_string (row, col + 5, rec[5] )
            # worksheet.write_string (row, col + 6, rec[6] )
            # worksheet.write_string (row, col + 7, rec[7] )
            # worksheet.write_string (row, col + 8, rec[8] ) 
       # row += 1   




         #   
          #   row += 1''''
workbook.close()
 
#csvfile = open('test3.txt', 'wb')

#s = "$$$"

#csvwriter = csv.writer(csvfile, delimiter = ';')
#for item in file_split:
 #       str1 = " "
   #     for ite in item:
    #            str = '^'.join(ite)
     #           str1 = (str1 + str )
                
                
      #  csvfile.write(str1) 
#    csvwriter.writerow(item)
#csvfile.close()
