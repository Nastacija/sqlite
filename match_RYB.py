from read_seg import read_seg

def match_levels(filename_sint, filename_word, filename_alloph):

    params, labels_word = read_seg(filename_word, encoding="cp1251")
    _, labels_alloph = read_seg(filename_alloph)
    _, labels_sint = read_seg(filename_sint)

    res_B_Y = []
    ctr = 0
    n_word = 1
    for start, end in zip(labels_word, labels_word[1:]):
        if not start["name"]:
            continue
        start_time_Y = round(start["position"] / params["SAMPLING_FREQ"], 3)
        end_time_Y = round(end["position"] / params["SAMPLING_FREQ"], 3)
        labels = []
        for label in labels_alloph[ctr:]:
            if start["position"] <= label["position"] < end["position"]:
                ctr += 1
                labels.append(label)
            elif end["position"] <= label["position"]:
                break
        label_names = []
        for i in labels:
            if i["name"]:
                name = i["name"]
                if name == 'ch_' or name == 'ch':
                    name = 'ч'
                if name == 'sh':
                    name = 'ш'
                if name == 'zh' or name == 'zh_':
                    name = 'ж'
                if name == 'sc':
                    name = 'щ'
                label_names.append(name)
        flYid = str(filename_word[-11:-7]) + str(filename_word[-2])
        word = str(n_word) + "," + start['name'].lstrip('[-]').lstrip('[+]')
        res_B_Y.append(flYid + ',' + f"{word}," + "".join(label_names) + ',' + str(start_time_Y) + ',' + str(end_time_Y) + "\n")
        n_word += 1

    res_Y_R = []
    ctr = 0
    n_sint = 1
    for start, end in zip(labels_sint, labels_sint[1:]):
        if start["name"].startswith('p'):
            continue
        start_time_R = round(start["position"] / params["SAMPLING_FREQ"], 3)
        end_time_R = round(end["position"] / params["SAMPLING_FREQ"], 3)
        labels = []
        for label in labels_word[ctr:]:
            if start["position"] <= label["position"] < end["position"]:
                ctr += 1
                labels.append(label)
            elif end["position"] <= label["position"]:
                break
        label_names = [i["name"].lstrip('[-]').lstrip('[+]') for i in labels if i["name"]]
        sint = str(n_sint) + ',' + start['name']
        flRid = str(filename_sint[-11:-7]) + str(filename_sint[-2])
        res_Y_R.append(flRid + ',' + f"{sint}," + "\t".join(label_names) + ',' + str(start_time_R) + ',' + str(end_time_R) + "\n")
        n_sint += 1
        
    return res_B_Y, res_Y_R