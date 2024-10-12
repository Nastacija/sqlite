from read_seg import read_seg

def alloph_start_end(seg_file_B1):

    params, labels = read_seg(seg_file_B1)

    data_list = []
    for start, end in zip(labels, labels[1:]):
        if not start["name"]:
            continue
        start_pos = start['position']
        start_time = start_pos / params['SAMPLING_FREQ'] # в секундах
        end_pos = end['position']
        end_time = end_pos / params['SAMPLING_FREQ'] # в секундах
        flBid = str(seg_file_B1[-11:-7]) + str(seg_file_B1[-2])
        data = flBid + ',' + start["name"] + ',' + str(round(start_time, 3)) + ',' + str(round(end_time, 3))
        data_list.append(data)

    return data_list
