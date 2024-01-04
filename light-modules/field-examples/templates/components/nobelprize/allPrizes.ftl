[#assign customValues = {"sort": "asc","nobelPrizeYear": "2000"} /]
[#assign prizes = restfn.call("nobelprize", "allPrizes", customValues)]

<h2>Categories and laureates in 2000</h2>
<br/>


[#list prizes.nobelPrizes.elements() as prize]
<div style="margin:10px">
    <ul>
    <li>${prize.categoryFullName.en.textValue()}</li>
        <ul>
        [#list prize.laureates.elements() as winner]
        <li>${winner.knownName.en.textValue()}</li>
        [/#list]
        </ul>
    </ul>
</div>
[/#list]
