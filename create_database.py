from match_RYB import match_levels
from B1_info import alloph_start_end
import glob
import os

B1_files = list(glob.glob(f"./cta/*.seg_B1"))

table_R = []
table_Y = []
table_B = []
table_fl = []

for B1_file in B1_files:

    filename = B1_file.rstrip('B1')
    Y1_file = f'{filename}Y1'
    if os.path.exists(Y1_file) == False:
        continue
    R2_file = f'{filename}R2'
    if os.path.exists(R2_file) == False:
        continue

    B2Y, Y2R = match_levels(R2_file, Y1_file, B1_file)
    table_R += Y2R
    table_Y += B2Y
    tB = alloph_start_end(B1_file)
    table_B += tB

    flBid = str(B1_file[-11:-7]) + str(B1_file[-2])
    flYid = str(Y1_file[-11:-7]) + str(Y1_file[-2])
    flRid = str(R2_file[-11:-7]) + str(R2_file[-2])

    B_line = str(flBid + ',' + B1_file[-14:] + '\n')
    table_fl.append(B_line)
    Y_line = str(flYid + ',' + Y1_file[-14:] + '\n')
    table_fl.append(Y_line)
    R_line = str(flRid + ',' + R2_file[-14:] + '\n')
    table_fl.append(R_line)

with open('table_fl.txt', "w") as f:
        heading = 'file_id,filename\n'
        f.writelines(heading)
        for line in table_fl:
            f.writelines(line)

id_ctr_R = 0
table_R_ids = []
for line in table_R:
    id_ctr_R += 1
    ln = str(id_ctr_R) + ',' + line
    table_R_ids.append(ln)

with open('table_R.txt', "w") as f:
        heading = 'ind,file_id,№sint,type,content,start,end\n'
        f.writelines(heading)
        for line in table_R_ids:
            f.writelines(line)

add_to_tY = []
for line in table_R_ids:
    content = line.split(',')[-3].split('\t')
    ind = line.split(',')[0]
    for item in content:
        ln = ind + ',' + item
        add_to_tY.append(ln)

id_ctr_Y = 0
table_Y_ids = []
for line, itm in zip(table_Y, add_to_tY):
    id_ctr_Y += 1
    sint_ind = itm.split(',')[0]
    ln = str(id_ctr_Y) + ',' + line.rstrip('\n') + ',' + sint_ind + '\n'
    table_Y_ids.append(ln)

with open('table_Y.txt', "w") as f:
        heading = 'ind,file_id,№word,word,transcription,start,end,sint_id\n'
        f.writelines(heading)
        for line in table_Y_ids:
            f.writelines(line)    

add_to_tB = []
for line in table_Y_ids:
    trscr = line.split(',')[4].replace("0", '').replace("1", '').replace("2", '').replace("4", '').replace("'", '')
    ind = line.split(',')[0]
    for item in trscr:
        ln = ind + ',' + item
        add_to_tB.append(ln)

id_ctr_B = 0
table_B_ids = []
for line, itm in zip(table_B, add_to_tB):
    id_ctr_B += 1
    word_ind = itm.split(',')[0]
    ln = str(id_ctr_B) + ',' + line.rstrip('\n') + ',' + word_ind + '\n'
    table_B_ids.append(ln)

with open('table_B.txt', "w") as f:
        heading = 'ind,file_id,alloph,start,end,word_id\n'
        f.writelines(heading)
        for line in table_B_ids:
            f.writelines(line)