<!-- cspell:ignore aklog besvis kinit klog mccor mlgpu Shuoping -->

<!-- Known issues and some solutions. -->

# Troubleshooting

## I lost read-write access in my {code}`afs` home folder

Formerly, this problem could be solved using the {code}`klog` command. Since
August 2019, this command has become:

```bash
kinit $USER
aklog -d
```

You should now be able to read-write in _all_ your sessions.

## I'm sure my job is set up correctly, but it keeps resulting this error

```text
JobOptionsSvc       ERROR # =======> <package>/share/jobOptions_<package>.txt
JobOptionsSvc       ERROR # (22,1): parse error
...
JobOptionsSvc       FATAL Job options errors.
ApplicationMgr      FATAL Error initializing JobOptionsSvc
```

Yep, this is a weird one... So far, the cause was usually that the
{code}`jobOptions_*.txt` ends in a comment. You can solve it by adding a new
line to the file.

## I cannot run a bash script, but I'm sure it should work

It could be that you wrote the {code}`.sh` script on Windows and the file
wasn't stored with Linux line endings. You can change these line endings back
to Linux using:

```bash
sed -i 's/\r$//' $fileName
```

## Some header files are not found when compiling my package

Check your {code}`requirements` file. Packages that you need should be declared
here as well. For instance, if you want to use {code}`McTruth` packages such as
{code}`McParticle.h` , you should add the line:

```text
use McTruth     McTruth-*     Event
```

## I am not the right group for submitting jobs

If you receive the error message

```text
hep_sub: error: argument -g/--group: invalid choice: 'physics'
(choose from 'gpupwa', 'mlgpu')
```

or something with different group names, it means you are in the wrong job
submit group. Write an email to Ms. Wen Shuoping to ask to be put in the group
{code}`physics` (or whatever group you need).

### No resources in job submit group

If you receive the error message

```text
No resources in your group(s). So the job can not be submitted.
```

you should ask to be put in a different group (probably {code}`physics`). Write
an email to Ms. Wen Shuoping.

I cannot submit a job through {code}`boss.condor` or {code}`hep_sub` but see

## {code}`ERROR: Failed to create new proc id` instead

Two known causes:

1. In the case of {code}`hep_sub` , you should submit an **executable** bash
   script. Make the {code}`sh` script executable using {code}`chmod +x`. Use
   {code}`boss.condor` in exactly the same way as {code}`boss.exe` , that is,
   feed it a job options file ({code}`txt`), not a bash script.

2. You sourced a bash script that contained an {code}`export -f` statement
   (exporting a bash {code}`function`). While this is correct way of exporting
   a function, it somehow affects BOSS. Change this statement into
   {code}`export` (omit the {code}`f` option) and the issue is fixed.

## I cannot run {code}`boss.exe` without jobs

It should be possible to run {code}`boss.exe` without jobs (see
{ref}`here <Step 6>`). Does it result in the following error message?

```text
boss.exe: error while loading shared libraries: libReflex.so:
cannot open shared object file: No such file or directory
```

If so, you probably forgot to {ref}`source TestRelease <Step 5>`.

## I get a message about {code}`sysInitialize()` when running a job

If you receive the following error message:

```text
**************************************************
              BOSS version: 7.0.4
************** BESIII Collaboration **************

the jobOptions file is : jobOptions_sim.txt
JobOptionsSvc       FATAL in sysInitialize(): standard std::exception is caught
JobOptionsSvc       ERROR locale::facet::_S_create_c_locale name not valid
ApplicationMgr      FATAL Error initializing JobOptionsS
```

it means you have encountered another nasty bug. It could have something to do
with the environment of the terminal with which you log in: in the case of
Windows, it is known to appear when using
{ref}`the wsl terminal <appendices/tips/tips-and-tricks:Compiling on Windows 10>`.
Try a different terminal (such as [git bash](https://gitforwindows.org)) and
the problem might disappear. It's magic!

```{note}
in Linux, the trick doesn't seem to work...
```

## I cannot use a graphical interface from {code}`lxslc`

If, for instance, you cannot view a {code}`TBrowser` or cannot open the event
display {code}`besvis.exe` , but instead see

```text
In case you run from a remote ssh session, reconnect with ssh -Y
```

you probably logged in with an SSH key and even using {code}`ssh -Y` won't
help. If you really need the graphical interfaces from {code}`lxslc` , you will
need to remove your public key from the {code}`~/.ssh/authorized_keys` file
(just open and edit, it's just a text file) and log in again.

## My analysis BOSS packages end in a segmentation fault

A common error is that you didn't book the `NTuple` or add the `NTuple::Item`s
with `NTuple::Tuple::addItem`. This usually results in the following error.

```text
...
DatabaseSvc: Connected to MySQL database
mccor = 0

 *** Break *** segmentation violation
    __boot()
    import sys, imp, os, os.path
```
