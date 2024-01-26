from pydantic import ValidationError,BaseModel

class Validator:
    def Validate(self, data, models:BaseModel):
        try:
            models.model_validate(data)
        except ValidationError as e:
            message = e
            for error_dict in e.errors():
                field_name = '.'.join(error_dict['loc'])
                error_msg = error_dict['msg']
                message = f'{error_msg} on {field_name}'
            return message
