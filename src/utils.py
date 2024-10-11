"""Utils module."""

from __future__ import annotations

from typing import TYPE_CHECKING

import prettytable

if TYPE_CHECKING:
    from asyncpg import Record


def make_table(data: list[Record]) -> prettytable.PrettyTable:
    """Generate beautiful table from list of asyn.

    Args:
        data (list): _description_

    Returns:
        prettytable.PrettyTable: _description_
    """
    table = prettytable.PrettyTable()
    if not data:
        return table
    table.field_names = data[0].keys()
    table.add_rows(data)
    return table
