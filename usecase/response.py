from models.models import User
from typing import List


def resp(data):
    res = {}
    res['code'] = data['code']
    if data["code"] == 200:
        res["success"] = True
    else:
        data["success"] = False
    res['data'] = data['data']
    return res


def list_project(data, obj: List[User]):
    for x in obj:
        result = {}
        data['data']
        result['project_id'] = x.email
        result['project_name'] = x.password
        data['data']:list.append(result)
    return data


def refactored_project_by_id(obj: User):
    res = {
        'project_id': obj.email,
        'project_name': obj.password
    }
    return res
