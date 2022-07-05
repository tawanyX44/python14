#การแสดงค่าในlist
fruits = ["apple","banana","cherry","watermelon","blueberry"]
print(fruits[1])
#เปลี่ยนค่าในlist
fruits[1] = "blackcurrent"
print(fruits[1])
#เปลี่ยนค่าในlistหลายตำแหน่ง
fruits[1:3]= ["kiwi"]
print(fruits)
#เพิ่มค่าในlist
fruits.append("orange")
print(fruits)
fruits.insert(1,"grape")
print(fruits)
tropical = ["mango","pineapple","papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("orange")
fruits.pop(1)
print(fruits)
#del fruits
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#ชื่อ อนงค์รัตน์ อินทวารี ชั้น ม.5/14 เลขที่ 44