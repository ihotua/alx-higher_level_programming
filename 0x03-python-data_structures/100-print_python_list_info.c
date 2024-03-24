#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject pointer
 * Return: no return
 */

void print_python_list_info(PyObject *p)
{
    long int size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[-] It is not a Python list\n");
        return;
    }

    size = Py_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", size);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        if (item == NULL)
        {
            PyErr_Print();
            printf("[-] Error: Failed to retrieve list item\n");
            return;
        }

        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
