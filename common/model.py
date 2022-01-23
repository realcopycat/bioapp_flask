import datetime

from entrance.extensions import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class BaseModel(db.Model):
    __abstract__ = True

    # insert and update
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class CommonModel(BaseModel):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, onupdate=datetime.datetime.now, comment='更新时间')


class CurdModel(BaseModel):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, onupdate=datetime.datetime.now, comment='更新时间')
    delete_at = db.Column(db.DateTime, comment='删除时间')


Column = db.Column
Table = db.Table
relationship = relationship
ForeignKey = ForeignKey
backref = backref

TypeDecorator = db.TypeDecorator
INT = db.INT
CHAR = db.CHAR
VARCHAR = db.VARCHAR
NCHAR = db.NCHAR
NVARCHAR = db.NVARCHAR
TEXT = db.TEXT
Text = db.Text
FLOAT = db.FLOAT
NUMERIC = db.NUMERIC
REAL = db.REAL
DECIMAL = db.DECIMAL
TIMESTAMP = db.TIMESTAMP
DATETIME = db.DATETIME
CLOB = db.CLOB
BLOB = db.BLOB
BINARY = db.BINARY
VARBINARY = db.VARBINARY
BOOLEAN = db.BOOLEAN
BIGINT = db.BIGINT
SMALLINT = db.SMALLINT
INTEGER = db.INTEGER
DATE = db.DATE
TIME = db.TIME
TupleType = db.TupleType
String = db.String
Integer = db.Integer
SmallInteger = db.SmallInteger
BigInteger = db.BigInteger
Numeric = db.Numeric
Float = db.Float
DateTime = db.DateTime
Date = db.Date
Time = db.Time
LargeBinary = db.LargeBinary
Boolean = db.Boolean
Unicode = db.Unicode
UnicodeText = db.UnicodeText
PickleType = db.PickleType
Interval = db.Interval
Enum = db.Enum
ARRAY = db.ARRAY
JSON = db.JSON

SQLAlchemyAutoSchema = SQLAlchemyAutoSchema
