# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UserInherit(models.Model):
    _inherit = 'res.users'

    pos_id = fields.Many2one(comodel_name="pos.config", string="Point of sale", required=False, )



class PosConfigInherit(models.Model):
    _inherit = 'pos.config'

    user_ids = fields.One2many(comodel_name="res.users", inverse_name="pos_id", string="Users", required=False, )
