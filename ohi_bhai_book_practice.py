# #while loop example
# jalani=3
#
# while jalani>0:
#     print("trine cholche",jalani)
#     jalani=jalani-1
# print("jalani sesh hoye gelo",jalani)
#
#
# #function example
#
# def salam_janao(name):
#     print("Assalamu Alaikum",name)
#
#
# salam_janao("John")
# salam_janao("Jan")

#first fastapi example
# to run this code, use the command: uvicorn ohi_bhai_book_practice:app --reload
from fastapi import FastAPI
app = FastAPI()

train_talika = [
{"id": 1, "naam": "Ekota Express", "gontobbo":"Dhaka"},
{"id": 2, "naam": "Turna Nishitha", "gontobbo":"Chittagong"},
]
@app.get("/trains")
def sob_train():
       return train_talika
@app.get("/trains/{train_id}")
def ekta_train(train_id: int):
    for train in train_talika:
        if train["id"] == train_id:
                    return train
    return {"vul": "Train পাওয়া যায়ـন"}