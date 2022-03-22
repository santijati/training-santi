from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'
    
    ayah = fields.Many2one('employee.family', string='Ayah')
    anggota_keluarga = fields.One2many('employee.family', 'employee_id', string='Anggota Keluarga')
    
class EmployeeFamily(models.Model):
    _inherit = 'employee.family'
    
    def compute_allowance(self):
        res = super(EmployeeFamily,self).compute_allowance()
        res.update(target='new')
        return res
    
    