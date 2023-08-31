#include <Python.h>
#include "py.h"


/**
 * print_python_list - Prints basic list info
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t count, mem_, i;
	const char *obj_type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	count = var->ob_size;
	mem_ = list->allocated;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", count);
	printf("[*] Allocated = %ld\n", mem_);

	for (i = 0; i < count; i++)
	{
		obj_type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, obj_type);
		if (strcmp(obj_type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(obj_type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints PyObject basic info
 * @p: byte object for @p
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t count, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		count = 10;
	else
		count = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", count);
	for (i = 0; i < count; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (count - 1))
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}

/**
 * print_python_float - Prints Python's float objects
 * @p: A float object for PyObject
 */
void print_python_float(PyObject *p)
{
	char *buf = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	buf = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buf);
	PyMem_Free(buf);
}
