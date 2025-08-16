import os
import subprocess
import time
import shutil

# 删除目录下所有的文件
directory = "./data/rules/"

# 确保目录存在并遍历删除其中的文件
if os.path.exists(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"无法删除文件: {file_path}, 错误: {e}")
else:
    print(f"目录 {directory} 不存在")

# 删除目录本身
try:
    shutil.rmtree(directory)
    print(f"成功删除目录 {directory} 及其中的所有文件")
except Exception as e:
    print(f"无法删除目录 {directory}, 错误: {e}")

# 创建临时文件夹
os.makedirs("./tmp/", exist_ok=True)

# 复制补充规则到tmp文件夹
subprocess.run("cp ./data/mod/adblock.txt ./tmp/adblock01.txt", shell=True)
subprocess.run("cp ./data/mod/whitelist.txt ./tmp/allow01.txt", shell=True)


# 拦截规则
adblock = [
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt",
    "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_224_Chinese/filter.txt",
    "https://perflyst.github.io/PiHoleBlocklist/SmartTV-AGH.txt",
    "https://easylist-downloads.adblockplus.org/easylist.txt",
    "https://easylist-downloads.adblockplus.org/easylistchina.txt",
    "https://easylist-downloads.adblockplus.org/easyprivacy.txt",
    "https://raw.githubusercontent.com/Noyllopa/NoAppDownload/master/NoAppDownload.txt",
    "https://raw.githubusercontent.com/sjhgvr/oisd/main/abp_small.txt",
    "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt",
    "https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/rule.txt",
    "https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt"
	"https://easylist-downloads.adblockplus.org/easylist.txt"
	"https://filters.adtidy.org/windows/filters/224_optimized.txt"
	"https://raw.githubusercontent.com/cjx82630/cjxlist/master/cjx-annoyance.txt"
	"https://easylist.to/easylist/fanboy-annoyance.txt"
	"https://easylist.to/easylist/easyprivacy.txt"
	"https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt"
	"https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt"
 	"https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-hosts-online.txt"
 	"https://raw.githubusercontent.com/lingeringsound/10007/main/all"
	"https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts"
	"https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt"
 	"https://easylist-downloads.adblockplus.org/antiadblockfilters.txt"
	"https://easylist-downloads.adblockplus.org/easylistchina.txt"
	"https://filters.adtidy.org/android/filters/15_optimized.txt"
	"https://filters.adtidy.org/extension/ublock/filters/224.txt"
	"https://filters.adtidy.org/extension/ublock/filters/11.txt"
	"https://github.com/Potterli20/file/releases/download/github-hosts/Accelerate-Hosts.txt"
	"https://anti-ad.net/easylist.txt"
	"https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts"
	"https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockfilters.txt"
	"https://raw.githubusercontent.com/pboymt/Steam520/main/hosts"
	"https://raw.githubusercontent.com/rentianyu/Ad-set-hosts/master/adguard"
	"https://lingeringsound.github.io/adblock_auto/Rules/adblock_auto.txt"
	"https://lingeringsound.github.io/adblock_auto/Rules/adblock_auto_lite.txt"
	"https://raw.fgit.ml/lingeringsound/adblock/master/Toutiao_block.txt"
	"https://raw.githubusercontent.com/uniartisan/adblock_list/master/adblock_plus.txt"
	"https://raw.githubusercontent.com/uniartisan/adblock_list/master/adblock_privacy.txt"
	"https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/rule.txt"
	"https://raw.githubusercontent.com/xinggsf/Adblock-Plus-Rule/master/mv.txt"
	"https://raw.githubusercontent.com/banbendalao/ADgk/master/ADgk.txt"
	"https://raw.githubusercontent.com/banbendalao/ADgk/master/kill-baidu-ad.txt"
	"https://raw.githubusercontent.com/jianboy/github-host/master/hosts"
	"https://raw.githubusercontent.com/damengzhu/banad/main/jiekouAD.txt"
	"https://raw.githubusercontent.com/zsakvo/AdGuard-Custom-Rule/master/rule/zhihu-strict.txt"
	"https://small.oisd.nl/"
	"https://raw.githubusercontent.com/francis-zhao/quarklist/master/dist/quarklist.txt"
	"https://raw.githubusercontent.com/neodevpro/neodevhost/master/lite_adblocker"
	"https://raw.githubusercontent.com/Cats-Team/AdRules/main/adblock_lite.txt"
	"https://gitlab.com/ineo6/hosts/-/raw/master/next-hosts"
	"https://raw.hellogithub.com/hosts"
	"https://raw.githubusercontent.com/Noyllopa/NoAppDownload/master/NoAppDownload.txt"
	"https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts"
	"https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt"
	"https://cdn.jsdelivr.net/gh/sbwml/halflife-list@master/ad.txt"
	"https://raw.githubusercontent.com/596546419/ad-filters-subscriber/main/rule/local-rule.txt"
	"https://raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/adblock.txt"
	"https://raw.githubusercontent.com/8680/GOODBYEADS/master/data/rules/allow.txt"
	"https://raw.githubusercontent.com/zsokami/ACL4SSR/main/hosts"
	"https://raw.githubusercontent.com/Clov614/SteamHostSync/main/Hosts"
	"https://github.com/entr0pia/fcm-hosts/raw/fcm/fcm-hosts"
	"https://raw.githubusercontent.com/JohyC/Hosts/refs/heads/main/hosts.txt"
	"https://raw.githubusercontent.com/geoisam/FuckScripts/main/adfuck.txt"    
]

# 白名单规则
allow = [
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/ChineseFilter/sections/allowlist.txt",
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/GermanFilter/sections/allowlist.txt",
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/TurkishFilter/sections/allowlist.txt",
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/SpywareFilter/sections/allowlist.txt"
]

# 下载
for i, adblock_url in enumerate(adblock):
    subprocess.Popen(f"curl -m 60 --retry-delay 2 --retry 5 -k -L -C - -o tmp/adblock{i}.txt --connect-timeout 60 -s {adblock_url} | iconv -t utf-8", shell=True).wait()
    time.sleep(1)

for j, allow_url in enumerate(allow):
    subprocess.Popen(f"curl -m 60 --retry-delay 2 --retry 5 -k -L -C - -o tmp/allow{j}.txt --connect-timeout 60 -s {allow_url} | iconv -t utf-8", shell=True).wait()
    time.sleep(1)
    
print('规则下载完成')


