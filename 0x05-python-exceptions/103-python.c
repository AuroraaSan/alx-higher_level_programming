#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n  size: %ld\n  trying string: %s\n", size, PyBytes_AsString(p));
    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02x", ((unsigned char *)PyBytes_AsString(p))[i]);
        if (i == 9) printf("\n");
        else printf(" ");
    }
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    double value = PyFloat_AsDouble(p);
    printf("[.] float object info\n  value: %lf\n", value);
}

