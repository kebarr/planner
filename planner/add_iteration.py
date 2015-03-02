def convert_iteration_dict_form_json(iteration_id):
    form_data = {"action": "/iterations/1/add",
                 "method": "get",
                 "html": [{"type": "hidden",
                          "value": iteration_id,
                          "name": "id"},
                          {"type": "text",
                           "caption": "Start Date",
                           "name": "startdate"},
                          {"type": "submit",
                           "value": "Add Iteration"}]}
    return form_data
