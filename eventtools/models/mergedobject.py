class MergedObject(object):
    """
    Objects of this class behave as though they are a merge of two other objects (which we'll call General and Special). The attributes of Special override the corresponding attributes of General, *unless* the value of the attribute in Special == None.
    
    All attributes are read-only, to save you from a world of pain.
    
    """

    def __init__(self, general, special):
        self._general = general
        self._special = special
    
    def __repr__(self):
        return "<%(class)s: %(special)s merged into %(general)s>" % {
            'class': type(self).__name__,
            'special': repr(self._special),
            'general': repr(self._general),
        }
    
    def __getattr__(self, value):
        
        try:
            result = getattr(self._special, value)
            if result is None:
                raise AttributeError
        except AttributeError:
            result = getattr(self._general, value)

        return result
        
    def __setattr__(self, attr, value):
        if attr in ['_general', '_special']:
            self.__dict__[attr] = value
        else:
            raise AttributeError("This is a Merged Object. Set the attribute on one of the objects that are being merged.")
            
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._general == other._general and self._special == other._special
        return False