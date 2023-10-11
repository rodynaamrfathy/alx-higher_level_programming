#include "Python.h"

/**
 * print_python_bytes - Print information about Python bytes object
 * @p: Pointer to the Python object
 */
void print_python_bytes(PyObject *p)
{
    int i, size, limit;
    char *str;

    printf("[.] bytes object info\n");

    if (PyBytes_Check(p))
    {
        size = PyBytes_Size(p);
        str = ((PyBytesObject *)p)->ob_sval;
        limit = size < 10 ? size : 10;

        printf("  size: %d\n", size);
        printf("  trying string: %s\n", str);
        printf("  first %d bytes: ", limit);
        for (i = 0; i < limit; i++)
            printf("%02x ", str[i] & 0xff);
        printf("\n");
    }
    else
    {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

/**
 * print_python_list - Print information about Python list object
 * @p: Pointer to the Python object
 */
void print_python_list(PyObject *p)
{
    int size, allocated, i;
    PyObject *item;

    printf("[*] Python list info\n");

    if (PyList_Check(p))
    {
        size = ((PyVarObject *)p)->ob_size;
        allocated = ((PyListObject *)p)->allocated;

        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", allocated);

        for (i = 0; i < size; i++)
        {
            item = ((PyListObject *)p)->ob_item[i];
            printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
        }
    }
    else
    {
        printf("[ERROR] Invalid List Object\n");
    }
}
