odoo.define("init_one2many_row_number_tree_view", function (require) {
  "use strict";
  var Pager = require("web.Pager");

  return Pager.include({
    _render: function () {
      this.options.single_page_hidden = false;
      this._super();
    },
  });
});
