#!/bin/bash

FUNCTION_RESULT=`./_fsnav_cmdline_controller.py apps $@`
cd ${FUNCTION_RESULT}