#include <Python.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = 0, i;

    if(PyList_checkExact(p))
    {
        size = Py_ssize_t(p);
        alloc = ((PyListObject *)p)->allocated
        printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", allocated);

        for (i = 0; i < size; i++)
        {
            item = PyObject_GetItem(p, i);
            printf("Element %d: %s\n", i item);
        }
    }
}