odoo.define('html_codeview.html_codeview', function(require) {
"use strict";

var FieldHtml = require('web_editor.field.html');
var config = require('web.config');

FieldHtml.include({
     commitChanges: function () {
        if (this.mode === 'edit') {
            var layoutInfo = $.summernote.core.dom.makeLayoutInfo(this.wysiwyg.$editor);
            $.summernote.pluginEvents.codeview(undefined, undefined, layoutInfo, false);
        }
        return this._super();
    },
    _getWysiwygOptions: function () {
        return Object.assign({}, this.nodeOptions, {
            recordInfo: {
                context: this.record.getContext(this.recordParams),
                res_model: this.model,
                res_id: this.res_id,
            },
            noAttachment: this.nodeOptions['no-attachment'],
            inIframe: !!this.nodeOptions.cssEdit,
            iframeCssAssets: this.nodeOptions.cssEdit,
            snippets: this.nodeOptions.snippets,
            tabsize: 0,
            height: 180,
            generateOptions: function (options) {
                var para = _.find(options.toolbar, function (item) {
                    return item[0] === 'para';
                });
                if (para && para[1] && para[1].indexOf('checklist') === -1) {
                    para[1].splice(2, 0, 'checklist');
                }
//                if (config.isDebug()) {
                    options.codeview = true;
                    var view = _.find(options.toolbar, function (item) {
                        return item[0] === 'view';
                    });
                    if (view) {
                        if (!view[1].includes('codeview')) {
                            view[1].splice(-1, 0, 'codeview');
                        }
                    } else {
                        options.toolbar.splice(-1, 0, ['view', ['codeview']]);
                    }
//                }
                options.prettifyHtml = false;
                return options;
            },
        });
    },
});
});