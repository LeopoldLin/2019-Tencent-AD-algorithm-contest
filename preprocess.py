import sys
import os.path as osp

dataset_dir = '/home/leopold/dataset/Tencent/testA'

total_ad_logs = []
ad_static = []
#
# with open(osp.join(dataset_dir, 'totalExposureLog_200000.out'), 'r') as f:
#     for line in f.readlines():
#         ad_log = line.rstrip().split('\t')
#         if len(ad_log) != 10:
#             print('exist missing value.')
#         else:
#             for i in range(len(ad_log)):
#                 if i < 7:
#                     ad_log[i] = int(ad_log[i])
#                 else:
#                     ad_log[i] = float(ad_log[i])
#                 # if ad_log[i] < 0:
#                 #     print(ad_log)
#         total_ad_logs.append(ad_log)


with open(osp.join(dataset_dir, 'ad_static_feature.out'), 'r') as f:
    for line in f.readlines():
        line = line.rstrip().split('\t')

        stat = [int(line[i]) for i in range(3)]
        
        if len(line) == 6:
            stat.append([-1])  # 商品id为空，推广目标为落地页
        else:
            commodity_id = line[3].split(',')
            commodity_id = [int(commodity_id[i]) for i in range(len(commodity_id))]
            stat.append(commodity_id)

        stat.append(int(line[-3]))  # 商品类型
        
        ad_industry_id = line[-2].split(',')
        ad_industry_id = [int(ad_industry_id[i]) for i in range(len(ad_industry_id))]
        stat.append(ad_industry_id)
        
        material_size = line[-1].split(',')
        material_size = [int(material_size[i]) for i in range(len(material_size))]
        stat.append(material_size)
        
        ad_static.append(stat)
        
commodity_id_dict = {}
commodity_type_dict = {}
ad_industry_id_dict = {}
material_size_dict = {}

for i in range(len(ad_static)):
    for item in ad_static[i][-2]:
        if item not in ad_industry_id_dict.keys():
            ad_industry_id_dict[item] = i

print(ad_industry_id_dict)
