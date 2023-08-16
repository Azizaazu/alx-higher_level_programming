#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints bytes
 * @p: python
 * Return: nothing
 *
 */


void print_python_bytes(PyObject *p)
{
	char *str;
	long int s, i, lmt;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		lmt = 10;
	else
		lmt = s + 1;

	printf("  first %ld bytes:", lmt);

	for (i = 0; i < lmt; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
}



/**
 * print_python_list - Prints list
 * @p: Python
 * Return: nothing
 *
 */


void print_python_list(PyObject *p)
{
	long int s, i;
	PyListObject *lst;
	PyObject *object;

	s = ((PyVarObject *)(p))->ob_size;
	lst = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (i = 0; i < s; i++)
	{
		object = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(object);
	}
}
