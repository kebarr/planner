import json

#@api.route('/api/add-contact', methods=['POST'])
#def update_json_with_client_id():
#    client_id = request.data
#    print client_id
#    with open("/static/add_contact_form.json", 'r') as f:
#        form_data = json.load(f)
#        form_data['html'][0]['value'] = client_id
#        assert form_data['html'][0]['type'] == 'hidden'
#    with open("/static/add_contact_form.json", 'w') as f:
#        json.dump(form_data, f)



# TODO: THESE COME OUT IN A FUNNY ORDER
def convert_client_dict_form_json(client_dict):
    contact_keys = client_dict.keys()
    form_data = {"action":"/clients/1/add", "method":"post", "html":[]}
    keys_to_exclude = ["clientid", "entity", "id"]
    for key in contact_keys:
        if key not in keys_to_exclude:
            key_formatted = format_key_for_form_caption(key)
            key_upper_case = key_formatted.title()
            form_data["html"].append({"type":"text", "caption": key_upper_case, "name": key})
    form_data["html"] = order_html_elements(form_data["html"])
    form_data["html"].append({"type":"submit", "value":"Add Contact"})
    form_data["html"].append({"type":"hidden", "value": "Contact", "name": "entity"})
    form_data["html"].append({"type":"hidden", "value": client_dict["clientid"], "name": "clientid"})
    return form_data


def format_key_for_form_caption(key):
    splits = ["no", "number", "code"]
    if any(string in key for string in splits):
        split_on = [string for string in splits if string in key][0]
        print split_on
        print key.split(split_on)
        key = " ".join(key.split(split_on)) + split_on
    if key == "streetname":
        key = "Street Name"
    return key


# this is basically hard coding, so very fragile
def order_html_elements(list_of_form_fields):
    # desired order: First name, last name, role; Telephone numbers Mobile number, landline; Address info Street number, street name, post code
    ordered_list = []
    names = [entry for entry in list_of_form_fields if "name" in entry["name"] and "street" not in entry["name"]]
    ordered_list.extend(names)
    role = get_specific_entry(list_of_form_fields, "role")
    ordered_list.extend(role)
    email = get_specific_entry(list_of_form_fields, "email")
    email[0]["placeholder"] = "name@example.com"
    ordered_list.extend(email)
    ordered_list.append({ "type" : "p", "html" : "Telephone information"})
    numbers = get_specific_entry(list_of_form_fields, "no")
    ordered_list.extend(numbers)
    ordered_list.append({ "type" : "p", "html" : "Address information"})
    street_info = get_specific_entry(list_of_form_fields, "street")
    ordered_list.extend(street_info)
    post_code = get_specific_entry(list_of_form_fields, "code")
    ordered_list.extend(post_code)
    return ordered_list

def get_specific_entry(list_of_form_fields, keyword):
    return [entry for entry in list_of_form_fields if keyword in entry["name"]]
