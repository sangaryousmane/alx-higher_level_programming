#ifndef LISTS_
#define LISTS_
#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);

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
	for (ptr2 = ptr; ptr2 < string + limit; ptr2++)
		printf(" %02x", (unsigned char)*ptr2);
	printf("\n");
}

#endif /** LISTS_ **/
