import pytest 
from src.homework_vectors_problem2 import find_common_meaning

model = {
    "good": [0.040527344, 0.0625, -0.017456055, 0.07861328, 0.032714844, -0.012634277, 0.009643555, 0.123535156, -0.021484375, 0.15234375, -0.05834961, -0.10644531, 0.021240234, 0.13574219, -0.13183594, 0.17675781, 0.27148438, 0.13769531, -0.17382812, -0.14160156, -0.030761719, 0.19628906, -0.032958984, 0.125, 0.25390625, 0.12695312, -0.15234375, 0.031982422, 0.011352539, -0.01361084, -0.12890625, 0.010192871, 0.23925781, -0.084472656, 0.140625, 0.13085938, -0.045166016, 0.064941406, 0.025390625, 0.056152344, 0.24609375, -0.20507812, 0.23632812, -0.008605957, -0.022949219, 0.05078125, 0.10644531, -0.03564453, 0.087402344, -0.057128906, 0.08496094, 0.23535156, -0.10107422, -0.03564453, -0.04736328, 0.04736328, -0.14550781, -0.10986328, 0.14746094, -0.23242188, -0.072753906, 0.19628906, -0.37890625, -0.072265625, 0.048339844, 0.119140625, 0.061035156, -0.12109375, -0.27929688, 0.052001953, 0.049072266, -0.02709961, 0.1328125, 0.033691406, -0.32226562, 0.042236328, -0.087890625, 0.15429688, 0.09472656, 0.103515625, -0.028564453, 0.0012817383, -0.004272461, 0.24609375, -0.059570312, -0.16894531, -0.096191406, 0.16796875, 0.013366699, 0.048828125, 0.083496094, 0.06347656, -0.008728027, -0.08642578, -0.03857422, -0.08251953, 0.15722656, 0.22753906, -0.0076293945, -0.19921875, -0.06347656, 0.12792969, -0.06347656, -0.030273438, 0.045654297, 0.06298828, -0.025268555, -0.067871094, -0.011413574, -0.13574219, 0.029785156, 0.104003906, -0.15917969, -0.084472656, 0.29882812, -0.12597656, 0.11425781, -0.08105469, -0.09082031, -0.07910156, -0.111816406, -0.096191406, 0.027709961, 0.14257812, -0.26757812, -0.09375, 0.039794922, -0.17871094, -0.028198242, 0.0146484375, -0.31640625, -0.24511719, -0.08935547, 0.09716797, -0.009643555, -0.14746094, 0.15234375, 0.21582031, 0.059814453, 0.23828125, -0.051513672, 0.14941406, 0.13574219, -0.032226562, -0.265625, -0.111816406, -0.23046875, -0.140625, 0.25585938, -0.15429688, 0.1796875, 0.15527344, -0.21582031, 0.36328125, -0.1015625, 0.049804688, 0.071777344, -0.14550781, -0.031982422, 0.009521484, -0.12109375, 0.12109375, 0.09765625, 0.07763672, 0.3203125, -0.22265625, -0.084472656, -0.107421875, 0.11279297, -0.13867188, -0.21875, 0.014587402, 0.13378906, -0.009216309, 0.009216309, 0.16894531, 0.16894531, -0.078125, -0.006652832, 0.037353516, -0.10888672, -0.25390625, 0.014526367, -0.09716797, -0.19628906, -0.017822266, -0.28125, -0.020507812, -0.029052734, -0.09375, -0.17675781, 0.21484375, -0.052246094, -0.115722656, -0.01977539, -0.10839844, -0.013427734, -0.15332031, -0.140625, -0.11816406, 0.092285156, 0.109375, 0.057617188, -0.03466797, 0.03564453, -0.12011719, -0.14257812, -0.0007247925, -0.06689453, 0.119140625, -0.10449219, 0.07861328, -0.12792969, 0.095703125, -0.008178711, 0.07128906, 0.20703125, -0.03149414, 0.095703125, 0.17285156, -0.079589844, -0.024291992, -0.07519531, -0.075683594, 0.095214844, -0.064941406, -0.0068969727, -0.09033203, 0.03100586, 0.19921875, -0.10644531, -0.114746094, 0.18652344, -0.05078125, 0.0859375, 0.0012893677, -0.18847656, -0.20019531, -0.028320312, 0.11328125, 0.25976562, 0.22070312, 0.041015625, 0.0017166138, 0.075683594, -0.011962891, 0.017700195, -0.05883789, -0.25976562, -0.234375, -0.049560547, 0.25976562, 0.15332031, 0.15136719, 0.08300781, -0.15527344, 0.049316406, 0.07519531, -0.05078125, -0.1328125, -0.13574219, 0.041992188, -0.14257812, 0.020996094, 0.07861328, 0.016113281, 0.016235352, -0.21582031, 0.015991211, -0.048828125, -0.024047852, 0.13476562, 0.08496094, -0.011962891, 0.100097656, -0.13867188, 0.080566406, -0.22070312, -0.12011719, 0.18945312, 0.05444336, -0.05053711, 0.0014724731, 0.14160156, -0.064941406, -0.055664062, -0.09033203, -0.026733398, -0.10498047, 0.024169922, 0.014221191, 0.1875, -0.16503906, 0.015380859, -0.041748047, 0.05444336, -0.01184082, -0.15625, 0.0019302368, -0.06982422],
    "evil": [0.052001953, 0.05493164, -0.01965332, 0.11376953, -0.33398438, 0.52734375, 0.17871094, 0.15527344, 0.13183594, 0.09033203, -0.09423828, 0.14941406, -0.087402344, 0.40039062, -0.22949219, 0.29101562, -0.071777344, 0.114746094, -0.088378906, -0.060791016, 0.049072266, 0.052246094, 0.33203125, 0.1171875, 0.15527344, 0.20605469, 0.14550781, -0.025268555, 0.052978516, -0.17089844, -0.049316406, -0.068359375, 0.040039062, 0.234375, -0.05078125, 0.30078125, 0.29492188, -0.11035156, 0.032470703, 0.04321289, 0.35742188, 0.15625, 0.17675781, -0.1640625, -0.14550781, -0.13574219, 0.08935547, -0.19921875, -0.19824219, -0.19140625, -0.390625, 0.3984375, -0.005645752, -0.12792969, 0.37695312, 0.07910156, -0.19726562, -0.34960938, -0.028198242, 0.15527344, 0.15625, 0.21582031, -0.017211914, 0.050048828, -0.13574219, 0.01977539, 0.20019531, 0.027832031, -0.38671875, 0.19238281, 0.1796875, 0.01574707, 0.00390625, 0.05517578, 0.12890625, -0.06982422, 0.04638672, 0.17089844, 0.1796875, -0.055419922, -0.002532959, 0.25976562, -0.31445312, -0.0625, -0.296875, -0.063964844, -0.115234375, 0.046875, 0.37695312, 0.10839844, -0.0034332275, 0.14453125, -0.3046875, 0.033691406, 0.075683594, -0.0126953125, -0.07714844, 0.079589844, 0.017822266, -0.1484375, -0.05908203, 0.15527344, 0.32226562, -0.20605469, 0.171875, -0.004272461, -0.3828125, 0.16210938, 0.041503906, 0.021362305, -0.2578125, -0.18652344, 0.10839844, 0.12060547, 0.08642578, 0.04663086, 0.11816406, -0.11816406, 0.15332031, 0.16992188, -0.24023438, -0.020629883, -0.048583984, -0.11376953, -0.34375, -0.15039062, 0.119628906, 0.014709473, 0.24707031, -0.20117188, -0.1953125, 0.10888672, -0.107421875, 0.08105469, 0.171875, -0.012573242, -0.076171875, -0.15722656, 0.16894531, 0.022949219, 0.421875, 0.05029297, -0.14355469, 0.018066406, -0.052246094, -0.09277344, -0.0059509277, 0.039794922, 0.003036499, -0.31835938, 0.2890625, 0.025146484, -0.0051574707, 0.15527344, -0.19140625, -0.13378906, -0.026733398, -0.31640625, 0.068359375, -0.09082031, -0.10058594, -0.16308594, -0.00680542, -0.140625, -0.10595703, -0.40820312, 0.10644531, -0.076660156, 0.030761719, 0.037353516, 0.12695312, 0.12695312, 0.091796875, 0.06542969, 0.03881836, -0.25585938, 0.067871094, -0.28125, -0.0058898926, -0.33007812, -0.07714844, -0.2734375, 0.123046875, -0.30664062, 0.21582031, 0.014465332, 0.0008125305, 0.064453125, 0.17382812, 0.111328125, 0.03881836, 0.44140625, 0.0030975342, -0.043945312, -0.15625, 0.20605469, 0.11376953, -0.29882812, -0.20605469, -0.17382812, 0.26757812, -0.109375, 0.30273438, -0.49414062, 0.14941406, 0.099609375, -0.016235352, -0.052001953, -0.45117188, -0.15136719, -0.3125, -0.01965332, -0.24023438, -0.3671875, -0.33203125, 0.24804688, -0.2265625, -0.37695312, -0.13378906, 0.087890625, -0.051757812, 0.09082031, 0.43359375, 0.031982422, -0.15625, -0.072753906, -0.012878418, 0.2109375, -0.17773438, -0.068847656, -0.044433594, -0.055419922, -0.13867188, 0.09277344, 0.30273438, 0.011413574, 0.10644531, 0.018676758, 0.31835938, -0.092285156, 0.12597656, -0.053710938, 0.027709961, -0.049072266, 0.12695312, 0.0546875, -0.061523438, -0.024658203, 0.03149414, -0.18457031, -0.096191406, -0.0058288574, 0.24414062, 0.16503906, -0.04321289, -0.24707031, -0.07519531, -0.27929688, 0.27539062, 0.0040283203, 0.096191406, -0.123535156, -0.17382812, 0.016113281, 0.026245117, -0.01184082, -0.15820312, 0.17285156, -0.08642578, 0.14355469, 0.05078125, 0.07421875, -0.103515625, 0.020385742, 0.24902344, 0.011779785, 0.04321289, 0.16210938, 0.0625, 0.40234375, -0.15136719, -0.030639648, -0.018432617, -0.14746094, -0.0859375, -0.084472656, -0.16308594, -0.26171875, -0.08154297, 0.028198242, -0.328125, 0.25195312, -0.43164062, 0.072265625, -0.44140625, -0.048583984, 0.06591797, -0.15917969, 0.15625, 0.09765625],
    "queen": [0.19628906, -0.022705078, 0.080078125, -0.10986328, 0.07910156, -0.19921875, 0.12988281, -0.08496094, 0.41796875, -0.0051879883, 0.017578125, 0.115722656, -0.053466797, -0.119140625, -0.014343262, -0.13769531, -0.109375, -0.234375, 0.123046875, -0.17480469, 0.3046875, -0.03100586, -0.06982422, -0.032958984, 0.28125, -0.33007812, -0.087890625, 0.01574707, 0.3984375, -0.19433594, -0.21875, 0.0048828125, 0.061767578, -0.11230469, 0.12402344, -0.06689453, 0.004547119, 0.23730469, 0.15820312, -0.22070312, -0.33007812, 0.18359375, 0.1640625, -0.17578125, -0.17578125, -0.25195312, -0.12451172, 0.078125, -0.018188477, 0.44140625, 0.027709961, 0.111816406, -0.111328125, -0.15039062, -0.14257812, 0.12207031, -0.09667969, 0.109375, 0.10449219, -0.13964844, 0.2109375, -0.140625, -0.18457031, -0.1953125, 0.13476562, 0.16503906, -0.19824219, 0.18164062, -0.22558594, -0.2421875, 0.057128906, -0.25976562, 0.027832031, -0.23730469, -0.115722656, 0.092285156, -0.35351562, 0.040283203, -0.11669922, -0.07763672, -0.052490234, 0.013916016, -0.0069885254, -0.11230469, -0.28515625, 0.36132812, -0.034179688, -0.24609375, 0.15527344, 0.1953125, -0.30859375, 0.110839844, -0.021240234, 0.087890625, -0.25195312, 0.0022277832, -0.15332031, 0.083496094, 0.067871094, -0.100097656, -0.15234375, 0.048339844, 0.025756836, 0.14941406, 0.25585938, 0.06347656, 0.006500244, -0.2734375, 0.22070312, 0.00793457, -0.10253906, -0.052734375, 0.05102539, -0.114746094, 0.22753906, -0.030029297, 0.0011444092, -0.092285156, -0.23925781, 0.16796875, 0.234375, 0.18652344, -0.24316406, 0.24902344, 0.044921875, -0.12158203, -0.23925781, 0.19433594, -0.037109375, 0.14941406, -0.002960205, 0.16601562, -0.22070312, -0.18945312, -0.018676758, -0.032958984, -0.09814453, -0.13964844, 0.28710938, 0.24707031, -0.375, 0.044921875, -0.06347656, 0.15039062, -0.056884766, -0.16503906, -0.3125, 0.020385742, -0.15332031, -0.17382812, 0.20898438, -0.3125, -0.110839844, -0.08203125, -0.20117188, 0.04711914, -0.15234375, -0.17675781, -0.08935547, 0.08642578, 0.106933594, 0.083984375, 0.0016555786, -0.1484375, -0.23730469, 0.008422852, 0.12695312, -0.38867188, -0.028564453, 0.21289062, -0.25195312, 0.20605469, -0.07128906, -0.21972656, 0.3046875, -0.23730469, -0.12207031, -0.029174805, -0.12792969, 0.31835938, -0.03515625, -0.12792969, -0.09814453, 0.05859375, 0.16894531, 0.099609375, 0.07519531, -0.16210938, 0.36523438, 0.030151367, 0.20507812, -0.171875, -0.11621094, -0.22167969, -0.09326172, -0.016723633, -0.21679688, 0.064453125, -0.12890625, -0.17382812, -0.13867188, -0.047607422, -0.0076293945, -0.08154297, 0.03149414, -0.12158203, -0.03112793, 0.17578125, 0.09863281, -0.031982422, -0.3515625, 0.09033203, -0.14550781, 0.04736328, -0.4375, -0.14355469, -0.12890625, -0.07861328, 0.056152344, 0.26171875, 0.3125, -0.20996094, 0.234375, -0.026855469, 0.021850586, -0.12890625, -0.25195312, 0.30078125, -0.053466797, 0.19921875, -0.056640625, 0.00027275085, -0.071777344, -0.19628906, -0.12060547, -0.3359375, 0.072265625, 0.04248047, 0.19335938, 0.16113281, 0.05029297, 0.010986328, -0.05053711, -0.104003906, 0.15820312, -0.23535156, -0.036132812, -0.072265625, -0.25, -0.24609375, 0.122558594, -0.016601562, -0.23535156, 0.12109375, -0.036865234, -0.21875, 0.033203125, 0.21289062, -0.21972656, -0.16992188, -0.10986328, -0.103515625, -0.002380371, -0.12109375, 0.22558594, 0.38476562, -0.28125, -0.20410156, -0.11425781, 0.25, 0.25390625, -0.15039062, 0.088378906, -0.10058594, 0.31054688, -0.1875, 0.106933594, -0.46484375, -0.16992188, -0.296875, -0.171875, 0.076660156, -0.13574219, 0.21875, 0.30273438, -0.083496094, -0.16796875, 0.12988281, 0.099121094, -0.12695312, -0.084472656, 0.023925781, -0.234375, 0.08642578, -0.0115356445, 0.008544922, 0.091796875, -0.17675781, 0.099609375, -0.21582031],
    "car": [0.13085938, 0.008422852, 0.033447266, -0.05883789, 0.040039062, -0.14257812, 0.049316406, -0.16894531, 0.20898438, 0.119628906, 0.18066406, -0.25, -0.104003906, -0.107421875, -0.018798828, 0.052001953, -0.002166748, 0.064453125, 0.14453125, -0.045410156, 0.16113281, -0.016113281, -0.030883789, 0.084472656, 0.16210938, 0.044677734, -0.15527344, 0.25390625, 0.33984375, 0.0075683594, -0.25585938, -0.017333984, -0.032958984, 0.16308594, -0.12597656, -0.099121094, 0.16503906, 0.068847656, -0.18945312, 0.028320312, -0.053466797, -0.030639648, 0.110839844, 0.24121094, -0.234375, 0.123535156, -0.0029449463, 0.1484375, 0.33203125, 0.052490234, -0.20019531, 0.37695312, 0.122558594, 0.11425781, -0.17675781, 0.100097656, 0.003036499, 0.26757812, 0.20117188, 0.037109375, 0.110839844, -0.09814453, -0.3125, 0.03515625, 0.028320312, 0.26171875, -0.08642578, -0.022583008, -0.05834961, -0.007873535, 0.11767578, -0.04296875, -0.17285156, 0.043945312, -0.23046875, 0.1640625, -0.114746094, -0.060302734, 0.011962891, -0.24707031, 0.32617188, -0.044921875, -0.11425781, 0.22851562, -0.016479492, -0.15039062, -0.13183594, 0.12597656, -0.17480469, 0.022094727, -0.1015625, 0.008178711, 0.107910156, -0.24609375, -0.109375, -0.09375, -0.016235352, -0.20214844, 0.23144531, -0.05444336, -0.055419922, -0.20898438, 0.26757812, 0.27929688, 0.17089844, -0.17578125, -0.027709961, -0.20410156, 0.023925781, 0.03125, -0.25390625, -0.125, -0.05493164, -0.17382812, 0.28515625, -0.23242188, 0.0234375, -0.20117188, -0.13476562, 0.26367188, 0.0076904297, 0.20507812, -0.017089844, -0.12988281, 0.04711914, 0.22070312, 0.020996094, -0.29101562, -0.028930664, 0.17285156, 0.04272461, -0.19824219, -0.040039062, -0.16992188, 0.10058594, -0.09326172, 0.15820312, -0.16503906, -0.060546875, 0.19433594, -0.07080078, -0.068847656, -0.096191406, -0.072265625, 0.048828125, 0.07324219, 0.11035156, 0.048583984, -0.17675781, -0.33789062, 0.22558594, 0.16308594, 0.05102539, -0.08251953, 0.079589844, 0.087402344, -0.16894531, -0.021606445, -0.19238281, 0.03857422, -0.05102539, 0.21972656, 0.080078125, -0.21191406, -0.07519531, -0.15039062, 0.3046875, -0.17089844, 0.123535156, -0.234375, -0.107421875, -0.067871094, 0.019042969, -0.14160156, -0.22753906, -0.16308594, 0.14453125, -0.15136719, -0.296875, 0.22363281, -0.10205078, -0.045654297, -0.21679688, -0.09033203, 0.09375, -0.15332031, -0.01550293, 0.3046875, -0.23730469, 0.08935547, 0.037109375, 0.029418945, -0.28515625, 0.15820312, -0.0030670166, 0.060546875, 0.0049743652, -0.15234375, -0.008361816, 0.021972656, -0.12109375, -0.13867188, -0.2734375, -0.068359375, 0.08251953, -0.26367188, -0.16992188, 0.14746094, 0.08496094, 0.020751953, 0.13671875, -0.049316406, -0.010070801, -0.003692627, -0.10839844, 0.14746094, -0.15527344, 0.16113281, 0.056152344, -0.050048828, -0.1640625, -0.26953125, 0.4140625, 0.060791016, -0.046875, -0.025146484, 0.10595703, 0.1328125, -0.16699219, -0.049072266, 0.04663086, 0.051513672, -0.079589844, -0.16503906, -0.29882812, 0.060546875, -0.15332031, -0.0059814453, 0.06640625, -0.045166016, 0.24316406, -0.07080078, -0.36914062, -0.23144531, -0.119140625, -0.08300781, 0.14746094, -0.057617188, 0.23535156, -0.123046875, 0.14648438, 0.13671875, 0.15429688, 0.021118164, -0.095703125, 0.05859375, 0.039794922, -0.08105469, 0.055908203, -0.16601562, 0.27148438, -0.20117188, -0.009155273, 0.07324219, 0.10449219, 0.34570312, -0.26367188, 0.020996094, -0.40039062, -0.034179688, -0.15917969, -0.087890625, 0.08203125, 0.23339844, 0.021362305, -0.11328125, 0.052490234, -0.10449219, -0.023803711, -0.083496094, -0.040039062, 0.019165039, -0.012268066, -0.18261719, -0.067871094, -0.08496094, -0.030395508, -0.053955078, 0.04248047, 0.12792969, -0.27539062, 0.28515625, -0.04736328, 0.064941406, -0.11230469, -0.025756836, -0.041259766, 0.22851562, -0.14941406, -0.15039062],
    "man": [0.32617188, 0.13085938, 0.03466797, -0.08300781, 0.08984375, -0.041259766, -0.19824219, 0.0068969727, 0.14355469, 0.0019454956, 0.028808594, -0.25, -0.083984375, -0.15136719, -0.10205078, 0.040771484, -0.09765625, 0.059326172, 0.029785156, -0.10058594, -0.13085938, 0.0012969971, 0.026123047, -0.27148438, 0.063964844, -0.19140625, -0.078125, 0.25976562, 0.375, -0.045410156, 0.16210938, 0.13671875, -0.063964844, -0.020629883, -0.09667969, 0.25390625, 0.24804688, -0.12695312, 0.071777344, 0.3203125, 0.03149414, -0.03857422, 0.21191406, -0.008117676, 0.22265625, -0.13476562, -0.076171875, 0.010498047, -0.051757812, 0.038085938, -0.13378906, 0.125, 0.055908203, -0.18261719, 0.08154297, -0.084472656, -0.07763672, -0.04345703, 0.08105469, -0.010925293, 0.17480469, 0.30664062, -0.04321289, -0.014160156, 0.09082031, -0.009277344, -0.034423828, -0.115234375, 0.12451172, -0.024658203, 0.08544922, 0.14355469, -0.27734375, 0.036621094, -0.11035156, 0.13085938, -0.017211914, -0.080566406, -0.007080078, -0.029541016, 0.30078125, -0.09033203, 0.03149414, -0.18652344, -0.111816406, 0.10253906, -0.25976562, -0.022094727, 0.16796875, -0.053222656, -0.14550781, -0.010498047, -0.030395508, -0.03857422, 0.115234375, -0.0062561035, -0.13964844, 0.080078125, 0.061035156, -0.15332031, -0.111328125, -0.14160156, 0.19824219, -0.06933594, 0.29296875, -0.16015625, 0.20898438, 0.00041770935, 0.018310547, -0.20214844, 0.047607422, 0.05810547, -0.012329102, -0.019897461, -0.0036468506, -0.013549805, -0.08251953, -0.03149414, 0.007171631, 0.20117188, 0.08300781, -0.048095703, -0.26367188, -0.09667969, -0.22558594, -0.09667969, 0.064941406, -0.025024414, 0.08496094, 0.031982422, -0.075683594, -0.25390625, -0.11669922, -0.014465332, -0.16015625, -0.007019043, -0.057128906, 0.028076172, -0.091796875, 0.25195312, 0.24121094, 0.06640625, 0.12988281, 0.17089844, -0.13671875, 0.1875, -0.100097656, -0.041992188, -0.12011719, 0.0052490234, 0.15625, -0.203125, -0.07128906, -0.061035156, 0.016357422, 0.18261719, 0.035888672, -0.04248047, 0.16796875, -0.15039062, -0.16992188, 0.018310547, 0.27734375, -0.0126953125, -0.0390625, -0.15429688, 0.18457031, -0.07910156, 0.09033203, -0.02709961, 0.08251953, 0.06738281, -0.16113281, -0.19628906, -0.15234375, -0.04711914, 0.047607422, 0.05908203, -0.16894531, -0.14941406, 0.12988281, 0.04321289, 0.026245117, -0.1796875, -0.19628906, 0.064453125, 0.08935547, 0.1640625, -0.038085938, -0.09814453, -0.014831543, 0.1875, 0.12792969, 0.22753906, 0.018188477, -0.079589844, -0.11376953, -0.06933594, -0.15527344, -0.08105469, -0.09277344, -0.11328125, -0.15136719, -0.080078125, -0.05126953, -0.15332031, 0.11669922, 0.068359375, 0.032470703, -0.33984375, -0.08154297, -0.083496094, 0.040039062, 0.049072266, -0.24121094, -0.13476562, -0.059326172, 0.12158203, -0.34179688, 0.16503906, 0.061767578, -0.18164062, 0.20117188, -0.07714844, 0.1640625, 0.0040283203, 0.30273438, -0.100097656, -0.13671875, -0.059570312, 0.0625, -0.21289062, -0.06542969, 0.1796875, -0.07763672, -0.01928711, -0.15039062, -0.0010604858, 0.034179688, 0.033447266, 0.19335938, 0.01965332, -0.19921875, -0.10644531, 0.015258789, 0.009277344, 0.014160156, -0.023925781, 0.05883789, 0.02368164, 0.125, 0.047607422, -0.055664062, 0.115722656, 0.14746094, 0.1015625, -0.07128906, -0.07714844, -0.12597656, 0.029174805, 0.095214844, -0.12402344, -0.109375, -0.12890625, 0.16308594, 0.28320312, -0.03149414, 0.123046875, -0.23242188, -0.09375, -0.12988281, 0.013549805, -0.03881836, -0.08251953, 0.008972168, 0.16308594, 0.10546875, -0.13867188, -0.16503906, -0.03857422, 0.10839844, -0.10498047, 0.063964844, 0.38867188, -0.059814453, -0.061279297, -0.10449219, -0.16796875, 0.071777344, 0.13964844, 0.15527344, -0.03125, -0.20214844, -0.12988281, -0.10058594, -0.063964844, -0.083496094, -0.30273438, -0.080078125, 0.020996094],
    "arch": [0.078125, 0.203125, -0.040039062, 0.06591797, 0.012145996, -0.028930664, 0.23925781, 0.019897461, -0.041015625, 0.21777344, 0.043701172, -0.05078125, 0.13085938, 0.068359375, 0.099609375, 0.072265625, -0.15136719, -0.123535156, 0.12890625, -0.14746094, 0.16699219, 0.31640625, -0.08886719, -0.14453125, -0.0032348633, -0.12109375, -0.103027344, 0.12402344, -0.016479492, -0.46679688, 0.06591797, -0.296875, 0.029541016, -0.10253906, 0.021606445, -0.0546875, 0.17773438, 0.390625, -0.08251953, -0.21386719, 0.0859375, -0.20996094, 0.2265625, -0.22949219, 0.15527344, -0.13867188, -0.16503906, -0.06933594, 0.18359375, 0.12792969, -0.09326172, 0.08935547, -0.22753906, -0.051757812, 0.23339844, -0.07763672, -0.17382812, -0.17382812, -0.027832031, 0.25390625, -0.115722656, -0.03491211, -0.22363281, -0.41992188, 0.024169922, 0.033203125, -0.20019531, -0.043945312, -0.296875, 0.111816406, 0.05078125, -0.002243042, -0.005279541, -0.22753906, -0.05517578, -0.20800781, 0.016479492, 0.17382812, 0.30859375, 0.026000977, 0.12988281, -0.15332031, -0.09863281, -0.25, -0.23339844, 0.111816406, -0.06347656, -0.15820312, 0.15234375, 0.017456055, -0.35546875, -0.02722168, -0.07861328, 0.29101562, 0.076171875, 0.0546875, -0.203125, -0.095214844, 0.07373047, 0.13574219, -0.15625, 0.026977539, 0.012390137, -0.28125, 0.16992188, 0.2734375, 0.16308594, 0.22949219, 0.04736328, -0.21679688, -0.22753906, -0.18359375, 0.020019531, 0.05859375, 0.056152344, -0.09472656, -0.06689453, -0.03540039, -0.0011901855, 0.11376953, 0.14648438, -0.15039062, 0.010498047, 0.1328125, -0.0044555664, -0.106933594, -0.024780273, -0.046142578, 0.052490234, -0.095703125, -0.09082031, 0.12988281, 0.009277344, -0.14257812, 0.029541016, -0.05126953, -0.076660156, 0.18554688, 0.13769531, 0.24804688, 0.10595703, 0.15527344, -0.16015625, 0.08496094, 0.30273438, 0.016723633, -0.06982422, -0.07324219, -0.33789062, 0.11621094, 0.0036773682, -0.31054688, 0.014282227, 0.043945312, 0.11767578, -0.12451172, -0.24511719, 0.03491211, 0.18554688, 0.10253906, 0.17578125, -0.114746094, 0.28320312, -0.14453125, -0.0053100586, -0.01574707, 0.091796875, -0.38671875, -0.41210938, 0.390625, -0.34960938, -0.18652344, -0.123046875, -0.087890625, 0.2734375, -0.17285156, -0.31835938, -0.13085938, 0.041748047, 0.109375, -0.33984375, -0.012023926, -0.18066406, -0.111816406, -0.0053710938, -0.08886719, 0.20898438, -0.110839844, 0.36914062, 0.046875, 0.14257812, 0.0035705566, -0.05883789, -0.18164062, -0.10449219, 0.06298828, -0.18261719, 0.20703125, 0.04663086, -0.04711914, 0.022460938, -0.110839844, -0.13183594, 0.13476562, 0.39648438, -0.16992188, 0.16210938, -0.08496094, 0.119628906, 0.016235352, -0.27148438, -0.03881836, -0.16210938, -0.049804688, -0.18945312, -0.31640625, -0.4921875, -0.079589844, 0.033447266, 0.119140625, 0.13183594, -0.23632812, -0.00289917, 0.061767578, 0.033935547, 0.11669922, -0.060058594, 0.18945312, -0.061767578, 0.12695312, -0.14746094, 0.03955078, -0.3125, -0.07080078, -0.08251953, 0.31054688, 0.08886719, 0.25585938, 0.0546875, -0.03564453, -0.0027008057, 0.07910156, 0.044677734, -0.12109375, 0.1484375, 0.20117188, 0.060302734, 0.052001953, -0.25585938, -0.06982422, 0.07519531, -0.3203125, 0.014892578, 0.16210938, -0.0023956299, -0.25976562, -0.036865234, 0.15527344, -0.33203125, -0.025756836, 0.140625, -0.016601562, -0.111328125, -0.0703125, 0.06738281, 0.1640625, 0.14355469, -0.19140625, -0.05834961, 0.16601562, -0.06689453, 0.047851562, 0.005493164, -0.119628906, 0.095214844, -0.19433594, -0.023803711, -0.19238281, -0.03149414, 0.047607422, -0.11279297, 0.19824219, 0.07421875, -0.052978516, 0.071777344, -0.17382812, -0.19238281, 0.0074157715, -0.110839844, -0.09814453, -0.07519531, 0.1640625, -0.14160156, -0.09277344, 0.049072266, -0.061035156, 0.23925781, -0.115722656, -0.13476562, 0.1796875],
    "man": [0.32617188, 0.13085938, 0.03466797, -0.08300781, 0.08984375, -0.041259766, -0.19824219, 0.0068969727, 0.14355469, 0.0019454956, 0.028808594, -0.25, -0.083984375, -0.15136719, -0.10205078, 0.040771484, -0.09765625, 0.059326172, 0.029785156, -0.10058594, -0.13085938, 0.0012969971, 0.026123047, -0.27148438, 0.063964844, -0.19140625, -0.078125, 0.25976562, 0.375, -0.045410156, 0.16210938, 0.13671875, -0.063964844, -0.020629883, -0.09667969, 0.25390625, 0.24804688, -0.12695312, 0.071777344, 0.3203125, 0.03149414, -0.03857422, 0.21191406, -0.008117676, 0.22265625, -0.13476562, -0.076171875, 0.010498047, -0.051757812, 0.038085938, -0.13378906, 0.125, 0.055908203, -0.18261719, 0.08154297, -0.084472656, -0.07763672, -0.04345703, 0.08105469, -0.010925293, 0.17480469, 0.30664062, -0.04321289, -0.014160156, 0.09082031, -0.009277344, -0.034423828, -0.115234375, 0.12451172, -0.024658203, 0.08544922, 0.14355469, -0.27734375, 0.036621094, -0.11035156, 0.13085938, -0.017211914, -0.080566406, -0.007080078, -0.029541016, 0.30078125, -0.09033203, 0.03149414, -0.18652344, -0.111816406, 0.10253906, -0.25976562, -0.022094727, 0.16796875, -0.053222656, -0.14550781, -0.010498047, -0.030395508, -0.03857422, 0.115234375, -0.0062561035, -0.13964844, 0.080078125, 0.061035156, -0.15332031, -0.111328125, -0.14160156, 0.19824219, -0.06933594, 0.29296875, -0.16015625, 0.20898438, 0.00041770935, 0.018310547, -0.20214844, 0.047607422, 0.05810547, -0.012329102, -0.019897461, -0.0036468506, -0.013549805, -0.08251953, -0.03149414, 0.007171631, 0.20117188, 0.08300781, -0.048095703, -0.26367188, -0.09667969, -0.22558594, -0.09667969, 0.064941406, -0.025024414, 0.08496094, 0.031982422, -0.075683594, -0.25390625, -0.11669922, -0.014465332, -0.16015625, -0.007019043, -0.057128906, 0.028076172, -0.091796875, 0.25195312, 0.24121094, 0.06640625, 0.12988281, 0.17089844, -0.13671875, 0.1875, -0.100097656, -0.041992188, -0.12011719, 0.0052490234, 0.15625, -0.203125, -0.07128906, -0.061035156, 0.016357422, 0.18261719, 0.035888672, -0.04248047, 0.16796875, -0.15039062, -0.16992188, 0.018310547, 0.27734375, -0.0126953125, -0.0390625, -0.15429688, 0.18457031, -0.07910156, 0.09033203, -0.02709961, 0.08251953, 0.06738281, -0.16113281, -0.19628906, -0.15234375, -0.04711914, 0.047607422, 0.05908203, -0.16894531, -0.14941406, 0.12988281, 0.04321289, 0.026245117, -0.1796875, -0.19628906, 0.064453125, 0.08935547, 0.1640625, -0.038085938, -0.09814453, -0.014831543, 0.1875, 0.12792969, 0.22753906, 0.018188477, -0.079589844, -0.11376953, -0.06933594, -0.15527344, -0.08105469, -0.09277344, -0.11328125, -0.15136719, -0.080078125, -0.05126953, -0.15332031, 0.11669922, 0.068359375, 0.032470703, -0.33984375, -0.08154297, -0.083496094, 0.040039062, 0.049072266, -0.24121094, -0.13476562, -0.059326172, 0.12158203, -0.34179688, 0.16503906, 0.061767578, -0.18164062, 0.20117188, -0.07714844, 0.1640625, 0.0040283203, 0.30273438, -0.100097656, -0.13671875, -0.059570312, 0.0625, -0.21289062, -0.06542969, 0.1796875, -0.07763672, -0.01928711, -0.15039062, -0.0010604858, 0.034179688, 0.033447266, 0.19335938, 0.01965332, -0.19921875, -0.10644531, 0.015258789, 0.009277344, 0.014160156, -0.023925781, 0.05883789, 0.02368164, 0.125, 0.047607422, -0.055664062, 0.115722656, 0.14746094, 0.1015625, -0.07128906, -0.07714844, -0.12597656, 0.029174805, 0.095214844, -0.12402344, -0.109375, -0.12890625, 0.16308594, 0.28320312, -0.03149414, 0.123046875, -0.23242188, -0.09375, -0.12988281, 0.013549805, -0.03881836, -0.08251953, 0.008972168, 0.16308594, 0.10546875, -0.13867188, -0.16503906, -0.03857422, 0.10839844, -0.10498047, 0.063964844, 0.38867188, -0.059814453, -0.061279297, -0.10449219, -0.16796875, 0.071777344, 0.13964844, 0.15527344, -0.03125, -0.20214844, -0.12988281, -0.10058594, -0.063964844, -0.083496094, -0.30273438, -0.080078125, 0.020996094],
    "woman": [0.24316406, -0.07714844, -0.103027344, -0.107421875, 0.11816406, -0.107421875, -0.11425781, 0.025634766, 0.111816406, 0.048583984, -0.09716797, -0.34375, -0.06298828, -0.125, -0.02709961, 0.09423828, -0.1875, -0.053466797, 0.0625, -0.030517578, -0.029052734, -0.048095703, -0.05517578, -0.40820312, 0.010131836, -0.23242188, -0.17089844, 0.26367188, 0.34960938, -0.21191406, 0.14355469, -0.006225586, -0.22558594, -0.10546875, -0.11621094, 0.123046875, 0.30664062, -0.048828125, -0.095703125, 0.19921875, -0.15722656, -0.028076172, 0.15820312, -0.024291992, 0.12988281, -0.08984375, -0.076171875, 0.03540039, -0.030639648, 0.15234375, 0.052490234, 0.0016098022, 0.055664062, 0.03955078, -0.07714844, -0.07128906, -0.092285156, -0.0703125, 0.203125, 0.015319824, 0.29882812, 0.17578125, -0.045410156, 0.095214844, 0.041259766, 0.07763672, 0.09472656, 0.16796875, 0.20117188, -0.072265625, 0.18359375, 0.21582031, -0.23828125, 0.10498047, -0.016601562, 0.24023438, 0.016723633, -0.045654297, 0.16894531, 0.18554688, 0.24707031, -0.10205078, 0.08496094, -0.104003906, -0.47460938, 0.26367188, -0.15722656, 0.08251953, 0.21972656, -0.030395508, -0.25585938, -0.19726562, -0.09277344, -0.012817383, 0.12695312, 0.03540039, 0.05883789, 0.032714844, 0.17285156, -0.020874023, -0.16503906, -0.28125, 0.08496094, -0.16992188, 0.23144531, -0.14160156, 0.07910156, -0.19238281, 0.076171875, -0.22363281, -0.010681152, 0.056640625, 0.15625, 0.071777344, -0.15625, -0.14453125, -0.08300781, -0.12109375, 0.056396484, 0.26171875, 0.079589844, -0.012878418, -0.20019531, -0.043945312, -0.1015625, 0.12988281, 0.09423828, 0.019042969, 0.14257812, 0.15917969, -0.07470703, -0.32421875, -0.20703125, 0.048095703, -0.041992188, 0.092285156, -0.043945312, -0.22070312, -0.0625, 0.083984375, 0.22949219, -0.111816406, 0.09033203, 0.20898438, -0.22851562, 0.28710938, -0.13867188, 0.18554688, -0.2109375, -0.20507812, 0.30078125, -0.18261719, 0.123046875, -0.16113281, 0.09375, 0.12597656, -0.08105469, 9.1552734e-05, 0.15332031, -0.08105469, -0.19335938, 0.007080078, 0.38476562, 0.10595703, -0.109375, -0.11376953, 0.091308594, -0.19238281, 0.061279297, 0.006072998, -0.045410156, 0.0625, -0.13085938, -0.18359375, -0.17675781, -0.1875, 0.24414062, 0.18945312, -0.19335938, -0.022949219, 0.025390625, 0.0039367676, -0.13867188, -0.28125, -0.18066406, 0.08691406, 0.03173828, 0.25585938, -0.23046875, -0.052490234, -0.0021820068, 0.16015625, 0.15722656, 0.27929688, 0.13769531, 0.10449219, -0.118652344, -0.05810547, -0.07324219, 0.010498047, -0.17773438, -0.107421875, -0.17675781, -0.123046875, -0.16992188, -0.13476562, 0.063964844, 0.122558594, 0.1953125, -0.49414062, -0.0390625, -0.031982422, -0.01586914, -0.041015625, -0.14355469, -0.0859375, -0.079589844, 0.24609375, -0.17773438, 0.20507812, 0.053222656, -0.025146484, 0.21484375, 0.021240234, 0.09765625, -0.21679688, 0.28515625, -0.119140625, -0.16699219, -0.0036010742, 0.046142578, -0.16308594, -0.25390625, 0.18945312, -0.07519531, -0.053955078, -0.17773438, -0.04321289, -0.007385254, 0.15722656, 0.25390625, -0.15234375, -0.052734375, -0.125, 0.15429688, 0.111816406, -0.0154418945, 0.008972168, -0.056396484, -0.025878906, 0.19335938, 0.052246094, -0.015625, -0.056884766, 0.1171875, 0.060058594, -0.026489258, -0.13964844, -0.072753906, -0.050048828, 0.029785156, -0.096191406, -0.16015625, -0.14160156, 0.21777344, 0.25585938, -0.045898438, 0.1171875, -0.24609375, -0.072753906, -0.08691406, 0.15722656, -0.18847656, 0.043945312, -0.005554199, 0.06933594, 0.14257812, -0.12060547, -0.104003906, -0.034179688, 0.18261719, -0.12988281, 0.016357422, 0.3203125, -0.11230469, -0.011291504, -0.13867188, -0.22070312, 0.00075912476, 0.39453125, 0.103515625, -0.06640625, -0.26757812, -0.24707031, -0.072753906, 0.107910156, 0.118652344, -0.08300781, 0.06542969, -0.029418945],
    "king": [0.12597656, 0.029785156, 0.008605957, 0.13964844, -0.025634766, -0.036132812, 0.111816406, -0.19824219, 0.05126953, 0.36328125, -0.2421875, -0.30273438, -0.17773438, -0.024902344, -0.16796875, -0.16992188, 0.03466797, 0.005218506, 0.04638672, 0.12890625, 0.13671875, 0.11279297, 0.059570312, 0.13671875, 0.10107422, -0.17675781, -0.25195312, 0.059814453, 0.34179688, -0.03112793, 0.10449219, 0.061767578, 0.12451172, 0.40039062, -0.32226562, 0.083984375, 0.0390625, 0.005859375, 0.0703125, 0.17285156, 0.13867188, -0.23144531, 0.28320312, 0.14257812, 0.34179688, -0.023925781, -0.10986328, 0.033203125, -0.0546875, 0.015319824, -0.16210938, 0.15820312, -0.25976562, 0.020141602, -0.16308594, 0.0013580322, -0.14453125, -0.056884766, 0.04296875, -0.024658203, 0.18554688, 0.44726562, 0.0095825195, 0.13183594, 0.09863281, -0.18554688, -0.100097656, -0.13378906, -0.125, 0.28320312, 0.123046875, 0.053222656, -0.17773438, 0.0859375, -0.021850586, 0.020507812, -0.13964844, 0.025146484, 0.13867188, -0.10546875, 0.13867188, 0.08886719, -0.07519531, -0.021362305, 0.17285156, 0.04638672, -0.265625, 0.008911133, 0.14941406, 0.037841797, 0.23828125, -0.12451172, -0.21777344, -0.18164062, 0.029785156, 0.057128906, -0.028930664, 0.012451172, 0.09667969, -0.23144531, 0.05810547, 0.06689453, 0.07080078, -0.30859375, -0.21484375, 0.14550781, -0.42773438, -0.009399414, 0.15429688, -0.076660156, 0.2890625, 0.27734375, -0.0004863739, -0.13671875, 0.32421875, -0.24609375, -0.003036499, -0.21191406, 0.125, 0.26953125, 0.20410156, 0.08251953, -0.20117188, -0.16015625, -0.037841797, -0.12011719, 0.115234375, -0.041015625, -0.03955078, -0.08984375, 0.0063476562, 0.203125, 0.18652344, 0.2734375, 0.06298828, 0.14160156, -0.09814453, 0.13867188, 0.18261719, 0.17382812, 0.17382812, -0.23730469, 0.17871094, 0.06347656, 0.23632812, -0.20898438, 0.087402344, -0.16601562, -0.07910156, 0.24316406, -0.08886719, 0.12695312, -0.21679688, -0.17382812, -0.359375, -0.08251953, -0.064941406, 0.05078125, 0.13574219, -0.07470703, -0.1640625, 0.0115356445, 0.4453125, -0.21582031, -0.111328125, -0.19238281, 0.17089844, -0.125, 0.0026550293, 0.19238281, -0.17480469, 0.13964844, 0.29296875, 0.11328125, 0.059570312, -0.063964844, 0.099609375, -0.02722168, 0.01965332, 0.04272461, -0.24609375, 0.063964844, -0.22558594, -0.16894531, 0.00289917, 0.08203125, 0.34179688, 0.04321289, 0.1328125, 0.14257812, 0.076171875, 0.059814453, -0.119140625, 0.002746582, -0.06298828, -0.02722168, -0.0048217773, -0.08203125, -0.024902344, -0.40039062, -0.106933594, 0.04248047, 0.07763672, -0.11669922, 0.07373047, -0.092285156, 0.107910156, 0.15820312, 0.04248047, 0.12695312, 0.036132812, 0.26757812, -0.10107422, -0.30273438, -0.057617188, 0.05053711, 0.0005264282, -0.20703125, -0.13867188, -0.008972168, -0.027832031, -0.14160156, 0.20703125, -0.15820312, 0.12792969, 0.14941406, -0.022460938, -0.084472656, 0.122558594, 0.21582031, -0.21386719, -0.3125, -0.37304688, 0.0040893555, 0.107421875, 0.106933594, 0.07324219, 0.008972168, -0.03881836, -0.12988281, 0.14941406, -0.21484375, -0.0018386841, 0.099121094, 0.15722656, -0.11425781, -0.20507812, 0.099121094, 0.36914062, -0.19726562, 0.03540039, 0.109375, 0.13183594, 0.16699219, 0.23535156, 0.10498047, -0.49609375, -0.1640625, -0.15625, -0.052246094, 0.103027344, 0.24316406, -0.18847656, 0.05078125, -0.09375, -0.06689453, 0.022705078, 0.076171875, 0.2890625, 0.31054688, -0.053710938, 0.22851562, 0.025146484, 0.067871094, -0.12109375, -0.21582031, -0.2734375, -0.030761719, -0.33789062, 0.15332031, 0.23339844, -0.20800781, 0.37304688, 0.08203125, 0.25195312, -0.076171875, -0.04663086, -0.022338867, 0.029907227, -0.059326172, -0.0046691895, -0.24414062, -0.20996094, -0.28710938, -0.045410156, -0.17773438, -0.27929688, -0.0859375, 0.091308594, 0.25195312],
    "bridge": [0.0052490234, -0.14355469, -0.06933594, 0.123535156, 0.13183594, -0.08886719, -0.07128906, -0.21679688, -0.19726562, 0.055664062, -0.075683594, -0.38085938, 0.104003906, -0.0008163452, 0.1328125, 0.11279297, 0.072753906, -0.046875, 0.06591797, 0.09423828, 0.19042969, 0.13671875, -0.23632812, -0.118652344, 0.06542969, -0.053222656, -0.30859375, 0.091796875, 0.18847656, -0.16699219, -0.15625, -0.13085938, -0.08251953, 0.21289062, -0.35546875, -0.13183594, 0.096191406, 0.26367188, -0.09472656, 0.18359375, 0.106933594, -0.41601562, 0.26953125, -0.027709961, 0.17578125, -0.11279297, -0.004119873, 0.14550781, 0.15625, 0.26757812, -0.017944336, 0.09863281, 0.052978516, -0.03125, -0.16308594, -0.05810547, -0.34375, -0.17285156, 0.11425781, -0.09033203, 0.13476562, 0.27929688, -0.049804688, 0.12988281, 0.17578125, -0.22167969, -0.0119018555, 0.140625, -0.18164062, 0.118652344, 0.16113281, 0.21484375, -0.21191406, 0.12695312, -0.100097656, 0.13671875, 0.12695312, 0.015319824, 0.10449219, -0.027832031, -0.060302734, 0.022216797, 0.18164062, -0.06738281, 0.049072266, 0.15429688, -0.25, 0.13964844, 0.29492188, 0.10644531, 0.3359375, -0.22265625, -0.125, -0.052978516, 0.19238281, 0.068359375, 0.06982422, -0.052001953, 0.14453125, 0.004486084, -0.010131836, -0.1484375, 0.21777344, -0.1953125, -0.390625, 0.07763672, -0.57421875, -0.07910156, -0.040527344, -0.1875, 0.25390625, 0.15722656, 0.125, 0.140625, 0.20117188, -0.05859375, 0.16894531, -0.28125, 0.171875, 0.19140625, 0.12109375, -0.15039062, -0.006958008, -0.23730469, 0.13964844, -0.008361816, -0.04711914, 0.14648438, -0.056884766, 0.10205078, 0.084472656, 0.21191406, -0.018310547, 0.50390625, -0.048583984, 0.22167969, -0.25585938, 0.034179688, 0.15820312, -0.033691406, 0.06738281, -0.25195312, 0.046142578, -0.072753906, 0.079589844, 0.042236328, -0.0012893677, 0.20214844, -0.13085938, -0.060302734, 0.037841797, 0.13574219, 0.111816406, -0.24609375, -0.23925781, -0.23632812, -0.04321289, -0.029052734, 0.23535156, -0.00390625, -0.05029297, 0.18457031, 0.50390625, -0.0066833496, -0.03466797, -0.075683594, 0.061523438, -0.31445312, -0.037597656, 0.23632812, -0.12792969, 0.15429688, 0.296875, 0.02709961, -0.17089844, -0.22460938, 0.0024108887, 0.10595703, -0.033203125, 0.014587402, -0.21582031, 0.24707031, -0.07421875, -0.10205078, 0.16894531, -0.05029297, 0.20800781, -0.03857422, -0.22265625, 0.27539062, -0.059570312, -0.017578125, 0.017944336, 0.08886719, 0.12890625, 0.18261719, 0.14453125, 0.104003906, -0.1328125, -0.32617188, 0.0038604736, -0.11376953, -0.05053711, -0.13085938, 0.022094727, -0.14648438, 0.107421875, 0.23046875, 0.15234375, 0.22753906, 0.048339844, 0.067871094, -0.067871094, -0.2578125, 0.11230469, 0.0036315918, -0.12011719, -0.21289062, 0.11230469, 0.12158203, 0.068359375, 0.049072266, 0.2734375, -0.0030212402, -0.0037841797, 0.0019378662, 0.1875, -0.29101562, 0.09033203, 0.26367188, -0.25585938, -0.28710938, -0.40820312, 0.10546875, 0.39648438, -0.072753906, -0.04321289, -0.06347656, -0.00060272217, -0.115234375, 0.31445312, -0.22265625, 0.13574219, -0.01965332, 0.15332031, 0.0036010742, -0.12011719, 0.064941406, 0.16210938, -0.16699219, 0.032714844, -0.0035095215, 0.18847656, 0.19335938, 0.1328125, 0.067871094, -0.34179688, -0.083496094, -0.29492188, -0.020996094, 0.08886719, 0.32421875, -0.36914062, -0.0859375, -0.049560547, 0.13183594, 0.044189453, 0.359375, 0.21484375, 0.265625, -0.2734375, 0.23535156, 0.11425781, 0.087890625, 0.1875, -0.33203125, 0.15136719, -0.036132812, -0.119140625, 0.27734375, 0.10839844, -0.072753906, 0.23242188, 0.0021972656, 0.23828125, -0.24902344, -0.123535156, -0.15917969, -0.006011963, 0.14550781, -0.0046081543, -0.22558594, -0.37890625, -0.37695312, -0.08251953, -0.041259766, 0.16796875, -0.046875, 0.16308594, 0.15429688]
}

