"""
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

- four numbers separated by three .

left right pointers
- iterate until right meets . ,
- record the digit
- move left and right to index after the .

- when done, return them together
"""


def ip_address(ip):
    ip = ip + "."
    print(ip)
    ip_digits = []
    period_count = 0
    left, right = 0, 0

    while period_count != 4:

        right += 1
        if ip[right] == ".":
            ip_digits.append(ip[left:right])
            left = right + 1
            right = left
            period_count += 1
        else:
            continue
    defanged_ip = ""
    for i in ip_digits:
        defanged_ip += i + "[.]"

    return defanged_ip[:-3]


ip = "1.1.1.1"
ip = "255.100.50.0"
print(ip_address(ip))


