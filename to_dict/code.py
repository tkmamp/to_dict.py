




class toDict():
    '''
    dict parser
    '''    
    def __init__(self):
        pass
    
    
    def to_dict(self, o:object, class_list=[]):
        d = dict()
        if '_to_dict' in o.__dir__():
            return o._to_dict()
        elif '__dict__' in o.__dir__():
            for k in o.__dict__:
                d[k], class_list = self.to_dict(o.__dict__[k], class_list)
            d['classname'] = o.__class__.__name__
            if d['classname'] not in class_list:
                class_list.append(d['classname'])
        else:
            if isinstance(o, list):
                return [self.to_dict(o_i) for o_i in o], class_list
            elif isinstance(o, dict):
                for k in o:
                    d[k] = self.to_dict(o[k], class_list)
            else:
                return o, class_list
        return d, class_list
    
    
    def reconstruct(self, frac, classes:list):
        if isinstance(frac, dict):
            if 'classname' in frac:
                c = None
                for cl in classes:
                    if frac['classname'] == cl.__name__:
                        c = cl
                        break
                if not c:
                    return 
                frac.pop('classname')
                kwargs = self.reconstruct(frac, classes)
                pop_l = []
                for kwarg in kwargs:
                    if not kwarg in c.__init__.__code__.co_varnames:
                        pop_l.append(kwarg)
                for pop_kwarg in pop_l:
                    kwargs.pop(pop_kwarg)
                return c(**kwargs)
            else:
                d = dict()
                for k in frac:
                    d[k] = self.reconstruct(frac[k], classes)
                return d
        elif isinstance(frac, list):
            return [self.reconstruct(frac_i, classes) for frac_i in frac]
        else:
            return frac
            
                
    
    