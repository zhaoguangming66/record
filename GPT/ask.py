import random
import pprint
import requests
import json

def rad():
    ck = ['FCMURHYAFZZ03LNZDH', 'FCCV4D18VEDU94HFZ9', 'FCX234A5EW45R47M7P', 'FCM39L5MAIGSRZGLHS', 'FCCRV3KREYXB66FG2Y', 'FCVV0OWGFPSP1MUR0Q', 'FCWOZUH486Y2I3B88S', 'FC0WU2TVXHD2YKGJRY', 'FCJ1LLYG2ZHVV38HYF', 'FCXRM90ELZYD3ETT9M', 'FCPYBNT1F45PRL2NYL', 'FCPXU4HXDGAWVQSQEL', 'FCAH56XJ2UAMDIITVJ', 'FC47NUZU7HCAZOXT1B', 'FCRN9QD8GEHL8XOG9E', 'FCFCCLHCNS67494WQE', 'FC66LMYP2OXXW2BZF4', 'FCHYY30D6NXWCR2TCW', 'FC0YJYE41B2DHF8FCI', 'FCGKHLOF1XMPVWUMV5', 'FC0QBF2EENSMOXS14U', 'FCAANX56TKWOOFD168', 'FC3C1JR8NG9UBJJHDI', 'FC8V8VWNA7SRN56W5X', 'FCQKVFPANF21Y0EUTG', 'FCEMBNXKRKACMFDXB8', 'FCSVVAG8MXZOHGF8AP', 'FCK55F08UGOJZ8AK1E', 'FC107J5U7DHKTHKM0V', 'FC2FSUN6G52XYPW4C5', 'FCVTIFT0P29CY3QENY', 'FCE8OOCMVOE9V3K7A0', 'FCLWMN4ZBLKX68NX88', 'FCLP8OXECT8EIGXC35', 'FCLXUDELLJJ5A1NG2V', 'FCS0N13XPUT5CCCUPM', 'FC15LUOGYFTJKAAZ5J', 'FCHPRUH94W2EKEBLVF', 'FCCHV5XKL0TMW5TUOC', 'FCDQAI9C80A3L5IL44', 'FCE4UV261CYQDC48BH', 'FCSVBF2NE8LLVJF8FK', 'FC4KJBK9SBJ24J7W72', 'FCTNWAUC5JWVEB95EC', 'FCOEGYXEQZSZUXDGKQ', 'FCRLWL6VW6Z81JX3WL', 'FCZGED54W42KYLAT5J', 'FCKC0E8HFM4IP0KBJX', 'FCT3ICY79SGTHX2YR4', 'FCBCDX04LAYBNPJX08', 'FC9QP3SPGDY7IAN710', 'FCZ3RZG4JKEWEDPO4Y', 'FCN773Q188YVUWCQEW', 'FC199RWAJPWUJA82WN', 'FCF8BNDBO5X7MFCA8O', 'FCG6MHW6H6XE5SIUG8', 'FCN3PP65L5UEQR4WKA', 'FCI1HHBU1MZRH0YU6V', 'FC0DXM4WDOZF5FH1YV', 'FC25IEE9DWNZK5YUXU', 'FC4YR2RF6GZGX70MBQ', 'FCBXEXAVE954GKPZXL', 'FCS5U9J5QFFI0FTBR0', 'FCDGA1W1FNEDTNSPNJ', 'FCSOC52DVARWXVB7BD', 'FCYXPDNPYO4F17HZZD', 'FCWQWMQM7WG0CLZ3BD', 'FCC9GQCLJPG0QFWIZR', 'FCP5VI0KCME3YLIPM5', 'FCAXZZ2JC4KN4RU5DT', 'FCZY7UB8T2I66FGJVT', 'FC8YJIRVCO5W1IR3TG', 'FCX1OF2OFZDDKQ1A0W', 'FCST3HWYXHE363I23F', 'FCF7W4BZ7ZN4475I1U', 'FCK0RXV8NQ4X6FWT3O', 'FC29KA8H5JIP04SB2N', 'FCN3H26NW35W92G2OI', 'FCUC8HT0X3070I8TOG', 'FCS3E2EP58OU0ZW57M', 'FC87E5XDGHDNLQI6EQ', 'FCYDFOEIXYRXHVUMNG', 'FC9GGYP7OL7TB7YCWR', 'FCHQ5HQWZ8U985YRTW', 'FCY091X7ZDXXEHT9WS', 'FCXIUKI4BBWRX8SNZR', 'FCD37ZVUSP3EC7K22P', 'FCQKH61UCM6VO7WOMD', 'FCS8MMOHBS5F9B7Q5F', 'FCL7HURZH60W2XY0BS', 'FCOF20LEZIOKR3BJTA', 'FCEUY02IH8OKCK3ZP2', 'FCTMKGOLPO1ACAQ85T', 'FCPBVSVLUHI0P609X7', 'FCG5E50DMMLB5IM12R', 'FCTCEWMQQZ6Q7XHASE', 'FCMYJQF8XYZZR6Y4MB', 'FCT9BJTYK842W71MAM', 'FCZB50S62VAAEJYIJF', 'FC9EGDYU30OX1UGM7F', 'FCMBJ4JG2SDE03XZRX', 'FCJXWZPY70A3YN076V', 'FCKP2N646SNZF4IIMO', 'FCLHAPHQ3DADQ8GR4G', 'FCIYNCGQQ3OGBDZG2N', 'FCNP5U9Y5X08NLCWUA', 'FC7ZQZSO4NNRGW4IMP', 'FCCKM61MOTL81A63ZQ', 'FCNPO8Z5G91Z0RI9FP', 'FCUX899XX0MYDV2GE4', 'FCP91O9TZUA6MMFGI5', 'FC1DSQNNHHB3J2V0NX', 'FC24YD1NW2DTXVRQP2', 'FCF32M4250B3OHCNZM', 'FCTLO66YU8Q40450T2', 'FCEEXE70KAXHMMC6P0', 'FCGJPVTNWRFARWRF2H', 'FCJIW2XFSDYQ4ZT3H0', 'FCI5LAG4FNLYGLIJSC', 'FCXH3G8N7A0KMB6N8Z', 'FCMOPKP34BCWWJG1GY', 'FCUDSGMWEBLN1GDXKV', 'FC02SJ3ZGJVDL78SAG', 'FCM6Z11JXB8AG9AT0D', 'FCU8ZGXIOLJ36RTAX4', 'FC60EGJP4K3EO8CQEM', 'FCA7VUBTKV2GFKHIEE', 'FCFQUR5YA5FW69MU8U', 'FCWMZN3GEJWP4CZ2TI', 'FC08OT4MC9I3SGXDSB', 'FCDYO7YQ1LCI7SD5AD', 'FC8J4FV9NGJRH97SU8', 'FCQN0RA7NG63Q6V0FM', 'FCUNZM18HUY9RSK078', 'FC6OGIZ7H36J5S9XSQ', 'FCFN92SJH4R3IJVFS2', 'FC61NDWRY2ZVQ6GZRO', 'FCPFT4YCMFIIYGWGWN', 'FC8F57WTBJSGF3W3VO', 'FC8JYK7UZ375HIHIAI', 'FCOO4YRKDUEB2164P3', 'FC1Q84AFKFFDEZTSU4', 'FCLOIN8ZFIOQYGDCCJ', 'FCFY8G0JN7TCH9KSJ4', 'FCTDFBIZ5PZL6FBG1E', 'FCBZ9GT8OHV1D7SQQ5', 'FC45ZR3XAMLXTBD2LI', 'FCM5UDZLHGISLAMARG', 'FCZV1SB5I8VAWDU5FN', 'FC90NU53IQLQRP1WTE', 'FC84L6IZU1G50VK1PW', 'FCHU68RMGUC9HAHBKI', 'FC14F2P5TIZRAN85J4', 'FCN3R2E2006JQZOS8F', 'FCBYSXWJI2VRDPFDW2', 'FCPQ4GOIDOOBIGLDL9', 'FC30MNK0YFZSDA1FSC', 'FC2CWEM594OOMTA77M', 'FCR4QYPB2X7KPRPCAR', 'FCY8TBKE5N5IHMPYVK', 'FC87BK3N4GMQTMKGRU', 'FC6KRGG92U2Y5QBA1O', 'FC8CQEWHLWASZXE698', 'FCQK6O2LTLVWEQXDXZ', 'FCWBW32X1Y9D5761GZ', 'FCB2KWM87SGSH81FJ8', 'FCF9TDZ0ERVHBELH09', 'FCMUA0CX5IASSVF7S5', 'FC05QMPQSYHB2HO75C', 'FC04IAGN3072UCV7EI', 'FCPPF5FAIXKY95MH59', 'FCNCDX6NUTPDCY0QX5', 'FC51UYM6LO7T9SAHU2', 'FCJ6Q7NXYNPK8VX0DJ', 'FCK4BLHV5J11QPDZIS', 'FC2CHKUO45XS3ZD17S', 'FC6LCV8B5X3XJ0GBUQ', 'FCXMYTQTDNMJHL9AIJ', 'FC8UK25STSZF5VX4DB', 'FC4S5LLLK3GJ94MM5R', 'FCFKQ4U6HQD3UELO42', 'FCQTQKSMXU1JUX984S', 'FCC22M70DXN2FR519O', 'FCZHX22GMT1CN93IQ1', 'FCY41RM0IOSFRY8TNH', 'FC6NIGIB5O2BG32GVY', 'FCQJ0F0T7TPELRLPIV', 'FCM71A30NODZ3AK5GN', 'FCH7JH84G2CSS74BQU', 'FCBOPDOXIIC31308NA', 'FCE55BQHCI4T6JASJ7', 'FCE5UJ3DIQCES8H3GT', 'FC6G41913PUJDY84WB', 'FCGTYHC1W1V05F4NKE', 'FCX604INOWWLDROSI9', 'FCC47T3MEMV6TQG1LL', 'FCRNTK62GZN3UGT719', 'FCK06NW5EDQZK4YLEB', 'FCHMVAY4ZWXPQT2KSL', 'FCST57SVU8VX80K1FO', 'FC7VJ4KPBGSF2WCMQ4', 'FCF2YDMM2NMHP43A3I', 'FCT39DBZE400MM9VEU', 'FCNF8Q7QDXS5050Y2R', 'FCP6UJ0LGPY8XZUKZZ', 'FCNYW53KTS0YBVJ0OB', 'FCRBKHJJAYEEJE8VRT', 'FC5RD2963E0DAUB3LX', 'FCUAMDGS6LZWFGN120', 'FCL9VGA3PB8J44GXMG', 'FCW7A7YWQHNVHS58LT', 'FC8ONX5ZKVLBOYRDUR', 'FC31FB6BCHI85KVIAD', 'FCP0V3VHP8L8TRX08A', 'FCVO8EZMGFELOX8EGQ', 'FC7YKXFT26TTHLGAE5', 'FCPRN0M81QYSSWGLB2', 'FCO1P04U0CSUVG8ON2', 'FC1UWX45BPBZCF8DF1', 'FC9MUJ4VAJBU67WCW2', 'FCJZK67SSDZ4H3ONXY', 'FCL03U8SYK06Y1P4V4', 'FC0WYJ4JBWZLL7L9HY', 'FCRGLO487VEJNB9I0H', 'FCY5MAR3V3IPH2O788', 'FCAHVIB3LMB8LRN2GX', 'FCNDT8M20ZYKKMZYMA', 'FCFLZV5NJXZOU787YH', 'FC94QZLUH4THZRDBR3', 'FCDV25U88JVQ6R2VVZ', 'FCPBEB8VZNVGPGJ04M', 'FCTJRRWZONJ7QT95QX', 'FCOHSPE92UTOPLA89I', 'FCNXAW1YT1TB9T8PF9', 'FCBEVW1MGUPTCAO1ZP', 'FCGIEAMF4YUIP70L7F', 'FCPBVQ79P8YGCGLR8R', 'FC88MSNYNN6KQP02AN', 'FCTE72Y8NACAJ36BW9', 'FC6D5VT8E091FFIBXR', 'FCOMEPE4I9W5S3KXWP', 'FC53WF3BUIJ7QUGTAZ', 'FCRS2MQ33PFZF2WPY9']
    return random.choice(ck)


def ask(text):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Content-Type": "application/json",
        "Origin": "https://chat.forchange.cn",
        "Referer": "https://chat.forchange.cn/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    }
    url = "https://api.aigcfun.com/api/v1/text"
    params = {
        "key": rad()
    }
    data = {
        "messages": [
            {
                "role": "system",
                "content": "请以markdown的形式返回答案"
            },
            {
                "role": "user",
                "content": text
            }
        ],
        "tokensLength": 38,
        "model": "gpt-3.5-turbo"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, params=params, data=data,timeout=None)

    print(response.json()["choices"][0]["message"]["content"])


if __name__ == '__main__':
    txt = "Python压缩文件夹"
    ask(txt)