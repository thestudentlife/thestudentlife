/**
 * @license Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function (config) {
    // Toolbar configuration generated automatically by the editor based on config.toolbarGroups.
    config.toolbar = [
        {name: 'insert', items: ['Image', 'Link', 'Iframe']},
        {name: 'font', items: ['Bold', 'Italic']},
        {name: 'styles', items: [ 'Styles', 'Format', 'Font', 'FontSize' ] },
        {name: 'operation', items: ['Undo', 'Redo']},
        {name: 'document', items:['Source']}
    ];

    config.uiColor = '#ffffff';
    config.width = 1000;
    config.height = 300;
};
