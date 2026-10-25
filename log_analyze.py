import re
from collections import Counter

def analyze_log(file_path):
    error_pattern = re.compile(r'ERROR')
    warn_pattern = re.compile(r'WARNING')
    ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')

    error_count = 0
    warn_count = 0
    ip_counter = Counter()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # 统计ERROR、WARNING
                if error_pattern.search(line):
                    error_count += 1
                if warn_pattern.search(line):
                    warn_count += 1
                # 提取IP
                ip_res = ip_pattern.search(line)
                if ip_res:
                    ip = ip_res.group()
                    ip_counter[ip] += 1

        print("===== 日志分析结果 =====")
        print(f"ERROR 总数：{error_count}")
        print(f"WARNING 总数：{warn_count}")
        print("访问IP统计（TOP5）：")
        for ip, cnt in ip_counter.most_common(5):
            print(f"  {ip} : {cnt} 次")
        return {
            "error": error_count,
            "warn": warn_count,
            "ip_stat": ip_counter.most_common(5)
        }
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
    except Exception as e:
        print(f"解析异常：{e}")

if __name__ == "__main__":
    # 读取同目录下的 test.log
    analyze_log("test.log")
