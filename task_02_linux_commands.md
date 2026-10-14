# Task 2 - Linux Commands (NAVTTC Week 1)

All commands were run in Git Bash (MINGW64) on Windows 10.

## Navigation: pwd, ls, cd

```
$ pwd
/c/Users/HAMMAD

$ cd Downloads
$ pwd
/c/Users/HAMMAD/Downloads

$ ls -a
./  ../  Programs/
```

## Files and folders: mkdir, touch, cp, mv, rm, rmdir

```
$ mkdir practice_folder
$ cd practice_folder
$ touch test1.txt
$ cp test1.txt test2.txt
$ ls
test1.txt  test2.txt

$ mv test2.txt renamed_file.txt
$ ls
renamed_file.txt  test1.txt

$ rm renamed_file.txt
$ cd ..
$ rmdir practice_folder
rmdir: failed to remove 'practice_folder': Directory not empty

$ rm practice_folder/test1.txt
$ rmdir practice_folder
```

`rmdir` refuses to delete a folder that still has files in it, so the file was removed first.

## Reading files and redirection: echo, cat, >, >>, head, less

```
$ echo "First line" > redirect_test.txt
$ echo "Second line" >> redirect_test.txt
$ cat redirect_test.txt
First line
Second line

$ echo -e "Line1\nline2\nline3\nline4\nline5" > multiline.txt
$ head -n 2 multiline.txt
Line1
line2

$ less multiline.txt      (press q to quit)
```

`>` overwrites a file, `>>` appends to it.

## Help: man and --help

```
$ man ls
bash: man: command not found

$ ls --help
Usage: ls [OPTION]... [FILE]...
```

`man` is not installed in Git Bash, so `--help` was used instead.

## alias, nano, chmod, ps, kill

```
$ alias ll='ls -la'
$ ll
total 26
drwxr-xr-x 1 HAMMAD 197121  0 Sep 11 15:15 ./
...

$ nano test1.txt          (Ctrl+O to save, Ctrl+X to exit)

$ chmod +x test1.txt
$ ls -l test1.txt
-rw-r--r-- 1 HAMMAD 197121 0 Sep 11 15:15 test1.txt

$ ps
      PID    PPID    PGID     WINPID   TTY         UID    STIME COMMAND
     1042     838    1042      16148  pty0      197610 15:18:05 /usr/bin/ps
      838     837     838      14344  pty0      197610 16:24:04 /usr/bin/bash
      837       1     837      12752  ?         197610 16:24:04 /usr/bin/mintty
```

`chmod +x` ran without error, but the execute bit does not show in `ls -l` because Windows (NTFS) does not store Unix permissions the same way Linux does.

`kill <PID>` ends a process by its ID. It was not run on a live process, because killing the bash process would close the terminal.

## Concept only (not meaningful on Windows)

`sudo` (run as administrator), `shutdown` and `restart` (power control), and `dpkg` (Debian package manager) are Linux system commands and were reviewed but not run.

## Command history

The full list of commands typed is saved in `all_commands.txt`.
