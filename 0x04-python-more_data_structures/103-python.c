#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));

    size = PyList_Size(p);
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_GET_SIZE(p);
    string = PyBytes_AS_STRING(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i < (size < 10 ? size : 10); i++)
        printf(" %02x", string[i]);

    printf("\n");
}

