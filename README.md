# eVa Conversions

## Dev Setup
The current setup is based on Anaconda Python 3.10. Ensure the Anaconda 3 bin directory is in your shell path. After cloning this repo and cd'ing into the project directory

```bash
conda env create # first time
conda activate eVa_Conversions
```

After that, it depends on how you like to work. If you want to add dependencies to the `environment.yml` file directly, just save the file and then do the following to update the conda environment with the file's state.

```bash
conda activate eVa_Conversions
conda env update
```

You can also install packages via conda and then use conda to update the `environment.yml` with the conda environment's state. see https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html for more on how to manage packages with conda

```bash
conda activate eVa_Conversions
conda install scipy
conda env export -n eVa_Conversions > ./environment.yml   # or however the slashes lean on your OS
```

Either way, know the `environment.yml` file is how you can move the environment between machines, so do your best to keep it sync'd with actual reality.
