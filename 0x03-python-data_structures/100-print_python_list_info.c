#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * print_python_list_info - A function that prints information about
 * a python list object
 * @p: the pointer to generic PyObject which is of PylistObject type
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the python List = %ld\n", Py_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0, i < Py_Size(p); i++)
	{
		printf("Element %d: %s\n", is Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}

}
