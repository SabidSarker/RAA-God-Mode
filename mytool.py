import os

# স্ক্রিন পরিষ্কার করার জন্য
os.system('clear')

print("--- স্বাগতম আমার পাইথন টুলে ---")

# ইউজারনেম এবং পাসওয়ার্ড সেট করা
correct_user = "admin"
correct_pass = "1234"

# ইউজারের কাছ থেকে ইনপুট নেওয়া
username = input("ইউজারনেম দিন: ")
password = input("পাসওয়ার্ড দিন: ")

# চেক করা হচ্ছে ইনপুট সঠিক কি না
if username == correct_user and password == correct_pass:
    print("\n[+] লগইন সফল! আপনার টুল এখন কাজ করছে...")
    # এখানে আপনার আসল টুলের কাজ শুরু হতে পারে
else:
    print("\n[!] ভুল তথ্য! আবার চেষ্টা করুন।")
