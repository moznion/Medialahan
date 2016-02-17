#!/bin/sh

sed='sed'
if [[ $OSTYPE =~ 'darwin' ]]; then
  sed='gsed'
fi

cat "$@" | grep -v '^#' | $sed -E 's/[\t]+/: /' | $sed -E 's/ /\n- /g'

