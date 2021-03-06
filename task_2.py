def cmp_to_key(comparator):
     class K(object):
         def __init__(self, obj, *args):
             self.obj = obj
         def __lt__(self, other):
             return comparator(self.obj, other.obj) < 0
         def __gt__(self, other):
            return comparator(self.obj, other.obj) > 0
         def __eq__(self, other):
             return comparator(self.obj, other.obj) == 0
     return K