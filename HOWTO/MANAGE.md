# MANAGEMENT

## CREATION

### Files

```
...
=================================================================
[0] file_1------------------------------------------size_1
=================================================================
...
pydirman>
```
To create a file : Enter `n`

```
pydirman> n
Enter file name [create]: 
```
Enter your newly created file name.
```
Enter file name [create]: file_2 
```
> Entering extensions will use custom templates for newly created files like 
> C, C++, Java etc.
```
...
=================================================================
[0] file_1------------------------------------------size_1
[1] file_2------------------------------------------size_2
=================================================================
...
pydirman>
```

### Directories

To create a new directory : Enter `m {directory_name}`

> Enter a directory name with no spaces

| Correct | Incorrect |
|----------|----------|
| hello_world | hello world |

```
...
=================================================================
[0] file_1------------------------------------------size_1
[1] file_2------------------------------------------size_2
[2] directory_name/
=================================================================
...
pydirman>
```
## DELETION

### Files

To delete a file : Enter `d`
```
pydirman> d
=================================================================
[0] file_1
[1] file_2
=================================================================
Enter file index [delete]: 
```
Enter your file index which you want to delete.

### Directories

To delete a directory : Enter `r`
```
pydirman> d
=================================================================
[2] directory_name
=================================================================
Enter directory name: 
```
Enter your directory name which you want to delete.

>For security purposes, system directories like lib, bin etc. cannot be deleted .
