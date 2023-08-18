#include "lists.h"

/**
 * print_python_list - Prints list information
 * @p: Python Object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int size;
	PyObject **items, **item;

	size = ((PyVarObject *)(p))->ob_size;
	items = ((PyListObject *)p)->ob_item;
	
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (item = items; item < items + size; item++)
	{
		printf("Element %ld: %s\n", item - items, (*item)->ob_type->tp_name);
		if (PyBytes_Check(*item))
		{
			print_python_bytes(*item);
		}
	}
}

