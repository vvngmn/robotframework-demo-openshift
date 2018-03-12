This is a simple demo for command line usage
```
$ pybot -V resource.py oc_test.txt 
==============================================================================
Oc Test :: This suite cover all oc login and projects related cases           
==============================================================================
case1 - scenario login and projects                                   Login successful.

You don't have any projects. You can try to create a new project, by running

    oc new-project <projectname>

case1 - scenario login and projects                                   | PASS |
------------------------------------------------------------------------------
Oc Test :: This suite cover all oc login and projects related cases   | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output:  /home/xiaocwan/test_robotframework/output.xml
Log:     /home/xiaocwan/test_robotframework/log.html
Report:  /home/xiaocwan/test_robotframework/report.html

```


By default the -L (debug level) is INFO, the print and return from lib func are printed to log.html
