# -*- coding: utf-8 -*-
##############################################################################
#
#    odoo, Open Source Enterprise Management Solution
#    GRP Estado Uruguay
#    Copyright (C) 2017 Quanam (ATEL SA., Uruguay)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import tools, api, fields, exceptions, models
import logging
_logger = logging.getLogger(__name__)


class GrpProductTemplate(models.Model):
    _inherit = 'product.template'

    viatico_ok = fields.Boolean(string=u"Viatico", default=False)
    devolucion_viatico = fields.Boolean(u'Devolución de viáticos')
