use std::ffi::c_double;

use pyo3::basic::CompareOp;
use pyo3::exceptions::{PyOverflowError, PyTypeError, PyValueError, PyZeroDivisionError};
use pyo3::prelude::{pyclass, pymethods, pymodule, IntoPy, PyModule, PyObject, PyResult, Python};
use pyo3::types::{PyBytes, PyFloat, PyTuple, PyType};
use pyo3::{PyAny, PyRef, PyTypeInfo};

#[pymodule]
fn _crustpy(_py: Python, module: &PyModule) -> PyResult<()> {
    unsafe {
        let py = Python::assume_gil_acquired();
        if py.version_info() < (3, 9) {
            GENERIC_ALIAS = Some(
                py.import("typing")?
                    .getattr("List")?
                    .get_item(py.import("builtins")?.getattr("int")?)?
                    .get_type(),
            );
        } else {
            GENERIC_ALIAS = Some(py.import("types")?.getattr("GenericAlias")?);
        }
    }

    module.setattr("__version__", env!("CARGO_PKG_VERSION"))?;
    module.setattr("__doc__", env!("CARGO_PKG_DESCRIPTION"))?;
    module.add_class::<Bool>()?;
    module.add_class::<Err_>()?;
    module.add_class::<F32>()?;
    module.add_class::<F64>()?;
    module.add_class::<I8>()?;
    module.add_class::<I16>()?;
    module.add_class::<I32>()?;
    module.add_class::<I64>()?;
    module.add_class::<I128>()?;
    module.add_class::<ISize>()?;
    module.add_class::<None_>()?;
    module.add_class::<Ok_>()?;
    module.add_class::<Some_>()?;
    module.add_class::<U8>()?;
    module.add_class::<U16>()?;
    module.add_class::<U32>()?;
    module.add_class::<U64>()?;
    module.add_class::<U128>()?;
    module.add_class::<USize>()?;
    Ok(())
}

static mut GENERIC_ALIAS: Option<&PyAny> = None;

#[pyclass(module = "rustpy.primitive", name = "bool_")]
#[derive(Clone)]
struct Bool(bool);

const TRUE: Bool = Bool(true);
const FALSE: Bool = Bool(false);

#[pymethods]
impl Bool {
    #[new]
    fn new(value: bool) -> Self {
        Self(value)
    }

    fn as_(&self, cls: &PyAny) -> PyResult<PyObject> {
        self.cast_as(cls)
    }

    fn __bool__(&self) -> bool {
        self.0
    }

    fn __repr__(&self) -> String {
        format!("bool_({})", if self.0 { "True" } else { "False" })
    }

    fn __richcmp__(&self, other: &PyAny, op: CompareOp) -> PyResult<PyObject> {
        let py = other.py();
        match other.extract::<Bool>() {
            Ok(other) => Ok(Bool(compare(&self.0, &other.0, op)).into_py(py)),
            Err(_) => Ok(py.NotImplemented()),
        }
    }

    fn __str__(&self) -> String {
        format!("{}", self.0)
    }
}

#[pyclass(module = "rustpy.result", name = "Err")]
#[derive(Clone)]
struct Err_(PyObject);

#[pymethods]
impl Err_ {
    #[new]
    fn new(_value: PyObject) -> Self {
        Self(_value)
    }

    fn and_<'a>(slf: PyRef<'a, Self>, _value: &PyAny) -> PyRef<'a, Self> {
        slf
    }

    fn and_then<'a>(slf: PyRef<'a, Self>, _function: &PyAny) -> PyRef<'a, Self> {
        slf
    }

    fn err(&self) -> Some_ {
        Some_(self.0.clone())
    }

    fn expect(&self, message: String, py: Python) -> PyResult<PyObject> {
        Err(PyValueError::new_err(format!(
            "{}: {}",
            message,
            self.0.as_ref(py).repr()?
        )))
    }

    fn expect_err(&self, _message: String) -> PyObject {
        self.0.clone()
    }

    fn is_err(&self) -> Bool {
        TRUE
    }

    fn is_ok(&self) -> Bool {
        FALSE
    }

    fn map<'a>(slf: PyRef<'a, Self>, _function: &PyAny) -> PyRef<'a, Self> {
        slf
    }

    fn map_err(&self, function: &PyAny, py: Python) -> PyResult<Self> {
        function
            .call1(PyTuple::new(py, [self.0.as_ref(py)]))
            .map(|result| Self(result.into_py(py)))
    }

    fn map_or(&self, default: PyObject, _function: &PyAny) -> PyObject {
        default
    }

    fn map_or_else<'a>(
        &self,
        default: &'a PyAny,
        _function: &PyAny,
        py: Python,
    ) -> PyResult<&'a PyAny> {
        default.call1(PyTuple::new(py, [self.0.as_ref(py)]))
    }

    fn ok(&self) -> None_ {
        None_()
    }

    fn or_<'a>(&self, value: &'a PyAny, py: Python) -> PyResult<&'a PyAny> {
        check_result_value(value, py).ok_or_else(|| {
            value
                .repr()
                .map(|result_repr| {
                    PyTypeError::new_err(format!(
                        "`Err` or `Ok` expected, but got {}.",
                        result_repr
                    ))
                })
                .unwrap_or_else(|err| err)
        })
    }

    fn or_else<'a>(&self, function: &'a PyAny, py: Python) -> PyResult<&'a PyAny> {
        let result = function.call1(PyTuple::new(py, [self.0.as_ref(py)]))?;
        check_result_value(result, py).ok_or_else(|| {
            result
                .repr()
                .map(|result_repr| {
                    PyTypeError::new_err(format!(
                        "Function should return either `None_` or `Some` instance, but got {}.",
                        result_repr
                    ))
                })
                .unwrap_or_else(|err| err)
        })
    }

    fn unwrap(&self, py: Python) -> PyResult<PyObject> {
        Err(PyValueError::new_err(format!(
            "Called `unwrap` on an `Err` value: {}.",
            self.0.as_ref(py).repr()?
        )))
    }

    fn unwrap_err(&self) -> PyObject {
        self.0.clone()
    }

    fn unwrap_or(&self, default: PyObject) -> PyObject {
        default
    }

    fn unwrap_or_else<'a>(&self, function: &'a PyAny, py: Python) -> PyResult<&'a PyAny> {
        function.call1(PyTuple::new(py, [self.0.as_ref(py)]))
    }

    #[classmethod]
    fn __class_getitem__<'a>(cls: &PyType, item: &PyAny, py: Python<'a>) -> PyResult<&'a PyAny> {
        unsafe { GENERIC_ALIAS.unwrap_unchecked() }.call1(PyTuple::new(
            py,
            [
                <&PyType as IntoPy<PyObject>>::into_py(cls, py),
                PyTuple::new(py, [item]).into_py(py),
            ],
        ))
    }

    fn __bool__(&self) -> PyResult<()> {
        Err(PyTypeError::new_err("Expected `bool_`, found `Err`."))
    }

    fn __richcmp__(&self, other: &PyAny, op: CompareOp) -> PyResult<PyObject> {
        let py = other.py();
        other
            .extract::<Self>()
            .and_then(|other| {
                self.0.as_ref(py).rich_compare(&other.0, op).map(|result| {
                    if let Ok(result) = result.extract::<bool>() {
                        Bool(result).into_py(py)
                    } else {
                        result.into_py(py)
                    }
                })
            })
            .or_else(|_| {
                if other.is_instance_of::<Ok_>()? {
                    Ok(
                        Bool(matches!(op, CompareOp::Ge | CompareOp::Gt | CompareOp::Ne))
                            .into_py(py),
                    )
                } else {
                    Ok(py.NotImplemented())
                }
            })
    }

    fn __repr__(&self, py: Python) -> PyResult<String> {
        self.0
            .as_ref(py)
            .repr()
            .map(|value_repr| format!("Err({})", value_repr))
    }
}

