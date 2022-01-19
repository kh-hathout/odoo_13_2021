odoo.define('hsp.no_quick_relational_fields', function (require) {
"use strict";

/**
 * Relational Fields
 *
 * In this file, we have a collection of various relational field widgets.
 * Relational field widgets are more difficult to use/manipulate, because the
 * relations add a level of complexity: a value is not a basic type, it can be
 * a collection of other records.
 *
 * Also, the way relational fields are edited is more complex.  We can change
 * the corresponding record(s), or alter some of their fields.
 */

var RelationalFields = require('web.relational_fields');


RelationalFields.FieldMany2One.include({
   

    /**
     * @override
     * @param {boolean} [options.noOpen=false] if true, there is no external
     *   button to open the related record in a dialog
     */
    init: function (parent, name, record, options) {
        this._super.apply(this, arguments);

        this.nodeOptions.no_quick_create = true
    },

});

// return {
//     FieldMany2One: FieldMany2One,
// };

});
