

from twisted.trial.unittest import TestCase


# TODO: update me...


class DeprecationTests(TestCase):
    """
    Deprecations in L{twisted.persistent}.
    """
    def helper(self, test, obj):
        path = 'twisted.persisted.{}'.format(obj.__name__)
        warnings = self.flushWarnings(
            [test])
        self.assertEqual(DeprecationWarning, warnings[0]['category'])
        self.assertEqual(1, len(warnings))
        self.assertIn(path, warnings[0]['message'])
