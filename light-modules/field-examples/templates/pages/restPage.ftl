<!DOCTYPE html>
<html xml:lang="${cmsfn.language()}" lang="${cmsfn.language()}">
  <head>
    [@cms.page /]
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>${content.windowTitle!content.title!}</title>
    <meta name="description" content="${content.description!""}" />
    <meta name="keywords" content="${content.keywords!""}" />

  </head>
  <body class="restPage ${cmsfn.language()}">

    <div class="container">
      <h1>REST examples</h1>
      <h2>Test links</h2>
      <ul>
        <li><a href="http://api.nobelprize.org/2.0//nobelPrizes" target="_blank">http://api.nobelprize.org/2.0//nobelPrizes</a></li>
        <li><a href="https://en.wikipedia.org/api/rest_v1/?spec" target="_blank">https://en.wikipedia.org/api/rest_v1/?spec</a></li>
      </ul>
      [@cms.area name="main"/]
    </div>

  </body>
</html>
