<!--
cspell:ignore evelibs glibs incdir rtcompile rtcompilerun rtdebugcompile
cspell:ignore Xmanager
-->

# Tips & Tricks

## Key generation for SSH

If you do not like to keep having to enter your password, have a look at generating an
ssh key [here](https://www.ssh.com/ssh/keygen) and
[here](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

1. Generate a key with the command `ssh-keygen`. You can choose to leave the password
   empty.

2. Add the SSH key to the `ssh-agent` and create a corresponding _public key_ with the
   commands: <br> `eval $(ssh-agent -s); ssh-add ~/.ssh/id_rsa`

3. Copy the public key to the server using: <br>
   `ssh-copy-id -i ~/.ssh/id_rsa <your user name>@lxslc7.ihep.ac.cn` You will be asked
   for your IHEP account password.

4. Try to log in to the server with: `ssh -Y <your user name>@lxslc7.ihep.ac.cn` If all
   went correctly, you don't have to enter your password anymore.

## Installing ROOT

The BOSS Starter Kit comes with a
[handy bash script](https://code.ihep.ac.cn/bes3/BOSS_StarterKit/-/tree/master/utilities/InstallCernRoot.sh)
to download and install CERN ROOT6 on a Ubuntu platform. It requires you to have `sudo`
(admin) rights. The script can be run in one go using:

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

## Visual Studio Code

**[Visual Studio Code](https://code.visualstudio.com) (VSCode)** is a popular IDE that
is regularly updated, is configurable with easy-to-access `json` files, and offers a
growing number of user-developed extensions. In recent years, it is has become
[the most widely used editor](https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-integrated-development-environment)
on the market.

### Remote SSH

For working with VSCode on `lxslc`, you can use the
[Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
extension. This lets you with VSCode work on the server with full functionality, such as
using the Source Control Manager and language navigation from any other VSCode
extensions you installed. See
[here](https://code.visualstudio.com/docs/remote/ssh-tutorial#_connect-using-ssh) for a
tutorial on how to connect to a remote SSH server.

There is one thing you need to change in your
[VSCode settings](https://code.visualstudio.com/docs/getstarted/settings). Following
[these instructions](https://code.visualstudio.com/docs/remote/troubleshooting#_troubleshooting-hanging-or-failing-connections),
set the following option:

:::{margin}

VSCode also
[recommends](https://code.visualstudio.com/docs/remote/troubleshooting#_troubleshooting-hanging-or-failing-connections)
settings `"remote.SSH.showLoginTerminal": true`, but this seems not to be required to
get VSCode to run on the IHEP server.

:::

```json
  "remote.SSH.useLocalServer": false,
```

In addition, you may need to set the remote platform to `"linux"`:

```json
  "remote.SSH.remotePlatform": {
    "lxslc7.ihep.ac.cn": "linux"
  },
```

where `"lxslc7.ihep.ac.cn"` is the name of the host in your
[SSH Config file](https://man7.org/linux/man-pages/man5/ssh_config.5.html).

:::::{tip}

VSCode Remote SSH installs some files into your home directory on the server, in a
folder called `.vscode-server`. This will not work if you experience this (rather
common) problem: {ref}`read-write-access`. It is therefore recommended that you move the
`.vscode-server` folder to a directory where you always have read-write access and then
create a symbolic link to that folder in your actual home folder. Do this as follows:

::::{tab-set}

:::{tab-item} `.vscode-server` does not yet exist

```shell
cd ~
mkdir /besfs5/users/$USER/.vscode-server
ln -s /besfs5/users/$USER/.vscode-server
```

:::

:::{tab-item} `.vscode-server` already exists

```shell
cd ~
mv -f .vscode-server /besfs5/users/$USER/
ln -s /besfs5/users/$USER/.vscode-server
```

:::
::::

Another major advantage of this set-up is that you won't have problems with
[data quota](../tutorials/getting-started/data-quota.md) when the
`.vscode-server` grows over time.
:::::

### Language navigation for BOSS

It is highly recommended to install the
[VS Code C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
extension when you are developing BOSS packages. One of its killer features is
[intellisense](https://code.visualstudio.com/docs/cpp/configure-intellisense-crosscompilation),
which gives language navigation on C++ libraries. To get full language navigation for
BOSS, create a `c_cpp_properties.json` file under the `.vscode` folder in your
[workspace](https://code.visualstudio.com/docs/editor/workspaces) with the following
content:

:::{note}

Please [comment](../contribute.md) here if you still see squiggle lines under `#include`
statements in your source code. It could be that the list of include paths has to be
updated.

:::

<!-- cspell:ignore GDML Saxana geant literalinclude -->

```{eval-rst}
.. literalinclude:: c_cpp_properties.json
  :class: full-width
  :language: json
```

This file can be downloaded {download}`here <c_cpp_properties.json>`. On the server, you
can quickly do this by navigating to your `.vscode` folder and running:

```shell
wget https://raw.githubusercontent.com/redeboer/bossdoc/main/docs/appendices/c_cpp_properties.json
```

:::{tip}

For BOSS language navigation locally, have a look at
[BOSS_ExternalLibs](https://code.ihep.ac.cn/bes3/BOSS_ExternalLibs).

:::

<!-- cspell:ignore cvmfs envs mlgpu -->

## Compiling

For compiling outside ROOT (that is, _not_ using the ROOT interpreter), you will need to
use a compiler like `g++`. The compiler needs to be told where the libraries for
included ROOT header files are located. You can do this using flags that ROOT set during
its installation. In case of `g++`, use:

```text
g++ YourCode.C -I$(root-config --incdir) $(root-config --libs --evelibs
--glibs) -o YourBinaryOutput.o
```

_Pro `bash` tip:_ You might like to create an easy command for this. You can do this by
adding the following lines to your `~/.bashrc`.

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

Note the flags added through `root-config`: there are includes (preceded by option `-I`)
and linked libraries (following that option, and preceding output option `-o`). Note
also that flags have been added for `RooFit`. For more information about ROOT flags, see
[this page](https://root.cern/install/build_from_source/#all-build-options).

Here, we give three examples of commands, one for compiling only (`rtcompile`), one for
compiling and executing if successful (`rtcompilerun`), and one for compiling with
`fsanitize` activated
([rtdebugcompile](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html)). The
latter is useful if you want to look for memory leaks etc --- only use if you are
interested in this, because it will decrease run-time. In addition, there are many
issues in root (like `TString`) that are identified by `fsanitize`.

### Compiling on Windows 10

Although it is highly recommended to on a Linux OS such as Ubuntu or CentOS, there are
still -certain advantages of working on Windows. As a developer, that brings problems,
however, if you want to start compiling your code.

Since Windows 10, there exists an easy solution:
[Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install)
(WSL). In the newest versions can be easily installed from the Windows Store (search for
"Ubuntu"). After installing, search for "Ubuntu" in the start menu. This is a bash
terminal that has full access to your windows system, but entirely through bash
commands.

As such, you have access to convenient commands like `apt install`, `vi`, and `g++`.
Best of all is that you can use this to
[install ROOT](https://root.cern/install/dependencies). If you are having trouble
installing ROOT through bash, have a look
[at this script](https://github.com/redeboer/NIKHEFProject2018/blob/master/docs/Install%20CERN%20ROOT6.sh)
(ROOT6).
