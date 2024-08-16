# -*- coding: utf-8 -*-
from odoo import models, fields

class ToolkinData(models.Model):
    _name = 'toolkin.data'
    _description = 'Datos Extraídos del Toolkit'

    toolkin_id = fields.Many2one('toolkin', string="Toolkit")
    name = fields.Char(string="Nombre")
    value = fields.Char(string="Valor")
    # Agrega más campos según los datos que desees manejar
