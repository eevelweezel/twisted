from twisted.trial.unittest import TestCase



class AotDeprecationTests(TestCase):
    """
    Deprecations in L{twisted.persisted.aot}.
    """
    def helper(self, test, obj):
        path = 'twisted.persisted.aot.{}'.format(obj.__name__)
        warnings = self.flushWarnings(
            [test])
        print(warnings)
        self.assertEqual(DeprecationWarning, warnings[0]['category'])
        self.assertEqual(1, len(warnings))
        self.assertIn(path, warnings[0]['message'])


    def test_aotJellier(self):
        from twisted.persisted.aot import AOTJellier
        self.helper(self.test_aotJellier,
                    AOTJellier)


    def test_aotUnjellier(self):
        from twisted.persisted.aot import AOTUnjellier
        self.helper(self.test_aotUnjellier,
                    AOTUnjellier)


    def test_class(self):
        from twisted.persisted.aot import Class
        self.helper(self.test_class,
                    Class)


    def test_copyreg(self):
        from twisted.persisted.aot import Copyreg
        self.helper(self.test_copyreg,
                    Copyreg)


    def test_deref(self):
        from twisted.persisted.aot import Deref
        self.helper(self.test_deref,
                    Deref)


    def test_dictToKW(self):
        from twisted.persisted.aot import dictToKW
        self.helper(self.test_dictToKW,
                    dictToKW)


    def test_function(self):
        from twisted.persisted.aot import Function
        self.helper(self.test_function,
                    Function)


    def test_getSource(self):
        from twisted.persisted.aot import getSource
        self.helper(self.test_getSource,
                    getSource)


    def test_identify(self):
        from twisted.persisted.aot import indentify
        self.helper(self.test_identify,
                    indentify)


    def test_instance(self):
        from twisted.persisted.aot import Instance
        self.helper(self.test_instance,
                    Instance)


    def test_instanceMethod(self):
        from twisted.persisted.aot import InstanceMethod
        self.helper(self.test_instanceMethod,
                    InstanceMethod)


    def test_jellyToSource(self):
        from twisted.persisted.aot import jellyToSource
        self.helper(self.test_jellyToSource,
                    jellyToSource)


    def test_jellyToAOT(self):
        from twisted.persisted.aot import jellyToAOT
        self.helper(self.test_jellyToAOT,
                    jellyToAOT)


    def test_module(self):
        from twisted.persisted.aot import Module
        self.helper(self.test_module,
                    Module)


    def test_named(self):
        from twisted.persisted.aot import Named
        self.helper(self.test_named,
                    Named)


    def test_nonFormattableDict(self):
        from twisted.persisted.aot import NonFormattableDict
        self.helper(self.test_nonFormattableDict,
                    NonFormattableDict)


    def test_prettify(self):
        from twisted.persisted.aot import prettify
        self.helper(self.test_prettify,
                    prettify)


    def test_ref(self):
        from twisted.persisted.aot import Ref
        self.helper(self.test_ref,
                    Ref)


    def test_unjellyFromSource(self):
        from twisted.persisted.aot import unjellyFromSource
        self.helper(self.test_unjellyFromSource,
                    unjellyFromSource)


    def test_unjellyFromAOT(self):
        from twisted.persisted.aot import unjellyFromAOT
        self.helper(self.test_unjellyFromAOT,
                    unjellyFromAOT)



class CrefutilDeprecationTests(TestCase):
    """
    Deprecations in L{twisted.persisted.crefutil}.
    """
    def helper(self, test, obj):
        path = 'twisted.persisted.crefutil.{}'.format(obj.__name__)
        warnings = self.flushWarnings(
            [test])
        self.assertEqual(DeprecationWarning, warnings[0]['category'])
        self.assertEqual(1, len(warnings))
        self.assertIn(path, warnings[0]['message'])


    def test_notKnown(self):
        from twisted.persisted.crefutil import NotKnown
        self.helper(self.test_notKnown,
                    NotKnown)