#[pyclass(module = "rustpy.result", name = "Ok")]
#[derive(Clone)]
struct Ok_(PyObject);

#[pymethods]
impl Ok_ {
    #[new]
    fn new(_value: PyObject) -> Self {
        Self(_value)
    }

    fn and_<'a>(&self, value: &'a PyAny, py: Python) -> PyResult<&'a PyAny> {
        check_result_value(value, py).ok_or_else(|| {
            value
                .repr()
                .map(|result_repr| {
                    PyTypeError::new_err(format!(
                        "`Err` or `Ok` expected, but got {}.",
                        result_repr
                    ))
                })
                .unwrap_or_else(|err| err)
        })
    }

    fn and_then<'a>(&self, function: &'a PyAny, py: Python) -> PyResult<&'a PyAny> {
        let result = function.call1(PyTuple::new(py, [self.0.as_ref(py)]))?;
        check_result_value(result, py).ok_or_else(|| {
            result
                .repr()
                .map(|result_repr| {
                    PyTypeError::new_err(format!(
                        "Function should return either `None_` or `Some` instance, but got {}.",
                        result_repr
                    ))
                })
                .unwrap_or_else(|err| err)
        })
    }

    fn err(&self) -> None_ {
        None_()
    }

    fn expect(&self, _message: String) -> PyObject {
        self.0.clone()
    }

    fn expect_err(&self, message: String, py: Python) -> PyResult<PyObject> {
        Err(PyValueError::new_err(format!(
            "{}: {}",
            message,
            self.0.as_ref(py).repr()?
        )))
    }

    fn is_err(&self) -> Bool {
        FALSE
    }

    fn is_ok(&self) -> Bool {
        TRUE
    }

    fn map(&self, function: &PyAny, py: Python) -> PyResult<Self> {
        function
            .call1(PyTuple::new(py, [self.0.as_ref(py)]))
            .map(|result| Self(result.into_py(py)))
    }

    fn map_err<'a>(slf: PyRef<'a, Self>, _function: &PyAny) -> PyRef<'a, Self> {
        slf
    }

    fn map_or<'a>(
        &self,
        _default: PyObject,
        function: &'a PyAny,
        py: Python,
    ) -> PyResult<&'a PyAny> {
        function.call1(PyTuple::new(py, [self.0.as_ref(py)]))
    }

    fn map_or_else<'a>(
        &self,
        _default: &PyAny,
        function: &'a PyAny,
        py: Python,
    ) -> PyResult<&'a PyAny> {
        function.call1(PyTuple::new(py, [self.0.as_ref(py)]))
    }

    fn ok(&self) -> Some_ {
        Some_(self.0.clone())
    }

    fn or_<'a>(slf: PyRef<'a, Self>, _value: &PyAny) -> PyRef<'a, Self> {
        slf
    }

    fn or_else<'a>(slf: PyRef<'a, Self>, _function: &PyAny) -> PyRef<'a, Self> {
        slf
    }

    fn unwrap(&self) -> PyObject {
        self.0.clone()
    }

    fn unwrap_err(&self, py: Python) -> PyResult<PyObject> {
        Err(PyValueError::new_err(format!(
            "Called `unwrap` on an `Err` value: {}.",
            self.0.as_ref(py).repr()?
        )))
    }

    fn unwrap_or(&self, _default: PyObject) -> PyObject {
        self.0.clone()
    }

    fn unwrap_or_else(&self, _function: &PyAny) -> PyObject {
        self.0.clone()
    }

    #[classmethod]
    fn __class_getitem__<'a>(cls: &PyType, item: &PyAny, py: Python<'a>) -> PyResult<&'a PyAny> {
        unsafe { GENERIC_ALIAS.unwrap_unchecked() }.call1(PyTuple::new(
            py,
            [
                <&PyType as IntoPy<PyObject>>::into_py(cls, py),
                PyTuple::new(py, [item]).into_py(py),
            ],
        ))
    }

    fn __bool__(&self) -> PyResult<()> {
        Err(PyTypeError::new_err("Expected `bool_`, found `Ok`."))
    }

    fn __repr__(&self, py: Python) -> PyResult<String> {
        self.0
            .as_ref(py)
            .repr()
            .map(|value_repr| format!("Ok({})", value_repr))
    }

    fn __richcmp__(&self, other: &PyAny, op: CompareOp) -> PyResult<PyObject> {
        let py = other.py();
        other
            .extract::<Self>()
            .and_then(|other| {
                self.0.as_ref(py).rich_compare(&other.0, op).map(|result| {
                    if let Ok(result) = result.extract::<bool>() {
                        Bool(result).into_py(py)
                    } else {
                        result.into_py(py)
                    }
                })
            })
            .or_else(|_| {
                if other.is_instance_of::<Err_>()? {
                    Ok(
                        Bool(matches!(op, CompareOp::Le | CompareOp::Lt | CompareOp::Ne))
                            .into_py(py),
                    )
                } else {
                    Ok(py.NotImplemented())
                }
            })
    }
}

