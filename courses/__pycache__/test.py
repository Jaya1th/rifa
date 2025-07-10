paste here
hi
hi
Internal Server Error: /ai_course_dashboard/
Traceback (most recent call last):
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 103, in _execute
    return self.cursor.execute(sql)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\mysql\base.py", line 76, in execute
    return self.cursor.execute(query, args)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\cursors.py", line 179, in execute
    res = self._query(mogrified_query)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\cursors.py", line 330, in _query
    db.query(q)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\connections.py", line 261, in query
    _mysql.connection.query(self, query)
MySQLdb.ProgrammingError: (1146, "Table 'edu_academy.trainingdatahub_employeeheadcountreportdetails' doesn't exist")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\core\handlers\base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\RIFAK\dev\datahub\eduacademy\ai_course_dashboard\views.py", line 22, in ai_course_dashboard
    cursor.execute("""
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\debug_toolbar\panels\sql\tracking.py", line 235, in execute
    return self._record(super().execute, sql, params)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\debug_toolbar\panels\sql\tracking.py", line 160, in _record
    return method(sql, params)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 122, in execute
    return super().execute(sql, params)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 79, in execute
    return self._execute_with_wrappers(
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 92, in _execute_with_wrappers     
    return executor(sql, params, many, context)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 103, in _execute
    return self.cursor.execute(sql)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\mysql\base.py", line 76, in execute
    return self.cursor.execute(query, args)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\cursors.py", line 179, in execute
    res = self._query(mogrified_query)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\cursors.py", line 330, in _query
    db.query(q)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\connections.py", line 261, in query
    _mysql.connection.query(self, query)
django.db.utils.ProgrammingError: (1146, "Table 'edu_academy.trainingdatahub_employeeheadcountreportdetails' doesn't exist")    
[10/Jul/2025 10:17:04] "GET /ai_course_dashboard/ HTTP/1.1" 500 172436
Internal Server Error: /ai_course_dashboard/
Traceback (most recent call last):
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 103, in _execute
    return self.cursor.execute(sql)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\mysql\base.py", line 76, in execute
    return self.cursor.execute(query, args)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\cursors.py", line 179, in execute
    res = self._query(mogrified_query)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\cursors.py", line 330, in _query
    db.query(q)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\connections.py", line 261, in query
    _mysql.connection.query(self, query)
MySQLdb.ProgrammingError: (1146, "Table 'edu_academy.trainingdatahub_employeeheadcountreportdetails' doesn't exist")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\core\handlers\base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\Users\RIFAK\dev\datahub\eduacademy\ai_course_dashboard\views.py", line 22, in ai_course_dashboard
    cursor.execute("""
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\debug_toolbar\panels\sql\tracking.py", line 235, in execute
    return self._record(super().execute, sql, params)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\debug_toolbar\panels\sql\tracking.py", line 160, in _record
    return method(sql, params)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 122, in execute
    return super().execute(sql, params)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 79, in execute
    return self._execute_with_wrappers(
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 92, in _execute_with_wrappers     
    return executor(sql, params, many, context)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\utils.py", line 103, in _execute
    return self.cursor.execute(sql)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\db\backends\mysql\base.py", line 76, in execute
    return self.cursor.execute(query, args)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\cursors.py", line 179, in execute
    res = self._query(mogrified_query)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\cursors.py", line 330, in _query
    db.query(q)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\MySQLdb\connections.py", line 261, in query
    _mysql.connection.query(self, query)
django.db.utils.ProgrammingError: (1146, "Table 'edu_academy.trainingdatahub_employeeheadcountreportdetails' doesn't exist")    
[10/Jul/2025 10:27:04] "GET /ai_course_dashboard/ HTTP/1.1" 500 172434
