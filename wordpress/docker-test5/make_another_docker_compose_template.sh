#!/bin/bash

# Prompt the user to enter a template number
echo -n "Enter template number: "
read template_number

# Print the template number
echo "Template number: $template_number"

tempfile="docker_compose_template"
# cat $tempfile
cat $tempfile | sed 's/db1/db2/g'
# cat $tempfile | sed 's/db1/db'$template_number'/g' | sed 's/redis1/redis'$template_number'/g' | sed 's/wordpress1/wordpress'$template_number'/g'
