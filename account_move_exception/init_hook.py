# Copyright 2021 ForgeFlow S.L.
#   (http://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import logging

logger = logging.getLogger(__name__)


def pre_init_hook(cr):
    """
    The objective of this hook is to speed up the installation
    of the module on an existing Odoo instance.
    """
    store_exception_fields(cr)


def store_exception_fields(cr):

    cr.execute(
        """SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_move' AND
    column_name='main_exception_id'"""
    )
    if not cr.fetchone():
        logger.info("Creating field main_exception_id on account_move")
        cr.execute(
            """
            ALTER TABLE account_move ADD COLUMN main_exception_id int;
            COMMENT ON COLUMN account_move.main_exception_id IS
            'Main Exception';
            """
        )

    cr.execute(
        """SELECT column_name
    FROM information_schema.columns
    WHERE table_name='account_move' AND
    column_name='exceptions_summary'"""
    )
    if not cr.fetchone():
        logger.info("Creating field exceptions_summary on account_move")
        cr.execute(
            """
            ALTER TABLE account_move ADD COLUMN exceptions_summary text;
            COMMENT ON COLUMN account_move.exceptions_summary IS
            'Exceptions Summary';
            """
        )
