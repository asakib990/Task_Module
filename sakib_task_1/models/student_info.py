from odoo import fields, models


class StudentInfo(models.Model):
    _name = 'student.info'
    _description = 'Store Student information.'

    s_id = fields.Char(string="Student Id", required=True)
    que_id = fields.Many2one("question.info", string="Question ID", required=True)
    name = fields.Char(string="Student Name", required=True)
    score = fields.Float(string="Student Score", required=True)
