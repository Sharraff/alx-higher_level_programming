#include "python.h"
#include <stdlib.h>

/**
 * print_python_list_info - A function that prints information about
 * a python list object
 * @p: the pointer to generic PyObject which is of PylistObject type
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *py_list = NULL;
	size_t len = 0, i = 0;
	const char *py_type = NULL;


	len = PyList_Size(p);
	pylist = (PylistObject *)p;
	printf("[*] Size of the python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));
	for (; i< len; i++)
	{
		py_type = Py_TYPE(py_list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, py_type);
	}
}
