# kitob='yaxshi ko\'rgan kitobizni kirgizing  chiqmoqchi bo\'lsangiz "exit"ni bosing:'
# qiymat=''
# while True:
#  qiymat=input(kitob)
#  if qiymat!='exit':
#   break
# print('rahmat')

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     age = int(qiymat)
    
#     if age<7:
#         narh = 2000
#     elif 7<=age<18:
#         narh = 3000
#     elif 18<=age<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit'.lower():
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")

print('Dastur tugadi')