import os 

sexs = ["MALE", "FEMALE" ]
clothes = ["AO_NI",
           "AO_LEN",
           "AO_GILE",
           "AP_POLO",
           "AO_THUN",
           "AO_KHOAC",
           "AO_SO_MI",
           "AO_THUN_DAI_TAY",
           "QUAN_SHORT",
           "QUAN_KHAKI",
           "QUAN_JEANS",
           "QUAN_JOGGER",
           "QUAN_VAI",
           "QUAN_LOT",
           "CHAN_VAY",
           "DAM_NU",
           "ACCESSORY"
           ]

for sex in sexs: 
    for cloth in clothes: 
        os.makedirs(os.path.join(sex, cloth), exist_ok=True)