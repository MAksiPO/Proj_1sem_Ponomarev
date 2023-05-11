from collections.abc import Sequence
from typing import NewType


SQLAbstractQuery = NewType('SQLAbstractQuery', str)

SQLUpdateQuery = NewType('SQLUpdateQuery', SQLAbstractQuery)
SQLUpdateQuerySequence = NewType('SQLUpdateQuerySequence', Sequence)

SQLSelectQuery = NewType('SQLSelectQuery', SQLAbstractQuery)
SQLSelectQuerySequence = NewType('SQLSelectQuerySequence', Sequence)

SQLDeleteQuery = NewType('SQLDeleteQuery', SQLAbstractQuery)
SQLDeleteQuerySequence = NewType('SQLDeleteQuerySequence', Sequence)
