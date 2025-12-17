#!/bin/bash

# This script compiles .tex files using xelatex and biber.
# If a filename is provided as an argument, it compiles only that file.
# Otherwise, it compiles all .tex files in the current directory.

compile_latex() {
  local texfile="$1"
  base="${texfile%.tex}"

  echo "--- Compiling ${base} ---"
  xelatex "$texfile"
  biber "$base"
  xelatex "$texfile"
  xelatex "$texfile"
  echo "--- Finished ${base} ---"
}

if [ "$#" -gt 0 ]; then
  # Compile the specified file(s)
  for arg in "$@"; do
    if [[ "$arg" != *.tex ]]; then
      echo "Error: File '$arg' is not a .tex file."
      continue
    elif [ ! -f "$arg" ]; then
      echo "Error: File '$arg' not found."
      continue
    fi
    compile_latex "$arg"
  done
else
  # Compile all .tex files in the directory
  for texfile in ./*.tex; do
    [ -f "$texfile" ] && compile_latex "$texfile"
  done
fi
