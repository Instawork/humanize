import six

if six.PY2:
    string_types = (basestring,)
else:
    string_types = (str,)

