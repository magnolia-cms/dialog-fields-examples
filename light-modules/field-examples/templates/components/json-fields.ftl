<h2>JSON datasource default field values</h2>
<ul>
[#if content.comboBoxFieldwithJSON?has_content]
  <li>Country: <i>${content.comboBoxFieldwithJSON!}</i></li>
[/#if]
[#if content.jsonLink?has_content]
  <li>Google maps link: <a href="${content.jsonLink!}" target="_blank">${content.jsonLink!}</a></li>
[/#if]
</ul>