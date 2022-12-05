#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	long int size = Py_Size(p);
	PyListObject *list = (PyListObject *)p;
	PyObject *item;
	int i;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		item = PyList_GetItem(p, i);
		printf("%s\n", Py_Type(item)->tp_name);
	}
}
