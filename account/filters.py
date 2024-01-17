from dj_rql.filter_cls import AutoRQLFilterClass
from account import models


class CurrentAccountFilters(AutoRQLFilterClass):
    MODEL = models.currentAccount
    FILTERS = (
        {"filter": "owner_id"},
        {"filter": "owner_name", "search": True}
    )