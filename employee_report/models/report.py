from odoo import models, api, fields

class ParticularReport(models.AbstractModel):
    _name = 'report.employee_report.employee_report_template_modif'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('employee_report.employee_report_template_modif')
        obj_employee = self.env['hr.employee'].browse(docids)
        anggota_keluarga = []
        for rec in obj_employee.anggota_keluarga:
            anggota_keluarga.append({'name': rec.name, 'family_relation': rec.family_relation,})
        data = {
            'name': obj_employee.name,
            'ayah': obj_employee.ayah.name,
            'anggota_keluarga': anggota_keluarga,
        }
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self.env[report.model].browse(docids),
            'data': [data],
        }
        return docargs