# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import os
import json


def find_file(find_path, file_type):
    """
    寻找文件
    :param find_path: 子路径
    :param file_type: 文件类型
    :return:
    """
    path = os.path.abspath('') + "\\" + find_path
    data_list = []
    for root, dirs, files in os.walk(path):
        if root != path:
            break
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.find(file_type) != -1:
                data_list.append(file_path)
    # print(data_list)
    return data_list


class uploda():
    def __init__(self):
        self.chrome_path = r"\firefox\firefox.exe"
        self.path = os.path.abspath('')
        self.context = None
        self.browser = None
        self.page = None
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
        self.img_list = []
        self.data_list = []

    def main(self):
        url = "https://mp.dcdapp.com/ugc/publish?is_new_connect=0&is_new_user=0#/post"
        self.img_list = find_file("img", 'png')
        with sync_playwright() as p:
            # , executable_path=self.path + self.chrome_path
            self.browser = p.firefox.launch(headless=True)
            try:
                self.context = self.browser.new_context(user_agent=self.ua, storage_state=self.path + r"\cookie.json")
            except FileNotFoundError:
                print("请先导入cookie")
            self.page = self.context.new_page()
            self.page.add_init_script("Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});")
            self.page.goto(url)
            try:
                with self.page.expect_file_chooser() as fc_info:
                    self.page.locator("div.syl-toolbar-tool:nth-child(1) > div:nth-child(1) > button:nth-child(1) "
                                      "> svg:nth-child(1) > path:nth-child(2)").click()
                file_chooser = fc_info.value
                file_chooser.set_files(self.img_list, timeout=3000)
                # time.sleep(1)
            except Exception as e:
                pass
            self.page.on("response", self.handler)
            self.page.wait_for_timeout(timeout=1000 * 3)
            return {"data": self.data_list}

    def handler(self, response):
        urls = response.url
        if 'imagex.bytedanceapi.com/?Action=CommitImageUpload' in urls:
            data = json.loads(response.text())
            print(data)
            self.data_list.append(data['Result']['Results'][0]['Uri'])
            x = len(self.data_list)
            print(f"正在上传第{x}个图片，上传进度：{round(x / len(self.img_list) * 100)}%")


if __name__ == '__main__':
    data = uploda().main()
    print(data)
