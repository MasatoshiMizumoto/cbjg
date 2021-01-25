#!python3

# ------------------------------------------------------------------------------------------------
# CloudEndure Bluprint Json Getter
#
# Usage:
# ガイダンスに従いパラメータを入力(username/password or api-key , projectname)
# Mode指定(Blueprints, Machines)
# 実行ディレクトリにjsonが生成
# ------------------------------------------------------------------------------------------------

import json
import sys

import requests

HOST = 'https://console.cloudendure.com'
headers = {'Content-Type': 'application/json'}
endpoint = '/api/latest/{}'
FileName = './{}-{}.json'

# ------------------------------------------------------------------------------------------------

# ログインパラメータ要求クラスの作成

def ce_getparam():

    while True:  # フォーマットチェック
        input1st = input('Please enter username or api-token :')
        if '@' in input1st or len(input1st) == 79:  # E-Mail or API Token
            break
        else:
            print('Please retype the correct string.')

    if '@' in input1st:
        ce_username = input1st
        ce_password = input('Please enter password :')
        login_data = {'username': ce_username, 'password': ce_password}
    else:
        ce_api_token = input1st
        login_data = {'userApiToken': ce_api_token}

    return login_data  # requestsに渡すパラメータを戻り値へ

# ------------------------------------------------------------------------------------------------
#　認証実行クラスの作成

def ce_login():
    session = {}
    r = requests.post(HOST + endpoint.format('login'),
                      data=json.dumps(login_params), headers=headers)
    print("Connecting to CloudEndure...")
    if r.status_code != 200 and r.status_code != 307:
        print("Bad login credentials")
        sys.exit(1)

    session = {'session': r.cookies['session']}
    headers['X-XSRF-TOKEN'] = r.cookies['XSRF-TOKEN']

    return session, headers  # sessionとheadersを戻り値へ

# ------------------------------------------------------------------------------------------------
# ProjectID取得クラスの作成

def ce_getProjectID(projectname):
    print('Getting ProjectID from you can access projects...')
    # project全体の取得
    r = requests.get(HOST + endpoint.format('projects'),
                     headers=ce_sessiondata[1], cookies=ce_sessiondata[0])  # rにproject全体の情報が格納
    if r.status_code != 200:
        print('Failed to fetch the project.')
        sys.exit(1)

    # project全体からNameでIDを絞り込む
    projects = json.loads(r.content)['items']  # jsonパースでprojectsに格納(itemsの中身)
    for project in projects:
        if project['name'] == projectname:
            return project['id'] # 戻り値

# ------------------------------------------------------------------------------------------------
# リスト取得API実行クラスの作成

def run_list_api():
    print(('Get {}...').format(get_info_type))
    r = requests.get(HOST + endpoint.format('projects/{}/{}').format(
        project_id, get_info_type), headers=ce_sessiondata[1], cookies=ce_sessiondata[0])
    if r.status_code != 200:
        print(('Failed to fetch {}}.').format(get_info_type))
        sys.exit(1)
    return r # 戻り値

# ------------------------------------------------------------------------------------------------
# ファイル保存クラスの作成

def get_list_data():
    with open(FileName.format(var_pjname, get_info_type), 'w', encoding='utf-8') as f:
        f.write(str(list_data.json()['items']))
    print('Finish.' + ' Saved to ' + str(FileName.format(var_pjname, get_info_type)))

# ------------------------------------------------------------------------------------------------


# タイトル
title = """\

------------------------------------------
      *                    *
     *     *         *    *   CloudEndure
    *         *          *    Bluprint
   *      *      *      *     Json
  *   *             *  *      Getter
 *                    *
------------------------------------------

"""
print(title)

# ログインパラメータの取得
login_params = ce_getparam()

# 認証の実行
# ce_sessiondata[0]=session ce_sessiondata[1]=headers
ce_sessiondata = ce_login()

# Project Nameを取得 filenameでも使うのでグローバルで
var_pjname = input('Please enter CloudEndure Project name :')

# ProjectIDを取得
# project_id = project['id']
project_id = ce_getProjectID(var_pjname)

# ModeIDを取得
while True:
    mode_id = int(
        input('Mode Select (1 = Blueprints, 2 = Machines（Include Replication Configurations)) :'))
    if mode_id != 0 and mode_id <= 2:
        break
    else:
        print('Please retype the correct value.')

if mode_id == 1:
    get_info_type = 'blueprints'
if mode_id == 2:
    get_info_type = 'machines'

# リスト取得API実行
# list_data = r
list_data = run_list_api()

# jsonファイルに保存
get_list_data()

exit()