#[pyclass(module = "rustpy.option", name = "None_")]
#[derive(Clone)]
struct None_();

#[pymethods]
impl None_ {
    #[new]
    fn new() -> Self {
        Self()
    }

    fn and_<'a>(slf: PyRef<'a, Self>, _value: &PyAny) -> PyRef<'a, Self> {
        slf
    }

    fn and_then<'a>(slf: PyRef<'a, Self>, _function: &PyAny) -> PyRef<'a, Self> {
        slf
    }

    fn expect(&self, message: String) -> PyResult<PyObject> {
        Err(PyValueError::new_err(message))
    }

    fn is_none(&self) -> Bool {
        TRUE
    }

    fn is_some(&self) -> Bool {
        FALSE
    }

    fn map<'a>(slf: PyRef<'a, Self>, _function: &PyAny) -> PyResult<PyRef<'a, Self>> {
        Ok(slf)
    }

    fn map_or(&self, default: PyObject, _function: &PyAny) -> PyObject {
        default
    }

    fn map_or_else<'a>(&self, default: &'a PyAny, _function: &PyAny) -> PyResult<&'a PyAny> {
        default.call0()
    }

    fn ok_or(&self, _err: PyObject) -> Err_ {
        Err_(_err)
    }

    fn ok_or_else(&self, _err: &PyAny, py: Python) -> PyResult<Err_> {
        _err.call0().map(|value| Err_(value.into_py(py)))
    }

    fn or_<'a>(&self, value: &'a PyAny, py: Python) -> PyResult<&'a PyAny> {
        check_option_value(value, py).ok_or_else(|| {
            value
                .repr()
                .map(|result_repr| {
                    PyTypeError::new_err(format!(
                        "`None` or `Some` expected, but got {}.",
                        result_repr
                    ))
                })
                .unwrap_or_else(|err| err)
        })
    }

    fn or_else<'a>(&self, function: &'a PyAny, py: Python) -> PyResult<&'a PyAny> {
        let result = function.call0()?;
        check_option_value(result, py).ok_or_else(|| {
            result
                .repr()
                .map(|result_repr| {
                    PyTypeError::new_err(format!(
                        "Function should return either `None_` or `Some` instance, but got {}.",
                        result_repr
                    ))
                })
                .unwrap_or_else(|err| err)
        })
    }

    fn unwrap(&self) -> PyResult<PyObject> {
        Err(PyValueError::new_err(
            "Called `unwrap()` on a `None` value.",
        ))
    }

    fn unwrap_or(&self, default: PyObject) -> PyObject {
        default
    }

    fn unwrap_or_else<'a>(&self, function: &'a PyAny) -> PyResult<&'a PyAny> {
        function.call0()
    }

    fn __bool__(&self) -> PyResult<()> {
        Err(PyTypeError::new_err("Expected `bool_`, found `None_`."))
    }

    fn __repr__(&self) -> &str {
        "None_()"
    }

    fn __richcmp__(&self, other: &PyAny, op: CompareOp) -> PyResult<PyObject> {
        let py = other.py();
        if other.is_instance_of::<Self>()? {
            Ok(Bool(matches!(op, CompareOp::Eq | CompareOp::Ge | CompareOp::Le)).into_py(py))
        } else if other.is_instance_of::<Some_>()? {
            Ok(Bool(matches!(op, CompareOp::Le | CompareOp::Lt | CompareOp::Ne)).into_py(py))
        } else {
            Ok(py.NotImplemented())
        }
    }
}

#[pyclass(module = "rustpy.option", name = "Some")]
#[derive(Clone)]
struct Some_(PyObject);

#[pymethods]
impl Some_ {
    #[new]
    fn new(_value: PyObject) -> Self {
        Self(_value)
    }

    fn and_<'a>(&self, value: &'a PyAny, py: Python) -> PyResult<&'a PyAny> {
        check_option_value(value, py).ok_or_else(|| {
            value
                .repr()
                .map(|result_repr| {
                    PyTypeError::new_err(format!(
                        "`None` or `Some` expected, but got {}.",
                        result_repr
                    ))
                })
                .unwrap_or_else(|err| err)
        })
    }

    fn and_then<'a>(&self, function: &'a PyAny, py: Python) -> PyResult<&'a PyAny> {
        let result = function.call1(PyTuple::new(py, [self.0.as_ref(py)]))?;
        check_option_value(result, py).ok_or_else(|| {
            result
                .repr()
                .map(|result_repr| {
                    PyTypeError::new_err(format!(
                        "Function should return either `None_` or `Some` instance, but got {}.",
                        result_repr
                    ))
                })
                .unwrap_or_else(|err| err)
        })
    }

    fn expect(&self, _message: String) -> PyObject {
        self.0.clone()
    }

    fn is_none(&self) -> Bool {
        FALSE
    }

    fn is_some(&self) -> Bool {
        TRUE
    }

    fn map(&self, function: &PyAny, py: Python) -> PyResult<Self> {
        function
            .call1(PyTuple::new(py, [self.0.as_ref(py)]))
            .map(|result| Self(result.into_py(py)))
    }

    fn map_or<'a>(
        &self,
        _default: PyObject,
        function: &'a PyAny,
        py: Python,
    ) -> PyResult<&'a PyAny> {
        function.call1(PyTuple::new(py, [self.0.as_ref(py)]))
    }

    fn map_or_else<'a>(
        &self,
        _default: &PyAny,
        function: &'a PyAny,
        py: Python,
    ) -> PyResult<&'a PyAny> {
        function.call1(PyTuple::new(py, [self.0.as_ref(py)]))
    }

    fn ok_or(slf: PyRef<Self>, _err: PyObject) -> Ok_ {
        Ok_(slf.0.clone())
    }

    fn ok_or_else(slf: PyRef<Self>, _err: &PyAny) -> Ok_ {
        Ok_(slf.0.clone())
    }

    fn or_<'a>(slf: PyRef<'a, Self>, _value: &PyAny) -> PyRef<'a, Self> {
        slf
    }

    fn or_else<'a>(slf: PyRef<'a, Self>, _function: &PyAny) -> PyRef<'a, Self> {
        slf
    }

    fn unwrap(&self) -> PyObject {
        self.0.clone()
    }

    fn unwrap_or(&self, _default: PyObject) -> PyObject {
        self.0.clone()
    }

    fn unwrap_or_else(&self, _function: &PyAny) -> PyResult<PyObject> {
        Ok(self.0.clone())
    }

    fn __bool__(&self) -> PyResult<()> {
        Err(PyTypeError::new_err("Expected `bool_`, found `Some`."))
    }

    #[classmethod]
    fn __class_getitem__<'a>(cls: &PyType, item: &PyAny, py: Python<'a>) -> PyResult<&'a PyAny> {
        unsafe { GENERIC_ALIAS.unwrap_unchecked() }.call1(PyTuple::new(
            py,
            [
                <&PyType as IntoPy<PyObject>>::into_py(cls, py),
                PyTuple::new(py, [item]).into_py(py),
            ],
        ))
    }

    fn __repr__(&self, py: Python) -> PyResult<String> {
        self.0
            .as_ref(py)
            .repr()
            .map(|value_repr| format!("Some({})", value_repr))
    }

    fn __richcmp__(&self, other: &PyAny, op: CompareOp) -> PyResult<PyObject> {
        let py = other.py();
        other
            .extract::<Self>()
            .and_then(|other| {
                self.0.as_ref(py).rich_compare(&other.0, op).map(|result| {
                    if let Ok(result) = result.extract::<bool>() {
                        Bool(result).into_py(py)
                    } else {
                        result.into_py(py)
                    }
                })
            })
            .or_else(|_| {
                if other.is_instance_of::<None_>()? {
                    Ok(
                        Bool(matches!(op, CompareOp::Ge | CompareOp::Gt | CompareOp::Ne))
                            .into_py(py),
                    )
                } else {
                    Ok(py.NotImplemented())
                }
            })
    }
}

