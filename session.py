# 리스트는 순서대로 차곡차곡
# 파이썬은 띄어쓰기 개중요
#item_list=["지원","동길","교현","민서","해윤"]

#a=item_list[2]

#item_list[0]="명준"
#print(item_list)

#리스트메소드
#item_list.append("영권")
#print(item_list)

#딕셔너리 순서 X 키로 접근
#item_dic={"key1":111,"key2":222}

#item_dic["key1"]=222
#item_dic["key3"]=333

#print(item_dic)

#쌍이 묶여서 
#dic_items = item_dic.items()
#print(dic_items)


#반복문은 조건문이랑 함께함니당

# item_list=["지원","동길","교현","민서","해윤"]

#item 이름은 아무거나 ㄱㅊ 콜론 꼭 써줄것 tab

# new_data=[]

# #for item in item_list:
# #    if item == "해윤":
# # #        new_data.append(item)

# # num_list={1,2,3,4,5,6,7,8,9,10}

# # new_data=[]
# # for n in num_list:
# #     if n%2==0:
# #         new_data.append(n)

# # print(new_data) 

# str= '쿠키 타니 해윤 해승 미정 상종'
# puppy = "쿠키"

item_list=["타니", "해윤", "해승", "미정", "상종"]
puppy = "쿠키"

if puppy in item_list:
    print("쿠키는 너무너문 귀여워")   
else:
    print("타니도 귀여워")