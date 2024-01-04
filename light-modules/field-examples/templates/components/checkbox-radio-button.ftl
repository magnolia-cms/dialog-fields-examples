[#if content.checkbox?has_content]
  [#assign checkbox_value = content.checkbox?string('yes', 'no')]
  <h2>Checkboxes and radio buttons section</h2>
  <p>Show title checkbox value: ${checkbox_value}</p>
[/#if]
