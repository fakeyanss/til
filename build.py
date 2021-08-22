#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Simple script to auto-generate the README.md file for a TIL project.
"""
import os
import json
import itertools
import subprocess as sp
import pathlib

BASE_DIR = "docs/"

AVOID_DIRS = [
        "dist",
        "_navbar.md",
        '_sidebar.md',
        ".nojekyll",
        ".asset"
    ]


HEADER = """
<h1 align="left">Things I Learn</h1>
<p align="center">
  <img alt="TILs Count" src="https://img.shields.io/badge/dynamic/json.svg?color=black&label=TILs&query=count&url=https%3A%2F%2Fraw.githubusercontent.com%2Ffakeyanss%2Ftil%2Fmaster%2Fcount.json">
  <img alt="last commit" src="https://img.shields.io/github/last-commit/fakeyanss/til?color=purple">
  <a href="https://github.com/fakeYanss/til/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/github/license/fakeyanss/til" target="_blank" />
  </a>
  <a href="https://foreti.me/til/">
    <img alt="Website" src="https://img.shields.io/website?url=https://foreti.me/til/">
  </a>
  <a href="https://twitter.com/fakeYanss">
    <img alt="Twitter: fakeYanss" src="https://img.shields.io/twitter/follow/fakeYanss.svg?style=social" target="_blank" />
  </a>
</p>

> Personal Wiki of Interesting things I learn every day at the intersection of software development, computer science & stuff.


"""

FOOTER = """## Usage

1. install docsify
```
npm i docsify-cli -g
```

2. create git repo, and init docsify
```
docsify init docs
```

3. customize index.html, just like my [index.html](docs/index.html)

4. preview your writing
```
docsify serve docs
```

5. install docsify-tools, for auto generate sidebar
```
npm i docsify-tools -g
```

generate sidebar
```
docsify-auto-sidebar -d docs
```

you can craete a git hook pre-commit, docsify-auto-sidebar will generate _narbar into sidebar, which is not expected, we can remove it manually
```
docsify-auto-sidebar -d docs

sed -i "" "/_navbar/d" docs/_sidebar.md # mac
sed -i "/_navbar/d" docs/_sidebar.md # linux

python build.py

git add .
```

## Author 

👤 **[FakeYanss](https://fakeyanss.github.io)** 

## About

TIL is inspired by [Bhupesh-V/til](https://github.com/Bhupesh-V/til).
"""

def get_category_list():
    """Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" of TILs."""
    
    dirs = [
        x
        for x in os.listdir(BASE_DIR)
        if os.path.isdir(BASE_DIR + x) and x not in AVOID_DIRS
    ]
    return dirs


def get_title(til_file):
    """Read the file until we hit the first line that starts with a #
    indicating a title in markdown.  We'll use that as the title for this
    entry."""
    with open(til_file) as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                return line[1:].lstrip()  # text after # and whitespace


def find_all_files(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            skip = False
            for avoid in AVOID_DIRS:
                if avoid in fullname:
                    skip = True
            if skip:
                continue
            yield fullname


def get_tils(category):
    """ For a given category, get the list of TIL titles. """
    til_files = [x for x in find_all_files(category)]
    titles = []
    for filename in til_files:
        if (os.path.isfile(filename)) and filename.endswith(".md"):
            title = get_title(filename)
            # changing path separator for Windows paths
            # https://mail.python.org/pipermail/tutor/2011-July/084788.html
            titles.append((title, filename.replace(os.path.sep, "/")))
    return titles


def get_category_dict(category_names):
    categories = {}
    count = 0
    for category in category_names:
        titles = get_tils(BASE_DIR + category)
        categories[category] = titles
        count += len(titles)
    return (count, categories)


def read_file(filename):
    with open(filename) as file:
        return file.read()


def print_file(category_names, count, categories):
    host_url = "https://github.com/fakeyanss/til/blob/master/"
    # used by shields.io for creating the TIL badge
    with open("count.json", "w") as json_file:
        data = {"count": count}
        json.dump(data, json_file, indent=" ")

    with open("README.md", "w") as file:
        file.write(HEADER)
        file.write("""\n\n## Categories\n""")
        # print the list of categories with links
        for category in sorted(category_names):
            tils = categories[category]
            file.write(
                f"""* [{category}](#{category.replace(' ', '-').lower()}) [**`{len(tils)}`**]\n"""
            )

        if len(category_names) > 0:
            file.write("""\n---\n\n""")
            # print the section for each category
        for category in sorted(category_names):
            file.write("\n\n\n### {0}\n\n".format(category))
            tils = categories[category]
            file.write("<ul>")
            for (title, filename) in sorted(tils):
                file.write("\n<li>")
                file.write(
                    f"""<a target="_blank" href="{host_url+filename}">{title}</a>"""
                )
            file.write("\n")
            file.write("</ul>\n\n")

        file.write(FOOTER)


def get_recent_tils(categories):
    cmd = "git log --no-color --date=format:'%d %b, %Y' --diff-filter=A --name-status --pretty=''"
    recent_tils = []

    result = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = result.communicate()
    clean_output = out.decode("utf-8").strip("\n").replace("A\t", "").split("\n")
    # filter filepaths that don't exist
    flattened_list = list(itertools.chain(*list(categories.values())))
    flattened_list = [item[1] for item in flattened_list]
    valid_files = list(
        filter(
            lambda path: pathlib.Path(path).exists() and path in flattened_list,
            clean_output,
        )
    )
    for til in valid_files[:5]:
        til_dict = {}
        til_dict["title"] = get_title(til)
        til_dict["url"] = f"https://foreti.me/til/#/{til.replace('docs/', '').replace('.md', '')}"
        recent_tils.append(til_dict)

    with open("recent_tils.json", "w") as json_file:
        json.dump(recent_tils, json_file, ensure_ascii=False, indent=" ")


def create_README():
    """Create a TIL README.md file with a nice index for using it directly
    from GitHub."""
    category_names = get_category_list()
    count, categories = get_category_dict(category_names)
    get_recent_tils(categories)
    print_file(category_names, count, categories)
    print("\n", count, "TILs read")


if __name__ == "__main__":
    create_README()
