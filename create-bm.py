#!/usr/bin/python3

# Import os for os.path usage.
import os
# Import sys module for taking system arguments from command line.
import sys

# Pass first argument as the url.
url = sys.argv[1]

# Pass second argument as the filename of the bookmark.
urlfile = sys.argv[2]


def remove_punctuation(s):
    """Strip all punctuation, except "_", "/" , "-" from s."""

    punctuation = "!\"#$%&'()*+,/.:;<=>?@[\\]^`{|}~"

    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct


def myreplace(old, new, s):
    """Replace all occurrences of old with new in s."""

    result = " ".join(s.split())  # firsly remove any multiple spaces " ".

    return new.join(result.split(old))


def build_file(url, urlfile):
    """ """
    myfile = open(urlfile, "w")
    myfile.write("[InternetShortcut]\n")
    myfile.write('''URL="{0}"'''.format(url))
    myfile.close()


# Encode urlfile, to ignore non ascii characters.
encoded = urlfile.encode("ascii", "ignore")

# Decode now to utf-8.
urlfileutf8 = encoded.decode("utf-8")

# Strip any punctuation, excluding "_"
clean = remove_punctuation(urlfileutf8)

# Replace spaces with underscore.
spaces = myreplace(" ", "_", clean)

# Constuct output location path and bookmark filename.
home_dir = os.path.expanduser("~")
urlfile2 = os.path.join(home_dir, "Bookmarks", spaces + ".url")

# Build the output file.
build_file(url, urlfile2)

# Text to display.
print("\n    New file created at....\n")
print("    " + urlfile2 + "\n")
