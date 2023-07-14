from odoo import fields, models

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    # production
    total_pieces = fields.Integer(string='Total de Piezas Producidas')
    theoretical_main_pieces = fields.Integer(string='Total de Primera - Teóricas')
    real_main_pieces = fields.Integer(string='Total de Primera - Reales')
    irregular_pieces = fields.Integer(string='Piezas Irregulares')
    recovered_pieces = fields.Integer(string='Piezas Recuperadas')
    theoretical_discarded_pieces = fields.Integer(string='Piezas descartadas - Teóricas')
    real_discarded_pieces = fields.Integer(string='Piezas descartadas - Reales')
    # Time
    total_time_worked = fields.Float(string='Tiempo total trabajado', digits=(6, 2))
    lost_time = fields.Float(string='Tiempo perdido', digits=(6, 2))
    # Machine
    machine_speed = fields.Float(string='Velocidad de la Máquina')
    machine_efficiency = fields.Float(string='Eficiencia de la Máquina')



