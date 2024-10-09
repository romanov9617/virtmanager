"""Module describes monitor.

Monitor is an object
that monitors every machine characteristics.

Monitor is responsible for making select queries in database
which can be used for machine efficiency, condition of machine and etc.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.database.base import DatabaseBase
from src.exceptions import database as custom_exceptions

if TYPE_CHECKING:
    from src.config import Settings


class Monitor(DatabaseBase):
    """Monitor class.

    It is needed for monitoring database.

    Methods:
        get_all_machine_by_enable_status(self) - get all machines
        that are enabled at the moment.
    """

    def __init__(self, config: Settings | None = None) -> None:
        """Initialize monitor.

        Monitor is responsible for making select queries in database
        which can be used for machine efficiency, condition of machine and etc.

        Args:
            config (Settings | None, optional): Settings object. Defaults to None.

        Raises:
            custom_exceptions.QueryPathDoesNotProvidedError: Exception raised when
            path to folder with queries is not provided.
        """
        super().__init__(config)
        self.base_path_to_query = "src/database/analysis_queries/"
        if not self.base_path_to_query:
            raise custom_exceptions.QueryPathDoesNotProvidedError
