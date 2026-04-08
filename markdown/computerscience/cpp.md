
# `const`

variables: prevents change in value after initialization"

```cpp
const type var = value;
// var can no longer can assigned another value.
```
functions: only useable on non-static member functions, prevents them from modifying any static variables.

```cpp
class Class{
    static int var;
    const rtype func(){
        // Class::var = 5 // <- not allowed.
    }
}
```

# `constexpr`

variables: for those fit for compile time evaluation

```cpp
int a = 5
constexpr int b = a + 7;
```
functions:
```cpp
// This function might be evaluated at compile-time, if the input
// is known at compile-time. Otherwise, it is executed at run-time.
constexpr unsigned factorial(unsigned n)
{
    return n < 2 ? 1 : n * factorial(n - 1);
}
```

# `consteval`

functions:
```cpp
// enforced evaluation at compile-time.
consteval unsigned combination(unsigned m, unsigned n)
{
    return factorial(n) / factorial(m) / factorial(n - m);
}
```
# `extern`

external declaration, global variable, assumes definition elsewhere.

variables: false by default:
```cpp 
// header.h
extern type var;
```
```cpp
// main.cpp

type var = value;
```
- functions: true by default
```cpp 
// header.h
rtype func(paratype para);
extern rtype func(paratype para);
// both same
```
```cpp
// main.cpp
rtype func(paratype para){
    // ...
};
```

# `inline`

functions: allows C++ to evalute the functions in Compile-Time and not Run-time, increases performance at the cost of storage & memory, false by default:

```cpp
inline rtype func(paratype para){
    // ...
};

rtype a = func(arg1);
rtype b = func(arg2);
```
this would be the same as just writing the result of `func` with both parameters directly.

# `static`

variables:

- global: restricts the declaration to the current file only.

```cpp
static type var = value;
```

- function scope: retrains it's value even through different function calls:

```cpp
void func(){
    static int counter = 0; // initial
    couter ++; // per run
};

```

- class scope: direct class call, no instance.

```cpp
class Class{
    public:
    static var;
    static rtype func();
}

Class::var;
Class::func();
```

functions: restricts the declaration to the current file only.

```cpp
static rtype func(){
    // ...
};
```