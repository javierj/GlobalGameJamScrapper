__author__ = 'Javier'

from databaseutils import InsertDatosFromTextFile, SQLiteDatabase, File

process = InsertDatosFromTextFile(SQLiteDatabase(), File())
process.insert()

print "Ok."
