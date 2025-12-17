#!/bin/bash

# This script compiles .tex files using xelatex and bibtex.
# If a filename is provided as an argument, it compiles only that file.
# Otherwise, it compiles all .tex files in the current directory.

compile_latex() {
  local texfile="$1"
  base="${texfile%.tex}"

  echo "--- Compiling ${base} ---"
  xelatex "$texfile"
  bibtex "$base"
  xelatex "$texfile"
  xelatex "$texfile"
  echo "--- Finished ${base} ---"
}

if [ "$#" -gt 0 ]; then
  # Compile the specified file
  if [ -f "$1" ]; then
    compile_latex "$1"
  else
    echo "Error: File '$1' not found."
    exit 1
  fi
else
  # Compile all .tex files in the directory
  for texfile in ./*.tex; do
    [ -f "$texfile" ] && compile_latex "$texfile"
  done
fi
