#include <Python.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes_obj;
    Py_ssize_t size, i;
    char *bytes_str;

    if (!PyBytes_Check(p)) 
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes_obj = (PyBytesObject *)p;
    size = PyBytes_GET_SIZE(bytes_obj);

    printf("[.] bytes object info\n");
    printf("  - Length: %ld\n", size);

    bytes_str = PyBytes_AsString(p);

    if (size > 10)
        size = 10;

    printf("  - First %ld bytes: ", size);
    for (i = 0; i < size; i++) 
    {
        printf("%02x", (unsigned char)bytes_str[i]);
        if (i != size - 1)
            printf(" ");
        else
            printf("\n");
    }
}
