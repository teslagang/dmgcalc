import cv2, pytesseract, re, csv

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


def str2int(x):
    return int(re.sub("[^0-9]", "", x))


def str2float(x):
    x = x.replace("%", "")
    return float(re.sub("[^0-9]", ".", x)) / 100


def get_stats(filename):
    img_rgb = cv2.imread(filename)
    img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    custom_config = r"--oem 3 --psm 6"
    d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT, config=custom_config)
    stats = dict()

    word_list = []
    last_word = ""
    for word in d["text"]:
        if word != "":
            word_list.append(word)
            last_word = word
        if (last_word != "" and word == "") or (word == d["text"][-1]):
            s = " ".join(word_list).lower()

            if "phy atk" in s and "increase" not in s:
                stats["phy atk"] = str2int(word_list[-1])
            if "phy atk increase" in s:
                stats["phy atk inc"] = str2float(word_list[-1])
            if "phy dmg increase" in s:
                stats["phy dmg inc"] = str2float(word_list[-1])
            if "mag atk" in s and "increase" not in s:
                stats["mag atk"] = str2int(word_list[-1])
            if "mag atk increase" in s:
                stats["mag atk inc"] = str2float(word_list[-1])
            if "mag dmg increase" in s:
                stats["mag dmg inc"] = str2float(word_list[-1])
            if "boss atk increase" in s:
                stats["boss atk inc"] = str2float(word_list[-1])
            if "crit rate" in s:
                stats["crit rate"] = str2float(word_list[-1])
            if "crit atk" in s:
                stats["crit atk"] = str2int(word_list[-1])
            if "crit dmg" in s:
                stats["crit dmg"] = str2float(word_list[-1])
            if "max dmg" in s:
                stats["max dmg inc"] = str2int(word_list[-1])
            if "final dmg" in s:
                stats["final dmg"] = str2float(word_list[-1])
            if "def ignore" in s:
                stats["def ignore"] = str2float(word_list[-1])

            word_list = []
    return stats
