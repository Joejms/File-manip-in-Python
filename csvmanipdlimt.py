import csv
import re
import numpy
import xlsxwriter

# Create a workbook and add a worksheet.
#workbook = xlsxwriter.Workbook('Expenses.xlsx')
#worksheet = workbook.add_worksheet()


f = open('mdRC_2015csv.csv', 'rb') 

reader_f =csv.reader(f)




#csv_f = csv.reader(f, delimiter = ';')

ofile = open('mdRC_2015output.csv', 'w')
write_ofile = csv.writer(ofile)


for row in reader_f :
        row[3] = "%$$%" + row[3]
        k =  re.split('%$$%|1.|2.|3.|4.|5.|6.|7.|8.|9.|10.|11.|12.|13.|14.|15.|16.|17.|18.|19.|20.|21.|22. \
                      |23.|24.|25.|26.|27.|28.|29.|30.|31.|32.|33.|34.|35.|36.|37.|38.|39.|40.\
                      |41.|42.|43.|44.|45.|46.|47.|48.|49.|50.|51.|52.|53.|54.|55.|56.|57.|58.|59. \
                      |60.|61.|62.|63.|64.|65.|66.|67.|68.|69.|70.|71.|72.|73.|74.|75.|76.|77.|78.|79.|80.', row[3])
                      
        for cell_data in k:
                row[3] = cell_data
                print cell_data
                write_ofile.writerow(row)
                
                
                





        
        #write_ofile.writerow(row)
        #print row


        



