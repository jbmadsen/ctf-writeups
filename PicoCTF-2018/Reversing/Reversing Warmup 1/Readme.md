# Reversing Warmup 1

**Category:** Reversing

**Points:** 50

## Task

> Throughout your journey you will have to run many programs. Can you navigate to /problems/reversing-warmup-1_2_a237211c4be8902c67102f827027e633 on the shell server and run this [program](Files/run) to retreive the flag? 


## Hints

> If you are searching online, it might be worth finding how to exeucte a program in command line.


## What do we need to know?

Running programs in a linux terminal is as simple as writing the name of the program, prefaced with `./`, either from the folder the program are placed in or into the folder.

Examples:

```bash
./program
```

or 

```bash
./folder/program
```

You have to make sure you have execute permissions for the file in question. You can check the [permissions](https://www.pluralsight.com/blog/it-ops/linux-file-permissions) of a file using `ls -l`, which outputs the following:

> -rwxr-xr-x 1 root root 7420 Feb 24 19:28 run

The very first dash (-) indicates we are looking at permissions for a file (d would have been for a directory).

The permissions are: r (read), w (write) and x (execute). 
Here, the permissions are split into three chunks: | rwx | r-x | r-x |, where the first chunk are for the owner of the file, second is for the group and last is for everyone else.
In this case, the owner can read, write and execute, and everyone else read and execute, but NOT write.

If you want to add execute permissions to the user, you can use the chmod command,

```bash
chmod +x
```

where `+x` would allow me to execute the file.


## Solution

So, armed with our new knowledge, lets move into the folder and run the program:

```bash
cd /problems/reversing-warmup-1_2_a237211c4be8902c67102f827027e633

./run
```

> picoCTF{welc0m3_t0_r3VeRs1nG}


## Flag

> picoCTF{welc0m3_t0_r3VeRs1nG}
