from ssql.tests.resources.core import execute, unknownTypeRet

execute("select * from employee where dept = $1", unknownTypeRet())
