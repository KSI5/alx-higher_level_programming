#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid PyListObject\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid PyBytesObject\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("[.] Bytes object info\n");
    printf("  [.] Size: %ld\n", size);
    printf("  [.] Trying string: %s\n", PyBytes_AsString(p));

    if (size > 10)
        size = 10;

    str = PyBytes_AsString(p);
    printf("  [.] First %ld bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", str[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    double value;

    if (!PyFloat_Check(p))
    {
        printf("[ERROR] Invalid PyFloatObject\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("[.] Float object info\n");
    printf("  [.] Value: %f\n", value);
}

