try:

    dic = {"a": 1, "b": 2}
    value = dic[9]

except KeyError as e:
    print(f"Error occure : {e}")


try:

    dic = {"a": 1, "b": 2}
    key = dic["l"]

except KeyError as e:
    print(f"Error occure : {e}")


# apply in function


def value(key):
    dict = {"a": 1, "b": 2}
    return dict[key]


try:
    value = value(3)

except KeyError as e:
    print(f"Erro occure: {str(e)}")
