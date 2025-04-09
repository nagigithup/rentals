// Copyright (c) 2025, nagi and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    onload(frm) {
        console.log("onload");
        
    },
    setup(frm) {
        console.log("setup");
        
    },
	refresh(frm) {
        console.log("refresh");

        if (frm.doc.status === "New") {
            frm.add_custom_button("Accept", () => {
                frm.set_value("status", "Accepted");
                frm.save();
            },"Action")

            frm.add_custom_button("Reject", () => {
                frm.set_value("status", "Rejected");
                frm.save();
            },"Action")
        }
        
            
        
	}
});
