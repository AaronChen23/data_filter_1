data = []
count = 0
sum_n = 0
large = []
nice = []
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 200000 == 0:
			print(len(data))
	print("總共有", len(data), "筆資料")



w_c = {} # w_c = word_count
for line in data:
	words = line.split(" ")
	for word in words:
		if word in w_c:
			w_c[word] = w_c[word] + 1
		else:
			w_c[word] = 1
	
#for word in w_c:
#	if w_c[word] > 10000:
#		print(word, "出現", w_c[word], "次")

#print(w_c["Also"])
#print(len(w_c))
#print(w_c)

while True:
	word = input("請輸入你/ 妳想查的字")
	if word == "q":
		break
	elif word in w_c:
		print(word, "出現", w_c[word], "次")	
	else:
		print("查無此字")

	









def befor():
	for n in data:
		sum_n = sum_n + len(n)
	print("平均每筆留言有", sum_n/len(data), "個字")

	for n in data:
		if len(n) > 1000:
			large.append(n)
	print("一共有", len(large), "筆資料自大於1000")	

	#print(large[len(large) - 1])	

	#for n in data:
	#	if "nice, good" in n and len(n) < 100:
	#		nice.append(n)
	nice = [n for n in data if "nice, good" in n and len(n) < 100 ]
	print("一共有", len(nice), "筆資料裡面包含nice & good 資訊")
	print(nice)		

	 