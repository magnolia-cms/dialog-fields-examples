[#assign responseJSON = restfn.call("countries", "allCountries")]

<h2>Countries</h2>
<br/>

<br/>
[#list responseJSON.elements() as element]
<div style="margin:10px">
    <p>${element.get("name").official.textValue()}</p>
</div>
[/#list]