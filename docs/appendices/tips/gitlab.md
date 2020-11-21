<!-- cspell:ignore testrepo testfile -->

# IHEP GitLab

IHEP supplies a GitLab server, which allows you to put your analysis code in a
{code}`git` repository. You can then enjoy all the benefits of version control,
different branches to collaborate as a team, a better overview through online
access, etc. The IHEP GitLab server can be accessed through
[code.ihep.ac.cn](http://code.ihep.ac.cn). Have a look
[here](https://guides.github.com/introduction/git-handbook) at what {code}`git`
does, it's worth it!

```{note}
Unfortunately, the IHEP GitLab server is only available on-campus through the
LAN network. In theory, it is possible to connect through the IHEP VPN
([ssl.ihep.ac.cn](http://ssl.ihep.ac.cn)) using EasyConnect, though to set this
up, you will first need to be in that LAN network. There are plans to make the
server available through the standard SSO account.
```

## Preparing access to the server

To be able to push files to a repository on the IHEP GitLab server, you will
first need to apply for an IHEP GitLab account. You can do this by sending an
email to [fanrh@ihep.ac.cn](mailto:fanrh@ihep.ac.cn).

When you have received your login credentials, log in to
[code.ihep.ac.cn](http://code.ihep.ac.cn/profile/keys/132) and have a look
around. As you have probably noticed, there is a warning that you have to add
an SSH key in order to pull and push to the server. The steps to create such a
key are comparable to those for login in to the
{ref}`IHEP server <appendices/tips/tips-and-tricks:Key generation for SSH>`.

1. Generate an SSH key with the command {code}`ssh-keygen`. You can choose to
   leave the password empty.

2. Add the SSH key to the {code}`ssh-agent` and create a corresponding _public
   key_ with the commands: <br>
   {code}`eval $(ssh-agent -s) ssh-add ~/.ssh/id_rsa`

3. Now, obtain the corresponding public key using: <br>
   {code}`cat ~/.ssh/id_rsa.pub` <br> and copy all the text you see there (from
   {code}`ssh-rsa` to {code}`@ihep.ac.cn`).

4. Go to [code.ihep.ac.cn/profile/keys](http://code.ihep.ac.cn/profile/keys),
   click "Add SSH Key", paste the code there, and "Add key".

5. That's it!

See
[here](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
for more elaborate instructions.

As a test, you can now create a new repository on the server. Just click
["New project"](http://code.ihep.ac.cn/projects/new) and follow the
instructions. This is a nice way to start, as you will be immediately shown
instructions on how to configure {code}`git` locally (such as setting the user
name).

## Pushing existing code to a new repository

Imagine the situation where you have already developed some code for your
analysis and you want to start tracking it using {code}`git`. Let's say the
directory containing this called is {code}`TestRepo`. Here, we go through the
steps required to put that code into a repository and push it to the IHEP
GitLab server.

### Step 1: Go to the files you want to track

Go to your the folder containing your code or, alternatively, make a directory
({code}`mkdir`), and add some test files there.

### Step 2: Initialize the repository

Initialize this folder as an empty {code}`git` repository using:

```bash
git init
```

The name of the repository that you just initialized is the name of the folder.

### Step 3: Add the files in the directory

Files in the directory are not tracked by {code}`git` automatically. You have
to add them manually. This can be done through the {code}`git add` command, for
instance:

```bash
git add temp.sh
git add config/testfile.txt
git add src/
git add inc/*.hpp
git add .
```

You now have _staged_ these files, that is, made them ready for a commit to the
repository. Files that have been added, will be tracked from then onward: if
you change such a file {code}`git` allows you to compare the changes, move back
to older version, compare the file to its counterpart in parallel branches,
etc.

Note that the paths are relative and that you can use {code}`git add` from any
subdirectory in the repository.

```{admonition} .gitignore
If there are certain files you never want to track (such as input data files or
output plots), you 'shield' them by creating a file called {code}`.gitignore`
(note the dot) in the main directory of the repository. This is a text file
contains relative paths of the files you want to ignore. Wildcards are allowed,
see [here](https://help.github.com/en/articles/ignoring-files) for more
information. Now, if you use {code}`git add .` , all new or modified files in
the folder will be staged, but for the ones excluded by {code}`.gitignore`.
```

### Step 4: Commit the changes

Once you have added the files, you can make {code}`commit` the changes using:

```bash
git commit -m "<some description>"
```

This will basically create a new point in the history of your {code}`git`
repository to which you can move back any time.

### Step 5: Check the status of the repository

Some commands that are useful from this stage onward:

- Use {code}`git status` to check which files have been tracked, which ones are
  modified compared to the previous commit, which ones removed, etc. If you
  added all the files you wanted to add, you can {code}`commit` or
  {code}`push`.

- Use {code}`git log` to see the history of all your commits.

- Use {code}`git diff <relative path>` to compare the differences in a tracked
  directory or file with its previous commit.

- Use {code}`git checkout <relative path>` to retrieve the previous version of
  the file or directory.

- See [here](https://git-scm.com/docs) for a full reference of {code}`git`
  commands.

```{note}
The above 5 steps are all you need to know if you just want to track your files
through Git **locally**. You do not have to work with a GitLab server, though
of course this does allow for team collaboration and is the best way to backup
your work.
```

### Step 6: Configure the Git repository

If you have applied for an account and
{ref}`added an SSH key <appendices/tips/gitlab:Pushing existing code to a new repository>`,
you can push this new repository to [code.ihep.ac.cn](http://code.ihep.ac.cn).
If you haven't already done so, set the user name and email address for this
repository:

```bash
git config user.name "<Your full name>"
git config user.email "<email>@ihep.ac.cn"
```

Use {code}`git config --global` if you want to use these credentials
everywhere.

Now you can add the SSH location to which you want to write your repository:

```bash
git remote add origin git@code.ihep.ac.cn:<username>/TestRepo
```

Here, {code}`<user name>` should be the one you were given when you registered.
Here, we use the directory name {code}`TestRepo` as repository name, but it can
be any name as long as it is unique within your account.

### Step 7: Create the repository on the server

Unfortunately, access through SSH does not allow you to create a new repository
on the server, so you have to do this through the web interface.

Go to [code.ihep.ac.cn](http://code.ihep.ac.cn) and click "New repository". Use
{code}`TestRepo` as the " _Project_ name", then click "Customize repository
name?" to ensure that the name of the repository is {code}`TestRepo` as well.
(If you don't, it will be named {code}`testrepo` , while **the _repository_
name should match the name of your directory**. As you see, the default option
for a new repository is private, so only you can see it.

### Step 8: Push your the first commit

Now, back to your files, you can push the commit you made to that new
{code}`TestRepo` on the server:

```bash
git push -u origin master
```

Later, you can just use {code}`git push` without arguments, but this is to
force the first commit to the master branch.

**That's it, the connection has been established!**

You can now edit and add files and then go through steps
{ref}`3 (add) <appendices/tips/gitlab:Step 3: Add the files in the directory>`,
{ref}`4 (commit) <appendices/tips/gitlab:Step 4: Commit the changes>`,
{ref}`5 (status) <appendices/tips/gitlab:Step 5: Check the status of the repository>`,
and {ref}`8 (push) <appendices/tips/gitlab:Step 8: Push your the first commit>`
to track your files.

```{note}
If you work together with others, you can use {code}`git pull` to get the
latest changes that others added. Working together through {code}`git` is,
however, a bit more complicated because you'll have to think about different
branches and how to deal with merge conflicts. Have a look at the
[Git Handbook](https://guides.github.com/introduction/git-handbook) for more
information.
```
