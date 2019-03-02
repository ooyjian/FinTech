import collections

import Brief_helper_funcitons

def combining(head, data, tail=None):
    """
    :param head: a head string
    :param data: data which will be added to the string
    :param tail: tail string(optional)
    :return: a combined string with head and data
    """
    if len(data) == 0:
        return head+'No Company:)'
    else:
        string = head
        for company, percentage in data.items():
            string += company + ' with percentage ' + str(percentage) + '; '
        return string

def return_brief(companies):
    brief = ""
    rise_comp = Brief_helper_funcitons.return_rise(companies)
    fall_comp = Brief_helper_funcitons.return_fall(companies)
    high_rise_comp = Brief_helper_funcitons.highest_rise(companies)
    high_fall_comp = Brief_helper_funcitons.highest_fall(companies)

    return_rising_string = combining("Rising stocks: ", rise_comp)
    return_falling_string = combining("Falling stocks: ", fall_comp)
    return_high_rise = "Highest rising stock: " + str(high_rise_comp[0]) + " with percentage " + str(high_rise_comp[1][0])
    return_high_fall = "Highest falling stock: " + str(high_fall_comp[0]) + " with percentage " + str(high_fall_comp[1][0])


    brief = return_rising_string+'\n'+return_falling_string+'\n' + return_high_rise+'\n' + return_high_fall
    return brief

sample = {'Apple': (1.05, [174.97, 156.82000732421875, 153.3000030517578, 153.9199981689453, 152.6999969482422, 157.75999450683594, 156.3000030517578, 154.67999267578125, 165.25, 166.44000244140625, 166.52000427246094, 171.25, 174.17999267578125, 174.24000549316406, 170.94000244140625, 170.41000366210938, 169.42999267578125, 170.88999938964844, 170.17999267578125, 170.8000030517578, 170.4199981689453, 170.92999267578125, 172.02999877929688, 171.05999755859375, 172.97000122070312, 174.22999572753906, 174.3300018310547, 174.8699951171875, 173.14999389648438, 174.97000122070312]), 'Amazon': (1.95, [1671.73, 1696.199951171875, 1632.1700439453125, 1640.02001953125, 1654.9300537109375, 1670.5699462890625, 1637.8900146484375, 1593.8800048828125, 1670.4300537109375, 1718.72998046875, 1626.22998046875, 1633.31005859375, 1658.81005859375, 1640.260009765625, 1614.3699951171875, 1588.219970703125, 1591.0, 1638.010009765625, 1640.0, 1622.6500244140625, 1607.949951171875, 1627.5799560546875, 1622.0999755859375, 1619.43994140625, 1631.56005859375, 1633.0, 1636.4000244140625, 1641.0899658203125, 1639.8299560546875, 1671.72998046875]), 'Facebook': (0.51, [162.28, 150.0399932861328, 147.57000732421875, 144.3000030517578, 145.8300018310547, 149.00999450683594, 147.47000122070312, 144.19000244140625, 150.4199981689453, 166.69000244140625, 165.7100067138672, 169.25, 171.16000366210938, 170.49000549316406, 166.3800048828125, 167.3300018310547, 165.7899932861328, 165.0399932861328, 164.07000732421875, 163.9499969482422, 162.5, 162.2899932861328, 162.55999755859375, 160.0399932861328, 161.88999938964844, 164.6199951171875, 164.1300048828125, 162.80999755859375, 161.4499969482422, 162.27999877929688]), 'Google': (1.95, [1148.52, 1107.300048828125, 1078.6300048828125, 1084.4100341796875, 1084.0, 1101.510009765625, 1079.8599853515625, 1070.06005859375, 1097.989990234375, 1125.8900146484375, 1118.6199951171875, 1141.4200439453125, 1151.8699951171875, 1122.8900146484375, 1105.9100341796875, 1102.3800048828125, 1102.1199951171875, 1127.5799560546875, 1128.6300048828125, 1129.199951171875, 1119.6300048828125, 1126.510009765625, 1120.5899658203125, 1104.2099609375, 1116.56005859375, 1117.3299560546875, 1122.010009765625, 1122.8900146484375, 1126.550048828125, 1148.52001953125]), 'IBM': (0.77, [139.2, 123.81999969482422, 122.5199966430664, 132.88999938964844, 132.52999877929688, 133.97000122070312, 134.27000427246094, 134.3300018310547, 134.3800048828125, 134.4199981689453, 134.10000610351562, 135.19000244140625, 135.5500030517578, 136.32000732421875, 133.19000244140625, 133.7100067138672, 133.99000549316406, 136.0500030517578, 137.52000427246094, 136.47999572753906, 138.02999877929688, 138.6999969482422, 138.0, 137.83999633789062, 139.25, 139.4600067138672, 139.72000122070312, 139.1699981689453, 138.1300048828125, 139.1999969482422]), 'Microsoft': (0.45, [112.53, 107.70999908447266, 105.68000030517578, 106.70999908447266, 106.19999694824219, 107.16999816894531, 105.08000183105469, 102.94000244140625, 106.37999725341797, 104.43000030517578, 102.77999877929688, 105.73999786376953, 107.22000122070312, 106.02999877929688, 105.2699966430664, 105.66999816894531, 105.25, 106.88999938964844, 106.80999755859375, 106.9000015258789, 108.22000122070312, 108.16999816894531, 107.1500015258789, 109.41000366210938, 110.97000122070312, 111.58999633789062, 112.36000061035156, 112.16999816894531, 112.02999877929688, 112.52999877929688]), 'Intel': (0.64, [53.3, 49.189998626708984, 48.27000045776367, 47.939998626708984, 49.7599983215332, 47.040000915527344, 46.709999084472656, 46.540000915527344, 47.540000915527344, 47.119998931884766, 48.72999954223633, 49.220001220703125, 50.0099983215332, 49.900001525878906, 49.22999954223633, 48.84000015258789, 48.77000045776367, 50.0099983215332, 50.470001220703125, 50.810001373291016, 51.65999984741211, 51.400001525878906, 51.38999938964844, 51.40999984741211, 52.4900016784668, 53.099998474121094, 53.22999954223633, 53.2400016784668, 52.959999084472656, 53.29999923706055])}
print return_brief(sample)












