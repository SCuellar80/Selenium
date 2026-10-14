import openpyxl

class ExcelReader:
    def __init__(self, file_path=None): #filepath is optional, when not passed it takes the default defined here.
        if file_path == None:
            file_path = "C:/Users/copca/OneDrive/GitHub/Selenium/Selenium/Data Driven Testing/data.xlsx"
        self.file_path = file_path

    def read_excel_data(self):
        # Cargar el archivo de Excel
        workbook = openpyxl.load_workbook(self.file_path)
        sheet = workbook.active

        # Lista para almacenar los datos
        data = []

        # Iterar sobre las filas del archivo de Excel
        for row in sheet.iter_rows(min_row=2, values_only=True):  # Suponiendo que la primera fila es el encabezado
            username = row[0]  # Primera columna
            password = row[1]  # Segunda columna
            login_text_result = row[2]  # Tercera columna

            # Agregar los datos a la lista como una tupla
            data.append((username, password, login_text_result))

        return data

# Ejemplo de uso
if __name__ == "__main__":
    file_path = "data.xlsx"  # Ruta al archivo de Excel
    excel_reader = ExcelReader(file_path)
    data = excel_reader.read_excel_data()

    # Imprimir los datos leídos
    for item in data:
        print(item)