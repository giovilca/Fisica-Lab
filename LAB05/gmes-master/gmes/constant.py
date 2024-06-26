# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_constant')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_constant')
    _constant = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_constant', [dirname(__file__)])
        except ImportError:
            import _constant
            return _constant
        try:
            _mod = imp.load_module('_constant', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _constant = swig_import_helper()
    del swig_import_helper
else:
    import _constant
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class _component(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _component, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _component, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._component_get_tag)
    else:
        get_tag = _constant._component_get_tag
    __swig_destroy__ = _constant.delete__component
    __del__ = lambda self: None
_component_swigregister = _constant._component_swigregister
_component_swigregister(_component)
cvar = _constant.cvar
pi = cvar.pi
h = cvar.h
hbar = cvar.hbar
c0 = cvar.c0
mu0 = cvar.mu0
eps0 = cvar.eps0
Z0 = cvar.Z0
YOTTA = cvar.YOTTA
ZETTA = cvar.ZETTA
EXA = cvar.EXA
PETA = cvar.PETA
TERA = cvar.TERA
GIGA = cvar.GIGA
MEGA = cvar.MEGA
KILO = cvar.KILO
MILLI = cvar.MILLI
MICRO = cvar.MICRO
NANO = cvar.NANO
PICO = cvar.PICO
FEMTO = cvar.FEMTO
ATTO = cvar.ATTO
ZEPTO = cvar.ZEPTO
YOCTO = cvar.YOCTO

def _component_get_tag():
    return _constant._component_get_tag()
_component_get_tag = _constant._component_get_tag

class _electric(_component):
    __swig_setmethods__ = {}
    for _s in [_component]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _electric, name, value)
    __swig_getmethods__ = {}
    for _s in [_component]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _electric, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._electric_get_tag)
    else:
        get_tag = _constant._electric_get_tag
    __swig_destroy__ = _constant.delete__electric
    __del__ = lambda self: None
_electric_swigregister = _constant._electric_swigregister
_electric_swigregister(_electric)

def _electric_get_tag():
    return _constant._electric_get_tag()
_electric_get_tag = _constant._electric_get_tag

class _ex(_electric):
    __swig_setmethods__ = {}
    for _s in [_electric]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _ex, name, value)
    __swig_getmethods__ = {}
    for _s in [_electric]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _ex, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._ex_get_tag)
    else:
        get_tag = _constant._ex_get_tag
    __swig_destroy__ = _constant.delete__ex
    __del__ = lambda self: None
_ex_swigregister = _constant._ex_swigregister
_ex_swigregister(_ex)

def _ex_get_tag():
    return _constant._ex_get_tag()
_ex_get_tag = _constant._ex_get_tag

class _ey(_electric):
    __swig_setmethods__ = {}
    for _s in [_electric]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _ey, name, value)
    __swig_getmethods__ = {}
    for _s in [_electric]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _ey, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._ey_get_tag)
    else:
        get_tag = _constant._ey_get_tag
    __swig_destroy__ = _constant.delete__ey
    __del__ = lambda self: None
_ey_swigregister = _constant._ey_swigregister
_ey_swigregister(_ey)

def _ey_get_tag():
    return _constant._ey_get_tag()
_ey_get_tag = _constant._ey_get_tag

class _ez(_electric):
    __swig_setmethods__ = {}
    for _s in [_electric]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _ez, name, value)
    __swig_getmethods__ = {}
    for _s in [_electric]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _ez, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._ez_get_tag)
    else:
        get_tag = _constant._ez_get_tag
    __swig_destroy__ = _constant.delete__ez
    __del__ = lambda self: None
_ez_swigregister = _constant._ez_swigregister
_ez_swigregister(_ez)

def _ez_get_tag():
    return _constant._ez_get_tag()
_ez_get_tag = _constant._ez_get_tag

class _magnetic(_component):
    __swig_setmethods__ = {}
    for _s in [_component]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _magnetic, name, value)
    __swig_getmethods__ = {}
    for _s in [_component]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _magnetic, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._magnetic_get_tag)
    else:
        get_tag = _constant._magnetic_get_tag
    __swig_destroy__ = _constant.delete__magnetic
    __del__ = lambda self: None
_magnetic_swigregister = _constant._magnetic_swigregister
_magnetic_swigregister(_magnetic)

def _magnetic_get_tag():
    return _constant._magnetic_get_tag()