fn check_option_value<'a>(value: &'a PyAny, py: Python) -> Option<&'a PyAny> {
    if value
        .is_instance(PyTuple::new(
            py,
            [Some_::type_object(py), None_::type_object(py)],
        ))
        .ok()?
    {
        Some(value)
    } else {
        None
    }
}

fn check_result_value<'a>(value: &'a PyAny, py: Python) -> Option<&'a PyAny> {
    if value
        .is_instance(PyTuple::new(
            py,
            [Err_::type_object(py), Ok_::type_object(py)],
        ))
        .ok()?
    {
        Some(value)
    } else {
        None
    }
}

trait CastAs {
    fn cast_as(&self, cls: &PyAny) -> PyResult<PyObject>;
}

impl CastAs for Bool {
    fn cast_as(&self, cls: &PyAny) -> PyResult<PyObject> {
        let py = cls.py();
        if cls.is(Bool::type_object(py)) {
            Ok(Bool(self.0).into_py(py))
        } else if cls.is(I8::type_object(py)) {
            Ok(I8(self.0 as i8).into_py(py))
        } else if cls.is(I16::type_object(py)) {
            Ok(I16(self.0 as i16).into_py(py))
        } else if cls.is(I32::type_object(py)) {
            Ok(I32(self.0 as i32).into_py(py))
        } else if cls.is(I64::type_object(py)) {
            Ok(I64(self.0 as i64).into_py(py))
        } else if cls.is(I128::type_object(py)) {
            Ok(I128(self.0 as i128).into_py(py))
        } else if cls.is(ISize::type_object(py)) {
            Ok(ISize(self.0 as isize).into_py(py))
        } else if cls.is(U8::type_object(py)) {
            Ok(U8(self.0 as u8).into_py(py))
        } else if cls.is(U16::type_object(py)) {
            Ok(U16(self.0 as u16).into_py(py))
        } else if cls.is(U32::type_object(py)) {
            Ok(U32(self.0 as u32).into_py(py))
        } else if cls.is(U64::type_object(py)) {
            Ok(U64(self.0 as u64).into_py(py))
        } else if cls.is(U128::type_object(py)) {
            Ok(U128(self.0 as u128).into_py(py))
        } else if cls.is(USize::type_object(py)) {
            Ok(USize(self.0 as usize).into_py(py))
        } else {
            Err(PyTypeError::new_err(format!(
                "Can't cast {} as {}",
                self.clone().into_py(py).as_ref(py).repr()?,
                cls.repr()?
            )))
        }
    }
}

macro_rules! cast_as_primitive_wrappers_impl {
    ($($wrapper:ty)*) => ($(
        impl CastAs for $wrapper {
            fn cast_as(&self, cls: &PyAny) -> PyResult<PyObject> {
                let py = cls.py();
                if cls.is(F32::type_object(py)) {
                    Ok(F32(self.0 as f32).into_py(py))
                } else if cls.is(F64::type_object(py)) {
                    Ok(F64(self.0 as f64).into_py(py))
                } else if cls.is(I8::type_object(py)) {
                    Ok(I8(self.0 as i8).into_py(py))
                } else if cls.is(I16::type_object(py)) {
                    Ok(I16(self.0 as i16).into_py(py))
                } else if cls.is(I32::type_object(py)) {
                    Ok(I32(self.0 as i32).into_py(py))
                } else if cls.is(I64::type_object(py)) {
                    Ok(I64(self.0 as i64).into_py(py))
                } else if cls.is(I128::type_object(py)) {
                    Ok(I128(self.0 as i128).into_py(py))
                } else if cls.is(ISize::type_object(py)) {
                    Ok(ISize(self.0 as isize).into_py(py))
                } else if cls.is(U8::type_object(py)) {
                    Ok(U8(self.0 as u8).into_py(py))
                } else if cls.is(U16::type_object(py)) {
                    Ok(U16(self.0 as u16).into_py(py))
                } else if cls.is(U32::type_object(py)) {
                    Ok(U32(self.0 as u32).into_py(py))
                } else if cls.is(U64::type_object(py)) {
                    Ok(U64(self.0 as u64).into_py(py))
                } else if cls.is(U128::type_object(py)) {
                    Ok(U128(self.0 as u128).into_py(py))
                } else if cls.is(USize::type_object(py)) {
                    Ok(USize(self.0 as usize).into_py(py))
                } else {
                    Err(PyTypeError::new_err(format!(
                        "Can't cast {} as {}",
                        self.clone().into_py(py).as_ref(py).repr()?,
                        cls.repr()?
                    )))
                }
            }
        }
    )*)
}

