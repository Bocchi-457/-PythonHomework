import sqlite3

def print_cookies(cookies_db):
    try:
        # 使用上下文管理器确保连接被正确关闭
        with sqlite3.connect(cookies_db) as conn:
            cursor = conn.cursor()
            # 执行SQL查询
            cursor.execute('SELECT host, name, value FROM moz_cookies')
            rows = cursor.fetchall()
            print('\n[*] -- 已找到的 Cookies --')
            for row in rows:
                host, name, value = row  # 直接解包，使代码更整洁
                print(f'[+] Host: {host}, Cookie: {name}, Value: {value}')
    
    except sqlite3.DatabaseError as e:
        # 捕获特定的数据库错误
        print(f'\n[*] 读取cookies数据库时发生错误: {e}')
        print('[*] 更新你的Python-Sqlite3库或检查数据库的完整性。')
    
    except Exception as e:
        # 捕获其他异常并打印通用错误消息
        print(f'\n[*] 发生了意外的错误: {e}')

# 示例用法：
print_cookies("C:\\Users\\12089\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\g4c1ucrq.default-release\\cookies.sqlite")


import sqlite3

def print_history(places_db):
    try:
        with sqlite3.connect(places_db) as conn:
            cursor = conn.cursor()
            # 修改后的SQL查询，去掉了visit_count条件
            cursor.execute("""
                SELECT moz_places.url, datetime(moz_historyvisits.visit_date/1000000, 'unixepoch')
                FROM moz_places JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id;
            """)
            print('\n[*] -- 已找到的历史记录 --')
            for row in cursor:
                url = str(row[0])
                date = str(row[1])
                print(f'[+] {date} - 访问过: {url}')
    except sqlite3.DatabaseError as e:
        print(f'\n[*] 读取你的places数据库时发生错误: {e}')
        print('[*] 升级你的Python-Sqlite3库或检查你的数据库完整性。')
    except Exception as e:
        print(f'\n[*] 发生了意外的错误: {e}')

# 示例用法:
print_history("C:\\Users\\12089\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\g4c1ucrq.default-release\\places.sqlite")

import sqlite3

def print_google_visits(places_db):
    try:
        with sqlite3.connect(places_db) as conn:
            cursor = conn.cursor()
            # 修改后的SQL查询，去掉了visit_count条件
            cursor.execute("""
                SELECT moz_places.url, datetime(moz_historyvisits.visit_date/1000000, 'unixepoch')
                FROM moz_places JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id;
            """)
            print('\n[*] -- 已找到的Google访问记录 --')
            for row in cursor:
                url = str(row[0])
                date = str(row[1])
                if 'google' in url.lower():
                    print(f'[+] {date} - 访问过: {url}')
    except sqlite3.DatabaseError as e:
        print(f'\n[*] 读取你的places数据库时发生错误: {e}')
        print('[*] 升级你的Python-Sqlite3库或检查你的数据库完整性。')
    except Exception as e:
        print(f'\n[*] 发生了意外的错误: {e}')

# 示例用法:
print_google_visits("C:\\Users\\12089\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\g4c1ucrq.default-release\\places.sqlite")