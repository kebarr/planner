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


def convert_client_dict_form_json(client_dict):
    contact_keys = client_dict.keys()
    form_data = {"action":"clients.html", "html":[{"type":"hidden", "value": client_dict["clientid"]}]}
    for key in contact_keys:
        key = format_key_for_form_caption(key)
        key_upper_case = key.title()
        form_data["html"].append({"type":"text", "caption": key_upper_case})
    return form_data


def format_key_for_form_caption(key):
    splits = ["name", "no", "number", "code"]
    if any(string in key for string in splits):
        split_on = [string for string in splits if string in key][0]
        print split_on
        print key.split(split_on)
        key = " ".join(key.split(split_on)) + split_on
    return key
