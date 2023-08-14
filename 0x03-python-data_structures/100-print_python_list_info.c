#include <stdio.h>
#include <Python.h>

/**
* print_python_list_info - prints basic info about python list
* @p: python object
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p), i = 0;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);
	while (i < size)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
		i++;
	}
}
