[#assign aDateTime = .now]
[#assign results = restfn.call("wikipedia", "onThisDay", {"type":"all", "mm":aDateTime?string["MM"], "dd":aDateTime?string["dd"]}) ] 

<h2>What happened on ${aDateTime?string["MMMM"]} ${aDateTime?string["dd"]} in the past?</h2>

[#list results.get("selected").elements() as event]

<p>
  ${event.get("text").textValue()} (${event.get("year").intValue()?c}) 
</p>

[/#list]

<p>(Source: en.wikipedia.org)</p>