_magnetic_get_tag = _constant._magnetic_get_tag

class _hx(_magnetic):
    __swig_setmethods__ = {}
    for _s in [_magnetic]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _hx, name, value)
    __swig_getmethods__ = {}
    for _s in [_magnetic]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _hx, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._hx_get_tag)
    else:
        get_tag = _constant._hx_get_tag
    __swig_destroy__ = _constant.delete__hx
    __del__ = lambda self: None
_hx_swigregister = _constant._hx_swigregister
_hx_swigregister(_hx)

def _hx_get_tag():
    return _constant._hx_get_tag()
_hx_get_tag = _constant._hx_get_tag

class _hy(_magnetic):
    __swig_setmethods__ = {}
    for _s in [_magnetic]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _hy, name, value)
    __swig_getmethods__ = {}
    for _s in [_magnetic]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _hy, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._hy_get_tag)
    else:
        get_tag = _constant._hy_get_tag
    __swig_destroy__ = _constant.delete__hy
    __del__ = lambda self: None
_hy_swigregister = _constant._hy_swigregister
_hy_swigregister(_hy)

def _hy_get_tag():
    return _constant._hy_get_tag()
_hy_get_tag = _constant._hy_get_tag

class _hz(_magnetic):
    __swig_setmethods__ = {}
    for _s in [_magnetic]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _hz, name, value)
    __swig_getmethods__ = {}
    for _s in [_magnetic]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _hz, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._hz_get_tag)
    else:
        get_tag = _constant._hz_get_tag
    __swig_destroy__ = _constant.delete__hz
    __del__ = lambda self: None
_hz_swigregister = _constant._hz_swigregister
_hz_swigregister(_hz)

def _hz_get_tag():
    return _constant._hz_get_tag()
_hz_get_tag = _constant._hz_get_tag

class _electriccurrent(_component):
    __swig_setmethods__ = {}
    for _s in [_component]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _electriccurrent, name, value)
    __swig_getmethods__ = {}
    for _s in [_component]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _electriccurrent, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._electriccurrent_get_tag)
    else:
        get_tag = _constant._electriccurrent_get_tag
    __swig_destroy__ = _constant.delete__electriccurrent
    __del__ = lambda self: None
_electriccurrent_swigregister = _constant._electriccurrent_swigregister
_electriccurrent_swigregister(_electriccurrent)

def _electriccurrent_get_tag():
    return _constant._electriccurrent_get_tag()
_electriccurrent_get_tag = _constant._electriccurrent_get_tag

class _jx(_electriccurrent):
    __swig_setmethods__ = {}
    for _s in [_electriccurrent]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _jx, name, value)
    __swig_getmethods__ = {}
    for _s in [_electriccurrent]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _jx, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._jx_get_tag)
    else:
        get_tag = _constant._jx_get_tag
    __swig_destroy__ = _constant.delete__jx
    __del__ = lambda self: None
_jx_swigregister = _constant._jx_swigregister
_jx_swigregister(_jx)

def _jx_get_tag():
    return _constant._jx_get_tag()
_jx_get_tag = _constant._jx_get_tag

class _jy(_electriccurrent):
    __swig_setmethods__ = {}
    for _s in [_electriccurrent]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _jy, name, value)
    __swig_getmethods__ = {}
    for _s in [_electriccurrent]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _jy, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._jy_get_tag)
    else:
        get_tag = _constant._jy_get_tag
    __swig_destroy__ = _constant.delete__jy
    __del__ = lambda self: None
_jy_swigregister = _constant._jy_swigregister
_jy_swigregister(_jy)

def _jy_get_tag():
    return _constant._jy_get_tag()
_jy_get_tag = _constant._jy_get_tag

class _jz(_electriccurrent):
    __swig_setmethods__ = {}
    for _s in [_electriccurrent]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _jz, name, value)
    __swig_getmethods__ = {}
    for _s in [_electriccurrent]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _jz, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._jz_get_tag)
    else:
        get_tag = _constant._jz_get_tag
    __swig_destroy__ = _constant.delete__jz
    __del__ = lambda self: None
_jz_swigregister = _constant._jz_swigregister
_jz_swigregister(_jz)

def _jz_get_tag():
    return _constant._jz_get_tag()
_jz_get_tag = _constant._jz_get_tag

