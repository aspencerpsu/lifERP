# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify


################## Spencer Tech Consulting Edits ############################

""" Use this file as a replacement to the initial downloaded pywraplp file"""

# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pywraplp')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pywraplp')
    _pywraplp = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pywraplp', [dirname(__file__)])
        except ImportError:
            import _pywraplp
            return _pywraplp
        if fp is not None:
            try:
                _mod = imp.load_module('_pywraplp', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pywraplp = swig_import_helper()
    del swig_import_helper
else:
    import _pywraplp
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

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pywraplp.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _pywraplp.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pywraplp.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pywraplp.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pywraplp.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pywraplp.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pywraplp.SwigPyIterator_copy(self)

    def next(self):
        return _pywraplp.SwigPyIterator_next(self)

    def __next__(self):
        return _pywraplp.SwigPyIterator___next__(self)

    def previous(self):
        return _pywraplp.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pywraplp.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pywraplp.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pywraplp.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pywraplp.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pywraplp.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pywraplp.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pywraplp.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _pywraplp.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


import numbers
from ortools.linear_solver.linear_solver_natural_api import OFFSET_KEY
from ortools.linear_solver.linear_solver_natural_api import inf
from ortools.linear_solver.linear_solver_natural_api import LinearExpr
from ortools.linear_solver.linear_solver_natural_api import ProductCst
from ortools.linear_solver.linear_solver_natural_api import Sum
from ortools.linear_solver.linear_solver_natural_api import SumArray
from ortools.linear_solver.linear_solver_natural_api import SumCst
from ortools.linear_solver.linear_solver_natural_api import LinearConstraint
from ortools.linear_solver.linear_solver_natural_api import VariableExpr

class Solver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Solver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Solver, name)
    __repr__ = _swig_repr
    CLP_LINEAR_PROGRAMMING = _pywraplp.Solver_CLP_LINEAR_PROGRAMMING
    GLOP_LINEAR_PROGRAMMING = _pywraplp.Solver_GLOP_LINEAR_PROGRAMMING
    CBC_MIXED_INTEGER_PROGRAMMING = _pywraplp.Solver_CBC_MIXED_INTEGER_PROGRAMMING
    BOP_INTEGER_PROGRAMMING = _pywraplp.Solver_BOP_INTEGER_PROGRAMMING

    def __init__(self, name, problem_type):
        this = _pywraplp.new_Solver(name, problem_type)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pywraplp.delete_Solver
    __del__ = lambda self: None
    if _newclass:
        SupportsProblemType = staticmethod(_pywraplp.Solver_SupportsProblemType)
    else:
        SupportsProblemType = _pywraplp.Solver_SupportsProblemType

    def Clear(self):
        return _pywraplp.Solver_Clear(self)

    def NumVariables(self):
        return _pywraplp.Solver_NumVariables(self)

    def LookupVariable(self, var_name):
        return _pywraplp.Solver_LookupVariable(self, var_name)

    def NumVar(self, lb, ub, name):
        return _pywraplp.Solver_NumVar(self, lb, ub, name)

    def IntVar(self, lb, ub, name):
        return _pywraplp.Solver_IntVar(self, lb, ub, name)

    def BoolVar(self, name):
        return _pywraplp.Solver_BoolVar(self, name)

    def NumConstraints(self):
        return _pywraplp.Solver_NumConstraints(self)

    def LookupConstraint(self, constraint_name):
        return _pywraplp.Solver_LookupConstraint(self, constraint_name)

    def Constraint(self, *args):
        return _pywraplp.Solver_Constraint(self, *args)

    def Objective(self):
        return _pywraplp.Solver_Objective(self)
    OPTIMAL = _pywraplp.Solver_OPTIMAL
    FEASIBLE = _pywraplp.Solver_FEASIBLE
    INFEASIBLE = _pywraplp.Solver_INFEASIBLE
    UNBOUNDED = _pywraplp.Solver_UNBOUNDED
    ABNORMAL = _pywraplp.Solver_ABNORMAL
    NOT_SOLVED = _pywraplp.Solver_NOT_SOLVED

    def Solve(self, *args):
        return _pywraplp.Solver_Solve(self, *args)

    def ComputeConstraintActivities(self):
        return _pywraplp.Solver_ComputeConstraintActivities(self)

    def VerifySolution(self, tolerance, log_errors):
        return _pywraplp.Solver_VerifySolution(self, tolerance, log_errors)

    def InterruptSolve(self):
        return _pywraplp.Solver_InterruptSolve(self)

    def SetSolverSpecificParametersAsString(self, parameters):
        return _pywraplp.Solver_SetSolverSpecificParametersAsString(self, parameters)
    FREE = _pywraplp.Solver_FREE
    AT_LOWER_BOUND = _pywraplp.Solver_AT_LOWER_BOUND
    AT_UPPER_BOUND = _pywraplp.Solver_AT_UPPER_BOUND
    FIXED_VALUE = _pywraplp.Solver_FIXED_VALUE
    BASIC = _pywraplp.Solver_BASIC
    if _newclass:
        infinity = staticmethod(_pywraplp.Solver_infinity)
    else:
        infinity = _pywraplp.Solver_infinity

    def EnableOutput(self):
        return _pywraplp.Solver_EnableOutput(self)

    def SuppressOutput(self):
        return _pywraplp.Solver_SuppressOutput(self)

    def set_time_limit(self, time_limit_milliseconds):
        return _pywraplp.Solver_set_time_limit(self, time_limit_milliseconds)

    def wall_time(self):
        return _pywraplp.Solver_wall_time(self)

    def iterations(self):
        return _pywraplp.Solver_iterations(self)

    def nodes(self):
        return _pywraplp.Solver_nodes(self)

    def ComputeExactConditionNumber(self):
        return _pywraplp.Solver_ComputeExactConditionNumber(self)

    def ExportModelAsLpFormat(self, obfuscated):
        return _pywraplp.Solver_ExportModelAsLpFormat(self, obfuscated)

    def ExportModelAsMpsFormat(self, fixed_format, obfuscated):
        return _pywraplp.Solver_ExportModelAsMpsFormat(self, fixed_format, obfuscated)

    def LoadModelFromProto(self, input_model):
        return _pywraplp.Solver_LoadModelFromProto(self, input_model)

    def Add(self, constraint, name=''):
      if isinstance(constraint, bool):
        if constraint:
          return self.RowConstraint(0, 0, name)
        else:
          return self.RowConstraint(1, 1, name)
      else:
        return constraint.Extract(self, name)

    def Sum(self, expr_array):
      result = SumArray(expr_array)
      return result

    def RowConstraint(self, *args):
      return self.Constraint(*args)

    def Minimize(self, expr, variables=None):
      objective = self.Objective()
      objective.Clear()
      objective.SetMinimization()
      if isinstance(expr, numbers.Number):
          objective.AddOffset(expr)
      else:
      	  objective.AddOffset(0)
      	  if not isinstance(expr, list):
	  	coeffs = expr.GetCoeffs()
		for v, c in coeffs.items():
		     objective.SetCoefficient(v, float(c))
	  else:
	  	coeffs = [(variables[expr.index(x)], x) for x in expr]
		for v,c in coeffs:
		     objective.SetCoefficient(v, c)

    def Maximize(self, expr,variables=None):
      objective = self.Objective()
      objective.Clear()
      objective.SetMaximization()
      if isinstance(expr, numbers.Number):
          objective.AddOffset(expr)
      else: 
          objective.AddOffset(0)
          if not isinstance(expr, list):
		  coeffs = expr.GetCoeffs()
		  for v, c in coeffs.items():
		       objective.SetCoefficient(v, float(c))
	  else:
	  	coeffs = [(variables[expr.index(x)],x) for x in expr]
		for v,c in coeffs:
		    objective.SetCoefficient(v,c)

    if _newclass:
        Infinity = staticmethod(_pywraplp.Solver_Infinity)
    else:
        Infinity = _pywraplp.Solver_Infinity

    def SetTimeLimit(self, x):
        return _pywraplp.Solver_SetTimeLimit(self, x)

    def WallTime(self):
        return _pywraplp.Solver_WallTime(self)

    def Iterations(self):
        return _pywraplp.Solver_Iterations(self)
