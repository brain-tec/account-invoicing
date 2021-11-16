[![Runbot Status](https://runbot.odoo-community.org/runbot/badge/flat/95/14.0.svg)](https://runbot.odoo-community.org/runbot/repo/github-com-oca-account-invoicing-95)
[![Build Status](https://travis-ci.com/OCA/account-invoicing.svg?branch=14.0)](https://travis-ci.com/OCA/account-invoicing)
[![codecov](https://codecov.io/gh/OCA/account-invoicing/branch/14.0/graph/badge.svg)](https://codecov.io/gh/OCA/account-invoicing)
[![Translation Status](https://translation.odoo-community.org/widgets/account-invoicing-14-0/-/svg-badge.svg)](https://translation.odoo-community.org/engage/account-invoicing-14-0/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# account-invoicing

TODO: add repo description.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[account_billing](account_billing/) | 14.0.1.0.1 | [![Saran440](https://github.com/Saran440.png?size=30px)](https://github.com/Saran440) | Group invoice as billing before payment
[account_invoice_base_invoicing_mode](account_invoice_base_invoicing_mode/) | 14.0.1.1.0 |  | Base module for handling multiple invoicing mode
[account_invoice_check_total](account_invoice_check_total/) | 14.0.1.0.1 |  | Check if the verification total is equal to the bill's total
[account_invoice_date_due](account_invoice_date_due/) | 14.0.1.0.1 | [![luisg123v](https://github.com/luisg123v.png?size=30px)](https://github.com/luisg123v) [![joao-p-marques](https://github.com/joao-p-marques.png?size=30px)](https://github.com/joao-p-marques) | Update Invoice's Due Date
[account_invoice_force_number](account_invoice_force_number/) | 14.0.1.0.0 |  | Allows to force invoice numbering on specific invoices
[account_invoice_mode_at_shipping](account_invoice_mode_at_shipping/) | 14.0.1.1.0 |  | Create invoices automatically when goods are shipped.
[account_invoice_mode_monthly](account_invoice_mode_monthly/) | 14.0.1.1.0 |  | Create invoices automatically on a monthly basis.
[account_invoice_mode_weekly](account_invoice_mode_weekly/) | 14.0.1.1.0 |  | Create invoices automatically on a weekly basis.
[account_invoice_payment_retention](account_invoice_payment_retention/) | 14.0.1.0.0 |  | Account Invoice Payment Retention
[account_invoice_refund_link](account_invoice_refund_link/) | 14.0.1.0.0 |  | Show links between refunds and their originator invoices
[account_invoice_restrict_linked_so](account_invoice_restrict_linked_so/) | 14.0.1.0.1 |  | Restricts editing the Product, Quantity and Unit Price columns for invoice lines that originated in Sales Orders.
[account_invoice_search_by_reference](account_invoice_search_by_reference/) | 14.0.1.0.0 |  | Account invoice search by reference
[account_invoice_section_sale_order](account_invoice_section_sale_order/) | 14.0.1.0.1 |  | For invoices targetting multiple sale order addsections with sale order name.
[account_invoice_supplier_ref_unique](account_invoice_supplier_ref_unique/) | 14.0.1.0.0 |  | Checks that supplier invoices are not entered twice
[account_invoice_tax_required](account_invoice_tax_required/) | 14.0.1.0.0 |  | This module adds functional a check on invoice to force user to set tax on invoice line.
[account_invoice_transmit_method](account_invoice_transmit_method/) | 14.0.1.0.1 | [![alexis-via](https://github.com/alexis-via.png?size=30px)](https://github.com/alexis-via) | Configure invoice transmit method (email, post, portal, ...)
[account_invoice_tree_currency](account_invoice_tree_currency/) | 14.0.1.0.0 |  | Show currencies in the invoice tree view
[account_invoice_triple_discount](account_invoice_triple_discount/) | 14.0.1.1.0 |  | Manage triple discount on invoice lines
[account_move_original_partner](account_move_original_partner/) | 14.0.1.0.0 |  | Display original customers when creating invoices from multiple sale orders.
[account_move_tier_validation](account_move_tier_validation/) | 14.0.1.0.1 |  | Extends the functionality of Account Moves to support a tier validation process.
[product_supplierinfo_for_customer_invoice](product_supplierinfo_for_customer_invoice/) | 14.0.1.0.0 |  | Based on product_customer_code, this module loads in every account invoice the customer code defined in the product
[purchase_stock_picking_return_invoicing](purchase_stock_picking_return_invoicing/) | 14.0.1.1.0 | [![pedrobaeza](https://github.com/pedrobaeza.png?size=30px)](https://github.com/pedrobaeza) [![MiquelRForgeFlow](https://github.com/MiquelRForgeFlow.png?size=30px)](https://github.com/MiquelRForgeFlow) | Add an option to refund returned pickings
[sale_order_invoicing_grouping_criteria](sale_order_invoicing_grouping_criteria/) | 14.0.1.0.0 | [![pedrobaeza](https://github.com/pedrobaeza.png?size=30px)](https://github.com/pedrobaeza) | Sales order invoicing grouping criteria
[stock_picking_invoicing](stock_picking_invoicing/) | 14.0.1.0.0 |  | Stock Picking Invoicing

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to OCA
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----

OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.
