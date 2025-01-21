# Type annotations in python

## Introduction

Type annotations are a way to add type hints to your code. They are not enforced by the Python interpreter, but they can be used by external tools to check your code for errors. Type annotations can help you catch bugs early, make your code more readable, and improve the performance of your code.

## Basic types

Python has several built-in types that you can use in type annotations. Here are some of the most common ones:

- `int`: Integer
- `float`: Floating point number
- `str`: String
- `bool`: Boolean
- `list`: List
- `tuple`: Tuple
- `dict`: Dictionary
- `set`: Set

You can use these types in your type annotations like this:

```python
def add(x: int, y: int) -> int:
	return x + y
```

In this example, the `add` function takes two arguments, `x` and `y`, which are both integers, and returns an integer.

## Optional types

You can also use optional types in your type annotations. Optional types are types that can be `None`. You can use the `Optional` type from the `typing` module to specify an optional type. Here's an example:

```python
from typing import Optional

def greet(name: Optional[str]) -> str:
	if name is None:
		return 'Hello, world!'
	else:
		return f'Hello, {name}!'
```

In this example, the `greet` function takes an optional string argument, `name`, and returns a string.

## Union types

You can use union types in your type annotations to specify that a value can be one of several types. You can use the `Union` type from the `typing` module to specify a union type. Here's an example:

```python
from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
	return x + y
```

In this example, the `add` function takes two arguments, `x` and `y`, which can be either integers or floating point numbers, and returns an integer or a floating point number.

## Type aliases

You can use type aliases in your type annotations to give a name to a type. You can use the `Type` type from the `typing` module to specify a type alias. Here's an example:

```python
from typing import Type

UserId = int

def get_user(user_id: UserId) -> str:
	return f'User {user_id}'
```

In this example, the `UserId` type alias is used to specify that the `user_id` argument to the `get_user` function is an integer.

## Conclusion

Type annotations are a powerful tool that can help you write better code. They can help you catch bugs early, make your code more readable, and improve the performance of your code. If you're not already using type annotations in your code, I highly recommend giving them a try.

## References

- [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [PEP 483 -- The Theory of Type Hints](https://www.python.org/dev/peps/pep-0483/)
- [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
- [Python Type Checking (Guide)](https://realpython.com/python-type-checking/)
- [Type hints cheat sheet (Python 3)](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
