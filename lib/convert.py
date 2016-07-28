__author__ = 'safetydoor'
# -*- coding: utf-8 -*-

class Convert(object):
    @staticmethod
    def dict2model(dict,model):
        for field in model._fields:
            if field in dict:
                model.__setattr__(field,dict[field])
        return model
    @staticmethod
    def dic_decode_utf8(dic):
        for key in dic.keys():
            val = dic[key]
            t = type(dic[key])
            if t is unicode:
                if val:
                    dic[key] = dic[key].encode('utf-8')
            elif t is list:
                list_res = []
                for v in val:
                    vt = type(v)
                    if vt is dict:
                        res = Convert.dic_decode_utf8(v)
                        list_res.append(res)
                pass
                dic[key] = list_res
        return dic

