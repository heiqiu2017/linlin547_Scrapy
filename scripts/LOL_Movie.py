#!/usr/bin/env python
# -*- coding: utf-8 -*-
import DUtils,copy,sys,json,threading
from DUtils.Utils import Utils_func
reload(sys)
sys.setdefaultencoding('utf-8')
class Movie_LoL:
    def __init__(self):
        self.uf = Utils_func()
        #保存所有movie链接
        self.new_movie_list = []
        #存储结果list
        self.all_movie_list = []
        self.new_movie_url = ''
    def get_new_movie_list(self,url):
        #获取最新电影列表url
        self.new_movie_q_obj = self.uf.query_body(self.uf.selem_one_get(url))
        self.new_movie_url = DUtils.LOL_HomePage + self.new_movie_q_obj("div.gxl span a").attr("href")
        #获取时间排序列表
        for i in range(1,4):
            if i != 1:
                self.new_movie_url = self.new_movie_url.replace("1.html",(str(i)+".html"))
            self.movie_list_page_source = self.uf.query_body(self.uf.selem_one_get(self.new_movie_url))
            for n in self.movie_list_page_source("div.box3_mid ul li div.img a").items():
                self.new_movie_list.append(n.attr("href"))
    def req_movie_list_link(self,filename,url):
        #[{"m_name":"p_link","down_link":[{"alias_name":"down_link"}]}]
        self.movie_dic = {}
        # 下载列表
        self.movie_down_list = []
        #下载组装字典
        self.movie_down_dic = {}

        self.get_new_movie_list(url)
        for i in self.new_movie_list:
            self.movie_info = self.uf.query_body(self.uf.selem_one_get(i))
            #图片
            self.movie_img = self.movie_info("div.haibao img").attr("src")
            #电影名
            self.movie_name = self.movie_info("div.haibao img").attr("alt")
            print u"线程名", threading.currentThread().getName()
            print u"图片地址:", self.movie_img
            print u"电影名称:", self.movie_name
            self.movie_dic[self.movie_name] = self.movie_img
            lockx.acquire()
            #下载地址和下载名称
            for n in self.movie_info("#ul1 div.loldytt a").items():
                self.movie_alis_name = n.text()
                self.movie_down_link = n.attr("href")
                self.movie_down_dic[self.movie_alis_name] = self.movie_down_link
                print u"下载别名:", self.movie_alis_name
                print u"迅雷下载地址:", self.movie_down_link

                self.movie_down_list.append(copy.deepcopy(self.movie_down_dic))
                self.movie_down_dic.clear()

            self.movie_dic["D_Link"] = self.movie_down_list
            self.all_movie_list.append(copy.deepcopy(self.movie_dic))
            del self.movie_down_list[:]
            self.movie_dic.clear()
            lockx.release()
        # lockx.acquire()
        with open("LOL_Movie_%s.json" % filename, "a") as f:
            f.write(json.dumps(self.all_movie_list, ensure_ascii=False, indent=4))
        # lockx.release()
        # self.uf.quit_driver()
if __name__ == "__main__":
    scrap_movie_dic = {"DongZuo":"http://www.loldytt.com/Dongzuodianying/","KeHuan":"http://www.loldytt.com/Kehuandianying/",
                       "KongBu":"http://www.loldytt.com/Kongbudianying/","XiJu":"http://www.loldytt.com/Xijudianying/",
                       "AiQing":"http://www.loldytt.com/Aiqingdianying/","JuQing":"http://www.loldytt.com/Juqingdianying/",
                       "ZhanZheng":"http://www.loldytt.com/Zhanzhengdianying/","DongMan":"http://www.loldytt.com/Anime/"}
    thread_list = []
    lockx = threading.Lock()
    for i in scrap_movie_dic:
        thread_obj = threading.Thread(target=Movie_LoL().req_movie_list_link, args=(i,scrap_movie_dic[i]))
        thread_obj.start()
        thread_list.append(thread_obj)
    for n in thread_list:
        n.join()
