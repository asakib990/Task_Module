from odoo import models, fields


class Question(models.Model):
    _name = "question.info"
    _description = "Store Question ID, Question, Answer, Marks"

    que_id = fields.Char(string="Question ID", required=True)
    que = fields.Text(string="Question", required=True)
    ans = fields.Text(string="Answer", required=True)
    marks = fields.Float(string="Marks", required=True)
