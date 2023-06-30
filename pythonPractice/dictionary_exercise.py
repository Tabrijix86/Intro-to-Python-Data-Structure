bd_division_info = {"Barishal": {"district": 6, "upazila": 39, "union": 333},
                    "Chittagong": {"district": 11, "upazila": 97, "union": 336},
                    "Dhaka": {"district": 13, "upazila": 93, "union": 1833},
                    "Khulna": {"district": 10, "upazila": 59, "union": 270},
                    "Mymensingh": {"district": 4, "upazila": 34, "union": 350},
                    "Rajshahi": {"district": 8, "upazila": 70, "union": 558},
                    "Rangpur": {"district": 8, "upazila": 58, "union": 536},
                    "Sylhet": {"district": 4, "upazila": 38, "union": 334}}

for i in bd_division_info:
    print(i)
    print(bd_division_info[i])
print(bd_division_info.keys())
