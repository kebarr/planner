$(document).ready(function() {$("#add_contact").dform({
    "action" : "clients.html",// probably want to go back to specific client eventually
    "method" : "post",
    "html" :
    [
     {"type": "hidden",
       "value" : $(this).attr('client_id')
    },
        {
            "type" : "text",
            "name" : "Forename",
            "caption" : "Forename"
        },

        {
            "type" : "text",
            "name" : "Surname",
            "caption" : "Surname"
        },
        {
            "type" : "text",
            "name" : "Role",
            "caption" : "Role"
        },
        {
            "type" : "text",
            "name" : "email",
            "placeholder" : "E.g. user@example.com",
            "caption" : "Email"
        },
        {
            "type" : "text",
            "name" : "Landline number",
            "caption" : "Landline number"
        },
        {
            "type" : "text",
            "name" : "Mobile number",
            "caption" : "Mobile number"
        },
        {
            "type" : "p",
            "html" : "Address information"
        },
        {
            "type" : "text",
            "name" : "Street number",
            "caption" : "Street number"
        },
        {
            "type" : "text",
            "name" : "Street name",
            "caption" : "Street name"
        },
        {
            "type" : "text",
            "name" : "Post code",
            "caption" : "Post code"
        },
        {
            "type" : "submit",
            "value" : "Add contact"
        }
    ]
});
  });
