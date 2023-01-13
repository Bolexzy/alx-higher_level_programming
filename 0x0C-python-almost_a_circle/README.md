# Almost a circle
Project done during **Full Stack Software Engineering studies** at **ALX Africa**. It aims to learn about unit testing, serialization, deserialization, JSON, `args` and `kwargs` in **Python**.

## Technologies
- Scripts written in Bash 5.0.17(1)
- Python Scripts are written with Python 3.8.1
- C files are compiled using gcc 9.4.01
- C files are written according to the C90 standard
- Tested on Ubuntu 20.04 LTS

## Files

Inside `models` folder:

| Filename | Description |
| -------- | ----------- |
| `__init__.py` | Script that converts the directory as a package |
| `base.py` | Base class of geometrical instances |
| `rectangle.py` | Class that inherits attributes references from `Base` class |
| `square.py` | Class that inherits attributes references from `Square` class |

Each class contains public/private attibutes, class and static methods. Also, these class raise exceptions when is required.

Inside `tests/test_models` folder:

| Filename | Description |
| -------- | ----------- |
| `__init__.py` | Script that converts the directory as a package |
| `test_base.py` | Module that contains unittests to `Base` class |
| `test_rectangle.py` | Module that contains unittests to `Rectangle` class |
| `test_square.py` | Module that contains unittests to `Square` class |
