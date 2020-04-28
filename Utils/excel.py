from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference

class Excel:
    
    workbook = Workbook()
    name = '././Reports/CreateReport.xlsx'
    def readExcel(self):
        try:
             return load_workbook(filename = self.name)
        except FileNotFoundError:
            print('File does not exists')
    
    def save(self):
        try:
            self.workbook.save(filename = self.name)
            return True
        except:
            return False

    def createIncidentsReport(self, elements_list): 
        try:
            sheet = self.workbook.active
            sheet.append(['Monitor','Dia','Hora de Inicio','Duracion', 'Tipo de Alerta'])
            for row in elements_list: # Show the list 
                sheet.append(row) #Add the list to excel
            
            lenght = int(len(elements_list) + 2)
            #Create new Sheet 
            final = self.workbook.create_sheet('Presentation')
            final.append(['Monitor','Dia','Hora de Inicio','Duracion', 'Tipo de Alerta'])

            for value in range(2, lenght):
                final['A{0}'.format(value)] = '=Sheet!A{0}'.format(value)
                final['B{0}'.format(value)] = '=TEXT(Sheet!{0}, "dddddddd, mmm dd, yyyy")'.format('B{0}'.format(value))
                final['C{0}'.format(value)] = '=UPPER(Sheet!C{0})'.format(value)
                final['D{0}'.format(value)] = '=UPPER(Sheet!D{0})'.format(value)
                final['E{0}'.format(value)] = '=Sheet!E{0}'.format(value)
           

            final.merge_cells('I3:J3')
            final.cell(row = 3, column = 9).value = 'IB'
            final["I4"] = 'Tipo de Alerta'
            final["J4"] = 'Incidencias'
            final["I5"] = 'Otras'
            final["J5"] = 0
            final["I6"] = 'Error rate > 5.0%'
            final["J6"] = 0
            final["I7"] = 'Apdex Score < 0.7'
            final["J7"] = '=COUNTIF(E2:E{}, "Apdex_IB")'.format(lenght)
            final["J8"] = '=COUNTIF(E2:E{}, "Availability_IB")'.format(lenght)
            final["I8"] = 'Ping Alerts'
            final.merge_cells('K3:L3')
            final.cell(row = 3, column = 11).value = 'CTF'
            final["K4"] = 'Tipo de Alerta'
            final["L4"] = 'Incidencias'
            final["K5"] = 'Otras'
            final["L5"] = 0
            final["K6"] = 'Error rate > 5.0%'
            final["L6"] = 0
            final["K7"] = 'Apdex Score < 0.7'
            final["L7"] = '=COUNTIF(E2:E{}, "Apdex_CTF")'.format(lenght)
            final["L8"] = '=COUNTIF(E2:E{}, "Availability_CTF")'.format(lenght)
            final["K8"] = 'Ping Alerts'
            final.merge_cells('M3:N3')
            final.cell(row = 3, column = 13).value = 'BM'
            final["M4"] = 'Tipo de Alerta'
            final["N4"] = 'Incidencias'
            final["M5"] = 'Otras'
            final["N5"] = 0
            final["M6"] = 'Error rate > 5.0%'
            final["N6"] = 0
            final["M7"] = 'Apdex Score < 0.7'
            final["N7"] = '=COUNTIF(E2:E{}, "Apdex_BM")'.format(lenght)
            final["N8"] = '=COUNTIF(E2:E{}, "Availability_BM")'.format(lenght)
            final["M8"] = 'Ping Alerts'
            

        except:
            return False
        finally:
            if self.save() == True:   
                return True
            