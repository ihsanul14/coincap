from pydantic import ValidationError


def Validate(data, models):
    try:
        models.parse_obj(data)
    except ValidationError as e:
        message = e
        for error_dict in e.errors():
            field_name = '.'.join(error_dict['loc'])
            error_msg = error_dict['msg']
            message = f'{error_msg} on {field_name}'
        return message
