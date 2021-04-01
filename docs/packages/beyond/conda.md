<!-- cspell:ignore condaenv cvmfs envs mlgpu -->

<!-- 'Or, how to use Python3 or TensorFlow on lxslc' -->

# Conda

The {code}`lxslc` server has a very outdated version of Python. If you do want
to use Python 3, you can work with Conda, which is available on the server.
Just add the following script:

```bash conda_env.sh
__conda_setup="$(
  '/cvmfs/mlgpu.ihep.ac.cn/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null
)"
if [ $? -eq 0 ]; then
  eval "$__conda_setup"
else
  if [ -f "/cvmfs/mlgpu.ihep.ac.cn/anaconda3/etc/profile.d/conda.sh" ]; then
    . "/cvmfs/mlgpu.ihep.ac.cn/anaconda3/etc/profile.d/conda.sh"
  else
    export PATH="/cvmfs/mlgpu.ihep.ac.cn/anaconda3/bin:$PATH"
  fi
fi
unset __conda_setup
```

You can then source it through whatever means you prefer, like creating an
alias {code}`alias condaenv="source <path_to_script>/conda_env.sh"` in your
{code}`.bashrc`.

Next, just run {code}`conda activate tensorflow-gpu` and you have
{code}`python3`, {code}`ipython` and even {code}`import tensorflow` available!
(At the time of writing, TensorFlow is version 1.13.1 though.)

Unfortunately, you don't have the rights to {code}`conda create` new
environments. To see which other environments are available, use
{code}`conda info --envs`.

```{note}

If you don't want to go through this whole hassle (it's quite slow indeed), and
just want to use {code}`python3`, you could also just add
{code}`/cvmfs/mlgpu.ihep.ac.cn/anaconda3/envs/tensorflow/bin` to your
{code}`PATH`. But keep in mind that you may run into trouble with certain
Python libraries!
```
