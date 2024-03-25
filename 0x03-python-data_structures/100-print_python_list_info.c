#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic info about a Python List instance
 * 
 * @p: A Python List object
 * * Return: no return
 */

void print_python_list_info(PyObject *p)
{
    PyObject *obj;
    PyListObject *list;
    int i, allocated, size;
    char *c_type;

    if (!PyList_Check(p))
    {
        printf("[*] Not a Python List\n");
        return;
    }

    list = (PyListObject *)p;
    allocated = list->allocated;
    size = list->size;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocated);

    for (i = 0; i < size; i++)
    {
        obj = PyList_GetItem(list, i);
        c_type = Py_TYPE(obj)->tp_name;
        printf("[*] Element %d: %s\n", i, c_type);
    }
}
