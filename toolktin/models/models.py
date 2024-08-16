from odoo import models, fields, api
import base64
import csv
import pandas as pd
import PyPDF2
import io

class AutoEntryToolkit(models.Model):
    _name = 'toolkin'
    _description = 'Toolkit'

    name = fields.Char(string="Nombre")
    file_type = fields.Selection([
        ('pdf', 'PDF'),
        ('csv', 'CSV'),
        ('xlsx', 'Excel'),
        ('txt', 'Texto')
    ], string="Tipo de Archivo")
    file_data = fields.Binary(string="Archivo")
    document_processed = fields.Boolean(string="Procesado", default=False)
    processing_log = fields.Text(string="Log de Procesamiento")
    extracted_text = fields.Text(string="Texto Extraído")  # Campo para almacenar el texto extraído

    def process_document(self):
        try:
            file_content = base64.b64decode(self.file_data)
            text = ""
            if self.file_type == 'csv':
                data = self._process_csv(file_content)
                text = "\n".join([str(row) for row in data])
            elif self.file_type == 'xlsx':
                data = self._process_xlsx(file_content)
                text = "\n".join([str(row) for row in data])
            elif self.file_type == 'pdf':
                text = self._process_pdf(file_content)
            elif self.file_type == 'txt':
                text = self._process_txt(file_content)
            
            # Guardar el texto extraído en el campo
            self.extracted_text = text
            
            self.document_processed = True
            self.processing_log = "Procesado correctamente"
        except Exception as e:
            self.processing_log = str(e)

    def _process_csv(self, file_content):
        decoded_file = file_content.decode('utf-8')
        reader = csv.DictReader(io.StringIO(decoded_file), delimiter=',')
        return [row for row in reader]

    def _process_xlsx(self, file_content):
        df = pd.read_excel(io.BytesIO(file_content))
        return df.to_dict(orient='records')

    def _process_pdf(self, file_content):
        reader = PyPDF2.PdfReader(io.BytesIO(file_content))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    def _process_txt(self, file_content):
        return file_content.decode('utf-8')
