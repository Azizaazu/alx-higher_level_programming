#include <Python.h>

// Function to print information about a Python list
void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        printf("Error: Not a Python list.\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python List Info\n");
    printf("[*] Size of the Python List = %zd\n", size);

    for (Py_ssize_t i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        PyObject *item_str = PyObject_Str(item);
        const char *item_cstr = PyUnicode_AsUTF8(item_str);
        printf("Element %zd: %s\n", i, item_cstr);
        Py_XDECREF(item_str);
    }
}

// Function to print information about a Python bytes object
void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("Error: Not a Python bytes object.\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    const char *data = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", data);

    printf("  first %zd bytes: ", (size <= 10) ? size : 10);
    for (Py_ssize_t i = 0; i < ((size <= 10) ? size : 10); i++)
    {
        printf("%02x", (unsigned char)data[i]);
        if (i < 9) printf(" ");
    }
    printf("\n");
}

int main(int argc, char *argv[])
{
    // Initialize the Python interpreter
    Py_Initialize();

    // Create a Python list and print its info
    PyObject *py_list = PyList_New(3);
    PyList_SetItem(py_list, 0, PyLong_FromLong(42));
    PyList_SetItem(py_list, 1, PyUnicode_DecodeUTF8("hello", 5, "strict"));
    PyList_SetItem(py_list, 2, PyFloat_FromDouble(3.14159));
    print_python_list(py_list);

    // Create a Python bytes object and print its info
    const char data[] = {0x01, 0x23, 0x45, 0x67, 0x89};
    PyObject *py_bytes = PyBytes_FromStringAndSize(data, sizeof(data));
    print_python_bytes(py_bytes);

    // Clean up and finalize the Python interpreter
    Py_XDECREF(py_list);
    Py_XDECREF(py_bytes);
    Py_Finalize();

    return 0;
}
