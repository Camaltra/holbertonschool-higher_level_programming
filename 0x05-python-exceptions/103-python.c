#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
* print_python_list - print info about the python
* Object
*
* @p: The python object
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
* print_python_bytes - Print info about the bytes content of a list
*
* @p: The item of type bytes
*
* Return: Anything, cause void function
*/
void print_python_bytes(PyObject *p)
{
	int size, i;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	size > 10 ? size = 10 : size++;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", ((PyBytesObject *)p)->ob_sval[i]);
		if (i > size - 2)
			printf("\n");
		else
			printf(" ");
	}
}

/**
* print_python_bytes - Print info about the bytes content of a list
*
* @p: The item of type bytes
*
* Return: Anything, cause void function
*/
void print_python_float(PyObject *p)
{
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("  value: %s\n", PyOS_double_to_string(((PyFloatObject *)p)->ob_fval,
	 	'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}