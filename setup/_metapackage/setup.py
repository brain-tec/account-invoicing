import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-account-invoicing",
    description="Meta package for oca-account-invoicing Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_invoice_blocking>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_change_currency>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_check_total>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_currency_taxes>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_fiscal_position_update>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_fixed_discount>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_force_number>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_mass_sending>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_merge>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_pricelist>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_pricelist_sale>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_refund_line_selection>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_refund_link>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_section_sale_order>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_show_currency_rate>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_supplier_ref_unique>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_supplierinfo_update>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_supplierinfo_update_discount>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_tax_required>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_transmit_method>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_tree_currency>=16.0dev,<16.1dev',
        'odoo-addon-account_invoice_triple_discount>=16.0dev,<16.1dev',
        'odoo-addon-account_menu_invoice_refund>=16.0dev,<16.1dev',
        'odoo-addon-account_move_tier_validation>=16.0dev,<16.1dev',
        'odoo-addon-account_receipt_journal>=16.0dev,<16.1dev',
        'odoo-addon-account_receipt_send>=16.0dev,<16.1dev',
        'odoo-addon-account_tax_change>=16.0dev,<16.1dev',
        'odoo-addon-account_tax_group_widget_base_amount>=16.0dev,<16.1dev',
        'odoo-addon-partner_invoicing_mode>=16.0dev,<16.1dev',
        'odoo-addon-partner_invoicing_mode_at_shipping>=16.0dev,<16.1dev',
        'odoo-addon-partner_invoicing_mode_monthly>=16.0dev,<16.1dev',
        'odoo-addon-purchase_stock_picking_return_invoicing>=16.0dev,<16.1dev',
        'odoo-addon-sale_line_refund_to_invoice_qty>=16.0dev,<16.1dev',
        'odoo-addon-sale_order_invoicing_grouping_criteria>=16.0dev,<16.1dev',
        'odoo-addon-stock_picking_return_refund_option>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
