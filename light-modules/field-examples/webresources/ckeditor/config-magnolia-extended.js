var VAADIN_DIR_URL = typeof CKEDITOR.vaadinDirUrl !== 'undefined'? CKEDITOR.vaadinDirUrl : "../../../";
 
// Loads magnoliaFileBrowser replacing CKEditor file browser. This is added to the custom config below at config.extraPlugins
CKEDITOR.plugins.addExternal('magnoliaFileBrowser', VAADIN_DIR_URL + 'js/filebrowser/');
 
CKEDITOR.editorConfig = function( config ) {
 
   // MIRROR info.magnolia.ui.field.RichTextFieldDefinition
 definition = {
   alignment: false,
   images: false,
   lists: true,
 source: false,
   tables: false,
 
   colors: null,
   fonts: null,
   fontSizes: null
 }
 
 // MIRROR info.magnolia.ui.field.RichTextFieldDefinition
 removePlugins = [];
 
 // magnolialink AND REMOVAL OF elementspath FROM DEFAULT RICH TEXT FIELD FACTORY
 removePlugins.push("elementspath");
 removePlugins.push("filebrowser");
 config.removePlugins = removePlugins.join(",");
 config.extraPlugins = "magnolialink,magnoliaexpand,magnoliaFileBrowser";
 
 config.baseFloatZIndex = 150;
 config.resize_enabled = false;
 config.toolbar = "Magnolia";
 config.toolbar_Magnolia = [
   {name: "basicstyles", items: ["Bold", "Italic", "Underline", "SpecialChar"] },
   {name: "paragraph",   items: ["NumberedList", "BulletedList", "JustifyLeft", "JustifyCenter", "JustifyRight", "JustifyBlock", "Image", "Table" ]},
   {name: "links",     items: [ "Link", "InternalLink", "DamLink", "Unlink"]},
   {name: "styles",    items: ["Font", "FontSize", "TextColor", "ColorButton"]},
   {name: "clipboard", items: ["Cut", "Copy", "Paste", "PasteText", "PasteFromWord"]},
   {name: "undo",      items: [ "Undo", "Redo" ] },
   {name: "tools",     items: [ "Source" ] },
   {name: "view",      items: [ "Expand" ] }
 ];
 config.specialChars = [
    ['&trade;','Trade mark'],
    ['&nbsp;','NB Space'],
    ['&#9660;','PV Triangle']]; 
};