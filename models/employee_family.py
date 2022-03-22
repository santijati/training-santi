# -*- coding: utf-8 -*-
from odoo import models, fields

class EmployeeFamily(models.Model):
    _name = 'employee.family'
    name = fields.Char('Name')
    date = fields.Date('Date of birth')
    family_relation = fields.Selection(selection=[('ayah','Ayah'),('ibu','Ibu'), ('suami','Suami'), ('istri','Istri'),('saudara','Saudara'),('anak','Anak')], string="Family Relation")
    employee_id = fields.Many2one('hr.employee',string='Family member of', required=True)
    
    def compute_allowance(self):
        view_id=self.env.ref('employee_family.employee_family_list_view')
        return{
            'type':'ir.actions.act_window',
            'name':'Family member of %s'%self.employee_id.display_name,
            'view_mode':'tree',
            'res_model':'employee.family',
            'view_id':view_id.id,
            'res_id':self.id,
            'domain':[('employee_id','=',self.employee_id.id)]
        }