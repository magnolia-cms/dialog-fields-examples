# -----------------------------------------------------------------------------------------
# This script copies all fields used in the docs from the definitions-from-the-docs folder
# to the light-modules/field-examples/dialogs/components folder.
#
# Usage:
# Run it in the definitions-from-the-docs folder
# The command is:
#   python3 sync-includes-to-light-modules.py
#
# Note: It comments each field with a link to the respective docs page online.


# -----------------------------------------------------------------------------------------
# checkbox-radio-button.yaml

import os

data = data2 = data3 = "";
 
# Reading data from file1
with open('checkBoxField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open('checkBoxGroupField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open('radioButtonGroupField.yaml') as fp:
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

with open('combined-fields.yaml') as infile, open('../../../../light-modules/field-examples/dialogs/components/checkbox-radio-button.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")

# -----------------------------------------------------------------------------------------
# chooser-fields.yaml

import os

data = data2 = data3 = data4 = "";
 
# Reading data from file1
with open('linkField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open('damLinkField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open('External-link-or-page-link.yaml') as fp:
    data3 = fp.read()

# Reading data from file4
with open('uploadField.yaml') as fp:
    data4 = fp.read()
 
# Merging 4 files
data = "# Start of the linkField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data
data += "\n# End of linkField example in the docs"
data2 = "\n# Start of the damLinkField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data2
data2 += "\n# End of damLinkField example in the docs"
data3 = "\n# Start of the External link example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data3
data3 += "\n# End of External link example in the docs"
data4 = "\n# Start of the uploadField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Upload-field.html#_example_definition\n" + data4 
data4 += "\n# End of uploadField example in the docs"
data += data2
data += data3
data += data4

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open('../../../../light-modules/field-examples/dialogs/components/chooser-fields.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")

# -----------------------------------------------------------------------------------------
# dropdown-list.yaml

import os

data = data2 = data3 = "";
 
# Reading data from file1
with open('pageLinkField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open('resourceLinkField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open('comboBoxField.yaml') as fp:
    data3 = fp.read()
 
# Merging 3 files
data = "# Start of the pageLinkField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data
data += "\n# End of pageLinkField example in the docs"
data2 = "\n# Start of the resourceLinkField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data2
data2 += "\n# End of resourceLinkField example in the docs"
data3 = "\n# Start of the comboBoxField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Combobox-field.html#_combobox_field\n" + data3
data3 += "\n# End of comboBoxField example in the docs"
data += data2
data += data3

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open('../../../../light-modules/field-examples/dialogs/components/dropdown-list.yaml', 'w') as outfile:
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
with open('compositeField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open('jcrMultiValueField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open('jcrMultiLinkField.yaml') as fp:
    data3 = fp.read()

# Reading data from file4
with open('jcrMultiField.yaml') as fp:
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

with open('combined-fields.yaml') as infile, open('../../../../light-modules/field-examples/dialogs/components/grouping-fields.yaml', 'w') as outfile:
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
 
# Reading data from file1
with open('jsonLinkField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open('jsonComboBoxField.yaml') as fp:
    data2 = fp.read()
 
# Merging 2 files
data = "# Start of the jsonLinkField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Link-field.html#_example_definitions\n" + data
data += "\n# End of jsonLinkField example in the docs"
data2 = "\n# Start of the jsonComboBoxField example in the docs\n# https://docs.magnolia-cms.com/product-docs/6.2/Developing/Templating/Dialog-definition/Field-definition/List-of-fields/Combobox-field.html#_json_combobox_field\n" + data2
data2 += "\n# End of jsonComboBoxField example in the docs"
data += data2

with open ('combined-fields.yaml', 'w') as fp:
    fp.write(data)

with open('combined-fields.yaml') as infile, open('../../../../light-modules/field-examples/dialogs/components/json-fields.yaml', 'w') as outfile:
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
with open('listSelectField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open('twinColSelectField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open('tokenField.yaml') as fp:
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

with open('combined-fields.yaml') as infile, open('../../../../light-modules/field-examples/dialogs/components/select-fields.yaml', 'w') as outfile:
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
with open('dateField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open('switchableField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open('sliderField.yaml') as fp:
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

with open('combined-fields.yaml') as infile, open('../../../../light-modules/field-examples/dialogs/components/switchable-slider-picker.yaml', 'w') as outfile:
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
with open('codeField.yaml') as fp:
    data = fp.read()
 
# Reading data from file2
with open('passwordField.yaml') as fp:
    data2 = fp.read()

# Reading data from file3
with open('richTextField.yaml') as fp:
    data3 = fp.read()

# Reading data from file4
with open('textField.yaml') as fp:
    data4 = fp.read()

# Reading data from file5
with open('emailValidator.yaml') as fp:
    data5 = fp.read()

# Reading data from file6
with open('hiddenField.yaml') as fp:
    data6 = fp.read()

# Reading data from file7
with open('staticField.yaml') as fp:
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

with open('combined-fields.yaml') as infile, open('../../../../light-modules/field-examples/dialogs/components/text-fields.yaml', 'w') as outfile:
    print('form:', file=outfile)
    print('  properties:', file=outfile)
    print('    populate: false', file=outfile)
    for line in infile:
        print('    ' + line, end='', file=outfile)

os.remove("combined-fields.yaml")