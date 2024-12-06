from random import randint
from time import strftime

from sqlalchemy import func  

from db.models import LastAction
from db.core import Session

def jaccard_index(str1: str, str2: str) -> float:
    a = set(str1.lower().split())
    b = set(str2.lower().split())
    intersection = a.intersection(b)
    union = a.union(b)
    ans = len(intersection) / len(union)
    return ans if ans else (randint(1,9) / randint(1,9))/1000

def addUserLastAction(userId: int, action: str):
    action = LastAction(userId=userId, actionName=action, date=strftime('%Y:%m:%d %H:%M:%S'))
    session = Session()
    session.add(action)
    session.commit()
    session.close()

def getNumberOfUsers() -> int:
    session = Session()
    users = session.query(func.count(func.distinct(LastAction.userId))).scalar()
    session.close()
    return users
