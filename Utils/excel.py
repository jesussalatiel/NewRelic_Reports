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
        sheet = self.workbook.active
        sheet.append(['Monitor','Dia','Hora de Inicio','Duracion', 'Tipo de Alerta'])
        sheet.auto_filter.ref = "A1:E100"
            
        for row in elements_list:
            sheet.append(row)

        range = len(elements_list)+1

        sheet.merge_cells('I3:J3')
        sheet.cell(row = 3, column = 9).value = 'IB'
        sheet["I4"] = 'Tipo de Alerta'
        sheet["J4"] = 'Incidencias'
        sheet["I5"] = 'Otras'
        sheet["J5"] = 0
        sheet["I6"] = 'Error rate > 5.0%'
        sheet["J6"] = 0
        sheet["I7"] = 'Apdex Score < 0.7'
        sheet["J7"] = '=COUNTIF(E2:E{}, "Apdex_IB")'.format(range)
        sheet["J8"] = '=COUNTIF(E2:E{}, "Availability_IB")'.format(range)
        sheet["I8"] = 'Ping Alerts'
        sheet.merge_cells('K3:L3')
        sheet.cell(row = 3, column = 11).value = 'CTF'
        sheet["K4"] = 'Tipo de Alerta'
        sheet["L4"] = 'Incidencias'
        sheet["K5"] = 'Otras'
        sheet["L5"] = 0
        sheet["K6"] = 'Error rate > 5.0%'
        sheet["L6"] = 0
        sheet["K7"] = 'Apdex Score < 0.7'
        sheet["L8"] = '=COUNTIF(E2:E{}, "Apdex_CTF")'.format(range)
        sheet["L7"] = '=COUNTIF(E2:E{}, "Availability_CTF")'.format(range)
        sheet["K8"] = 'Ping Alerts'
        sheet.merge_cells('M3:N3')
        sheet.cell(row = 3, column = 13).value = 'BM'
        sheet["M4"] = 'Tipo de Alerta'
        sheet["N4"] = 'Incidencias'
        sheet["M5"] = 'Otras'
        sheet["N5"] = 0
        sheet["M6"] = 'Error rate > 5.0%'
        sheet["N6"] = 0
        sheet["M7"] = 'Apdex Score < 0.7'
        sheet["N7"] = '=COUNTIF(E2:E{}, "Apdex_BM")'.format(range)
        sheet["N8"] = '=COUNTIF(E2:E{}, "Availability_BM")'.format(range)
        sheet["M8"] = 'Ping Alerts'

        
        if self.save() == True:   
            return True
        return False