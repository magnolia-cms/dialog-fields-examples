<h2>JSON datasource fields section</h2>
[#if content.comboBoxFieldwithJSON?has_content]
  <p>${content.comboBoxFieldwithJSON!}</p>
[/#if]
[#if content.jsonLink?has_content]
  <p><a href="${content.jsonLink!}" target="_blank">${content.jsonLink!}!</a></p>
[/#if]