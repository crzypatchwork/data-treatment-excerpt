import json

class validate():
    def __init__(self):
        pass

    def read_requests(self, request):
        if (request.data.__len__() == 0):
            return request.args.to_dict(flat=True)
        else:
            return json.loads(request.data)
