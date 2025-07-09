paste here
hi
hi
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Program Files\Python310\lib\threading.py", line 1009, in _bootstrap_inner
    self.run()
  File "C:\Program Files\Python310\lib\threading.py", line 946, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\core\management\commands\runserver.py", line 134, in inner_run
    self.check(display_num_errors=True)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\core\management\base.py", line 486, in check
    all_issues = checks.run_checks(
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\core\checks\registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\core\checks\urls.py", line 16, in check_url_config
    return check_resolver(resolver)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\core\checks\urls.py", line 26, in check_resolver
    return check_method()
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\urls\resolvers.py", line 531, in check
    for pattern in self.url_patterns:
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\urls\resolvers.py", line 718, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\urls\resolvers.py", line 711, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Program Files\Python310\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\Users\RIFAK\dev\datahub\eduacademy\eduacademy\urls.py", line 44, in <module>
    path('ai_course_dashboard/', include('ai_course_dashboard.urls'))
  File "C:\Users\RIFAK\dev\datahub\.venv\lib\site-packages\django\urls\conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
  File "C:\Program Files\Python310\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\Users\RIFAK\dev\datahub\eduacademy\ai_course_dashboard\urls.py", line 7, in <module>
    path('', views.index, name='ai_dashbaord_index'),
AttributeError: module 'ai_course_dashboard.views' has no attribute 'index'
