# -----------------------------------------------------------------------------------------
# This script copies all fields used in the docs from the definitions-from-the-docs folder
# to the light-modules/field-examples/dialogs/components folder.
#
# Usage:
# Run it from the bin folder (relative path variables at the start of the script).
# The command is:
#   python3 copy-fields-to-light-modules.py
#
# Note: It comments each field with a link to the respective docs page online.

relative_path_to_examples = "../examples/definitions-from-the-docs/"
relative_path_to_light_modules_dialogs_subfolder = "../../../light-modules/field-examples-copy/dialogs/components/"


# -----------------------------------------------------------------------------------------
# checkbox-radio-button.yaml

import os

data = data2 = data3 = "";

# Reading data from file1
with open(relative_path_to_examples + 'checkBoxField.yaml') as fp:
    data = fp.read()

# Reading data from file2
with open(relative_path_to_examples + 'checkBoxGroupField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open(relative_path_to_examples + 'radioButtonGroupField.yaml') as fp:
    data3 = fp.read()

# Merging 3 files
data = "# Start of the checkBoxField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Checkbox-field.html#_example_definition\n" + data
data += "\n# End of checkBoxField example in the docs"
data2 = "\n# Start of the checkBoxGroupField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Checkbox-group-field.html#_example_definition\n" + data2
data2 += "\n# End of checkBoxGroupField example in the docs"
data3 = "\n# Start of the radioButtonGroupField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Radio-button-group-field.html#_example_definition\n" + data3
data3 += "\n# End of radioButtonGroupField example in the docs"
data += data2
data += data3

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open(relative_path_to_light_modules_dialogs_subfolder + 'checkbox-radio-button.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")

# -----------------------------------------------------------------------------------------
# chooser-fields.yaml

import os

data = data2 = data3 = data4 = data5 = data6 = "";

# Reading data from file1
with open(relative_path_to_examples + 'linkField.yaml') as fp:
    data = fp.read()

# Reading data from file2
with open(relative_path_to_examples + 'damLinkField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open(relative_path_to_examples + 'External-link-or-page-link.yaml') as fp:
    data3 = fp.read()

# Reading data from file4
with open(relative_path_to_examples + 'uploadField.yaml') as fp:
    data4 = fp.read()

# Reading default value from the last line of External-link-or-page-link_defaultValue.yaml
with open(relative_path_to_examples + 'External-link-or-page-link_defaultValue.yaml', 'r') as f:
    data5 = f.readlines()[-1]

# Reading default value from the last line of damLinkField_defaultValue.yaml
with open(relative_path_to_examples + 'damLinkField_defaultValue.yaml', 'r') as f:
    data6 = f.readlines()[-1]

# Merging 4 files
data = "# Start of the linkField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data
data += "\n# End of linkField example in the docs"
data2 = "\n# Start of the damLinkField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data2 + "\n" + data6
data2 += "\n# End of damLinkField example in the docs"
data3 = "\n# Start of the External link example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data3 + "\n" + data5
data3 += "\n# End of External link example in the docs"
data4 = "\n# Start of the uploadField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Upload-field.html#_example_definition\n" + data4
data4 += "\n# End of uploadField example in the docs"
data += data2
data += data3
data += data4

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open(relative_path_to_light_modules_dialogs_subfolder + 'chooser-fields.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")

# -----------------------------------------------------------------------------------------
# dropdown-list.yaml

import os

data = data2 = data3 = data4 = data5 = "";

# Reading data from file1
with open(relative_path_to_examples + 'pageLinkField.yaml') as fp:
    data = fp.read()

# Reading data from file2
with open(relative_path_to_examples + 'resourceLinkField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open(relative_path_to_examples + 'comboBoxField.yaml') as fp:
    data3 = fp.read()

# Reading default value from the last line of resourceLinkField_defaultValue.yaml
with open(relative_path_to_examples + 'resourceLinkField_defaultValue.yaml', 'r') as f:
    data4 = f.readlines()[-1]

# Reading default value from the last line of pageLinkField_defaultValue.yaml
with open(relative_path_to_examples + 'pageLinkField_defaultValue.yaml', 'r') as f:
    data5 = f.readlines()[-1]

# Merging 3 files
data = "# Start of the pageLinkField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data + "\n" + data5
data += "\n# End of pageLinkField example in the docs"
data2 = "\n# Start of the resourceLinkField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data2 + "\n" + data4
data2 += "\n# End of resourceLinkField example in the docs"
data3 = "\n# Start of the comboBoxField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Combobox-field.html#_combobox_field\n" + data3
data3 += "\n# End of comboBoxField example in the docs"
data += data2
data += data3

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open(relative_path_to_light_modules_dialogs_subfolder + 'dropdown-list.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")

# -----------------------------------------------------------------------------------------
# grouping-fields.yaml

import os

data = data2 = data3 = data4 = "";

# Reading data from file1
with open(relative_path_to_examples + 'compositeField.yaml') as fp:
    data = fp.read()

# Reading data from file2
with open(relative_path_to_examples + 'jcrMultiValueField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open(relative_path_to_examples + 'jcrMultiLinkField.yaml') as fp:
    data3 = fp.read()

# Reading data from file4
with open(relative_path_to_examples + 'jcrMultiField.yaml') as fp:
    data4 = fp.read()

# Merging 4 files
data = "# Start of the compositeField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Composite-field.html#_composite_field\n" + data
data += "\n# End of compositeField example in the docs"
data2 = "\n# Start of the jcrMultiValueField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Multi-field.html#_example_definitions\n" + data2
data2 += "\n# End of jcrMultiValueField example in the docs"
data3 = "\n# Start of the jcrMultiLinkField examples in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Multi-field.html#_example_definitions\n" + data3
data3 += "\n# End of jcrMultiLinkField examples in the docs"
data4 = "\n# Start of the jcrMultiField examples in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Multi-field.html#_example_definitions\n" + data4
data4 += "\n# End of jcrMultiField example in the docs"
data += data2
data += data3
data += data4

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open(relative_path_to_light_modules_dialogs_subfolder + 'grouping-fields.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")

# -----------------------------------------------------------------------------------------
# json-fields.yaml

import os

data = data2 = "";
data3 = data4 = "";

# Reading data from file1
with open(relative_path_to_examples + 'jsonLinkField.yaml') as fp:
    data = fp.read()

# Reading data from file2
with open(relative_path_to_examples + 'jsonComboBoxField.yaml') as fp:
    data2 = fp.read()

# Reading default value from the last line of jsonComboBoxField_defaultValue.yaml
with open(relative_path_to_examples + 'jsonComboBoxField_defaultValue.yaml', 'r') as f:
    data3 = f.readlines()[-1]

# Reading default value from the last line of jsonLinkField_defaultValue.yaml
with open(relative_path_to_examples + 'jsonLinkField_defaultValue.yaml', 'r') as f:
    data4 = f.readlines()[-1]

# Merging 2 files
data = "# Start of the jsonLinkField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data + "\n" + data4
data += "\n# End of jsonLinkField example in the docs"
data2 = "\n# Start of the jsonComboBoxField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Combobox-field.html#_json_combobox_field\n" + data2 + "\n" + data3
data2 += "\n# End of jsonComboBoxField example in the docs"
data += data2

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open(relative_path_to_light_modules_dialogs_subfolder + 'json-fields.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")

# -----------------------------------------------------------------------------------------
# select-fields.yaml

import os

data = data2 = data3 = "";
 
# Reading data from file1
with open(relative_path_to_examples + 'listSelectField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open(relative_path_to_examples + 'twinColSelectField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open(relative_path_to_examples + 'tokenField.yaml') as fp:
    data3 = fp.read()
 
# Merging 3 files
data = "# Start of the listSelectField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/List-field.html#_example_definition\n" + data
data += "\n# End of listSelectField example in the docs"
data2 = "\n# Start of the twinColSelectField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Twin-column-field.html#_example_definition\n" + data2
data2 += "\n# End of twinColSelectField example in the docs"
data3 = "\n# Start of the tokenField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Token-field.html#_example_definition\n" + data3
data3 += "\n# End of tokenField example in the docs"
data += data2
data += data3

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open(relative_path_to_light_modules_dialogs_subfolder + 'select-fields.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")

# -----------------------------------------------------------------------------------------
# switchable-slider-picker.yaml

import os

data = data2 = data3 = "";
 
# Reading data from file1
with open(relative_path_to_examples + 'dateField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open(relative_path_to_examples + 'switchableField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open(relative_path_to_examples + 'sliderField.yaml') as fp:
    data3 = fp.read()
 
# Merging 3 files
data = "# Start of the dateField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Date-field.html#_example_definition\n" + data
data += "\n# End of dateField example in the docs"
data2 = "\n# Start of the switchableField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Switchable-field.html#_example_definition\n" + data2
data2 += "\n# End of switchableField example in the docs"
data3 = "\n# Start of the sliderField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Slider-field.html#_example_definition\n" + data3
data3 += "\n# End of sliderField example in the docs"
data += data2
data += data3

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open(relative_path_to_light_modules_dialogs_subfolder + 'switchable-slider-picker.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")

# -----------------------------------------------------------------------------------------
# text-fields.yaml

import os

data = data2 = data3 = data4 = data5 = data6 = data7 = "";
 
# Reading data from file1
with open(relative_path_to_examples + 'codeField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open(relative_path_to_examples + 'passwordField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open(relative_path_to_examples + 'richTextField.yaml') as fp:
    data3 = fp.read()

# Reading data from file4
with open(relative_path_to_examples + 'textField.yaml') as fp:
    data4 = fp.read()

# Reading data from file5
with open(relative_path_to_examples + 'emailValidator.yaml') as fp:
    data5 = fp.read()

# Reading data from file6
with open(relative_path_to_examples + 'hiddenField.yaml') as fp:
    data6 = fp.read()

# Reading data from file7
with open(relative_path_to_examples + 'staticField.yaml') as fp:
    data7 = fp.read()

# Merging 7 files
data = "# Start of the codeField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Code-field.html#_example_definition\n" + data
data += "\n# End of codeField example in the docs"
data2 = "\n# Start of the passwordField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Password-field.html#_example_definition\n" + data2
data2 += "\n# End of passwordField example in the docs"
data3 = "\n# Start of the richTextField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Rich-text-field.html#_example_definition\n" + data3
data3 += "\n# End of richTextField example in the docs"
data4 = "\n# Start of the textField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Text-field.html#_example_definition\n" + data4
data4 += "\n# End of textField example in the docs"
data5 = "\n# Start of the Email example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/Field-validators.html#_example_definition\n" + data5
data5 += "\n# End of Email example in the docs"
data6 = "\n# Start of the hiddenField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Hidden-field.html#_example_definition\n" + data6
data6 += "\n# End of hiddenField example in the docs"
data7 = "\n# Start of the staticField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Static-field.html#_example_definition\n" + data7
data7 += "\n# End of staticField example in the docs"
data += data2
data += data3
data += data4
data += data5
data += data6
data += data7

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open(relative_path_to_light_modules_dialogs_subfolder + 'text-fields.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")