<h2>Default values for dropdown lists</h2>
<ul>
[#if content.pageLink?has_content]
  <li>External link or page link: <i>${content.pageLink!}</i></li>
[/#if]
[#if content.resourceLink?has_content]
  <li>Resource link: <i>${content.resourceLink!}</i></li>
[/#if]
</ul>