Solver_swigregister = _pywraplp.Solver_swigregister
Solver_swigregister(Solver)

def Solver_SupportsProblemType(problem_type):
    return _pywraplp.Solver_SupportsProblemType(problem_type)
Solver_SupportsProblemType = _pywraplp.Solver_SupportsProblemType

def Solver_infinity():
    return _pywraplp.Solver_infinity()
Solver_infinity = _pywraplp.Solver_infinity

def Solver_Infinity():
    return _pywraplp.Solver_Infinity()
Solver_Infinity = _pywraplp.Solver_Infinity


def __lshift__(os, status):
    return _pywraplp.__lshift__(os, status)
__lshift__ = _pywraplp.__lshift__
class Objective(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Objective, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Objective, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def Clear(self):
        return _pywraplp.Objective_Clear(self)

    def SetCoefficient(self, var, coeff):
        return _pywraplp.Objective_SetCoefficient(self, var, coeff)

    def GetCoefficient(self, var):
        return _pywraplp.Objective_GetCoefficient(self, var)

    def SetOffset(self, value):
        return _pywraplp.Objective_SetOffset(self, value)

    def offset(self):
        return _pywraplp.Objective_offset(self)

    def AddOffset(self, value):
        return _pywraplp.Objective_AddOffset(self, value)

    def SetOptimizationDirection(self, maximize):
        return _pywraplp.Objective_SetOptimizationDirection(self, maximize)

    def SetMinimization(self):
        return _pywraplp.Objective_SetMinimization(self)

    def SetMaximization(self):
        return _pywraplp.Objective_SetMaximization(self)

    def maximization(self):
        return _pywraplp.Objective_maximization(self)

    def minimization(self):
        return _pywraplp.Objective_minimization(self)

    def Value(self):
        return _pywraplp.Objective_Value(self)

    def BestBound(self):
        return _pywraplp.Objective_BestBound(self)

    def Offset(self):
        return _pywraplp.Objective_Offset(self)
    __swig_destroy__ = _pywraplp.delete_Objective
    __del__ = lambda self: None
Objective_swigregister = _pywraplp.Objective_swigregister
Objective_swigregister(Objective)

class Variable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Variable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Variable, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")

    def name(self):
        return _pywraplp.Variable_name(self)

    def integer(self):
        return _pywraplp.Variable_integer(self)

    def solution_value(self):
        return _pywraplp.Variable_solution_value(self)

    def index(self):
        return _pywraplp.Variable_index(self)

    def lb(self):
        return _pywraplp.Variable_lb(self)

    def ub(self):
        return _pywraplp.Variable_ub(self)

    def reduced_cost(self):
        return _pywraplp.Variable_reduced_cost(self)

    def basis_status(self):
        return _pywraplp.Variable_basis_status(self)

    def __str__(self):
        return _pywraplp.Variable___str__(self)

    def __repr__(self):
        return _pywraplp.Variable___repr__(self)

    def __getattr__(self, name):
      return getattr(VariableExpr(self), name)


    def SolutionValue(self):
        return _pywraplp.Variable_SolutionValue(self)

    def Integer(self):
        return _pywraplp.Variable_Integer(self)

    def Lb(self):
        return _pywraplp.Variable_Lb(self)

    def Ub(self):
        return _pywraplp.Variable_Ub(self)

    def SetLb(self, x):
        return _pywraplp.Variable_SetLb(self, x)

    def SetUb(self, x):
        return _pywraplp.Variable_SetUb(self, x)

    def ReducedCost(self):
        return _pywraplp.Variable_ReducedCost(self)
    __swig_destroy__ = _pywraplp.delete_Variable
    __del__ = lambda self: None
Variable_swigregister = _pywraplp.Variable_swigregister
Variable_swigregister(Variable)

class Constraint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Constraint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Constraint, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def name(self):
        return _pywraplp.Constraint_name(self)

    def SetCoefficient(self, var, coeff):
        return _pywraplp.Constraint_SetCoefficient(self, var, coeff)

    def GetCoefficient(self, var):
        return _pywraplp.Constraint_GetCoefficient(self, var)

    def lb(self):
        return _pywraplp.Constraint_lb(self)

    def ub(self):
        return _pywraplp.Constraint_ub(self)

    def SetLB(self, lb):
        return _pywraplp.Constraint_SetLB(self, lb)

    def SetUB(self, ub):
        return _pywraplp.Constraint_SetUB(self, ub)

    def SetBounds(self, lb, ub):
        return _pywraplp.Constraint_SetBounds(self, lb, ub)

    def set_is_lazy(self, laziness):
        return _pywraplp.Constraint_set_is_lazy(self, laziness)

    def index(self):
        return _pywraplp.Constraint_index(self)

    def dual_value(self):
        return _pywraplp.Constraint_dual_value(self)

    def basis_status(self):
        return _pywraplp.Constraint_basis_status(self)

    def Lb(self):
        return _pywraplp.Constraint_Lb(self)

    def Ub(self):
        return _pywraplp.Constraint_Ub(self)

    def SetLb(self, x):
        return _pywraplp.Constraint_SetLb(self, x)

    def SetUb(self, x):
        return _pywraplp.Constraint_SetUb(self, x)

    def DualValue(self):
        return _pywraplp.Constraint_DualValue(self)
    __swig_destroy__ = _pywraplp.delete_Constraint
    __del__ = lambda self: None
Constraint_swigregister = _pywraplp.Constraint_swigregister
Constraint_swigregister(Constraint)

class MPSolverParameters(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MPSolverParameters, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MPSolverParameters, name)
    __repr__ = _swig_repr
    RELATIVE_MIP_GAP = _pywraplp.MPSolverParameters_RELATIVE_MIP_GAP
    PRESOLVE = _pywraplp.MPSolverParameters_PRESOLVE

    def __init__(self):
        this = _pywraplp.new_MPSolverParameters()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetDoubleParam(self, param, value):
        return _pywraplp.MPSolverParameters_SetDoubleParam(self, param, value)

    def SetIntegerParam(self, param, value):
        return _pywraplp.MPSolverParameters_SetIntegerParam(self, param, value)

    def GetDoubleParam(self, param):
        return _pywraplp.MPSolverParameters_GetDoubleParam(self, param)

    def GetIntegerParam(self, param):
        return _pywraplp.MPSolverParameters_GetIntegerParam(self, param)
    __swig_destroy__ = _pywraplp.delete_MPSolverParameters
    __del__ = lambda self: None
MPSolverParameters_swigregister = _pywraplp.MPSolverParameters_swigregister
MPSolverParameters_swigregister(MPSolverParameters)
cvar = _pywraplp.cvar
MPSolverParameters.kDefaultPrimalTolerance = _pywraplp.cvar.MPSolverParameters_kDefaultPrimalTolerance


def setup_variable_operator(opname):
  setattr(Variable, opname,
          lambda self, *args: getattr(VariableExpr(self), opname)(*args))
for opname in LinearExpr.SUPPORTED_OPERATOR_METHODS:
  setup_variable_operator(opname)

# This file is compatible with both classic and new-style classes.
