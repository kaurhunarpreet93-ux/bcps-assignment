# Labs 1–2: CLI Folder and File Management

## Aim
To create folders and files using command-line commands and perform basic file-management operations.

## Procedure
1. Open Command Prompt on Windows or Terminal on Linux.
2. Run the commands for your operating system below.
3. Check the created folder and file using the directory-listing command.
4. Optional: practise renaming or copying a file.
5. Remove the practice folder only after checking its path and contents.

## Windows Command Prompt
```bat
cd
dir
mkdir CollegeLab
cd CollegeLab
mkdir Records
type nul > student.txt
echo Computer Fundamentals Lab > student.txt
dir
cd ..
```

## Linux Terminal
```bash
pwd
ls
mkdir -p CollegeLab/Records
cd CollegeLab
touch student.txt
echo "Computer Fundamentals Lab" > student.txt
ls -la
cd ..
```

## Expected Output
A folder named `CollegeLab` is created, containing a `Records` subfolder and a `student.txt` file. The listing command displays these items.

## Conclusion
Folder creation, directory navigation, file creation, and directory listing were practised using CLI commands.

## Optional cleanup
Windows: `rmdir CollegeLab /s` (asks for confirmation).
Linux: `rm -r CollegeLab`.
**Warning:** Cleanup permanently deletes the selected folder and its contents. Run only after verifying the path.
