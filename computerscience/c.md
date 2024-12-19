C a General-Purpose, Low-level, Compiled, Fast Programming Language

# Basics

"Hello, World!"

```c
#include<stdio.h>

int main(){
    printf("Hello, World!");
    return 0;
}
```

```c
#include<library.h>

int main(){
    // Main Logic
    return 0;
}
```
***library*** where you can import pre-made external code to provide additional functionality to your code, this section of the code is also known as the header

the ***main*** function is where the main code of the function start's to execute, the function can return either a `0` for ***success***, or a `1` for ***error***
```c
int main(int argc, char **argv)
```

- Line/Statement in C must end with a `;` in the end
- Any newlines and white spaces, comments are ignored

# Variables

Variables are Addresses in Memory that store Certain Kinds of Data such as strings, integers, floats etc.

## Declaration:

```c
type name = value;
name = value; 
```

Example:
```c
int number = 255;
            
number2 = 64;

number = 32; // Overwrite previously written data
```

## Constants
They are Variables that can't be overwritten after declaration
```c
const type Name = value;
const Name = value;
```

## Variable Rules:
        
- Case Sensitivity
- No Spaces or Comma Allowed (` `, `,`).
- No Special Characters are allowed other than underscore (`_`).
- First Character must be an Aplhabet or underscore (`a-z`, `_`).

## Reserved Keywords

`auto`, `break`, `case`, `char`, `const`, `continue`, `default`, `do`, `double`, `long`, `return`, `register`, `short`, `signed`, `sizeof`, `static`, `int`, `else`, `enum`, `extern`, `float`, `for`, `goto`, `if`, `struct`, `switch`, `typedef`, `union`, `unsigned`, `void`, `volatile`, `while`

## Memory Address

**Memory Address** 8 bytes of space on the Memory that is used by variables to store data on, and each Memory Address is `32bit` or `64bit` unsigned integer that references the block of memory.

The memory address can be obtained using the `&` operator:
```c
&variable
```

### Pointer

---

**Pointer** a type of Variable that contains Memory Address of another Variable, and the variable can be referenced, using that pointer

**Declaration**:
```c
type *ptr
```
- `type` is the datatype it expects to find when the pointer is deferenced

**Address**:
```c
ptr
```
Deference the value at the Memory location
```c
*ptr
```

Example:-
```c
// declaration
int a = 25;

int *ptr = &a;

printf("Address: %p\n", ptr); // Address: 0061FF18
printf("int: %d\n", *ptr); // int: 25
```

Format Specifier: `%p`

### Pointer Arithmetic

---

The Pointer is a `32bit` or `64bit` unsigned integer, meaning it can be Added/Subtracted to found Adjacent Elements.

Depending size of the type of pointer, the added/subtracted number will be multiplied by that number, skipping all the memory blocks that are used by that variable

```c
ptr + n
ptr - n
```

example:

```c
int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

printf("Address: %p Value: %d\n", arr, *arr);
printf("Address: %p Value: %d\n", arr+1, *arr+1);
printf("Address: %p Value: %d\n", arr+2, *arr+2);

/*
Address: 000000C14E5FF6A0 Value: 1
Address: 000000C14E5FF6A4 Value: 2
Address: 000000C14E5FF6A8 Value: 3

The Difference in each of the is 4, since sizeof(int) is 4 bytes
*/
```
# Data Types

Data Types are Types of Data that can be stored in Variables

The Data Types are divided in 3 main types: **Primitive**, **Derived**

## Primitive


- `signed`: represents both Positive and Negative Values, used with either `int` or `char`
- `unsigned`: represents only Positive Values, used with either `int` or `char`

### char
`char`: A Single Byte Character UTF-8 Character
    
```c
char c = 'a';
```

The character is written in-between 2 single quotes `''`

`'o'`

