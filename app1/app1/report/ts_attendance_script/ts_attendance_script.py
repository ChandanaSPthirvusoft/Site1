# Copyright (c) 2013, pub and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	filters= frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data
	
def get_columns(filters):
	columns = [
		{
  			"fieldname": "name1",
 			"fieldtype": "Data",
 	 		"in_list_view": 1,
   			"label": "NAME",
  			"reqd": 1
  		},
 	 	{
   			"fieldname": "id",
 		    "fieldtype": "Data",
 			"in_list_view": 1,
   			"label": "ID",
    		"reqd": 1
  		},
 		 {
  			"fieldname": "date",
   			"fieldtype": "Date",
   			"in_list_view": 1,
   			"label": "DATE",
   			"reqd": 1
 		},
  		{
  			"fieldname": "intime",
  			"fieldtype": "Time",
   			"in_list_view": 1,
   			"label": "INTIME"
  		},
  		{
   			"fieldname": "outtime",
  			"fieldtype": "Time",
   			"label": "OUTTIME"
 		}
	]

	return columns

def get_conditions(filters):
	conditions = {}

	if filters.date:
		conditions["date"] = filters.date

	if filters.id:
		conditions["id"] = filters.id
	

	return conditions

def get_data(filters):

	data = []
	conditions = get_conditions(filters)
	accounts = frappe.db.get_all("TS Attendance Doc", fields=["name1", "date","id","intime",'outtime'],
		filters=conditions)

	for d in accounts:
		row = {"name1": d.name1, "date": d.date, "id": d.id,"intime": d.intime , "outtime": d.outtime}

		data.append(row)

	return data 
