#!/bin/bash

exec 2>> $HOME/log.hook

echo "--" $(date) -- "$0" "$@" 1>&2

[[ ! $PATH =~ (^|:)/Xopt/conda/xbin(:|$) ]] && PATH=/opt/conda/bin:"$PATH"

printenv | sort | egrep '^(PATH|CLAUDE|PYTHON)' 1>&2
set -x

[ -d "$CLAUDE_PROJECT_DIR" ] || exit 1
cd "${CLAUDE_PROJECT_DIR}" || exit 1

VENV_DIRNAME=".venv"

if [ \! -d "${VENV}" ]; then
	python -mvenv "${VENV_DIRNAME}"
fi

cat > "${CLAUDE_ENV_FILE}" << EOM
export VIRTUAL_ENV="${CLAUDE_PROJECT_DIR}/${VENV_DIRNAME}"
export PATH="${CLAUDE_PROJECT_DIR}/${VENV_DIRNAME}/bin:$PATH"
EOM

