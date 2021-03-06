<!--
cspell:ignore evelibs glibs incdir rtcompile rtcompilerun rtdebugcompile
cspell:ignore Xmanager
-->

# Tips & Tricks

## Key generation for SSH

If you do not like to keep having to enter your password, have a look at
generating an ssh key [here](https://www.ssh.com/ssh/keygen) and
[here](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

1. Generate a key with the command `ssh-keygen`. You can choose to leave the
   password empty.

2. Add the SSH key to the `ssh-agent` and create a corresponding _public key_
   with the commands: <br> `eval $(ssh-agent -s); ssh-add ~/.ssh/id_rsa`

3. Copy the public key to the server using: <br>
   `ssh-copy-id -i ~/.ssh/id_rsa <your user name>@lxslc7.ihep.ac.cn` You will
   be asked for your IHEP account password.

4. Try to log in to the server with:
   `ssh -Y <your user name>@lxslc7.ihep.ac.cn` If all went correctly, you don't
   have to enter your password anymore.

## Recommended software

Although I recognize that any programmer will and should develop her or his own
habits, there are a few simple recommendations I would like to make, in
particular for beginners.

### Installing ROOT

The BOSS Starter Kit comes with a
[handy bash script](http://code.ihep.ac.cn/bes3/BOSS_StarterKit/-/tree/master/utilities/InstallCernRoot.sh)
to download and install CERN ROOT6 on a Ubuntu platform. It requires you to
have `sudo` (admin) rights. The script can be run in one go using:

```bash
wget https://raw.githubusercontent.com/redeboer/BOSS_StarterKit/master/utilities/InstallCernRoot.sh
sudo bash InstallCernRoot.sh
```

For more information, see the official pages:

- [Installing the right prerequisite packages](https://root.cern/install/dependencies)
- [Downloading ROOT](https://root.cern.ch/downloading-root)
- [Building ROOT](https://root.cern.ch/building-root)

```{warning}
You will download around **1 GB** of source code.
```

### Visual Studio Code

[**Visual Studio Code**](https://code.visualstudio.com) **(VS Code).** Note the
"Code" here—I am not referring to the infamous IDE version. Microsoft decided
to strip Visual Studio of its compile capabilities and develop this editor in
parallel. Since it has been made available _for free_ on all OS platforms, is
regularly updated, is configurable with easy-to-access `json`files, offers a
growing number of user-developed extensions, it is has become the most widely
used editor on the market. Even for users who prefer not to touch the mouse, VS
Code has much to offer as well. (OK, if your are really hardcore keyboard only,
just go for [vim](https://www.vim.org), but this really only offers advantages
if you use it properly.)

For working on `lxslc`, you will need to install this handy
[SSH FS extension](https://marketplace.visualstudio.com/items?itemName=Kelvin.vscode-sshfs).
This allows you to edit files in for instance your workarea and browse around
in the file structure. There are a few steps that are useful to do at this
stage:

1. Create an SSH configuration. This specifies where the extension should find
   `lxslc`, your user name, the folder you want to access, etc. For this, you
   can use the graphical interface that comes along with the extension (have a
   look at the manual that comes along with it). You can later edit these
   configurations in the JSON file of the global settings (use `Ctrl+Shift+P`
   to search for and open "preferences open settings json"). You can also add a
   path to your SSH key file (see below) so that you won't have to enter your
   log in details each time.

2. In the bottom left of the left sidebar, right-click the configuration you
   just made and click "Connect as Workspace folder". You now have all your
   folders available in the Explorer sidebar and can edit files here nicely.

3. Use "Save Workspace As..." under "File" to store the settings of this
   workspace and have the folder opened each time you open this Workspace.

Unfortunately, this extension does not allow to use the full potential of
VSCode, such as autocomplete and browsing through header files. VSCode has
recently provided its own way of working through SSH, which does allow to use
all functionality on the server. For now, it does not work for `lxslc`, but
keep an eye on [Remote-SSH](https://code.visualstudio.com/docs/remote/ssh) for
further developments.

### Other access to the IHEP server through SSH/SFTP

- [**Xmanager**](https://www.netsarang.com/en/xmanager)
- [**WinSCP**](https://winscp.net/eng/index.php)
- [**PuTTY**](https://www.putty.org)

## Compiling

For compiling outside ROOT (that is, _not_ using the ROOT interpreter), you
will need to use a compiler like `g++`. The compiler needs to be told where the
libraries for included ROOT header files are located. You can do this using
flags that ROOT set during its installation. In case of `g++`, use:

```text
g++ YourCode.C -I$(root-config --incdir) $(root-config --libs --evelibs
--glibs) -o YourBinaryOutput.o
```

_Pro `bash` tip:_ You might like to create an easy command for this. You can do
this by adding the following lines to your `~/.bashrc`.

```bash
function rtcompile () {
  g++ "$1"
    -I$(root-config --incdir) \
    $(root-config --libs --evelibs --glibs) \
    -lRooFit -lRooFitCore -lRooStats -lMinuit -o "${1/._/.o}"
}
function rtcompilerun () {
  rtcompile "$1"
  if [ $? -eq 0 ]; then
    ./${1/._/.o}
  fi
}
function rtdebugcompile () {
  g++ "$1"
    -I$(root-config --incdir) \
    $(root-config --libs --evelibs --glibs) \
    -lRooFit -lRooFitCore -lRooStats -lMinuit -fsanitize=address -g -o "${1/.\*/}"
}
export -f rtcompile
export -f rtcompilerun
export -f rtdebugcompile
```

Note the flags added through `root-config`: there are includes (preceded by
option `-I`) and linked libraries (following that option, and preceding output
option `-o`). Note also that flags have been added for `RooFit`. For more
information about ROOT flags, see
[this page](https://root.cern/install/build_from_source/#all-build-options).

I give three examples of commands here, one for compiling only (`rtcompile`),
one for compiling and executing if successful (`rtcompilerun`), and one for
compiling with `fsanitize` activated
([rtdebugcompile](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html)).
The latter is useful if you want to look for memory leaks etc --- only use if
you are interested in this, because it will decrease run-time. In addition,
there are many issues in root (like `TString`) that are identified by
`fsanitize`.

### Compiling on Windows 10

Although I highly recommend working on a Linux OS such as Ubuntu or Scientific
Linux, there are still -certain advantages of working on Windows. As a
developer, that brings problems, however, if you want to start compiling your
code.

Since Windows 10, there exists an easy solution: the
[Linux Subsystem](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
In the newest versions can be easily installed from the Windows Store (search
for "Ubuntu"). After installing, search for "Ubuntu" in the start menu. This is
a bash terminal that has full access to your windows system, but entirely
through bash commands.

As such, you have access to convenient commands like `apt install`, `vi`, and
`g++`. Best of all is that you can use this to
[install ROOT](https://root.cern/install/dependencies). If you are having
trouble installing ROOT through bash, have a look
[at this script](https://github.com/redeboer/NIKHEFProject2018/blob/master/docs/Install%20CERN%20ROOT6.sh)
(ROOT6).
