<!DOCTYPE html>
<html xml:lang="${cmsfn.language()}" lang="${cmsfn.language()}">
  <head>
    [@cms.page /]
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>${content.windowTitle!content.title!}</title>
    <meta name="description" content="${content.description!""}" />
    <meta name="keywords" content="${content.keywords!""}" />

    [#-- To load resources you can link them manually (e.g. line below) --]
    <link rel="stylesheet" type="text/css" href="${ctx.contextPath}/.resources/fields/webresources/fields.css" media="all" /> 
  </head>
  <body class="fields-style ${cmsfn.language()}">

    <div class="container">
      <h1>${content.title!}</h1>
      [@cms.area name="main"/]
    </div>

    [#-- use resfn to load all js which matches the globbing pattern or link resources manually or via theme --]
    ${resfn.js(["/fields/.*js"])!}
  </body>
</html>
