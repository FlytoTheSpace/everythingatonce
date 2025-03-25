# `stdio.h`

- [`File`](#file)
- [`Functions`](#functions)
    - [`fopen()`](#fopen)
    - [`fclose()`](#fclose)
    - [`ferror()`](#ferror)
    - [`rename()`](#rename)
    - [`remove()`](#remove)
    - [`perror()`](#perror)
    - [`fseek()`](#fseek)
    - [`ftell()`](#ftell)
    - [`rewind()`](#rewind)
    - [`feof()`](#feof)
    - [`fwrite()`](#fwrite)
    - [`fprintf()`](#fprintf)
    - [`fputs()`](#fputs)
    - [`fputc()`](#fputc)
    - [`printf()`](#printf)
    - [`puts()`](#puts)
    - [`putc()`](#putc)
    - [`putchar()`](#putchar)
    - [`snprintf()`](#snprintf)
    - [`sprintf()`](#sprintf)
    - [`fread()`](#fread)
    - [`fscanf()`](#fscanf)
    - [`fgets()`](#fgets)
    - [`fgetc()`](#fgetc)
    - [`scanf()`](#scanf)
    - [`gets()`](#gets)
    - [`getc()`](#getc)
    - [`getchar()`](#getchar)
    - [`sscanf()`](#sscanf)

The Standard Input/Output Library

## Data Types

### File

File that can read/written to as a stream

`FILE`: The File Datatype

```c
FILE *fptr;
```

## Functions

### Miscellaneous

#### `fopen()`

Opens a file, creates a Pointer to the File and returns the Pointer

```c
FILE *fopen(const char * filename, const char * mode);
```

- `mode`:

    - `r`: Allows *Read* from the File, return *NULL* if file doesn't exists.
    - `w`: Allows *Write* from the File, *creates* file if not exists.
    - `a`: Allows *Appending* to the end of the File, *creates* file if not exists.
    - `r+`: Allows *Read* and *Write* to The File, returns *NULL* if file doesn't exists.
    - `w+`: Allows *Read* and *Write* to The File, creates *file* if not exists.
    - `a+`: Allows *Read* and *Write* to The File, creates *file* if not exists.

    Extra Appended:

    - `b`: read/write as raw Binary

#### `fclose()`

closes a File

```c
int fclose(FILE *fptr);
```

- return `0` on **successfully** close, any other integer on error

#### `ferror()`

Returns a true value if a recent file operation had an error

```c
int ferror(File * fpr);
```

#### `rename()`

Changes the name of a file

```c
int rename(const char * oldname, const char * newname);
```

- returns `0` if **successfully** renamed. any other int if error occured;
        
#### `remove()`

Deletes a file

```c
int remove(const char * filename);
```

- returns `0` if **successfully** deleted. any other int if error occured;

#### `perror()`

prints the error message for the last operation with a label

```c
perror(const char * ErrMsg);
```
example:-
```c
int msg;
int success = fscanf(stdin, "%d", &msg);

if(success != 1){
    perror("Invalid Input");
    exit(1);
}

printf("Success!");
```

### Position Indicator

#### `fseek()`

Moves the position indicator of a file pointer

```c
int fseek(FILE * fptr, long int offset, int origin);
```
         
- `fptr`: Required. A file pointer, usually created by the fopen() function.
- `offset`: Required. Specifies a position in the file relative to the origin.
- `origin`: Required. Specifies the position in the file from which the offset is applied. It can be one of the following constants:

    - `SEEK_SET`: Offset is relative to the beginning of the file
    - `SEEK_CUR`: Offset is relative to the current position in the file
    - `SEEK_END`: Offset is relative to the end of the file
                
    > (The SEEK_END value may not be fully supported by some implementations of the library. )
```c
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
```

- returns `0` if successful and non-zero if an error occurred.

#### `ftell()`

Returns the value of the position indicator of a file pointer as an `int`

```c
int ftell(FILE * fptr)
```
example:-
```c
FILE *fptr = fopen("./read.txt", "r");

char block[11];
fread(block, 1, 10, fptr);
block[11] = '\0';
long indicator = ftell(fptr);

printf("%lu", indicator); // 10
``` 

#### `rewind()`

Moves the position indicator to the beginning of the file

```c
void rewind(FILE * fptr);
```

example:-

```c
FILE *fptr = fopen("./read.txt", "r");

char block[11];
fread(block, 1, 10, fptr);
block[11] = '\0';

rewind(fptr);
long indicator = ftell(fptr);

printf("%lu", indicator); // 0
```        

#### `feof()`

Returns a true value when the position indicator has reached the end of the file

```c
int feof(FILE * fptr);
```

### Write

#### `fwrite()`

Writes data from a block of memory into a file

```c
size_t fwrite(const void * source, size_t size, size_t amount, FILE * fptr);
```

Parameters
- `destination`: pointer to a Block of memory to read data from.
- `size`: size of an element.
- `amount`: amount of elements to read from memory and write to memory.
- `fptr`: File Pointer.

- returns `size_t` value representing the number of elements that were written into the file.

#### `fprintf()`

writes a Formatted string to The File.

```c
int fprintf(FILE * fptr, const char * format, arg1, arg2...);
```

- returns an `int` value representing the number of characters written to the file. If an error occurred then it returns a negative number.

#### `fputs()`

Writes a string into a file and advances the position indicator.

```c
int fputs(const char * str, FILE * fptr);
```

- return an int value that is not negative if the function was successful. It returns the constant EOF if an error occurred.

#### `fputc()`

Writes a character into a file and advances the position indicator.

```c
int fputc(int c, FILE * fptr);
```

- returns an `int` value representing the ASCII value of the character, or the constant EOF if the character could not be written into the file.

#### `printf()`

Writes a Formatted string to The stdout (Standard Output).

```c
int printf(const char * format, arg1, arg2...);
```

- returns an `int` value representing the number of characters written to the stdout. If an error occurred then it returns a negative number.

#### `puts()`

writes a string to the the stdout

```c
int puts(const char * str);
```

- returns an `int` value that is not negative if the function was successful. It returns the constant EOF if an error occurred.

#### `putc()`

The same as [`fputc()`](#fputc)

```c
int putc(int c, FILE * fptr);
```

- return `int` value representing the ASCII value of the character that was written.
        
#### `putchar()`

Outputs a single character to the stdout

```c
int putchar(int c);
```

- return an `int` value representing the ASCII value of the character that was written.

#### `snprintf()`

Writes a formatted string into a char array (memory-safe)

```c
int snprintf(char * destination, size_t * size, const char * format, arg1, arg2...);
```

- `destination`: String to write to 
- `size`: amount of bytes write to the string, (including the null terminating character).
- `format`: A Formatted String to write to the Destionation String
- `arg1`, `arg2`...

- returns an `int` value representing the number of characters that were intended to be written to the array (excluding the null terminating character). If this is greater than or equal to the size argument then there are some characters that could not be written to the array. If an error occurred then it returns a negative number.

```c
char destination[20];

int a = 3;
int size = snprintf(destination, 19, "Hello, World! %d", a);

if(size<0){
    fprintf(stderr, "Error Unable to write to string");
    return 1;
}
destination[size] = '\0';

printf("string: %s", destination); // string: Hello, World! 3
```

#### `sprintf()`

Writes a formatted string into a char array

```c
int sprintf(char * destination, const char * format, arg1, arg2...);
```

- `destination`:	Required. A char array to which the formatted string is written.
- `format`: Required. A string representing the format of the data to be written to the array.
- `arg1`, `arg2`...: Optional. Any number of additional arguments, their values can be formatted and written to the destination array using the specifiers in the format argument.

- returns an `int` value representing the number of characters that were written to the array (excluding the null terminating character). If an error occurred then it returns a negative number.

### Read
    
#### `fread()`

Reads data from a file and writes it into a block of memory

```c
fread(void * destination, size_t size, size_t amount, FILE * fptr);
```

- `destination`: pointer to a Block of memory to write data at.
- `size`: size of an element.
- `amount`: amount of elements to read and write to memory.
- `fptr`: File Pointer.

- returns a `size_t` value representing the number of elements that were read. If this number is different than the amount parameter then the end of the file has been reached or an error occurred.

```c
FILE * fptr = fopen("./test.txt", "r");

char data[21];
int n = fread(data, 1, 20, fptr);
data[n] = '\0';

printf("%s", data);

fclose(fptr);
```     

#### `fscanf()`

Reads formatted data from a file and writes it into a number of memory locations, increases Position Indicator.

```c
int fscanf(FILE * fptr, const char * format, arg1, arg2...);
```

- Format Specifier
                
    - [characterset]: reads 1 character if matches
    - [^characterset]: reads 1 character if doesn't matches

- return `1` if Input is Valid, any other int if invalid

example:-
```c
// ./test.txt:  Hello, World!
FILE *fptr = fopen("./test.txt", "r");

char a[20];
char b[20];
fscanf(fptr, "%s%s", a, b);

printf("%s%s", a, b);

fclose(fptr);
```

#### `fgets()`

Reads the Line from FILE, increases Position Indicator.

```c
char *fgets(char *destination, int size, FILE *fptr);
```
example:-
```
char string[20];

printf("input: ");
fgets(string, sizeof(string), stdin);
printf("\ninterpreted: %s", string);

/*
inout: The Quick Brown Fox Jumps over The Lazy Dog.

interpreted: The Quick Brown Fox
*/
```

- returns the `destination` ptr

#### `fgetc()`

Reads a Single Characters from the file and returns it's value, increases Position Indicator.

```c
fgetc(FILE *fptr);
```

- return an `int` corresponding to the ASCII value of the Character, or the constant EOF if the end of the file has been reached or an error occurred.
        
#### `scanf()`

Reads formatted data from the stdin and writes it into a number of memory locations, increases Position Indicator

```c
int scanf(const char * format, arg1, arg2...);
```
example:-
```c
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
```

- it considers space (whitespace, tabs, etc) as a terminating character
- with Strings, must specify their size in format specifier
- return `1` if Input is Valid, any other number if input is invalid
        
#### `gets()`

Insecure Do not use

#### `getc()`

The same as [`fgetc()`](#fgetc)

```c
getc(FILE *fptr);
```

#### `getchar()`

```c
int getchar();
```
Reads one character of from the stdin and returns its ASCII value

- return an `int` value representing the ASCII value of the character that was read.
        
#### `sscanf()`

Reads a formatted string from a char array and writes it into a number of memory locations

```c
sscanf(char * source, const char * format, arg1, arg2...)
```
- return an int value representing the number of arguments that were written to. It returns the constant EOF if an error occurred.

```c
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
```

# stdlib.h

- [`abs()`](#abs)
- [`atof()`](#atof)
- [`atoi()`](#atoi)
- [`atol()`](#atol)
- [`atoll()`](#atoll)
- [`div()`](#div)
- [`exit()`](#exit)
- [`malloc()`](#malloc)
- [`calloc()`](#calloc)
- [`free()`](#free)
- [`realloc()`](#realloc)
- [`qsort()`](#qsort)
- [`srand()`](#srand)
- [`rand()`](#rand)

## Functions

#### `abs()`

Return the absolute (positive) value of a whole number

```c
int abs(int number);
````

```c
int value = abs(-5);
printf("%d", value); // 5
```

Interfaces:
```c
int abs(int number);
long int labs(long int number);
long long int llabs(long long int number);
```

#### `atof()`

Returns a double value from a string representation of a number

```c
double atof(const char * str)
```

example:-
```c
char string[20] = " 22.3$ is the price";

double num = atof(string);
printf("num: %lf\n", num); // 22.300000

char string2[20] = "the price is 45.2$";

double num2 = atof(&string2[13]);
printf("num2: %lf\n", num2); // 45.200000
```

#### `atoi()`

Return an `int` value from a string representation of a whole number

```c
int atoi(const char * str)
```
#### `atol()`

Return a `long int` value from a string representation of a whole number

```c
atol(const char * str)
```
#### `atoll()`

Return a `long long int` value from a string representation of a whole number

```c
atoll(const char * str)
```

#### `div()`

Return the quotient and remainder of an integer division

```c
div(int dividend, int divisor)
```

- returns a structure `div_t`, which has 2 members `quot` and `rem` 

Interfaces:

```c
div_t div(int dividend, int divisor);
ldiv_t ldiv(long int dividend, long int divisor);
lldiv_t lldiv(long long int dividend, long long int divisor);
```

#### `exit()`

End the program with the status code

```c
exit(int status);
```

#### `malloc()`

Allocates Dynamic Memory as an Array, and returns it's memory address

```c
malloc(size_t size);
```
- Return: `void *` or NULL if unable to allocate

example:-
```c
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
```

#### `calloc()`

Allocate dynamic memory and fill it with zeroes

```c
calloc(size_t amount, size_t size)
```

- `amount`: The amount of total capacity
- `size`: amount of total bytes allocated each element

```c
int *ptr = calloc(2, 4); // Manually Allocate Size for each item
// int *ptr = calloc(2, sizeof(*ptr)); // Dynamically Allocate Size for each item based on type


// Access
*(ptr+1) = 12; // using Deference
ptr[2] = 50; // using index

printf("%d\n", ptr[1] ); // 12
printf("%d\n", *(ptr+2)); // 50
```

#### `free()`

deallocates dynamic memory

```c
void free(void *ptr);
```

example:-

```c
int *ptr = malloc(sizeof(*ptr));
*ptr = 1024;
printf("Pointer: %p, Value: %d\n", ptr, *ptr); // Pointer: 0000021189C753C0, Value: 1024

free(ptr);
ptr = NULL; // set Pointer to NULL after freeing

/*
after freeing memory and Not setting the Pointer to NULL:

printf("Pointer: %p, Value: %d\n", ptr, *ptr); // Pointer: 0000021189C753C0, Value: -1983415456
*/
```

#### `realloc()`

Reallocate dynamic memory

```c
realloc(void * ptr, size_t size)
```
            
- `ptr`: pointer to memory where dynamic memory is allocated        
- `size`: the new size of memory to be assigned
- returns either the at same memory address or an address at a new destination, returns NULL if unable to reallocate

example: -
```c
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
```

#### `qsort()`

Sort the contents of an array

```c
qsort(void * arr, size_t amount, size_t size, int compare(const void *, const void *))
```

#### `srand()`

Initialize the random number generator

```c
srand(unsigned int seed)
```

```c
srand(time(0));
```

#### `rand()`

Generate a random integer

```c
srand(time(0));
int random = rand();
// int random = (rand()%100)+1; //  Generate a Random Number in-between 1-100
printf("%d", random);
```

# `stdbool.h`

## Constants

```c
#define true	1
#define false	0
```

## Data Types

(a) `bool` A Boolean true or false,  0 or 1

```c
bool a = true;
bool b = false;
```

- Size: `1bit`
- Range: `0 | 1`
- Format Specifier: --

# `time.h`


# `unistd.h`

# `math.h`

#### `sqrt()`

square Roots The Number, returns float
#### `ceil()`

rounds up a Floating Point Number to the Closest Next Integer.
#### `floor()`

rounds up a Floating Point Number to the Closest Previous Integer.
#### `pow(a, b)`

Exponents `a` to the power of `b`

# `string.h`

Utility Functions for Strings

- [`strlen()`](#strlen)
- [`strcat()`](#strcat)
- [`strcpy()`](#strcpy)
- [`strcmp()`](#strcmp)

#### `memchr()`

returns the first pointer to the byte in memory which contains the specific `value`

returns `NULL` if the unable to find a match.

```c
void * memchr(void * pointer, int value, size_t size);
```
- `pointer`: the pointer the memory block to search in
- `value`: the value to search for
- `size`: the count of the memory block to check in

```c
int arr[7] = {3, 2, 4, 5, 6, 2, 0};

int *addr = memchr(arr, 6, sizeof(arr));

if(addr == NULL){
    fprintf(stderr,"Unable to find a match");
    return 1;
}

printf("Address: %p\nValue: %d", addr, *addr);
/*
Address: 00000042689FFD50
Value: 6
*/
```

#### `strlen()`

returns the size of the string, excludes the ending NULL character, also excludes unused space left for the string

```c
int strlen(char * str);
```

```c
char string[4] = "abc";
printf("string: %s\nbyte length: %d\nstring length: %d", string, sizeof(string), strlen(string));

/*
string: abc
byte length: 4
string length: 3
*/
```

#### `strcat()`

Concatinates both strings and stores them in the `destination` string

```c
char * strcat(void * destination, void * source);
```

make sure the `destination` string has enough space to contain the string, otherwise the function may write to completely unrelated string

```c
// without Enough Space
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
```

#### `strcpy()`

Copies Data from one string to another

make sure the `destination` string has enough space to contain the string, otherwise the function may write to completely unrelated string

```c
char * strcpy(char * destination, char * source);
```

```c
char str1[] = "Hello, World";
char str2[14];
strcpy(str2, str1);
printf("%s\n", str2);
```
            
#### `strcmp()`

Compares 2 strings and returns an `int` based on the comparsion
- `0` if Both string are exactly equal
- *Positive Integer* if at the first mismatch, the ASCII value of the character in the ***first*** string is greater than the other's ASCII value at that index
- *Negative Integer* if at the first mismatch, the ASCII value of the character in the ***second*** string is greater than the other's ASCII value at that index

```c
int strcmp(const char * str1, const char * str2);
```

```c
char string1[20] = "Hello";
char string2[10] = "Hello";
int isEqual = strcmp(string1, string2);
printf("Match: %d", isEqual); // 0
```
