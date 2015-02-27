$(document).ready(function() {
    $("#add_contact").dform("/static/add_contact_form.json")// if successful, render form
  });

//$(document).ready(function() {
//    var client_id = $('form').attr('client_id')
//    $.post("/api/add-contact", client_id,
//           function() {$("#add_contact").dform("/static/add_contact_form.json")// if successful, render form
//        });
//  });
