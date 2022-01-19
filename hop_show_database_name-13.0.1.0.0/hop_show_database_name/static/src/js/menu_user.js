odoo.define('hop_show_database_name.UserMenu', function (require) {
    "use strict";
        
    var um = require('web.UserMenu');
    um.include({
       start: function () {
           var self = this;
           var session = this.getSession();
           return this._super.apply(this, arguments).then(function () {
    
              var tbar_name = session.name;
              tbar_name = _.str.sprintf("%s (%s)", tbar_name, session.db);
              self.$('.oe_topbar_name').text(tbar_name);
            });
           },
    
    });
});
    