cast_as_primitive_wrappers_impl!(
    F32 F64 I8 I16 I32 I64 I128 ISize U8 U16 U32 U64 U128 USize
);

macro_rules! define_floating_point_python_binding {
    ($float:ident => ($name:literal, $wrapper:ident)) => {
        const _: () = assert!(are_strings_equal($name, stringify!($float)));

        #[pyclass(module = "rustpy.primitive", name = $name)]
        #[derive(Clone)]
        struct $wrapper($float);

        #[pymethods]
        impl $wrapper {
            #[classattr]
            const DIGITS: U32 = U32(<$float>::DIGITS);
            #[classattr]
            const EPSILON: Self = Self(<$float>::EPSILON);
            #[classattr]
            const INFINITY: Self = Self(<$float>::INFINITY);
            #[classattr]
            const MANTISSA_DIGITS: U32 = U32(<$float>::MANTISSA_DIGITS);
            #[classattr]
            const MAX: Self = Self(<$float>::MAX);
            #[classattr]
            const MAX_10_EXP: I32 = I32(<$float>::MAX_10_EXP);
            #[classattr]
            const MAX_EXP: I32 = I32(<$float>::MAX_EXP);
            #[classattr]
            const MIN: Self = Self(<$float>::MIN);
            #[classattr]
            const MIN_10_EXP: I32 = I32(<$float>::MIN_10_EXP);
            #[classattr]
            const MIN_EXP: I32 = I32(<$float>::MIN_EXP);
            #[classattr]
            const MIN_POSITIVE: Self = Self(<$float>::MIN_POSITIVE);
            #[classattr]
            const NAN: Self = Self(<$float>::NAN);
            #[classattr]
            const NEG_INFINITY: Self = Self(<$float>::NEG_INFINITY);
            #[classattr]
            const RADIX: U32 = U32(<$float>::RADIX);

            #[new]
            fn new(value: $float) -> Self {
                Self(value)
            }

            #[classmethod]
            fn from_be_bytes(_cls: &PyType, _bytes: &PyBytes) -> PyResult<Self> {
                let bytes = _bytes.as_bytes();
                bytes
                    .try_into()
                    .map(|bytes| Self(<$float>::from_be_bytes(bytes)))
                    .map_err(|_| {
                        PyTypeError::new_err(format!(
                            "Invalid number of bytes, got {}.",
                            bytes.len()
                        ))
                    })
            }

            #[classmethod]
            fn from_le_bytes(_cls: &PyType, _bytes: &PyBytes) -> PyResult<Self> {
                let bytes = _bytes.as_bytes();
                bytes
                    .try_into()
                    .map(|bytes| Self(<$float>::from_le_bytes(bytes)))
                    .map_err(|_| {
                        PyTypeError::new_err(format!(
                            "Invalid number of bytes, got {}.",
                            bytes.len()
                        ))
                    })
            }

            #[classmethod]
            fn from_ne_bytes(_cls: &PyType, _bytes: &PyBytes) -> PyResult<Self> {
                let bytes = _bytes.as_bytes();
                bytes
                    .try_into()
                    .map(|bytes| Self(<$float>::from_ne_bytes(bytes)))
                    .map_err(|_| {
                        PyTypeError::new_err(format!(
                            "Invalid number of bytes, got {}.",
                            bytes.len()
                        ))
                    })
            }

            fn abs(&self) -> Self {
                Self(self.0.abs())
            }

            fn add(&self, other: &Self) -> Self {
                Self(self.0 + other.0)
            }

            fn as_(&self, cls: &PyAny) -> PyResult<PyObject> {
                self.cast_as(cls)
            }

            fn ceil(&self) -> Self {
                Self(self.0.ceil())
            }

            fn div(&self, other: &Self) -> Self {
                Self(self.0 / other.0)
            }

            fn div_euclid(&self, other: &Self) -> Self {
                Self(self.0.div_euclid(other.0))
            }

            fn floor(&self) -> Self {
                Self(self.0.floor())
            }

            fn fract(&self) -> Self {
                Self(self.0.fract())
            }

            fn is_finite(&self) -> Bool {
                Bool(self.0.is_finite())
            }

            fn is_infinite(&self) -> Bool {
                Bool(self.0.is_infinite())
            }

            fn is_nan(&self) -> Bool {
                Bool(self.0.is_nan())
            }

            fn mul(&self, other: &Self) -> Self {
                Self(self.0 * other.0)
            }

            fn neg(&self) -> Self {
                Self(-self.0)
            }

            fn rem(&self, other: &Self) -> Self {
                Self(self.0 % other.0)
            }

            fn rem_euclid(&self, other: &Self) -> Self {
                Self(self.0.rem_euclid(other.0))
            }

            fn round(&self) -> Self {
                Self(self.0.round())
            }

            fn sub(&self, other: &Self) -> Self {
                Self(self.0 - other.0)
            }

            fn to_be_bytes<'a>(&self, py: Python<'a>) -> &'a PyBytes {
                PyBytes::new(py, &self.0.to_be_bytes())
            }

            fn to_le_bytes<'a>(&self, py: Python<'a>) -> &'a PyBytes {
                PyBytes::new(py, &self.0.to_le_bytes())
            }

            fn to_ne_bytes<'a>(&self, py: Python<'a>) -> &'a PyBytes {
                PyBytes::new(py, &self.0.to_ne_bytes())
            }

            fn trunc(&self) -> Self {
                Self(self.0.trunc())
            }

            fn __add__(&self, other: &PyAny, py: Python) -> PyObject {
                match other.extract::<Self>() {
                    Ok(other) => Self(self.0 + other.0).into_py(py),
                    Err(_) => py.NotImplemented(),
                }
            }

            fn __bool__(&self) -> PyResult<()> {
                Err(PyTypeError::new_err(format!(
                    "Expected `bool_`, found `{}`.",
                    $name
                )))
            }

            fn __float__(&self) -> $float {
                self.0
            }

            fn __mod__(&self, other: &PyAny, py: Python) -> PyObject {
                match other.extract::<Self>() {
                    Ok(other) => Self(self.0 % other.0).into_py(py),
                    Err(_) => py.NotImplemented(),
                }
            }

            fn __mul__(&self, other: &PyAny, py: Python) -> PyObject {
                match other.extract::<Self>() {
                    Ok(other) => Self(self.0 * other.0).into_py(py),
                    Err(_) => py.NotImplemented(),
                }
            }

            fn __neg__(&self) -> Self {
                Self(-self.0)
            }

            fn __sub__(&self, other: &PyAny, py: Python) -> PyObject {
                match other.extract::<Self>() {
                    Ok(other) => Self(self.0 - other.0).into_py(py),
                    Err(_) => py.NotImplemented(),
                }
            }

            fn __repr__(&self, py: Python) -> PyResult<String> {
                Ok(format!(
                    "{}({})",
                    $name,
                    PyFloat::new(py, self.0 as c_double).repr()?
                ))
            }

            fn __richcmp__(&self, other: &PyAny, op: CompareOp) -> PyResult<PyObject> {
                let py = other.py();
                match other.extract::<Self>() {
                    Ok(other) => Ok(Bool(compare(&self.0, &other.0, op)).into_py(py)),
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __str__(&self) -> String {
                format!("{}{}", self.0, $name)
            }

            fn __truediv__(&self, other: &PyAny, py: Python) -> PyObject {
                match other.extract::<Self>() {
                    Ok(other) => Self(self.0 / other.0).into_py(py),
                    Err(_) => py.NotImplemented(),
                }
            }
        }
    };
}

