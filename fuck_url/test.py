import requests
import hashlib
import json


def getToken(data):
    salt = "HF0000424J" + data
    return hashlib.sha1(salt.encode("utf-8")).hexdigest()


def get(url):
    headers = {
        "Host":
        "dc.simuwang.com",
        "Pragma":
        "no-cache",
        "Referer":
        "https://dc.simuwang.com/product/HF0000424J.html",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "X-Requested-With":
        "XMLHttpRequest",
        "Cookie":
        "sajssdk_2015_cross_new_user=1; guest_id=1536583229; regsms=1557925684000; Hm_lvt_c3f6328a1a952e922e996c667234cdae=1557925685; _9755xjdesxxd_=32; stat_sessid=0gqv6sm9a76tdo0q5crjqtcpe1; focus-certification-pop=-1; smppw_tz_auth=1; sensro_profile_has_set=1; rz_token_6658=f98c432cc619a59475f0a18721b5ef0c.1557934413; PHPSESSID=oddut76r9ct969ehvdava7smb3; gdxidpyhxdE=IQczOVWh2w9lBY5t65mhQ4Xiy1Ev3e1L6jURAwzc%5CtvAkE0rhsn0S0E5nuidi94XmuAdN2ZGrNjSePwM09ZXtw9aYmVGYJNmRwutdRa9H4eYzlIHaRm5DR4CQk2NwMai%2FyXmkEEmhN5eLeH9BC4hyvjQ%2FwxsMK18E7BAR%2B%2FyYa%5C%2Bu7gw%3A1557935313543; YD00211262352233%3AWM_NI=7UeK%2Buh1O1LgO6H50yiBiEAf9tYNnkhgk5kChwc78Xrgya0eGby%2FW2qUjxQb%2BPFGSyC%2BdKrccJXVJBzfggy6hvhOAPY8%2Fjkqbqnr6Im3XdrFcXAf06n70ZxwzqIyOUWkTjQ%3D; YD00211262352233%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee8ae66295baa4d2e97daa9a8ba2d14e928a9eaeee629aafb8a5c44988effba8e62af0fea7c3b92af58babacaa7facef81d2cf6d8dea88d6b373ab9ea7a6c46efbac97afed61acb9a5d6ea49aca9add8bb54b2b9b782b36f85beb7d0d63ab38ba699d46ae9908aa8d27381f5acacf169a19698b7c94ababaa988fc3eacaaa8b0c45c9be8e18bea7ba2afa293b543afed9885f14ea1888f87b33eaee900bbfb7dbaaf879ace5f95b59c8bd437e2a3; YD00211262352233%3AWM_TID=xJe5E1R5uZNAFFFVBQZoiIqlGFDDwtHl; http_tK_cache=56a993499791ce352b1d7edc20fc23bb73b2562f; cur_ck_time=1557934435; ck_request_key=e3Xc7To%2F2%2FKmJLvJq0CDZvRIFqJrIc2%2FR9cxzqQYF34%3D; passport=462071%09u2351047346350%09BQUFBQwAAQldUwQBWlBWDFJcAQEGCgkJAFZeXgYHAVY%3D9710d4c4e7; rz_u_p=d41d8cd98f00b204e9800998ecf8427e%3Du2351047346350; rz_rem_u_p=FYObVYCGsGkPHH6WWLagvQBSXxjVYKI80iHkv1ptzOQ%3D%24MbAeRfFK25WoayAgqnHSsxVhuoQIUjXaIp1D9LOj2OU%3D; certification=1; qualified_investor=1; evaluation_result=5; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22462071%22%2C%22%24device_id%22%3A%2216abb9b650524f-0320446f9b422e-6353160-2073600-16abb9b650661e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22462071%22%7D; Hm_lpvt_c3f6328a1a952e922e996c667234cdae=1557934436; autologin_status=0"
    }
    r = requests.get(url, headers=headers)
    data = eval(r.content)['data']
    token = getToken(data)
    new_url = "https://dc.simuwang.com/fund/getNavList.html?id=HF0000424J&muid=462071&page=2&token=" + token
    r = requests.get(new_url, headers=headers)
    result = json.loads(r.content.decode("utf-8"))
    print(result)


def main():
    get("https://dc.simuwang.com/Api/getToken?id=HF0000424J&sign=09c6e547a76b780eea4b11f67258dff8fefda0ff"
        )


if __name__ == "__main__":
    main()