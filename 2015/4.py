import hashlib

def mine(secretKey, zeros):
    result = 0
    output = ""
    while (
        output != "".join(
            ["0" for _ in range(0, zeros)]
        )
    ):
        result += 1
        output = hashlib.md5(
            str(
                secretKey +
                str(result)
            ).encode()
        ).hexdigest()[:zeros]

    return result

print(mine("yzbqklnj", 5))