define_floating_point_python_binding!(f32 => ("f32", F32));
define_floating_point_python_binding!(f64 => ("f64", F64));

macro_rules! define_signed_integer_python_binding {
    ($integer:ident => ($name:literal, $wrapper:ident)) => {
        const _: () = assert!(are_strings_equal($name, stringify!($integer)));

        #[pyclass(module = "rustpy.primitive", name = $name)]
        #[derive(Clone)]
        struct $wrapper($integer);

        #[pymethods]
        impl $wrapper {
            #[classattr]
            const BITS: U32 = U32(<$integer>::BITS);
            #[classattr]
            const MAX: Self = Self(<$integer>::MAX);
            #[classattr]
            const MIN: Self = Self(<$integer>::MIN);

            #[new]
            fn new(value: $integer) -> Self {
                Self(value)
            }

            #[classmethod]
            fn from_be_bytes(_cls: &PyType, _bytes: &PyBytes) -> PyResult<Self> {
                let bytes = _bytes.as_bytes();
                bytes
                    .try_into()
                    .map(|bytes| Self(<$integer>::from_be_bytes(bytes)))
                    .map_err(|_| {
                        PyTypeError::new_err(format!(
                            "Invalid number of bytes, got {}.",
                            bytes.len()
                        ))
                    })
            }

            #[classmethod]
            fn from_le_bytes(_cls: &PyType, _bytes: &PyBytes) -> PyResult<Self> {
                let bytes = _bytes.as_bytes();
                bytes
                    .try_into()
                    .map(|bytes| Self(<$integer>::from_le_bytes(bytes)))
                    .map_err(|_| {
                        PyTypeError::new_err(format!(
                            "Invalid number of bytes, got {}.",
                            bytes.len()
                        ))
                    })
            }

            #[classmethod]
            fn from_ne_bytes(_cls: &PyType, _bytes: &PyBytes) -> PyResult<Self> {
                let bytes = _bytes.as_bytes();
                bytes
                    .try_into()
                    .map(|bytes| Self(<$integer>::from_ne_bytes(bytes)))
                    .map_err(|_| {
                        PyTypeError::new_err(format!(
                            "Invalid number of bytes, got {}.",
                            bytes.len()
                        ))
                    })
            }

            fn abs(&self) -> PyResult<Self> {
                match self.0.checked_abs() {
                    Some(result) => Ok(Self(result)),
                    None => Err(PyOverflowError::new_err(format!(
                        "Absolute value of {} overflows.",
                        self.__repr__()
                    ))),
                }
            }

            fn add(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_add(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(PyOverflowError::new_err(format!(
                        "Sum of {} and {} overflows.",
                        self.__repr__(),
                        other.__repr__(),
                    ))),
                }
            }

            fn as_(&self, cls: &PyAny) -> PyResult<PyObject> {
                self.cast_as(cls)
            }

            fn checked_abs(&self, py: Python) -> PyObject {
                match self.0.checked_abs() {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_add(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_add(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_div(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_div(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_div_euclid(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_div_euclid(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_mul(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_mul(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_neg(&self, py: Python) -> PyObject {
                match self.0.checked_neg() {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_rem(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_rem(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_rem_euclid(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_rem_euclid(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_sub(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_sub(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn div(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_div(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(if other.0 == 0 {
                        PyZeroDivisionError::new_err("Division by zero is undefined.")
                    } else {
                        PyOverflowError::new_err(format!(
                            "Division of {} by {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))
                    }),
                }
            }

            fn div_euclid(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_div_euclid(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(if other.0 == 0 {
                        PyZeroDivisionError::new_err("Euclidean division by zero is undefined.")
                    } else {
                        PyOverflowError::new_err(format!(
                            "Euclidean division of {} by {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))
                    }),
                }
            }

            fn is_negative(&self) -> Bool {
                Bool(self.0.is_negative())
            }

            fn is_positive(&self) -> Bool {
                Bool(self.0.is_positive())
            }

            fn mul(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_mul(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(PyOverflowError::new_err(format!(
                        "Multiplication of {} and {} overflows.",
                        self.__repr__(),
                        other.__repr__(),
                    ))),
                }
            }

            fn neg(&self) -> PyResult<Self> {
                self.0.checked_neg().map(Self).ok_or_else(|| {
                    PyOverflowError::new_err(format!("Negation of {} overflows.", self.__repr__()))
                })
            }

            fn rem(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_rem(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(if other.0 == 0 {
                        PyZeroDivisionError::new_err("Division by zero is undefined.")
                    } else {
                        PyOverflowError::new_err(format!(
                            "Division of {} by {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))
                    }),
                }
            }

            fn rem_euclid(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_rem_euclid(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(if other.0 == 0 {
                        PyZeroDivisionError::new_err("Euclidean division by zero is undefined.")
                    } else {
                        PyOverflowError::new_err(format!(
                            "Euclidean division of {} by {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))
                    }),
                }
            }

            fn sub(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_sub(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(PyOverflowError::new_err(format!(
                        "Difference of {} and {} overflows.",
                        self.__repr__(),
                        other.__repr__(),
                    ))),
                }
            }

            fn to_be_bytes<'a>(&self, py: Python<'a>) -> &'a PyBytes {
                PyBytes::new(py, &self.0.to_be_bytes())
            }

            fn to_le_bytes<'a>(&self, py: Python<'a>) -> &'a PyBytes {
                PyBytes::new(py, &self.0.to_le_bytes())
            }

            fn to_ne_bytes<'a>(&self, py: Python<'a>) -> &'a PyBytes {
                PyBytes::new(py, &self.0.to_ne_bytes())
            }

            fn __add__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => match self.0.checked_add(other.0) {
                        Some(result) => Ok(Self(result).into_py(py)),
                        None => Err(PyOverflowError::new_err(format!(
                            "Sum of {} and {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))),
                    },
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __and__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => Ok(Self(self.0 & other.0).into_py(py)),
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __bool__(&self) -> PyResult<()> {
                Err(PyTypeError::new_err(format!(
                    "Expected `bool_`, found `{}`.",
                    $name
                )))
            }

            fn __int__(&self) -> $integer {
                self.0
            }

            fn __invert__(&self) -> Self {
                Self(!self.0)
            }

            fn __lshift__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<U32>() {
                    Ok(other) => Ok(Self(self.0 << other.0).into_py(py)),
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __mod__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => match self.0.checked_rem(other.0) {
                        Some(result) => Ok(Self(result).into_py(py)),
                        None => Err(if other.0 == 0 {
                            PyZeroDivisionError::new_err("Division by zero is undefined.")
                        } else {
                            PyOverflowError::new_err(format!(
                                "Division of {} by {} overflows.",
                                self.__repr__(),
                                other.__repr__(),
                            ))
                        }),
                    },
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __mul__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => match self.0.checked_mul(other.0) {
                        Some(result) => Ok(Self(result).into_py(py)),
                        None => Err(PyOverflowError::new_err(format!(
                            "Multiplication of {} and {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))),
                    },
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __neg__(&self) -> PyResult<Self> {
                self.0.checked_neg().map(Self).ok_or_else(|| {
                    PyOverflowError::new_err(format!("Negation of {} overflows.", self.__repr__()))
                })
            }

            fn __rshift__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<U32>() {
                    Ok(other) => Ok(Self(self.0 >> other.0).into_py(py)),
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __sub__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => match self.0.checked_sub(other.0) {
                        Some(result) => Ok(Self(result).into_py(py)),
                        None => Err(PyOverflowError::new_err(format!(
                            "Difference of {} and {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))),
                    },
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __repr__(&self) -> String {
                format!("{}({})", $name, self.0)
            }

            fn __richcmp__(&self, other: &PyAny, op: CompareOp) -> PyResult<PyObject> {
                let py = other.py();
                match other.extract::<Self>() {
                    Ok(other) => Ok(Bool(compare(&self.0, &other.0, op)).into_py(py)),
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __str__(&self) -> String {
                format!("{}{}", self.0, $name)
            }

            fn __truediv__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => match self.0.checked_div(other.0) {
                        Some(result) => Ok(Self(result).into_py(py)),
                        None => Err(if other.0 == 0 {
                            PyZeroDivisionError::new_err("Division by zero is undefined.")
                        } else {
                            PyOverflowError::new_err(format!(
                                "Division of {} by {} overflows.",
                                self.__repr__(),
                                other.__repr__(),
                            ))
                        }),
                    },
                    Err(_) => Ok(py.NotImplemented()),
                }
            }
        }
    };
}

define_signed_integer_python_binding!(i8 => ("i8", I8));
define_signed_integer_python_binding!(i16 => ("i16", I16));
define_signed_integer_python_binding!(i32 => ("i32", I32));
define_signed_integer_python_binding!(i64 => ("i64", I64));
define_signed_integer_python_binding!(i128 => ("i128", I128));
define_signed_integer_python_binding!(isize => ("isize", ISize));

macro_rules! define_unsigned_integer_python_binding {
    ($integer:ident => ($name:literal, $wrapper:ident)) => {
        const _: () = assert!(are_strings_equal($name, stringify!($integer)));

        #[pyclass(module = "rustpy.primitive", name = $name)]
        #[derive(Clone)]
        struct $wrapper($integer);

        #[pymethods]
        impl $wrapper {
            #[classattr]
            const BITS: U32 = U32(<$integer>::BITS);
            #[classattr]
            const MAX: Self = Self(<$integer>::MAX);
            #[classattr]
            const MIN: Self = Self(<$integer>::MIN);

            #[new]
            fn new(value: $integer) -> Self {
                Self(value)
            }

            #[classmethod]
            fn from_be_bytes(_cls: &PyType, _bytes: &PyBytes) -> PyResult<Self> {
                let bytes = _bytes.as_bytes();
                bytes
                    .try_into()
                    .map(|bytes| Self(<$integer>::from_be_bytes(bytes)))
                    .map_err(|_| {
                        PyTypeError::new_err(format!(
                            "Invalid number of bytes, got {}.",
                            bytes.len()
                        ))
                    })
            }

            #[classmethod]
            fn from_le_bytes(_cls: &PyType, _bytes: &PyBytes) -> PyResult<Self> {
                let bytes = _bytes.as_bytes();
                bytes
                    .try_into()
                    .map(|bytes| Self(<$integer>::from_le_bytes(bytes)))
                    .map_err(|_| {
                        PyTypeError::new_err(format!(
                            "Invalid number of bytes, got {}.",
                            bytes.len()
                        ))
                    })
            }

            #[classmethod]
            fn from_ne_bytes(_cls: &PyType, _bytes: &PyBytes) -> PyResult<Self> {
                let bytes = _bytes.as_bytes();
                bytes
                    .try_into()
                    .map(|bytes| Self(<$integer>::from_ne_bytes(bytes)))
                    .map_err(|_| {
                        PyTypeError::new_err(format!(
                            "Invalid number of bytes, got {}.",
                            bytes.len()
                        ))
                    })
            }

            fn add(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_add(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(PyOverflowError::new_err(format!(
                        "Sum of {} and {} overflows.",
                        self.__repr__(),
                        other.__repr__(),
                    ))),
                }
            }

            fn as_(&self, cls: &PyAny) -> PyResult<PyObject> {
                self.cast_as(cls)
            }

            fn checked_add(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_add(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_div(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_div(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_div_euclid(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_div_euclid(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_mul(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_mul(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_rem(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_rem(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_rem_euclid(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_rem_euclid(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn checked_sub(&self, other: &Self, py: Python) -> PyObject {
                match self.0.checked_sub(other.0) {
                    Some(result) => Some_(Self(result).into_py(py)).into_py(py),
                    None => None_().into_py(py),
                }
            }

            fn div(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_div(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(if other.0 == 0 {
                        PyZeroDivisionError::new_err("Division by zero is undefined.")
                    } else {
                        PyOverflowError::new_err(format!(
                            "Division of {} by {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))
                    }),
                }
            }

            fn div_euclid(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_div_euclid(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(if other.0 == 0 {
                        PyZeroDivisionError::new_err("Euclidean division by zero is undefined.")
                    } else {
                        PyOverflowError::new_err(format!(
                            "Euclidean division of {} by {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))
                    }),
                }
            }

            fn mul(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_mul(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(PyOverflowError::new_err(format!(
                        "Multiplication of {} and {} overflows.",
                        self.__repr__(),
                        other.__repr__(),
                    ))),
                }
            }

            fn rem(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_rem(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(if other.0 == 0 {
                        PyZeroDivisionError::new_err("Division by zero is undefined.")
                    } else {
                        PyOverflowError::new_err(format!(
                            "Division of {} by {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))
                    }),
                }
            }

            fn rem_euclid(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_rem_euclid(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(if other.0 == 0 {
                        PyZeroDivisionError::new_err("Euclidean division by zero is undefined.")
                    } else {
                        PyOverflowError::new_err(format!(
                            "Euclidean division of {} by {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))
                    }),
                }
            }

            fn sub(&self, other: &Self) -> PyResult<Self> {
                match self.0.checked_sub(other.0) {
                    Some(result) => Ok(Self(result)),
                    None => Err(PyOverflowError::new_err(format!(
                        "Difference of {} and {} overflows.",
                        self.__repr__(),
                        other.__repr__(),
                    ))),
                }
            }

            fn to_be_bytes<'a>(&self, py: Python<'a>) -> &'a PyBytes {
                PyBytes::new(py, &self.0.to_be_bytes())
            }

            fn to_le_bytes<'a>(&self, py: Python<'a>) -> &'a PyBytes {
                PyBytes::new(py, &self.0.to_le_bytes())
            }

            fn to_ne_bytes<'a>(&self, py: Python<'a>) -> &'a PyBytes {
                PyBytes::new(py, &self.0.to_ne_bytes())
            }

            fn __add__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => match self.0.checked_add(other.0) {
                        Some(result) => Ok(Self(result).into_py(py)),
                        None => Err(PyOverflowError::new_err(format!(
                            "Sum of {} and {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))),
                    },
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __and__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => Ok(Self(self.0 & other.0).into_py(py)),
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __bool__(&self) -> PyResult<()> {
                Err(PyTypeError::new_err(format!(
                    "Expected `bool_`, found `{}`.",
                    $name
                )))
            }

            fn __int__(&self) -> $integer {
                self.0
            }

            fn __mod__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => match self.0.checked_rem(other.0) {
                        Some(result) => Ok(Self(result).into_py(py)),
                        None => Err(if other.0 == 0 {
                            PyZeroDivisionError::new_err("Division by zero is undefined.")
                        } else {
                            PyOverflowError::new_err(format!(
                                "Division of {} by {} overflows.",
                                self.__repr__(),
                                other.__repr__(),
                            ))
                        }),
                    },
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __lshift__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<U32>() {
                    Ok(other) => Ok(Self(self.0 << other.0).into_py(py)),
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __mul__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => match self.0.checked_mul(other.0) {
                        Some(result) => Ok(Self(result).into_py(py)),
                        None => Err(PyOverflowError::new_err(format!(
                            "Multiplication of {} and {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))),
                    },
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __repr__(&self) -> String {
                format!("{}({})", $name, self.0)
            }

            fn __richcmp__(&self, other: &PyAny, op: CompareOp) -> PyResult<PyObject> {
                let py = other.py();
                match other.extract::<Self>() {
                    Ok(other) => Ok(Bool(compare(&self.0, &other.0, op)).into_py(py)),
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __rshift__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<U32>() {
                    Ok(other) => Ok(Self(self.0 >> other.0).into_py(py)),
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __sub__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => match self.0.checked_sub(other.0) {
                        Some(result) => Ok(Self(result).into_py(py)),
                        None => Err(PyOverflowError::new_err(format!(
                            "Difference of {} and {} overflows.",
                            self.__repr__(),
                            other.__repr__(),
                        ))),
                    },
                    Err(_) => Ok(py.NotImplemented()),
                }
            }

            fn __str__(&self) -> String {
                format!("{}{}", self.0, $name)
            }

            fn __truediv__(&self, other: &PyAny, py: Python) -> PyResult<PyObject> {
                match other.extract::<Self>() {
                    Ok(other) => match self.0.checked_div(other.0) {
                        Some(result) => Ok(Self(result).into_py(py)),
                        None => Err(if other.0 == 0 {
                            PyZeroDivisionError::new_err("Division by zero is undefined.")
                        } else {
                            PyOverflowError::new_err(format!(
                                "Division of {} by {} overflows.",
                                self.__repr__(),
                                other.__repr__(),
                            ))
                        }),
                    },
                    Err(_) => Ok(py.NotImplemented()),
                }
            }
        }
    };
}

define_unsigned_integer_python_binding!(u8 => ("u8", U8));
define_unsigned_integer_python_binding!(u16 => ("u16", U16));
define_unsigned_integer_python_binding!(u32 => ("u32", U32));
define_unsigned_integer_python_binding!(u64 => ("u64", U64));
define_unsigned_integer_python_binding!(u128 => ("u128", U128));
define_unsigned_integer_python_binding!(usize => ("usize", USize));

const fn are_strings_equal(first: &str, second: &str) -> bool {
    if first.len() != second.len() {
        false
    } else {
        let mut index = 0;
        let (first, second) = (first.as_bytes(), second.as_bytes());
        while index < first.len() {
            if first[index] != second[index] {
                return false;
            }
            index += 1;
        }
        true
    }
}

fn compare<T: PartialOrd<U>, U>(left: &T, right: &U, op: CompareOp) -> bool {
    match op {
        CompareOp::Eq => left == right,
        CompareOp::Ge => left >= right,
        CompareOp::Gt => left > right,
        CompareOp::Le => left <= right,
        CompareOp::Lt => left < right,
        CompareOp::Ne => left != right,
    }
}