class _magneticcurrent(_component):
    __swig_setmethods__ = {}
    for _s in [_component]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _magneticcurrent, name, value)
    __swig_getmethods__ = {}
    for _s in [_component]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _magneticcurrent, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._magneticcurrent_get_tag)
    else:
        get_tag = _constant._magneticcurrent_get_tag
    __swig_destroy__ = _constant.delete__magneticcurrent
    __del__ = lambda self: None
_magneticcurrent_swigregister = _constant._magneticcurrent_swigregister
_magneticcurrent_swigregister(_magneticcurrent)

def _magneticcurrent_get_tag():
    return _constant._magneticcurrent_get_tag()
_magneticcurrent_get_tag = _constant._magneticcurrent_get_tag

class _mx(_magneticcurrent):
    __swig_setmethods__ = {}
    for _s in [_magneticcurrent]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _mx, name, value)
    __swig_getmethods__ = {}
    for _s in [_magneticcurrent]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _mx, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._mx_get_tag)
    else:
        get_tag = _constant._mx_get_tag
    __swig_destroy__ = _constant.delete__mx
    __del__ = lambda self: None
_mx_swigregister = _constant._mx_swigregister
_mx_swigregister(_mx)

def _mx_get_tag():
    return _constant._mx_get_tag()
_mx_get_tag = _constant._mx_get_tag

class _my(_magneticcurrent):
    __swig_setmethods__ = {}
    for _s in [_magneticcurrent]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _my, name, value)
    __swig_getmethods__ = {}
    for _s in [_magneticcurrent]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _my, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._my_get_tag)
    else:
        get_tag = _constant._my_get_tag
    __swig_destroy__ = _constant.delete__my
    __del__ = lambda self: None
_my_swigregister = _constant._my_swigregister
_my_swigregister(_my)

def _my_get_tag():
    return _constant._my_get_tag()
_my_get_tag = _constant._my_get_tag

class _mz(_magneticcurrent):
    __swig_setmethods__ = {}
    for _s in [_magneticcurrent]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _mz, name, value)
    __swig_getmethods__ = {}
    for _s in [_magneticcurrent]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _mz, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._mz_get_tag)
    else:
        get_tag = _constant._mz_get_tag
    __swig_destroy__ = _constant.delete__mz
    __del__ = lambda self: None
_mz_swigregister = _constant._mz_swigregister
_mz_swigregister(_mz)

def _mz_get_tag():
    return _constant._mz_get_tag()
_mz_get_tag = _constant._mz_get_tag

class _directional(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, _directional, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, _directional, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._directional_get_tag)
    else:
        get_tag = _constant._directional_get_tag
    __swig_destroy__ = _constant.delete__directional
    __del__ = lambda self: None
_directional_swigregister = _constant._directional_swigregister
_directional_swigregister(_directional)

def _directional_get_tag():
    return _constant._directional_get_tag()
_directional_get_tag = _constant._directional_get_tag

class _x(_directional):
    __swig_setmethods__ = {}
    for _s in [_directional]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _x, name, value)
    __swig_getmethods__ = {}
    for _s in [_directional]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _x, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._x_get_tag)
    else:
        get_tag = _constant._x_get_tag
    __swig_destroy__ = _constant.delete__x
    __del__ = lambda self: None
_x_swigregister = _constant._x_swigregister
_x_swigregister(_x)

def _x_get_tag():
    return _constant._x_get_tag()
_x_get_tag = _constant._x_get_tag

class _y(_directional):
    __swig_setmethods__ = {}
    for _s in [_directional]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _y, name, value)
    __swig_getmethods__ = {}
    for _s in [_directional]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _y, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._y_get_tag)
    else:
        get_tag = _constant._y_get_tag
    __swig_destroy__ = _constant.delete__y
    __del__ = lambda self: None
_y_swigregister = _constant._y_swigregister
_y_swigregister(_y)

def _y_get_tag():
    return _constant._y_get_tag()
_y_get_tag = _constant._y_get_tag

class _z(_directional):
    __swig_setmethods__ = {}
    for _s in [_directional]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _z, name, value)
    __swig_getmethods__ = {}
    for _s in [_directional]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _z, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._z_get_tag)
    else:
        get_tag = _constant._z_get_tag
    __swig_destroy__ = _constant.delete__z
    __del__ = lambda self: None
_z_swigregister = _constant._z_swigregister
_z_swigregister(_z)

def _z_get_tag():
    return _constant._z_get_tag()
_z_get_tag = _constant._z_get_tag

