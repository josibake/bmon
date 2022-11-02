import decimal
import json
import cProfile
import time
import pstats

from django.db import models
from django.db.models.sql.query import Query

from . import server_tasks


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


def json_dumps(*args, **kwargs):
    """Handles serialization of decimals."""
    kwargs.setdefault('cls', DecimalEncoder)
    return json.dumps(*args, **kwargs)


json_loads = json.loads


def print_sql(q: models.QuerySet | Query):
    from pygments import highlight
    from pygments.formatters import TerminalFormatter
    from pygments.lexers import PostgresLexer
    from sqlparse import format

    """Prettyprint a Django queryset."""
    if hasattr(q, 'q'):
        q = q.query  # type: ignore
    formatted = format(str(q), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))


def profile(cmd):
    cProfile.run(cmd, 'stats')
    p = pstats.Stats('stats')
    p.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats(30)


def exec_tasks(n, huey_instance):
    for _ in range(n):
        t = time.time()
        task = huey_instance.dequeue()
        print("executing task %s" % task)
        assert task
        task.execute()
        print("  took %s" % (time.time() - t))


def exec_mempool_tasks(n):
    return exec_tasks(n, server_tasks.mempool_q)
