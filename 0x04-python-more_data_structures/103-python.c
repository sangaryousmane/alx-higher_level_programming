#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);

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


/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *ptr, *ptr2;
	long int size, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	ptr = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", ptr);
	limit = (size >= 10) ? 10 : size + 1;
	printf("  first %ld bytes:", limit);
	for (ptr2 = ptr; ptr2 < ptr + limit; ptr2++)
		printf(" %02x", (unsigned char)*ptr2);
	printf("\n");
}
