#include <Python.h>
#include <stdio.h>

/**
* print_python_list_info - print info about the python
* Object
*
* @p: The python object
*/
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = 0, i, alloc;

    if(PyList_CheckExact(p))
    {
        size = ((PyVarObject *)p)->ob_size;
        alloc = ((PyListObject *)p)->allocated;

        printf("[*] Python info list\n")
        printf("[*] Size of the Python List = %lu\n", size);
		printf("[*] Allocated = %lu\n", alloc);

        for (i = 0; i < size; i++)
        {
            printf("Element %ld: %s\n", i, ((PyListObject *)p)->ob_item[i]->ob_type->tp_name)
            if (strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "byte") == 0)
            {
                print_python_bytes(((PyListObject *)p)->ob_item[i])
            }
        }
    }
}

/**
* print_python_bytes - Print info about the bytes content of a list
*
* @p The item of type bytes
*
* Return: Anything, cause void function
*/
void print_python_bytes(PyObject *p)
{
    int size, i

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("[ERROR] Invalid Bytes Object");
        return;
    }
    size = ((PyVarObject *)p)->ob_size;
    printf("  size: %d", size);
    printf("  trying string: %s", ((PyBytesObject *)p)->ob_sval)

    size >= 10 ? size = 10 : size

    printf("  first %d bytes: ", size)
    for (i = 0; i <= size; i++)
    {
        printf("%02x", ((PyBytesObject *)p)->ob_sval[i])
        if (i == size)
            printf("\n")
        else
            printf(" ")
    }
}