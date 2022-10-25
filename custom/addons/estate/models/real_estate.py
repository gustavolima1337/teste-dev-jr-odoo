from odoo import models, fields

class estate(models.Model):
	_name = "estate_property"
	
	name = fields.Char(string = "Name",required = True)
	description = fields.Text(string = "Description")
	postcode = fields.Char(string = "Postal Code")
	date_availability = fields.Date("Date Availability")
	expected_price = fields.Float("Expected Price", required = True)
	selling_price = fields.Float("Selling Price")
	Bedrooms = fields.Integer("Bedrooms")
	living_area = fields.Integer("Living Area")
	facades = fields.Integer("Facades")
	garage = fields.Boolean("Garage")
	garder = fields.Boolean("Garden")
	garden_area = fields.Integer("Garden Area")
	garden_orientation = fields.Selection(string='Type', [('north','North'),('south','South'),('east','East'),('west','West')])
