# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Twisted Persisted: Utilities for managing persistence.
"""

from twisted.python.deprecate import deprecatedModuleAttribute
from twisted.python.versions import Version
from twisted.persisted import (
    aot,
    crefutil,
    dirdbm,
    sob,
    styles
)



for mod in [aot, crefutil, dirdbm, sob, styles]:
    for obj in mod.__all__:
        deprecatedModuleAttribute(
            Version('Twisted', 'NEXT', 0, 0),
            '{} has been depricated and may be removed in the '
            'next version'.format(obj),
            mod.__name__,
            obj)
