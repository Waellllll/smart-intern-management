from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import re
app=FastAPI(title="Smart Internship AI")
class Student(BaseModel): fullName:str; skills:str=""; preferredDomain:str=""; experienceMonths:int|str=0
class Offer(BaseModel): id:int; title:str; company:str; domain:str=""; requiredSkills:str=""; location:str=""
class Request(BaseModel): student:Student; offers:List[Offer]
def tok(x): return {s.lower().strip() for s in re.split(r"[,;\s]+",x or "") if s.strip()}
@app.get("/health")
def health(): return {"status":"UP"}
@app.post("/recommend")
def recommend(x:Request):
    ss=tok(x.student.skills); pref=x.student.preferredDomain.lower().strip(); out=[]
    for o in x.offers:
        req=tok(o.requiredSkills); matched=sorted(ss & req); skill=(len(matched)/len(req)*70) if req else 0; domain=30 if pref and o.domain.lower().strip()==pref else 0; score=min(100,round(skill+domain)); reason=f"{len(matched)} required skill(s) matched" + (f"; matched: {', '.join(matched)}" if matched else "") + ("; preferred domain matches." if domain else ".")
        out.append({"offerId":o.id,"title":o.title,"company":o.company,"domain":o.domain,"location":o.location,"score":score,"reason":reason})
    return sorted(out,key=lambda z:z["score"],reverse=True)