class DirDBMDeprecationTests(TestCase):
    """
    Deprecations in L{twisted.persisted.dirdbm}.
    """
    def helper(self, test, obj):
        path = 'twisted.persisted.dirdbm.{}'.format(obj.__name__)
        warnings = self.flushWarnings(
            [test])
        self.assertEqual(DeprecationWarning, warnings[0]['category'])
        self.assertEqual(1, len(warnings))
        self.assertIn(path, warnings[0]['message'])


    def test_open(self):
        from twisted.persisted.dirdbm import open
        self.helper(self.test_open,
                    open)


    def test_dirDBM(self):
        from twisted.persisted.dirdbm import DirDBM
        self.helper(self.test_dirDBM,
                    DirDBM)


    def test_shelf(self):
        from twisted.persisted.dirdbm import Shelf
        self.helper(self.test_shelf,
                    Shelf)



class SobDeprecationTests(TestCase):
    """
    Deprecations in L{twisted.persisted.sob}.
    """
    def helper(self, test, obj):
        path = 'twisted.persisted.sob.{}'.format(obj.__name__)
        warnings = self.flushWarnings(
            [test])
        self.assertEqual(DeprecationWarning, warnings[0]['category'])
        self.assertEqual(1, len(warnings))
        self.assertIn(path, warnings[0]['message'])


    def test_loadValueFromFile(self):
        from twisted.persisted.sob import loadValueFromFile
        self.helper(self.test_loadValueFromFile,
                    loadValueFromFile)


    def test_load(self):
        from twisted.persisted.sob import load
        self.helper(self.test_load,
                    load)


    def test_persistent(self):
        from twisted.persisted.sob import Persistent
        self.helper(self.test_persistent,
                    Persistent)


    def test_persistant(self):
        from twisted.persisted.sob import Persistant
        self.helper(self.test_persistant,
                    Persistant)


    def test_ipersistable(self):
        from twisted.persisted.sob import IPersistable
        self.helper(self.test_ipersistable,
                    IPersistable)


    def test_guessType(self):
        from twisted.persisted.sob import guessType
        self.helper(self.test_guessType,
                    guessType)




class StylesDeprecationTests(TestCase):
    """
    Deprecations in L{twisted.persisted.styles}.
    """
    def helper(self, test, obj):
        path = 'twisted.persisted.styles.{}'.format(obj.__name__)
        warnings = self.flushWarnings(
            [test])
        self.assertEqual(DeprecationWarning, warnings[0]['category'])
        self.assertEqual(1, len(warnings))
        self.assertIn(path, warnings[0]['message'])


    def test_doUpgrade(self):
        from twisted.persisted.styles import doUpgrade
        self.helper(self.test_doUpgrade,
                    doUpgrade)


    def test_ephemeral(self):
        from twisted.persisted.styles import Ephemeral
        self.helper(self.test_ephemeral,
                    Ephemeral)


    def test_pickleMethod(self):
        from twisted.persisted.styles import pickleMethod
        self.helper(self.test_pickleMethod,
                    pickleMethod)


    def test_pickleModule(self):
        from twisted.persisted.styles import pickleModule
        self.helper(self.test_pickleModule,
                    pickleModule)


    def test_pickleStringI(self):
        from twisted.persisted.styles import pickleStringI
        self.helper(self.test_pickleStringI,
                    pickleStringI)


    def test_pickleStringO(self):
        from twisted.persisted.styles import pickleStringO
        self.helper(self.test_pickleStringO,
                    pickleStringO)


    def test_unpickleMethod(self):
        from twisted.persisted.styles import unpickleMethod
        self.helper(self.test_unpickleMethod,
                    unpickleMethod)


    def test_unpickleModule(self):
        from twisted.persisted.styles import unpickleModule
        self.helper(self.test_unpickleModule,
                    unpickleModule)


    def test_unpickleStringI(self):
        from twisted.persisted.styles import unpickleStringI
        self.helper(self.test_unpickleStringI,
                    unpickleStringI)


    def test_unpickleStringO(self):
        from twisted.persisted.styles import unpickleStringO
        self.helper(self.test_unpickleStringO,
                    unpickleStringO)


    def test_versioned(self):
        from twisted.persisted.styles import Versioned
        self.helper(self.test_versioned,
                    Versioned)