def test_find_common_meaning_missing_model():
    assert find_common_meaning("misiing", "man", "good", "evil") == 0

def test_find_common_meaning_missing_base_word():
    assert find_common_meaning(model, "missing_base", "good", "evil") == 0

def test_find_common_meaning_missing_related_word():
    assert find_common_meaning(model, "good", "missing_related", "evil") == 0

def test_find_common_meaning_missing_target_word():
    assert find_common_meaning(model, "good", "evil", "missing_target") == 0

def test_find_common_meaning_none_base_word():
    assert find_common_meaning(model, None, "good", "evil") == 0

def test_find_common_meaning_none_model():
    assert find_common_meaning(None, "good", "evil", "man") == 0

def test_find_common_meaning_none_related_word():
    assert find_common_meaning(model, "good", None, "evil") == 0

def test_find_common_meaning_none_target_word():
    assert find_common_meaning(model, "good", "evil", None) == 0

def test_find_common_meaning_zero_vector_target():
    model["zero_target"] = [0, 0]
    assert find_common_meaning(model, "good", "zero_target", "evil") == 'good'

def test_find_common_meaning_zero_vectors_base():
    model["zero_target"] = [0, 0]
    assert find_common_meaning(model, "zero_target", "evil", "good") == 'zero_target'

def test_find_common_meaning():
    assert find_common_meaning(model, 'man', 'king', 'woman') == 'queen'