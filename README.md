# PYDIRMAN

## Watch the tutorial here: 
[![What happened here :/](https://img.youtube.com/vi/1B1_kWp-WCY/0.jpg)](https://www.youtube.com/watch?v=1B1_kWp-WCY)


A Python script to manage your directories. \
(Only for DEBIAN systems)
## Getting Started
```
git clone https://github.com/sadbro/pydirman.git
cd ./pydirman/main
sudo python3 setup.py
sudo pydirman
```

## Contact Us

[Facebook](https://www.facebook.com/codelogs)
<br>
[Google](mailto:sadbro.linux@gmail.com)
<br>
[Github Wiki](https://github.com/sadbro/pydirman/wiki)


# WIKI
---

# Walking through directories

### Syntax

> g {index}

### Example

```
=================================================================
[0] directory_1
[1] directory_2
[2] directory_3
[3] directory_4
=================================================================
...
YOUR CURRENT LOCATION: "your_current_path"
...
=================================================================
pydirman> 
```
To go into 'directory_1' :  enter `g 0` 
```
=================================================================
[0] file_1
[1] file_2
=================================================================
...
YOUR CURRENT LOCATION: "your_current_path/directory_1"
...
=================================================================
pydirman> 
```

To return to previous directory: enter `p`

```
=================================================================
[0] directory_1
[1] directory_2
[2] directory_3
[3] directory_4
=================================================================
...
YOUR CURRENT LOCATION: "your_current_path"
...
=================================================================
pydirman> 
```
---

# MANAGEMENT
---

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
pydirman> r
=================================================================
[2] directory_name
=================================================================
Enter directory name: 
```
Enter your directory name which you want to delete.

>For security purposes, system directories like lib, bin etc. cannot be deleted .
>Also directories with items inside them cannot be deleted .

---

# FILE
---
## Reading Contents

### Syntax

`g {index}`

### Example
```
=================================================================
[0] file_1-----------------------------------------size_1
[1] file_2-----------------------------------------size_2
=================================================================
...
YOUR CURRENT LOCATION: "your_current_path/"
...
=================================================================
pydirman> 
```
To go to 'file_1' : enter `g 0`
```
=================================================================
[0] file_1-----------------------------------------size_1
[1] file_2-----------------------------------------size_2
=================================================================
...
YOUR CURRENT LOCATION: "your_current_path/"
...
=================================================================
pydirman> g 0
FILE=[file_1]
[p]rint/[c]ancel/[e]xit: 
```
<pre>
To print :     `p`
To cancel:     `c`
To exit:       `e`
</pre>

**PRINT**
```
[p]rint/[c]ancel/[e]xit: p
===============================START=============================
*CONTENTS OF YOUR FILE*
================================END==============================

```
**CANCEL**

```
[p]rint/[c]ancel/[e]xit: c
...
=================================================================
[0] file_1-----------------------------------------size_1
[1] file_2-----------------------------------------size_2
=================================================================
...
YOUR CURRENT LOCATION: "your_current_path/"
...
=================================================================
pydirman> 

```
**EXIT**
>It exits from pydirman.

---
## Start File Handle

> P.S. Only Handles One file at a time.

### Syntax
---
`test {index}`

**Custom Profile :**

Pydirman supports custom profiling for use of special profiles, i.e. compile arguments that C, C++ uses during custom build. 
if the file is of such a extension then you will be asked to use a default profile (No custom build) or a previous profile or a whole new profile.

a Profile is of the following type: `[profile_context] profile_args`

> profile_args cannot be written in next line. It must complete in the
> same line.

A profile context is like it's name. It is used to identify and load the profile_args in the file handler.

### Example
---

```
Get Profile? [New/Load/{press Enter to skip}] 
```
#### Usage of Profiles

Enter `l`

> `l` will load all the profiles and ask you for which profile you want to use

```
-----------------------------------------------------------------
CONTEXT[profile_1]: `...`
CONTEXT[profile_2]: `...`
-----------------------------------------------------------------
Enter profile context: 
```
enter which profile you want to use and press Enter.

#### Creation of Profiles

Enter `n` 

> `n` will prompt you to enter a new profile context and it's args.

```
Enter profile context: your_new_profile_context
Enter profile: your_new_profile_args
```
The  new profile will be created and instantly used for this handle.

---

## After Starting File Handling

```
FILE -> file_name
Enter command [exit|test|nano|clear|hex]
```

> Only the first letter for each command is used.

### Utility Commands

* **CLEAR :**
As it suggests, It clears and refreshes the screen.
* **EXIT :**
It exits from the handle and goes to the main screen.
* **HEX :**
It displays hexadecimal format of the contents of the handled file.
* **NANO :**
It opens the nano editor and enables you the edit the file.

### Testing Commands

* **TEST :**
It will run the the file with appropriate compiler or interpreter. If any 
arguments is to be passed, It should be passed as it is after this command.
* **GC :**
It will get the current profile and display it.
* **CC :**
It will open the context file and it enables you to edit or add profiles.
> Adding profiles should be done with proper syntax given in the profiling wiki.

---
# SPECIAL COMMANDS <br>
[that will make your life easier...] ;)

## `ED`
This stands for "edit-source". It opens your current source code in a buffer of NANO.<br>
**The path is at /etc/pydirman.py**

## `EDN`

This stands for "edit-source-nano". It opens your current nano configuration in a buffer of NANO.<br>
**The path is at /etc/nanorc**

## `U`

This stands for "usb-open". It opens the path to folder where all your external devices, e.g. USB drives are located.<br>
**The path is at /media/your_name**

## `T`

This stands for "terminal-execute". It executes the command which you pass after this command.<br>
**>t  ...args => $...args**

# OTHER COMMANDS:

Let's see the below example:<br>

```
[9] file_9.ext_9---------------99 bytes
=======================================
...
=======================================
```


**&9 will return "file_9.ext_9"**<br>
**$file_9.ext_9 will return "9"**

# USING PYTHON COMMANDS:

You can now manipulate the output of a string using the EOC '^'<br>

Lets say:<br>

-> your file file_69.ext_69 is at index 69<br>

you can extract only the file by using `&69^.split(".")[0]` which will return file_69<br>

---

