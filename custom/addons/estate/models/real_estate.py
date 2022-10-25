from odoo import models, fields

class estate(models.Model):
	_name = "real_estate"
	
	fname = fields.Text(string="First Name", required = True)
	midname = fields.Text(string="MiddleName", required = True)
	lname = fields.Text(string="LastName", required = True)
	id = fields.Text(integer="Id", required = True)
	create_uid = fields.Text(integer ="Create UID")
	create_date = fields.Date("Date Creation")
	write_uid = fields.Text(integer="Write UID")
	write_date = fields.Date("Write Date")
	description = fields.Text(string="Description")
	postcode = fields.Char(default="Postal Code") 
