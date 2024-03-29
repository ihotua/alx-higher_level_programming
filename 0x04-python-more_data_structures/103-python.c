#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
    if (!p || !PyList_Check(p)) {
        printf("[ERROR] Invalid Python List Object\n");
        return;
    }

    PyListObject *list = (PyListObject *)p;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; i++)
    {
        PyObject *item = list->ob_item[i];
        const char *type = item->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(item);
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
    if (!p || !PyBytes_Check(p)) {
        printf("[ERROR] Invalid Python Bytes Object\n");
        return;
    }

    PyBytesObject *bytes = (PyBytesObject *)p;
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", bytes->ob_sval);

    printf("  first 10 bytes: ");
    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    if (size > 10) size = 10;
    for (Py_ssize_t i = 0; i < size; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (size - 1)) printf("\n");
        else printf(" ");
    }
}
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
    if (!p || !PyList_Check(p)) {
        printf("[ERROR] Invalid Python List Object\n");
        return;
    }

    PyListObject *list = (PyListObject *)p;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; i++)
    {
        PyObject *item = list->ob_item[i];
        const char *type = item->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(item);
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
    if (!p || !PyBytes_Check(p)) {
        printf("[ERROR] Invalid Python Bytes Object\n");
        return;
    }

    PyBytesObject *bytes = (PyBytesObject *)p;
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", bytes->ob_sval);

    printf("  first 10 bytes: ");
    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    if (size > 10) size = 10;
    for (Py_ssize_t i = 0; i < size; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (size - 1)) printf("\n");
        else printf(" ");
    }
}
