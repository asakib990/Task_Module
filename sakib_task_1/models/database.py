from odoo import models, fields


class Question(models.Model):
    _name = "question.info"
    _description = "Store Question ID, Question, Answer, Marks"

    que_id = fields.Char(string="Question ID", required=True)
    que = fields.Text(string="Question", required=True)
    ans = fields.Text(string="Answer", required=True)
    marks = fields.Float(string="Marks", required=True)


class StudentInfo(models.Model):
    _name = 'student.info'
    _description = 'Store Student information.'

    s_id = fields.Char(string="Student Id", required=True)
    que_id = fields.Many2one("question.info", string="Question ID", required=True)
    name = fields.Char(string="Student Name", required=True)
    score = fields.Float(string="Student Score", required=True)