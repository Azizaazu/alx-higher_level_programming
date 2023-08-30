#ifndef PYTHON_H
#define PYTHON_H

typedef struct _object {
    PyObject_HEAD
} PyObject;

typedef struct {
    PyObject_VAR_HEAD
    Py_ssize_t ob_size;
} PyVarObject;

typedef struct {
    PyObject_VAR_HEAD
    PyObject *ob_item[1];
} PyListObject;

typedef struct {
    PyObject_VAR_HEAD
    char *ob_sval;
} PyBytesObject;


typedef long Py_ssize_t;

// Define PyObject_HEAD and related macros
#define PyObject_HEAD PyVarObject ob_base;
#define PyObject_VAR_HEAD Py_ssize_t ob_refcnt; PyTypeObject *ob_type;

// Define PyObject types (placeholders for demonstration purposes)
typedef struct _typeobject PyTypeObject;

// Define constants (placeholders for demonstration purposes)
#define PyList_Check(op) 1
#define PyBytes_Check(op) 1

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);


#endif
