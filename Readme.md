# __main__ python landing page script async

### Creates an async loop with the called classes and functions.

### _________________________________________________________

example uses:

python Main_Script_Dir somepypage.func *arg *arg

python Main_Script_Dir somepypage.class.func *arg *arg

python Main_Script_Dir somefolder.somepypage.class.func

python Main_Script_Dir somefolder.somefolder.somepypage.func

python Main_Script_Dir somefolder.somefolder.somepypage.class.func

### _________________________________________________________


### Wrote this because I needed a way to run commands from various python scripts using the terminal so crontab and other apps could run python tasks async.


### Unfortunately this script does not give the ability to add *args to class with class.func or kwargs at the moment. You can only add *args to func when running class.func
### I do have a script to run all **kwargs and *args for classes and functions if interested.

### I do this for a hobby, please realize I'm not a programmer by trade and this is the first script I've shared with the world. It took me multiple versions and brain pain so I've decided to share.

