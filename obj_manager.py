class ObjManager():
    def __init__(self):
        self.obj={}
    def add_obj(self, obj):
        uid = obj.uid
        obj_type = obj.type
        data = {
                "type":obj_type,
                "obj":obj
                }
        self.obj[uid] = data
    def get_type_by_uid(self, uid):
        return self.obj[uid]["type"]

    def get_all_objects(self):
        obj = []
        for value in self.obj.values():
            obj.append(value["obj"])
        return obj
        
    def remove_obj(self, uid):
        del self.obj[uid]