class _plus_x(_x):
    __swig_setmethods__ = {}
    for _s in [_x]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _plus_x, name, value)
    __swig_getmethods__ = {}
    for _s in [_x]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _plus_x, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._plus_x_get_tag)
    else:
        get_tag = _constant._plus_x_get_tag
    if _newclass:
        get_vector = staticmethod(_constant._plus_x_get_vector)
    else:
        get_vector = _constant._plus_x_get_vector
    __swig_destroy__ = _constant.delete__plus_x
    __del__ = lambda self: None
_plus_x_swigregister = _constant._plus_x_swigregister
_plus_x_swigregister(_plus_x)

def _plus_x_get_tag():
    return _constant._plus_x_get_tag()
_plus_x_get_tag = _constant._plus_x_get_tag

def _plus_x_get_vector():
    return _constant._plus_x_get_vector()
_plus_x_get_vector = _constant._plus_x_get_vector

class _minus_x(_x):
    __swig_setmethods__ = {}
    for _s in [_x]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _minus_x, name, value)
    __swig_getmethods__ = {}
    for _s in [_x]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _minus_x, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._minus_x_get_tag)
    else:
        get_tag = _constant._minus_x_get_tag
    if _newclass:
        get_vector = staticmethod(_constant._minus_x_get_vector)
    else:
        get_vector = _constant._minus_x_get_vector
    __swig_destroy__ = _constant.delete__minus_x
    __del__ = lambda self: None
_minus_x_swigregister = _constant._minus_x_swigregister
_minus_x_swigregister(_minus_x)

def _minus_x_get_tag():
    return _constant._minus_x_get_tag()
_minus_x_get_tag = _constant._minus_x_get_tag

def _minus_x_get_vector():
    return _constant._minus_x_get_vector()
_minus_x_get_vector = _constant._minus_x_get_vector

class _plus_y(_y):
    __swig_setmethods__ = {}
    for _s in [_y]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _plus_y, name, value)
    __swig_getmethods__ = {}
    for _s in [_y]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _plus_y, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._plus_y_get_tag)
    else:
        get_tag = _constant._plus_y_get_tag
    if _newclass:
        get_vector = staticmethod(_constant._plus_y_get_vector)
    else:
        get_vector = _constant._plus_y_get_vector
    __swig_destroy__ = _constant.delete__plus_y
    __del__ = lambda self: None
_plus_y_swigregister = _constant._plus_y_swigregister
_plus_y_swigregister(_plus_y)

def _plus_y_get_tag():
    return _constant._plus_y_get_tag()
_plus_y_get_tag = _constant._plus_y_get_tag

def _plus_y_get_vector():
    return _constant._plus_y_get_vector()
_plus_y_get_vector = _constant._plus_y_get_vector

class _minus_y(_y):
    __swig_setmethods__ = {}
    for _s in [_y]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _minus_y, name, value)
    __swig_getmethods__ = {}
    for _s in [_y]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _minus_y, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._minus_y_get_tag)
    else:
        get_tag = _constant._minus_y_get_tag
    if _newclass:
        get_vector = staticmethod(_constant._minus_y_get_vector)
    else:
        get_vector = _constant._minus_y_get_vector
    __swig_destroy__ = _constant.delete__minus_y
    __del__ = lambda self: None
_minus_y_swigregister = _constant._minus_y_swigregister
_minus_y_swigregister(_minus_y)

def _minus_y_get_tag():
    return _constant._minus_y_get_tag()
_minus_y_get_tag = _constant._minus_y_get_tag

def _minus_y_get_vector():
    return _constant._minus_y_get_vector()
_minus_y_get_vector = _constant._minus_y_get_vector

class _plus_z(_z):
    __swig_setmethods__ = {}
    for _s in [_z]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _plus_z, name, value)
    __swig_getmethods__ = {}
    for _s in [_z]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _plus_z, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._plus_z_get_tag)
    else:
        get_tag = _constant._plus_z_get_tag
    if _newclass:
        get_vector = staticmethod(_constant._plus_z_get_vector)
    else:
        get_vector = _constant._plus_z_get_vector
    __swig_destroy__ = _constant.delete__plus_z
    __del__ = lambda self: None
_plus_z_swigregister = _constant._plus_z_swigregister
_plus_z_swigregister(_plus_z)

def _plus_z_get_tag():
    return _constant._plus_z_get_tag()
