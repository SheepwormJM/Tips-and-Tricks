# Permissions: 
https://linuxhandbook.com/linux-file-permissions/ 
https://linuxhandbook.com/content/images/2020/06/file-permission-explanation-2-1.png![image](https://github.com/user-attachments/assets/897004a3-40c0-48d4-b02a-451eb8cc3a0a)


# To help reduce the chance a file will be deleted by accident

1. Make a back up somewhere else (e.g. Lainglab)
2. Put your raw sequencing reads on a public server (e.g. ENA) once you've finished the project!
3. Change the file permissions to remove the 'writeable' aspect. This will then add a check question to see if you are sure you want to delete it. Obviously, this is still easy to do.... AND remember that you can still overwrite the file - so with another file with the same name. Which will effectively delete the original.
```
chmod -w filename
```
