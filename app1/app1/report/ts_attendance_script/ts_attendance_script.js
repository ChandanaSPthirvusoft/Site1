// Copyright (c) 2016, pub and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["TS Attendance Script"] = {
	"filters": [
		{   fieldname:"date",
            label: __("DATE"),
            fieldtype: "Date",
            width: 50
		},
		/*{   fieldname:"name1",
            label: __("NAME"),
            fieldtype: "Select",
			options:[
			{ "value": "Chandana", "label": __("Chandana") },
			{ "value": "Gokulnath", "label": __("Gokulnath ")},
			{ "value": "Naveen", "label": __("Naveen") }],
            width: 50
		}*/
		{   fieldname:"id",
            label: __("ID"),
            fieldtype: "Int",
            width: 50
		}
	]
};
