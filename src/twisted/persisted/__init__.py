# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Twisted Persisted: Utilities for managing persistence.
"""

from twisted.python.deprecate import deprecatedModuleAttribute
from twisted.python.versions import Version

from twisted import persisted

# TODO: define __all__ for modules...
for obj in persisted.__all__:
    deprecatedModuleAttribute(
        Version('Twisted', 'NEXT', 0, 0),
        '{} has been depricated and may be removed in the '
        'next version'.format(obj),
        'twisted.persisted',
        obj)
