def bson_to_json(bson):
    from bson import json_util
    import json
    json_string = json.dumps(bson, default=json_util.default)
    return json.loads(json_string)