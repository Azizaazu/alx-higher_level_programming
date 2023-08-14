#include <Python.h>



/**
 * print_python_list_info - Prints info about Python
 * @p: PyObject
 *
 */


void print_python_list_info(PyObject *p)
{
	int size, allocate, id;
	PyObject *object;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (id = 0; id < size; id++)
	{
		printf("Element %d: ", id);

		object = PyList_GetItem(p, id);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
