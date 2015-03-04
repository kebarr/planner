def convert_iteration_dict_form_json():
    form_data = {"action": "/iteration/new",
                 "method": "post",
                 "html": [{"type": "text",
                           "caption": "Start Date",
                           "name": "startdate"},
                          {"type": "submit",
                           "value": "Add Iteration"}]}
    form_data["html"].append({"type": "hidden",
                              "value": "Iteration",
                              "name": "entity"})
    return form_data



#{"type": "hidden",
#                          "value": iteration_id,
#                          "name": "id"},
