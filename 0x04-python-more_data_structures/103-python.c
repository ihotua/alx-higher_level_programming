#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */

void print_python_list(PyObject *p)
{
	PyListObject *list_obj;
	Py_ssize_t i, size, allocated;
	const char *type;

	if (p == NULL || !PyList_Check(p))
		return;

	list_obj = (PyListObject *)p;
	size = PyList_Size(p);
	allocated = list_obj->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		type = Py_TYPE(list_obj->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list_obj->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes_obj;
	Py_ssize_t i, size, first_n_bytes;
	const char *type;
	unsigned char *bytes;

	if (p == NULL || !PyBytes_Check(p))
	{
		printf("Invalid Python bytes object\n");
		return;
	}

	bytes_obj = (PyBytesObject *)p;
	size = PyBytes_Size(p);
	type = Py_TYPE(p)->tp_name;

	printf("[.] bytes object info\n");
	printf("  type: %s\n", type);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	if (size > 10)
		first_n_bytes = 10;
	else
		first_n_bytes = size;

	bytes = (unsigned char *)PyBytes_AsString(p);

	printf("  first %ld bytes: ", first_n_bytes);
	for (i = 0; i < first_n_bytes; i++)
		printf("%02x ", bytes[i]);

	printf("\n");
}
