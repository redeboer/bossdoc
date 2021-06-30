<!-- cspell:ignore aklog besvis kinit klog mccor mlgpu Shuoping -->

<!-- Known issues and some solutions. -->

# Troubleshooting

## I lost read-write access in my `afs` home folder

Formerly, this problem could be solved using the `klog` command. Since August
2019, this command has become:

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
`jobOptions_*.txt` ends in a comment. You can solve it by adding a new line to
the file.

## I cannot run a bash script, but I'm sure it should work

It could be that you wrote the `.sh` script on Windows and the file wasn't
stored with Linux line endings. You can change these line endings back to Linux
using:

```bash
sed -i 's/\r$//' $fileName
```

## Some header files are not found when compiling my package

Check your `requirements` file. Packages that you need should be declared here
as well. For instance, if you want to use `McTruth` packages such as
`McParticle.h`, you should add the line:

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
`physics` (or whatever group you need).

### No resources in job submit group

If you receive the error message

```text
No resources in your group(s). So the job can not be submitted.
```

you should ask to be put in a different group (probably `physics`). Write an
email to Ms. Wen Shuoping.

I cannot submit a job through `boss.condor` or `hep_sub` but see

## `ERROR: Failed to create new proc id` instead

Two known causes:

1. In the case of `hep_sub`, you should submit an **executable** bash script.
   Make the `sh` script executable using `chmod +x`. Use `boss.condor` in
   exactly the same way as `boss.exe`, that is, feed it a job options file
   (`txt`), not a bash script.

2. You sourced a bash script that contained an `export -f` statement (exporting
   a bash `function`). While this is correct way of exporting a function, it
   somehow affects BOSS. Change this statement into `export` (omit the `f`
   option) and the issue is fixed.

## I cannot try out `boss.exe` without jobs

It should be possible to run `boss.exe` without jobs (see
{ref}`here <step-6>`). Does it result in the following error message?

```text
boss.exe: error while loading shared libraries: libReflex.so:
cannot open shared object file: No such file or directory
```

If so, you probably forgot to {ref}`source TestRelease <step-5>`.

## I get a message about `sysInitialize()` when running a job

If you receive the following error message:

```text
**************************************************
              BOSS version: 7.0.4
************** BESIII Collaboration **************

the jobOptions file is: jobOptions_sim.txt
JobOptionsSvc       FATAL in sysInitialize(): standard std::exception is caught
JobOptionsSvc       ERROR locale::facet::_S_create_c_locale name not valid
ApplicationMgr      FATAL Error initializing JobOptionsS
```

it means the `LANG` environment variable has been set to a value that BOSS
cannot handle. Set it to `C` instead by running:

```bash
export LANG=C
```

## I cannot use a graphical interface from `lxslc`

If, for instance, you cannot view a `TBrowser` or cannot open the event display
`besvis.exe`, but instead see

```text
In case you run from a remote ssh session, reconnect with ssh -Y
```

you probably logged in with an SSH key and even using `ssh -Y` won't help. If
you really need the graphical interfaces from `lxslc`, you will need to remove
your public key from the `~/.ssh/authorized_keys` file (just open and edit,
it's just a text file) and log in again.

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