[ASCII Table](./computer_science.md#ascii-table)

- Size: `1 Byte`, `8bit`
- Range: (`-128` to `127`) or (`0` to `255`)
- Format Specifier: `%c`



Variations:
- `signed`
    - Range: (`-128` to `127`)
- `unsigned`
    - Range: (`0` to `255`)

### int

`int` an Integer Number

```c            
int a = 2;
```
- Size: `4 Bytes`, `32bit`
- Range: `-2,147,483,648` - `2,147,483,647`,
- Format Specifier: `%d`
- implicitally `signed`

Variations:

- `unsigned int`

    - Size: `4 Bytes`, `32bit`
    - Range: 0 - 4,294,967,295 
    - Format Specifier: `%u` 

- `short int`

    - Size: `2 Bytes`, `16bit`
    - Range: `-32,768` to `32,767`
    - Format Specifier: `%hd`
    - implicitally `signed`
    
    - `unsigned short int`

        - Format Specifier: `%hu`
        - Range: `0` to `65,535`

- `long int`
    
    - Size: `4 Bytes`, `32bit`
    - Range: `-2,147,483,648` to `2,147,483,647`
    - Format Specifier: `%ld`
    - implicitally `signed`

    - `unsigned long int`

        - Range: `0` - `4,294,967,295` 
        - Format Specifier: `%lu`

- `long long int`

    - Size: `8 Bytes`, `64bit`
    - Range: `-(2^63)` to `(2^63)-1 `
    - Format Specifier: `%lld` 

    - `unsigned long long int`

        - Range: `0` to `18,446,744,073,709,551,615`
        - Format Specifier: `%llu`

### Float

`float` a Decimal/Floating point Number

```c
float b = 1.4;
```
- Size: `4 Bytes`, `32bit`
- Range: `1.2E-38` to `3.4E+38`
- Format Specifier: `%f` 

Variations:

- `double`

    - Size: `8 Bytes`, `64bit`
    - Range: `1.7E-308` to `1.7E+308`
    - Format Specifier: `%lf`

- `long double`

    - Size: `16 Bytes`, `128bit`
    - Range: `3.4E-4932` to `1.1E+4932`
    - Format Specifier: `%Lf`

## Deriaved

- [Functions](#)

- [Arrays](#)

- [Pointer](#)

## User defined

- [Structures](#)

## Format Specifiers:

Format Specifiers Allows specifies the representation of certain datatypes and modify it's I/O

`%[flags][width][.precision][length]specifier`


- `flags` - Optional. A sequence of any of the following characters:

    - `-`: Makes the output left-justified by adding any padding spaces to the right instead of to the left.
    - `#`: Shows an alternate representation of the formatted data depending on the conversion.
    - `+`: Causes positive numbers to always be prefixed with `+`.
    - ` `: (A space character) This prefixes a space to positive numbers, primarily so that the digits can be lined up with the digits of negative numbers.
    - `0`: Pads numbers with zeroes on the left.

- `width` - Optional. A whole number specifying the minimum number of characters that the output should occupy. If necessary, spaces are added to the right to reach this number, or to the left if the - flag is used. If an *asterisk is used then the width is given by the argument preceding the one being represented.
- `.precision` - Optional. A . followed by a whole number indicating how many decimal digits to show in the formatted data.
- `length` - Optional. A sequence of characters which changes the expected data type of the argument. It can be one of the following:

    - `hh`: Expect char type for whole numbers.
    - `h`: Expect short int type for whole numbers.
    - `l`: Expect long int type for whole numbers.
        - Expect `wint_t` type for characters.
        - Expect `wchar_t*` type for strings.
    - `ll`: Expect long long int type for whole numbers.
    - `j`: Expect intmax_tor uintmax_t type for whole numbers.
    - `z`: Expect size_t type for whole numbers.
    - `t`: Expect ptrdiff_t type for whole numbers.
    - `L`: Expect long double type for floating point numbers.

- `specifier` - Required. A character which indicates how an argument's data should be represented

    - `c`: char, signed char, unsigned char
    - `d`, `i` : Decimal Integer
    - `u`: Unsigned Decimal
    - `o`: Octal Number (base 7), `#` prefixes with "0"
    - `x`, `X` : Hexadecimal Integer, upper/lower case, `#` prefixes with "0x"
    - `f`, `F` : Floating Point Number, upper/lower case, `#` forces decimal point
    - `e`, `E` : Floating Point Number in Scientific Notation, upper/lower case, `#` forces decimal point
    - `g`, `G` : Shortest Representation between `f` and `e`, upper/lower for corresponding `f` and `e`.
    - `a`, `A` : Floating Point Number as Hexadecimal as Internal Representation, upper/lower case.
    - `s`: String
    - `p`: pointer, Memory Address
    - `n`: no output
    - `zu`: function output
    - `%`: literal `%`

Example:-
```c
int myNum = 15;
float myFloatNum = 5.99;
char myLetter = 'D';

printf("%d", myNum);
printf("%f", myFloatNum);
printf("%c", myLetter); 
```
## Type Casting

Cast a Value into a DataType

```c   
(type) value;
```

Values are usually already casted when defining a variable and assigning a value

```c
type variable = value;
```

Example::

```c
int = 5;
float b = (float) a; // 5.0000000
// float b = a; // 5.0000000, this will also work.
```

Type Conversion Stream:

```c
bool -> char -> short int -> int -> unsigned int -> long -> unsigned -> long long -> float -> double -> long double
```

`bool`: In Type Conversion to boolean every Value other than 0 is represeted as `true` (`1`)

```c
bool a = (bool) 0; // false
bool a = (bool) 1; // true
bool a = (bool) 2; // true
bool a = (bool) 5.3; // true
bool a = (bool) 'f'; // true
bool a = (bool) 2*2*2*2*2*2*2*2 - 1; // true
```

# Comments

Comments are Peice of Text in The Source Code that are made to be ignored by the Interpreter/Compiler, any *whitespaces* and *newlines* are also ignored.

One Line Comment:
```c
// TEXT
```

```c
int main(){
    // This is a Comment, It won't effect the code and is usually used for Documentation in code;
    printf("Hello");
    return 0;
};
```
**Multiline**:

```c
/* TEXT */
```

A Comment that only exists in-between `/*` and `*/`, it can also be multi-<br>line

```c
int main(){
    printf("Hello"); /* This is a Multi-
    Line Comment
    */
    return 0;
};
```

# Declaration, Expressions, Statements

 **Declarations**: defining/initialization of variables, functions, structs etc.

```c
int num = 5;
```

**Expressions**: are a set of operations that do not impact the control flow of the program and returns a value. eg Operators, function calling etc.

```c
sum(52, 6);
```

**Statements**: Controls that Impact the Control Flow of the Executing Program, eg If, switch, loops etc.

```c
if (condition) {
    // Do something
} else {
    // else do that.
}
```

**Labels**: A Group of Statements Labeled with a unique name

all statements inside All labels are run by default
```c
printf("Outside\n");

label1:
    printf("Label 1\n");
    
label2:
    printf("Label 2\n");
    char a = 5;
```

- `goto`: a jump statement / unconditional jump statement which allows skipping of statements and jump to given label

    syntax:        
    ```c
    goto label;
    ```

    example:-
    
    ```c
    printf("Outside\n");

    goto label2;

    // These lines won't run:
    printf("After Jump\n");

    label1:
        printf("Label 1\n");

    printf("Middle\n");

    // Lines from here will run:
    label2:
        printf("Label 2\n");
        char a = 5;

    // a is still accessible
    printf("a: %d\n", a);
    printf("End\n");

    /* stdout
    Outside
    Label 2
    a: 5
    End
    */
    ```

# Operators

## Arithmetic

- `+` : **Addition**, Adds together two values

    ```c
    a + b
    ```

- `-` : **Subtraction**, Subtracts one value from another
    
    ```c
    a - b
    ```

- `*` : **Multiplication**, Multiplies two values

    ```c
    a * b
    ```

- `/` : **Division**, Divides one value by another

    ```c
    a / b
    ```

- `%` : **Modulus**, Returns the division remainder

    ```c        
    a % b
    ```

- `++`: **Increment**

    - Prefix, increment by 1 assign and return it's incremented value
        
        ```c
        ++a
        ```

    - Suffix, return it's value (*before increment*), increment value and assign
        
        ```c
        a++
        ```

- `--`: **Decrement**

    - Prefix, decrement by 1 assign and return it's decremented value
        
        ```c
        --a
        ```

    - Suffix, return it's value (*before decrement*), decrement value and assign
        
        ```c
        a--
        ```

### Evaluation

Arithmetic Expressions in C doesn't Follow rules of BEDMAS/BODMAS and instead uses it's own Evaluation System

Expressions Inside Brackets are Always Evaluated Seperately regardless of the Rules

**Operator Precendence**: Arithmetic Operator in C have their Own Priority List:

| Order | Operators     | Operator Names                                |
| ----- | ------------- | --------------------------------------------- |
| $1$   | `*`, `/`, `%` | **Multiplication**, **Division**, **Modulus** |
| $2$   | `+`, `-`      | **Addition**, **Subtraction**                 |
| $3$   | `=`           | **Evaluation**                                |

**Operator Associativity**: If 2 Arithmetic Operators are on the Same Priority, then Their Order is Used to Evaluate Them:

```c
a*b/c == (a*b)/c
a/b*c == (a/b)*c
```

## Comparison Operators

- `==`: **Equal to**, Returns 1 if the values are equal

    ```c
    a == b
    ```

- `!=`: **Not equal**, Returns 1 if the values are not equal
    
    ```c
    a != b
    ```

- `> `: **Greater than**, Returns 1 if the first value is greater than the second value
    
    ```c
    a > b
    ```

- `< `: **Less than**, Returns 1 if the first value is less than the second value
    
    ```c
    a < b
    ```

- `>=`: **Greater than or equal to**, Returns 1 if the first value is greater than, or equal to, the second value
    
    ```c
    a >= b
    ```

- `<=`: **Less than or equal to**, Returns 1 if the first value is less than, or equal to, the second value
    
    ```c
    a <= b
    ```

## Logic Operators

- `&&`:	**AND**, performs logical *AND* operation on 2 inputs and return's it's output
- `||`:	**OR**, performs logical *OR* operation on 2 inputs and return's it's output
- `!`: **NOT**, performs logical *NOT* operation on an input and return's it's output

## Bitwise

- `&`: **Bitwise AND**, takes 2 numbers and performs *AND* operation on each bit with the other number's
    
    ```c
    a & b
    ```

- `|`: **Bitwise OR**, takes 2 numbers and performs *OR* operation on each bit with the other number's
    
    ```c
    a | b
    ```

- `^`: **Bitwise XOR**: takes 2 numbers and performs *OR* operation on each bit with the other number's
    
    ```c
    a ^ b
    ```

- `<<`: **Left Shift**: takes 2 numbers and *offset*'s every bit of `a` to the *Left* by `b` count of bits

    ```c
    a << b
    ```

- `>>`: **Right Shift**: takes 2 numbers and *offset*'s every bit of `a` to the *Right* by `b` count of bits

    ```c
    a >> b
    ```

- `~`: **bitwise NOT**: takes 1 number and all of it's bits.

    ```c
    ~a
    ```

## Unary
Unary operators are the operators that perform operations on a single operand to produce a new value.

- `–`: Unary minus

    ```c
    (–a)
    ```

- `++`: **Increment**

    - Prefix, increment by 1 assign and return it's incremented value
        
        ```c
        ++a
        ```

    - Suffix, return it's value (*before increment*), increment value and assign
        
        ```c
        a++
        ```

- `--`: **Decrement**

    - Prefix, decrement by 1 assign and return it's decremented value
        
        ```c
        --a
        ```

    - Suffix, return it's value (*before decrement*), decrement value and assign
        
        ```c
        a--
        ```
- `!`: **NOT**, performs logical *NOT* operation on an input and return's it's output
- `&`: **Addressof**, return's Memory Address of a variable

    ```c
    &a
    ```

## Misc Operators 

- `&`: **Addressof**, return's Memory Address of a variable

- `*`: **Pointer**, pointer declaration or Pointer Deference

    ```c
    type *ptr;
    *ptr
    ```

- `? :` Ternary Expression, minimized version of IF-ELSE but as Expression.
    
    ```c
    a? b : c
    ```

- `.` **Member Access**, access a member of a structure

    ```c
    structure.property
    ```

- `−>` **Pointer Member Access**, Access a member of a Structure with it's pointer

    ```c
    structurePtr->property
    ```
    also equivalent to:
    ```c
    (*structurePtr).property
    ```

## Assignment

        () = 	(a = b): Assignment
            
            int a = 5

            (b) Same as: `a = 5`
        () += 	(a += b): Addition Assignment
            
            int a += 3

            (b) Same as: `a = a + 3`
        () -= 	(a -= b): Subtraction Assignment
            
            int a -= 3

            (b) Same as: `a = a - 3`
        () *= 	(a *= b): MultiplicationAssignment
            
            int a *= 3

            (b) Same as: `a = a * 3`
        () /= 	(a /= b): Division Assignment
            
            int a /= 3

            (b) Same as: `a = a / 3`
        () %= 	(a %= b): Modulus Assignment
            
            int a %= 3

            (b) Same as: `a = a % 3`

        () &= 	(a &= b): Bitwise AND Assignment
            
            int a &= 3

            (b) Same as: `a = a & 3`
        () |= 	(a |= b): Bitwise OR Assignment
            
            int a |= 3

            (b) Same as: `a = a | 3`
        () ^= 	(a ^= b): Bitwise XOR Assignment
            
            int a ^= 3

            (b) Same as: `a = a ^ 3`
        () >>= 	(a >>= b): Left Shift Assignment
            
            int a >>= 3

            (b) Same as: `a = a >> 3`
        () <<= 	(a <<= b): Right Shift Assignment
            
            int a <<= 3

            (b) Same as: `a = a <<`

## Operator Precendence

        (a) Evaluation Order:
| Order | Operator             | Operator Name                                                                      |
| ----- | -------------------- | ---------------------------------------------------------------------------------- |
| $1$   | `!`                  | **Not**                                                                            |
| $2$   | `*`, `/`, `%`        | **Muliplication**, **Divison**, **Modulus**                                        |
| $3$   | `+`, `-`             | **Addition**, **Subtraction**                                                      |
| $4$   | `<`, `>`, `<=`, `>=` | **Greater-than**, **Less-than**, **Greater-than-or-Equal**, **Less-than-or-Equal** |
| $5$   | `==`, `!=`           | **Equal**, **NOT-Equal**                                                           |
| $6$   | `&&`                 | **AND**                                                                            |
| $7$   | `\|\|`               | **OR**                                                                             |
| $8$   | `=`                  | **ASSIGMENT**                                                                      |

# Conditionals

## if Statement

Syntax:

Runs a Specific Block of Code ONLY IF The Condition is true

```c
if (condition){
    // Execute on condition
};
```

Example:-

```c
int a = 5;
int b = 3;
if(a>b){
    printf("A is Bigger than B");
};

/*
stdout:
A is Bigger than B
*/

int a = 2;
int b = 10;
if(a>b){
    printf("A is Bigger than B");
};

if(a%2==0){
    printf("A is an Even Number!");
};

/*
stdout:
A is an Even Number!
*/
```
## if-else Statement

It's Chained with an If-Statement and runs a Block of code only IF the Condition isn't true

Syntax:-
```c
if (condition){
    // Execute on condition
} else {
    // Execute if the condition is NOT met
}
```

Example: -
```c
int a = 2;
int b = 10;
if(a>b){
    printf("A is Bigger than B");
} else {
    printf("A is Not Bigger than B");
};

/*
stdout:
A is Not Bigger than B
*/
```

## if-else-if... Statment

It Must be Chained after an If Statement, and there's no limit for **else-if statements**

Syntax:

```c
if (condition1){
    // Execute on condition
} else if (condition2){
    // Execute if condition2 is met and condition1 is not met
}
```
```c
if (condition1){
    // Execute on condition
} else if (condition2){
    // Execute if condition2 is met and condition1 is not met
}
// else-if ...
else {
    // Execute if All of The Conditions in IF and ELSE IF Statments are Not Met or Failed
}
```
examples: -
```c

int a = 5;
int b = 10;
if(a>b){
    printf("A is Bigger than B\n");
} else if (a % 2 != 0){
    printf("A is Odd Number");
} else {
    printf("A is Smaller than B and A is Even");
};

/*
stdout:
A is Odd Number
*/
```

```c
int a = 4;
int b = 10;
if(a>b){
    printf("A is Bigger than B\n");
} else if(a<3){
    printf("A is Smaller than 3\n");
} else if (a % 2 != 0){
    printf("A is Odd Number\n");
} else {
    printf("A is Smaller than B and A is Even\n");
};

/*
stdout:
A is Smaller than B and A is Even
*/
```
```c
int a = 2; // less than 3 and is Even
int b = 10;
if(a>b){
    printf("A is Bigger than B\n");
} else if(a<3){ // true
    printf("A is Smaller than 3\n");
} else if (a % 2 != 0){ // also true, but will be skipped due to the upper one is also true
    printf("A is Odd Number\n");
} else {
    printf("A is Smaller than B and A is Even\n");
};

// Order Matters

/*
stdout:
A is Smaller than 3
*/
```

## Ternary

Similar to If-else Statment, but is an Expression, meaning it doesn't allows code to be run inside blocks and instead return's a value/expression

Syntax:

```c
condition? dothis : dothat
```

Example:

```c
char mychar = (5>2)? 'a': 'b';
printf("%c\n", mychar); // a

char mychar2 = (2>5)? 'a': 'b';
printf("%c\n", mychar2); // b
```

## Switch-Case

A Special Type of IF-statement where a `RootValue` is passed, and ***cases*** are added to the expression, the cases will be checked if they are equal to `RootValue`, the code inside that case statement will be executed, 
and if a `break` statement is not added inside the case, then after hitting match all of the code blocks in the cases below the match will be executed regardless of them matching or not.

Syntax:

```c
switch (cmprvalue){
    case value1:
        // If value1 == cmprvalue
    // more cases...
};
```

without break:
```c
case value:
    // ...
```
with break:

**Default**: a type of case that always evaluates to true, works similar to an `ELSE` statement

```c
default:
    // ...
```

```c
switch (rootValue){
    case value1:
        // If value1 == rootValue
    case <value2:
        // If value2 == rootValue
    // more cases....
    case valueN:
        // If valueN == rootValue
    default:
        // If none of the above matches
};

```
Examples:-

```c    
char myChar = 'a'
switch (myChar){
    case 'b': // Doesn't match
        printf("case 'b' matched!\n");
    case 'c': // Doesn't match
        printf("case 'c' matched!\n");
    case 'a': // Matches
        printf("case 'a' matched!\n");
    case 'd': // Doesn't matches but there's no Break Statement Above
        printf("case 'd' matched!\n");
    default: // isn't true, but there's no Break Statement Above
        printf("No Case Matched!\n");
};

/* Output:
case 'a' matched!
case 'd' matched!
No Case Matched!
*/
```
```c
// With break Statement
char myChar = 'a';
switch (myChar){
    case 'b': // Doesn't match
        printf("case 'b' matched!\n");
        break;
    case 'c': // Doesn't match
        printf("case 'c' matched!\n");
        break;
    case 'a': // Matches
        printf("case 'a' matched!\n");
        break;
    case 'd': // Doesn't match
        printf("case 'd' matched!\n");
        break;
    default: // One Matched, doesn't runs
        printf("No Case Matched!\n");
        break;
};

/* Output:
case 'a' matched!
*/
```

# Loops

## For-Loops

Runs a Specific Peice of Code until the Iteration Ends

Syntax:
```c
for(declaration; condition; modification){
    // Block of Code to Run until Condition is no-longer true
};
```

- `declaration`: is a variable initialization, determines the index at which the loop will start
    ```c
    int i = 0
    ```
- `condition`: If the Condition then the iteration will continue otherwise, it'll end the loop
    ```c
    i<1000
    ```
- `modification`: a change in the declaration variable so the loop will not be infinite
    ```c
    i++
    ```

Examples:-

```c
for(int i = 1; i<=10; i++){
    printf("This Code Ran [%d] Times!\n",i);
};
/*
This Code Ran [1] Times!
This Code Ran [2] Times!
This Code Ran [3] Times!
This Code Ran [4] Times!
This Code Ran [5] Times!
This Code Ran [6] Times!
This Code Ran [7] Times!
This Code Ran [8] Times!
This Code Ran [9] Times!
This Code Ran [10] Times!
*/
```
```c
// Reverse Loop
for(int i = 10; i>0; i--){
    printf("Value of i is [%d]\n", i);
};
/* Output:
Value of i is [10]
Value of i is [9]
Value of i is [8]
Value of i is [7]
Value of i is [6]
Value of i is [5]
Value of i is [4]
Value of i is [3]
Value of i is [2]
Value of i is [1]
*/
```

## While

The Original/Traditional Version of Loops, Checks if the Condition is True, then runs the code for each iteration

syntax: -
```c
while(condition){
    // Code to Runs While <condition> is true
}
```

examples: -
```c
int i = 0;
while (i<=10){
    printf("It Ran %d Times!\n", i);
    i++; // WARNING: If the Condition Doesn't never becomes 'false', It will cause a An Infinite Loop        
};

// Progress:
int i = 1;
while (i<=100){
    printf("\rProgressed [%d]", i);
    i++; // Increases Progress by 1
    sleep(1); // Pause for 1 second
};
printf("\n");
```

## Do-While Loops

A Variant of Traditional While Loops, but it runs the Code First and then checks the condition, and if the conditon matches it continues with the next iteration

Syntax:

```c
do {
    // Code to Run
} while (condition);
```
Examples:-

```c
int i = 5;
do {
    // Runs atleast once
    printf("%d\n", i);
} while (i>10); // Checks Conditon for the Next Iteration
// stdout: 5
```

```c
int i = 2;
do {
    // Runs atleast once
    printf("%d\n", i);
    i++;
} while (i<10); // Checks Conditon for the Next Iteration
/* stdout:
2
3
4
5
6
7
8
9
*/
```

## Loop Controls

`break`: Exists The Loop

```c
for (int i = 1; i<=10; i++){
    if(i == 6){ break; };
    printf("i: %d\n", i);
};
printf("Loop Ended\n");

// Loop Ends after 5th iteration, even though it should have continued until 10th
/* stdout:
i: 1
i: 2
i: 3
i: 4
i: 5
Loop Ended
*/
```

`continue`: Skips the Current Iteration

```c
for (int i = 1; i<=10; i++){
    if(i == 6){ continue; };
    printf("i: %d\n", i);
};
printf("Loop Ended\n");

// Skips The 6th Iteration
/* stdout:
i: 1
i: 2
i: 3
i: 4
i: 5
i: 7
i: 8
i: 9
i: 10
Loop Ended
*/
```
`return`: If the loop is runnning inside a function, and it returns inside a loop then the loop will also end

# Functions

**Functions** They are used to define reusable blocks of code that can be executed when called. Function is a Block of code that is designed to perform a particular task, it can be used for code lines that are repeated.

It part of the Functional Programming Paradyme

Syntax:

```c
// Function Declaration

rtype name(type var){
    // code    
};
```

Format Specifier: `%zu`

## Function Prototypes
They are expressions that make a Function be accessible before it's declaration with complete functionality

Syntax:-
```c
// Function Prototype

rtype name(type);
rtype name(type var);
```

```c
#include<stdio.h>
int sum(int, int);

int main(){
    int a = 5;
    int b = 10;
    int a_plus_b = sum(a, b);
    printf("%d", a_plus_b); // 15
    return 0;
}

int sum(int num1, int num2){
    return num1 + num2;
};
```
## Static

static are variables that are defined inside a function and can continue to hold their values even after the function returns

syntax:

```c
static variable;
```     

example:-
```c
int trackCalls(){
    static int calls = 0; // Initial, Only declared on first call
    calls += 1;
    return calls;
}

int main(){
    printf("Calls: %d\n", trackCalls()); // Calls: 1
    printf("Calls: %d\n", trackCalls()); // Calls: 2
    printf("Calls: %d\n", trackCalls()); // Calls: 3
    printf("Calls: %d\n", trackCalls()); // Calls: 4
    return 0;
};
```     
## Built-in

- `sizeof(<Varable/DataType>)`: returns the size of The Variable/DataType in Bytes

    ```c
    printf("%zu")
    ```

# Arrays

Array a fixed sized collection of elements of the same type

syntax:

```c
// declaration
type arr[size];
type arr[] = /* ... */; // implicit size,

// Read
arr[index];

// Write
arr[index] = value;
```

- `size` is a Non-Negative number which determines how many elements the Array can have, it can be implicit ONLY if the array is assigned an **Array Value** in which case the size will be obtained from the array-value

    ```c
    sizeof(arr)/sizeof(arr[0])
    ```
- `index` is also a Non-Negative number which from $0$ to $\text{size}-1$, each element in the array are ordered and given the index based on their position in the array.
- `type` is what type of elements are gonna be in the array

**Array value**:
```c
{x_1, x_2, x_3, x_4, /* ... */}
```

`sizeof(array)`: function returns the amount of bytes occupied by all of it's elements

    ```c
    sizeof(array)/sizeof(array[0]) // Length of The Array, Amount of Elements in the Array useful for Looping Through
    ```

example:-
```c
int list[10]; // fixed length array
int list[]; // Dynamic Array

// Looping
int list[] = {26, 23, 3, 2, 4, 6};

for(int i = 0; i<sizeof(list)/sizeof(list[0]); i++){
    printf("index: %d, element: %d\n", i, list[i]);
};

/*
index: 0, element: 26
index: 1, element: 23
index: 2, element: 3
index: 3, element: 2
index: 4, element: 4
index: 5, element: 6
*/
```

In Memory All the Elements of an Array are always Adjacent to each other, meaning with only the address of the first element, all of the other elements in that arry can be accessed/written to.

The Variable created from the declaration of an array is the Memory Address of the first element
```c
int arr[4] = {1, 2, 3, 4};
printf("Pointer: %p, Deference: %d", arr, *arr); // Pointer: 0000001C04FFF8B0, Deference: 1
```

```c

int list[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
printf("Array Address: %p Deference: %d\n", list, *list);
for(int i = 0; i<sizeof(list)/sizeof(list[0]); i++){
    printf("Address: %p Element: %d\n", &list[i], list[i]);
};

/*
Array Address: 0000007C22FFF640 Deference: 1
Address: 0000007C22FFF640 Element: 1
Address: 0000007C22FFF644 Element: 2
Address: 0000007C22FFF648 Element: 3
Address: 0000007C22FFF64C Element: 4
Address: 0000007C22FFF650 Element: 5
Address: 0000007C22FFF654 Element: 6
Address: 0000007C22FFF658 Element: 7
Address: 0000007C22FFF65C Element: 8
Address: 0000007C22FFF660 Element: 9
Address: 0000007C22FFF664 Element: 1
*/
```
# Strings

**String**: A type of Array that holds an Array of Characters

syntax:

```c
char str[]
char str[length]
```

- Format Specifier: `%s`

- A String is written inside a set of 2 Double Quotes

    `"Text"`

**NULL Character**, "**Null Terminating Character**" (`\0`, `\x00`, `\u0000`, `\000`, `0`): a Special Character that determines the Ending of a string in I/O Operations, it's automatically added to the string when writting using double quotes

example:-

```c
char string[] = "Yello, World!";
string; // memory address of the String
string[0] = 'H';
printf("%s", string); // Hello, World!

// define as traditional array:
char string2[] = {'H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'};

char string3[4] = "abc"; // Always Leave space for the Ending NULL character
```

# File

File that can read/written to as a stream

`FILE`: The File Datatype

```c
FILE *fptr;
```
- `fclose(ptr)`: closes a File I/O Stream

- See [`stdio.h`](#stdioh) for I/O Operations

# Structures/Types

## Enumeration (enum)

 A Special Type of Structure, that represents a group of Constants

syntax:        
```c
// declaration
enum Name {
    constant,
};
enum Name {
    constant = value,
}

// usage
enum Name constant;
enum Name constant = <Constant>;

enum Name{
    Constant,
    // Constants...
};
enum Name{
    Constants = Value,
    // ...
};

// usage
enum Name <variable>;
enum Name <variable> = <Constant>;
```
examples:

- Integer Constant:
```c

// without any values set
enum Level {
    Low,
    Medium,
    High,
};

enum Level low = Low; // 0
enum Level medium = Medium; // 1
enum Level high = High; // 2

// one value set:
enum Level {
    Low = 5,
    Medium,
    High,
};

enum Level low = Low; // 5
enum Level medium = Medium; // 6
enum Level high = High; // 7

// middle value set:
enum Level {
    Low,
    Medium = 6,
    High,
};

enum Level low = Low; // 0
enum Level medium = Medium; // 6
enum Level high = High; // 7
```
            (II) Other Types:
```
                enum Level {
                    Low = 'z',
                    Medium = 'x',
                    High = 'y',
                };

                enum Level low = Low; // z
                enum Level medium = Medium; // x
                enum Level high = High; // y

                // Treats them as Byte Integer and Increments their value by 1
                enum Level {
                    Low = 'a',
                    Medium,
                    High,
                };

                enum Level low = Low; // a
                enum Level medium = Medium; // b
                enum Level high = High; // c
```
    () Unions

        union UnionName {
            dataType1 member1;
            dataType2 member2;
            // Other members...
        };

    (ii) structures (struct)

        (a) A way to Organize variables and data into a Structure
        
        (b) Syntax:

            // Declaration
            struct <Structure> {
                <...variables>;
            };
            

            // assignment
            struct <Structure> <structObj>;
            struct <Structure> <structObj> = {<params...>};

        Compound Literal:

            struct Point p = (struct Point){.x = 10, .y = 20};

        (c) Access

            (I) Variable inside The Structure AKA Properties of Structure can be accessed to Read and Write to.

                <structObj>.<property>; // get value
                <structObj>.<property> = <value>; // write
                
                structObj.property; // get value
                structObj.property = value; // write

            (II) struct Pointer access

                struct <StructObj> *<structPtr> = &<structObj>; // Pointer to the structure

                <structPtr>-><property>; // read
                <structPtr>-><property>; // write
                // equivalent to (*<structPtr>).<property>
                
                struct StructObj *structPtr = &structObj; // Pointer to the structure

                structPtr->property; // read
                structPtr->property; // write
                // equivalent to (*structPtr).property
        
        (d) Bit Fields

            (a) variables inside structures that don't follow the standard sizes
            (b) syntax:

                type var: size;

            (c) the size of defined in Bit's (not bytes)

                struct Structure{
                    unsigned int integer: 8;
                };
                int main(){
                    struct Structure a = {255};
                    // printf("size of a.integer : %u", sizeof(a.integer)); // <-- size of a bit field can't be obtained
                    printf("a.integer: %u", a.integer); // 255
                    return 0;
                }

        (e) Example

                struct Structure {
                    char name[20];
                    unsigned short int age;
                };

                struct Structure obj = {"Name", 32};

                // access
                printf("%s\n", obj.name); // Name
                printf("%d\n", obj.age); // 32

                obj.age = 41; // overwrite
        
    (iii) `typedef`: defines/redefines data types under new names/aliases

        (a) Syntax:

            typedef <Type/Structure> <Name>;
            
            typedef Type Name;

            typedef struct Structure { /* ... */} Name;

        Examples:-

        (b) redefine

            typedef double longfloat;
            int main(){
                longfloat a = 0.0L;
                for(int i = 1; i<100; i++){
                    a += 1.0/i;
                }
                printf("a: %.32lf\n", a); // a: 5.1773775760084390640258789062500
                return 0;
            };

        (c) List/Array

            #include<stdio.h>
            #include<stdlib.h>
            #include<math.h>
            #include<stdbool.h>

            typedef struct List {
                int *data;
                int length;
                int capacity;
            } Array;

    
            bool ListPush(struct List *list, int data);
            void ListPrint(struct List *list);

            int main(){

                Array list;
                // struct List list;

                list.length = 0;
                list.capacity = 10;
                list.data = malloc(list.capacity*sizeof(int));

                if(list.data == NULL){
                    printf("Unable to allocate Memory\n");
                    return 1;
                }

                ListPush(&list, 123);
                ListPush(&list, 321);
                ListPush(&list, pow(2, 9));

                printf("Length: %d\n", list.length); // Length: 3
                printf("Capacity: %d\n", list.capacity); // Capacity: 10
                ListPrint(&list); // [123, 321, 512]

                return 0;
            };

            void ListPrint(struct List *list){
                for(int i = 0; i<list->length; i++){
                    printf("%d", list->data[i]);
                    if(list->length-1 != i){ printf(", ");};
                }
            }


            bool ListPush(struct List *list, int data){
                // Pushes data to a List
                if(list->length >= list->capacity){
                    // resize list if not enough capacity
                    list->capacity += 10;
                    list->data = realloc(list->data, list->capacity*sizeof(int));
                    if(list->data == NULL){ return false; };
                }

                // add data
                list->data[list->length] = data;  
                list->length += 1;

                return true;
            }

# Memory

    (i) Static Memory

        (a) Memory reserved for variable before the Program starts executing

    (ii) Dynamic Memory

        (a) Memory that is allocated after the Program starts executing

        (b) Characteristics
            
            (I) Runtime Memory Allocation: Allocation of Dynamic memory

            (II) Complete Control Over Memory

            (III) Doesn't belong to any Variable and can only be accessed via Pointers

        (See Section "/14./(ii)/Memory Management:" for Dynamic Memory Manipulation Functions)

        (c) Stack Memory:

            (I) A Type of Dynamic Memory, which is reserved for variables inside functions

            (II) when the function is returned, the stack memory for that function is freed

        (d) Memory Leak

            (I) a Memory leak is when a Dynamic Memory is allocated but is never freed.
            (II) Examples:

# Library

    Import:

    (i) `#include<<name>>`: imports the specified library

        #include<stdio.h>

# Built-in Libraries:

## stdio.h
 Standard Input Out:

        (a) `fopen(const char * filename, const char * mode)`: Opens a file, creates a Pointer to the File and returns the Pointer

            (I) Modes:

                (A) "r": Allows Read from the File, return NULL if file doesn't exists
                (B) "w": Allows Write from the File, creates file if not exists
                (C) "a": Allows Appending to the end of the File, creates file if not exists
                (D) "r+": Allows Read and Write to The File, returns NULL if file doesn't exists
                (E) "w+": Allows Read and Write to The File, creates file if not exists
                (F) "a+": Allows Read and Write to The File, creates file if not exists

            (III) Extra Appended:

                (A) "b": read/write as Binary

        (b) `fclose(FILE *fptr)`: closes a File

            (I) return `0` on successful close, any other integer on error

        (c) `ferror(File * fpr)`: Returns a true value if a recent file operation had an error

        (d) `rename(const char * oldname, const char * newname)`: Changes the name of a file

            (I) returns an int, 0 if successfully renamed. any other int if error occured;
        
        (e) `remove(const char * filename)`: Deletes a file

            (I) returns an int, 0 if successfully deleted. any other int if error occured;

        (f) `perror(const char * ErrMsg)`: prints the error message for the last operation with a label

            int msg;
            int success = fscanf(stdin, "%d", &msg);

            if(success != 1){
                perror("Invalid Input");
                exit(1);
            }

            printf("Success!");

        Indicator:

        (g) `fseek(FILE * fptr, long int offset, int origin)`: Moves the position indicator of a file pointer
            
            () `fptr`: Required. A file pointer, usually created by the fopen() function.
            () `offset`: Required. Specifies a position in the file relative to the origin.
            () `origin`: Required. Specifies the position in the file from which the offset is applied. It can be one of the following constants:

                () `SEEK_SET`: Offset is relative to the beginning of the file
                () `SEEK_CUR`: Offset is relative to the current position in the file
                () `SEEK_END`: Offset is relative to the end of the file
                
                The SEEK_END value may not be fully supported by some implementations of the library. 

            // ./test.txt:  Hello, World!
            FILE * fptr = fopen("./test.txt", "r");

            if(fseek(fptr, 7, SEEK_SET) != 0){
                fprintf(stderr, "File Error");
                return 1;
            }

            char a = fgetc(fptr);

            if(a == EOF){
                fprintf(stderr, "char a = EOF, File Error");
                return 1;
            }

            printf("Character: %c", a); // Character: W

            (I) returns An int value which is zero if successful and non-zero if an error occurred.

        (h) `ftell(FILE * fptr)`: Returns the value of the position indicator of a file pointer as an Int

            FILE *fptr = fopen("./read.txt", "r");

            char block[11];
            fread(block, 1, 10, fptr);
            block[11] = '\0';
            long indicator = ftell(fptr);

            printf("%lu", indicator); // 10
        
        (i) `rewind(FILE * fptr)`: Moves the position indicator to the beginning of the file

            FILE *fptr = fopen("./read.txt", "r");

            char block[11];
            fread(block, 1, 10, fptr);
            block[11] = '\0';

            rewind(fptr);
            long indicator = ftell(fptr);

            printf("%lu", indicator); // 0
        
        (j) `feof(FILE * fptr)`: Returns a true value when the position indicator has reached the end of the file

        WRITE/UPDATE:

        (k) `fwrite(const void * source, size_t size, size_t amount, FILE * fptr)`: Writes data from a block of memory into a file

            (I) `destination`: pointer to a Block of memory to read data from.
            (II) `size`: size of an element.
            (III) `amount`: amount of elements to read from memory and write to memory.
            (IV) `fptr`: File Pointer.

            (V) returns `size_t` value representing the number of elements that were written into the file.

        (l) `fprintf(FILE * fptr, const char * format, arg1, arg2...)`: writes a Formatted string to The File.

            (I) returns an int value representing the number of characters written to the file. If an error occurred then it returns a negative number.

        (m) `fputs(const char * str, FILE * fptr)`: Writes a string into a file and advances the position indicator.

            (I) return an int value that is not negative if the function was successful. It returns the constant EOF if an error occurred.

        (n) `fputc(int c, FILE * fptr)`: Writes a character into a file and advances the position indicator.

            (I) returns an int value representing the ASCII value of the character, or the constant EOF if the character could not be written into the file.

        (o) `printf(const char * format, arg1, arg2...)`: Writes a Formatted string to The stdout (Standard Output).

            (I) returns an int value representing the number of characters written to the stdout. If an error occurred then it returns a negative number.

        (p) `puts(const char * str)`: writes a string to the the stdout

            (I) returns int value that is not negative if the function was successful. It returns the constant EOF if an error occurred.

        (q) `putc(int c, FILE * fptr)`: The same as `fputc()`

            (I) return int value representing the ASCII value of the character that was written.
        
        (r) `putchar(int c)`: Outputs a single character to the stdout

            (I) return an int value representing the ASCII value of the character that was written.

        (s) `snprintf(char * destination, size_t * size, const char * format, arg1, arg2...)`: Writes a formatted string into a char array (memory-safe)

            (I) destination: String to write to 
            (II) size: amount of bytes write to the string, (including the null terminating character).
            (III) format: A Formatted String to write to the Destionation String
            (IV) arg1, arg2...


            (V) returns an int value representing the number of characters that were intended to be written to the array (excluding the null terminating character). If this is greater than or equal to the size argument then there are some characters that could not be written to the array. If an error occurred then it returns a negative number.

            char destination[20];


            int a = 3;
            int size = snprintf(destination, 19, "Hello, World! %d", a);

            if(size<0){
                fprintf(stderr, "Error Unable to write to string");
                return 1;
            }
            destination[size] = '\0';

            printf("string: %s", destination); // string: Hello, World! 3

        (t) `sprintf(char * destination, const char * format, arg1, arg2...)`: Writes a formatted string into a char array

            (I) destination:	Required. A char array to which the formatted string is written.
            (II) format: Required. A string representing the format of the data to be written to the array.
            (III) arg1, arg2...: Optional. Any number of additional arguments, their values can be formatted and written to the destination array using the specifiers in the format argument.

            (IV) returns an int value representing the number of characters that were written to the array (excluding the null terminating character). If an error occurred then it returns a negative number.

        READ:
        
        (u) `fread(void * destination, size_t size, size_t amount, FILE * fptr)`: Reads data from a file and writes it into a block of memory

            (I) `destination`: pointer to a Block of memory to write data at.
            (II) `size`: size of an element.
            (III) `amount`: amount of elements to read and write to memory.
            (IV) `fptr`: File Pointer.

            (V) returns a size_t value representing the number of elements that were read. If this number is different than the amount parameter then the end of the file has been reached or an error occurred.

            FILE * fptr = fopen("./test.txt", "r");

            char data[21];
            int n = fread(data, 1, 20, fptr);
            data[n] = '\0';

            printf("%s", data);

            fclose(fptr);
        
        (v) `fscanf(FILE * fptr, const char * format, arg1, arg2...)`: Reads formatted data from a file and writes it into a number of memory locations, increases Position Indicator.

            (I) Format Specifier
                
                (A) [characterset]: reads 1 character if matches
                (B) [^characterset]: reads 1 character if doesn't matches

            (II) return 1 if Input is Valid, return 0 if Input is Invalid

            // ./test.txt:  Hello, World!
            FILE *fptr = fopen("./test.txt", "r");

            char a[20];
            char b[20];
            fscanf(fptr, "%s%s", a, b);

            printf("%s%s", a, b);

            fclose(fptr);

        (w) `fgets(char *destination, int size, FILE *fptr)`: Reads the Line from FILE, increases Position Indicator.

            char string[20];

            printf("input: ");
            fgets(string, sizeof(string), stdin);
            printf("\ninterpreted: %s", string);

            /*
            inout: The Quick Brown Fox Jumps over The Lazy Dog.

            interpreted: The Quick Brown Fox
            */

            (II) returns the destination pointer

        (x) `fgetc(FILE *fptr)`: Reads a Single Characters from the file and returns it's value, increases Position Indicator.

            (I) return an `int` corresponding to the ASCII value of the Character, or the constant EOF if the end of the file has been reached or an error occurred.
        
        (y) `scanf(const char * format, arg1, arg2...)`: Reads formatted data from the stdin and writes it into a number of memory locations, increases Position Indicator

            int num;
            printf("Input:");
            scanf("%d", &num);
            printf("Value of Num = %d", num);

            if(scanf("%d", &num) == 0){ // verify correct input
                fprintf(stderr, "Invalid Input");
            };

            // Multiple Input
            char num, character;
            scanf("%d %c", &num, &character);

            // strings:

            char a[20];
            if (scanf("%19s", a) != 1){
                printf("Invalid Input");
                return 1;
            }
            a[20] = '\0';

            printf("%s", a);

            (I) it considers space (whitespace, tabs, etc) as a terminating character
            (II) with Strings, must specify their size in format specifier
            (III) return 1 if Input is Valid, return 0 if Input is Invalid
        
        (z) `gets()`: -

        (za) `getc()`: The same as `fgetc()`

        (zb) `getchar()`: Reads one character of from the stdin and returns its ASCII value

            (I) return an int value representing the ASCII value of the character that was read.
        
        (zc) `sscanf(char * source, const char * format, arg1, arg2...)`: Reads a formatted string from a char array and writes it into a number of memory locations

            (I) return an int value representing the number of arguments that were written to. It returns the constant EOF if an error occurred.

            int a;
            int b;
            int c;
            char source[20] = "4^2 + 3^2 = 5^2";

            int isvalid = sscanf(source, "%d^2 + %d^2 = %d^2", &a, &b, &c);

            if(isvalid != 3){
                fprintf(stderr, "Unable to find all 3");
                return 1;
            };
            printf("a: %d\n", a); // 4
            printf("b: %d\n", b); // 3
            printf("c: %d\n", c); // 5

    (ii) `stdlib.h`

        () abs(int number): Return the absolute (positive) value of a whole number

            int value = abs(-5);
            printf("%d", value); // 5

            
            Interfaces:

            abs(int number);
            labs(long int number);
            llabs(long long int number);

        () atof(const char * str): Returns a double value from a string representation of a number

            char string[20] = " 22.3$ is the price";
        
            double num = atof(string);
            printf("num: %lf\n", num); // 22.300000
            
            char string2[20] = "the price is 45.2$";
        
            double num2 = atof(&string2[13]);
            printf("num2: %lf\n", num2); // 45.200000

        () atoi(const char * str): Return an int value from a string representation of a whole number
        () atol(const char * str): Return a long int value from a string representation of a whole number
        () atoll(const char * str): Return a long long int value from a string representation of a whole number

        () `calloc(size_t amount, size_t size)`: Allocate dynamic memory and fill it with zeroes

            (I) `amount`: The amount of total capacity
            (II) `size`: amount of total bytes allocated each element

            int *ptr = calloc(2, 4); // Manually Allocate Size for each item
            // int *ptr = calloc(2, sizeof(*ptr)); // Dynamically Allocate Size for each item based on type
        

            // Access
            *(ptr+1) = 12; // using Deference
            ptr[2] = 50; // using index

            printf("%d\n", ptr[1] ); // 12
            printf("%d\n", *(ptr+2)); // 50
            

            (I) `sizeof(ptr)`: doesn't returns the Size of The Array and instead returns the length of the Memory Address

                // Find Amount of Bytes Allocated
                int length = 10;
                int *ptr = calloc(length, sizeof(*ptr));
                int size = sizeof(*ptr)*length; // Amount of Bytes Allocated
                printf("%d", size); // 40

        () `div(int dividend, int divisor)`: Return the quotient and remainder of an integer division

            (I) returns a structure `div_t`, which has 2 members `quot` and `rem` 

            Interfaces:

            div_t div(int dividend, int divisor);
            ldiv_t ldiv(long int dividend, long int divisor);
            lldiv_t lldiv(long long int dividend, long long int divisor);

        () `exit(int status)`: End the program with the status code

        () `free(void *ptr)`: deallocates dynamic memory

            int *ptr = malloc(sizeof(*ptr));
            *ptr = 1024;
            printf("Pointer: %p, Value: %d\n", ptr, *ptr); // Pointer: 0000021189C753C0, Value: 1024

            free(ptr);
            ptr = NULL; // set Pointer to NULL after freeing
            
            /*
            after freeing memory and Not setting the Pointer to NULL:

            printf("Pointer: %p, Value: %d\n", ptr, *ptr); // Pointer: 0000021189C753C0, Value: -1983415456
            */

        () `malloc(size_t size)`: Allocates Dynamic Memory as an Array, and returns it's memory address

            (I) Return: `void *` or NULL if unable to allocate

            // Allocate Size based on datatype
            int *ptr = malloc(sizeof(*ptr));


            // Manually Allocating Size
            int *ptr = malloc(8);

            // access
            *ptr = 1024;
            printf("%d", *ptr); // 1024

            // Type Casted

            int *ptr1 = malloc(4); // pointer "ptr1" and Allocate 4 Bytes

            char *ptr2 = (char*) ptr1; // pointer "ptr2", assign "ptr1" deferenced, and casted to "char"
        
            ptr1[0] = 1684234849; // Storing an Integer to "ptr1"
        
            ptr2[0]; // first Byte of the Integer 
            ptr2[1]; // second Byte of the Integer 
            // ...
        
            printf("%d is %c %c %c %c", *ptr1, ptr2[0], ptr2[1], ptr2[2], ptr2[3]); 
        
        () `realloc(void * ptr, size_t size)`: Reallocate dynamic memory
            
            (I) `ptr`: pointer to memory where dynamic memory is allocated
            
            (II) `size`: the new size of memory to be assigned

            (III) returns either the at same memory address or an address at a new destination, returns NULL if unable to reallocate

            char *ptr1 = calloc(8, sizeof(*ptr1)); // create a Pointer named "ptr1"
            char string[7] = "Hello"; // create a String
            strcpy(ptr1, string); // Copy String into Pointer "ptr1"

            char *ptr2 = realloc(ptr1, 15); // Change Size of String

            // Handle Null Pointer
            if(ptr2 == NULL){
                fprintf(stderr, "Unable to ReAllocate Memory");
            };

            // Modify Data/Read in new Memory
            ptr2[5] = '!';
            ptr2[6] = '!';
            ptr2[7] = '!';

            printf("ptr1: %s\n", ptr1); // "Hello" or "Hello!!!"
            printf("ptr2: %s\n", ptr2); // ptr2: Hello!!!

        () `qsort(void * arr, size_t amount, size_t size, int compare(const void *, const void *))`: Sort the contents of an array

        () `srand(unsigned int seed)`: Initialize the random number generator

            srand(time(0))

        () `rand()`: Generate a random integer

            srand(time(0));
            int random = rand();
            // int random = (rand()%100)+1; //  Generate a Random Number in-between 1-100
            printf("%d", random);

    (iii) `stdbool.h` Boolean Data Type

        (a) `bool` A Boolean true or false,  0 or 1
            
            bool a = true;
            bool b = false;

            (I) Size: 1bit
            (II) Range: true | false
            (III) Format Specifier: --

    (iv) `time.h`

        (a) `sleep(<n>)`: pauses execution for `n` count of seconds, and returns the current UTC time in Miliseconds since January 1st, 1970 

    (v) `unistd.h`

    (vi) `math.h`

        (a) `sqrt(n)`: square Roots The Number, returns float

        (b) `ceil(n)`: rounds up a Floating Point Number to the Closest Next Integer.

        (c) `floor(n)`: rounds up a Floating Point Number to the Closest Previous Integer.

        (d) `pow(a, b)`: Exponents `a` to the power of `b`

    (vii) `string.h`: Utility Functions for Strings

        (a) `strlen(string)`: works same as `sizeof()` but excludes the string ending NULL  character from the end(`\x00`), and It also does not Include extra Reserved Space for the String

            char string[4] = "abc";
            printf("string: %s\nbyte length: %d\nstring length: %d", string, sizeof(string), strlen(string));

            /*
            string: abc
            byte length: 4
            string length: 3
            */

        (b) `strcat(string1, string2)`: Concatinates both strings and stores them in `string1` (make sure `string1` has a fixed length have enough memory allocated)


            // Dynamic or without Enough Space
            char str[] = "test";
            char str1[] = "Hello ";
            char str2[] = "World!";
            strcat(str1, str2);
            printf("%s %s %s",str, str1, str2); // orld! Hello World! World!
            // string `str` completely unrelated to strcopy gets modified because of not Allocating enough space to `str1`

            // Correct Way
            char str[] = "test";
            char str1[20] = "Hello ";
            char str2[] = "World!";
            strcat(str1, str2);
            printf("%s %s %s",str, str1, str2); // orld! Hello World! World!

        (c) `strcpy(string2, string1)`: `string1` a String into another String `string2` (make sure `string1` also have enough space otherwise it would cause the same behavior as strcat )

            char str1[] = "Hello, World";
            char str2[14];
            strcpy(str2, str1);
            printf("%s\n", str2);
            
        (d) `strcmp(string1, string2)`: returns 0 If the Both strings are Equal, otherwise an Integer is returned

            char string1[20] = "Hello";
            char string2[10] = "Hello";
            int isEqual = strcasecmp(string1, string2);
            printf("Match: %d", isEqual); // 0

