from odoo import models, fields

class TpJury(models.Model):
    _name = "tp.jury"
    _description = "Jurys et décisions"

    name = fields.Char(string="Nom du jury", required=True)
    responsable = fields.Char(string="Responsable")
    date_jury = fields.Date(string="Date du jury")
    decision = fields.Selection([
        ("en_attente", "En attente"),
        ("valide", "Validé"),
        ("rejete", "Rejeté"),
    ], string="Décision", default="en_attente")
    commentaire = fields.Text(string="Commentaire")
