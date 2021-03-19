from json import JSONDecoder, JSONEncoder

class DHLEncoder(JSONEncoder):
    def default(self,obj):
        d = {}
        tmp=obj.__dict__
        if ('_sa_instance_state' in tmp):
            tmp.pop('_sa_instance_state')
        d.update(tmp)
        return d