_plus_z_get_tag = _constant._plus_z_get_tag

def _plus_z_get_vector():
    return _constant._plus_z_get_vector()
_plus_z_get_vector = _constant._plus_z_get_vector

class _minus_z(_z):
    __swig_setmethods__ = {}
    for _s in [_z]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, _minus_z, name, value)
    __swig_getmethods__ = {}
    for _s in [_z]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, _minus_z, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        get_tag = staticmethod(_constant._minus_z_get_tag)
    else:
        get_tag = _constant._minus_z_get_tag
    if _newclass:
        get_vector = staticmethod(_constant._minus_z_get_vector)
    else:
        get_vector = _constant._minus_z_get_vector
    __swig_destroy__ = _constant.delete__minus_z
    __del__ = lambda self: None
_minus_z_swigregister = _constant._minus_z_swigregister
_minus_z_swigregister(_minus_z)

def _minus_z_get_tag():
    return _constant._minus_z_get_tag()
_minus_z_get_tag = _constant._minus_z_get_tag

def _minus_z_get_vector():
    return _constant._minus_z_get_vector()
_minus_z_get_vector = _constant._minus_z_get_vector


class Component(_component):
    tag = _component_get_tag()

class Electric(Component):
  tag = _electric_get_tag()

class Ex(Electric):
    tag = _ex_get_tag()

    @classmethod
    def str(cls):
        return 'ex'

class Ey(Electric):
    tag = _ey_get_tag()

    @classmethod
    def str(cls):
        return 'ey'

class Ez(Electric):
    tag = _ez_get_tag()

    @classmethod
    def str(cls):
        return 'ez'

class Magnetic(Component):
    tag = _magnetic_get_tag()

class Hx(Magnetic):
    tag = _hx_get_tag()

    @classmethod
    def str(cls):
        return 'hx'

class Hy(Magnetic):
    tag = _hy_get_tag()

    @classmethod
    def str(cls):
        return 'hy'

class Hz(Magnetic):
    tag = _hz_get_tag()

    @classmethod
    def str(cls):
        return 'hz'

class ElectricCurrent(Component):
  tag = _electriccurrent_get_tag()

class Jx(ElectricCurrent):
    tag = _jx_get_tag()

    @classmethod
    def str(cls):
        return 'jx'

class Jy(ElectricCurrent):
    tag = _jy_get_tag()

    @classmethod
    def str(cls):
        return 'jy'

class Jz(ElectricCurrent):
    tag = _jz_get_tag()

    @classmethod
    def str(cls):
        return 'jz'

class MagneticCurrent(Component):
    tag = _magneticcurrent_get_tag()

class Mx(Magnetic):
    tag = _mx_get_tag()

    @classmethod
    def str(cls):
        return 'mx'

class My(MagneticCurrent):
    tag = _my_get_tag()

    @classmethod
    def str(cls):
        return 'my'

class Mz(MagneticCurrent):
    tag = _mz_get_tag()

    @classmethod
    def str(cls):
        return 'mz'

class Directional(_directional):
    tag = _directional_get_tag()

class X(Directional):
    tag = _x_get_tag()

    @classmethod
    def str(cls):
        return 'x'

class Y(Directional):
    tag = _y_get_tag()

    @classmethod
    def str(cls):
        return 'y'

class Z(Directional):
    tag = _z_get_tag()

    @classmethod
    def str(cls):
        return 'z'

class PlusX(X):
    tag = _plus_x_get_tag()
    vector = _plus_x_get_vector()
    @classmethod
    def str(cls):
        return '+x'

class MinusX(X):
    tag = _minus_x_get_tag()
    vector = _minus_x_get_vector()

    @classmethod
    def str(cls):
        return '-x'

class PlusY(Y):
    tag = _plus_y_get_tag()
    vector = _plus_y_get_vector()

    @classmethod
    def str(cls):
        return '+y'

class MinusY(Y):
    tag = _minus_y_get_tag()
    vector = _minus_y_get_vector()

    @classmethod
    def str(cls):
        return '-y'

class PlusZ(Z):
    tag = _plus_z_get_tag()
    vector = _plus_z_get_vector()

    @classmethod
    def str(cls):
        return '+z'

class MinusZ(Z):
    tag = _minus_z_get_tag()
    vector = _minus_z_get_vector()

    @classmethod
    def str(cls):
        return '-z'

# This file is compatible with both classic and new-style classes.


