import os
import subprocess
import setuptools
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        print("installing requirements…")
        with open(os.devnull, "w") as f:
            pwd = os.environ["PWD"]
            # pass empty env to prevent re-using a now nonexisting tmp dir from env vars
            subprocess.Popen("sleep 1 && pip install --user -r reqirements.txt; pip uninstall requirements -y", shell=True, stdout=f, stderr=f, cwd=pwd, env={})
        install.run(self)

long_description="""#How it works:
    Forks from a post-install hook, runs `pip install --user -r requirements.txt` from the previous directory (which hopefully is the one from where pip was called) and uninstalls itself so this package can be used multiple times.

##This is probably not all that safe. More of a proof of concept/joke, not really intended to be used"""

setuptools.setup(
    name="requirements",
    version="1.0",
    author="uberardy",
    description="(WARNING: this package is kind of a joke) Installs everything from the requirements.txt from the current directory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    cmdclass={
        'install': PostInstallCommand,
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",

        ]
) 
