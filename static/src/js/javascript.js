odoo.define('moldeo_interactive_custom.javascript', function (require) {
    'use strict';

    console.log('Moldeo Interactive Custom Module Loaded');
    var AbstractAction = require('web.AbstractAction');
    // Odoo class to calling an url with jsonRpc
    // It allows to communicate the Odoo frontend and backend using the Python controllers
    var ajax = require('web.ajax');

    var result = [];
    console.log('Moldeo Interactive Custom Javascript Search Data Started');
    // Call URL (Odoo Controller route) /get_products with jsonRpc
    ajax.jsonRpc("/get_products", 'call', {}, {
        'async': false
    }).then(function (data) {
        result.push(data);
    });
    console.log(result);
    console.log('Moldeo Interactive Custom Javascript Data showed');
    
});

