#!/bin/bash

papermill try_papermill.ipynb output.ipynb \
          --request-save-on-cell-execute --prepare-execute \
          -p alpha 1 \
          -p beta 7 \
          -p gamma 10 \
          -p delta 25 \
          -p epsilon 3