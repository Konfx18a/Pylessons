from multiprocessing import Process
from pprint import pprint


class IntroTest:
    __class_attr1 = 10
    __class_attr2 = 20

    def __init__(self, test1, test2, *args, **kwargs):
        self._test1 = test1
        self.__test2 = test2
        self.args = args
        self.kdict = kwargs


    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __str__(self):
        pass

    def test_func1(self):
        pass

    def test_func2(self):
        pass


def void_func():
    pass

def introspection_info(obj):
    intro_dict = {}
    intro_dict['type'] = type(obj)
    intro_dict['ID'] = id(obj)
    intro_dict['Module'] = obj.__module__
    intro_dict['Class'] = obj.__class__
    intro_dict['Local vars'] = locals()
    attribs = []
    funcs =[]
    for i in dir(obj):
        try:
            attr = getattr(obj, i)
        except ValueError:
            continue
        # attribs.append((attr, type(attr)))
        if callable(attr):
            funcs.append(attr)
        else:
            attribs.append(attr)
    intro_dict['attributes'] = attribs
    intro_dict['functions'] = funcs
    return intro_dict

proc = Process(target=void_func())
print(proc.name)
pprint(introspection_info(proc))


dict_ = {1: 5, 2: 6, 3: 7}
it = IntroTest(5,3, 9, 10, dict_)
pprint(introspection_info(it))
print(dir(it))