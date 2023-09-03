#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - prints Python strings.
 * @p: the python objec
 * Return: nothing
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t size;

	fflush(stdout);

	printf("[.] string object info\n");
	for (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	size = PyUnicode_GET_LENGTH(p);
	
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %zd\n", size);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &size));
