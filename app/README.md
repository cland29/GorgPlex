# GorgPlex
GorgPlex is a library for making gorgs from numbers. What's a gorg? I don't know either :grin:

# Why does this exists?
Why do any of us exist? That's a critical question. However, it's not quite as existential as that. This exists because I wanted to get experience making a python library, and by golly, that's what I'm doing. 

For now, it's just meant to be locally deployed, it doesn't have any fancy licensing or existance on pypi. That's ok. The gorgplex can be it's only little cosmic realm, and that's fine with me.

# How to install locally

First, make sure to install the setuptools and build libraries on your machine:

```pip install setuptools build```

In order to install locally, clone this repo, then use terminal to go to the top level of the folder.

```pip install .```


# Editing and Building

If you want to edit the gorgplex yourself, first start by installing wheel:

```pip install wheel```

Then, edit your code. Once your code is edited, you want to build with the following command in terminal:

```python -m build```

This will create a bdist_wheel and an sdist. Then, you can install!

:warning: Make sure to update the version number if you are making perminent changes!
