#include <Python.h>

void print_python_bytes(PyObject *p)
{
    if (!p || !PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  - Length: %ld\n", ((PyVarObject *)p)->ob_size);

    printf("  - First 10 bytes: ");
    char *bytes = ((PyBytesObject *)p)->ob_sval;
    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    for (Py_ssize_t i = 0; i < 10 && i < size; i++)
    {
        printf("%02x", (unsigned char)bytes[i]);
        if (i < 9 && i + 1 < size)
            printf(" ");
    }
    printf("\n");
}

