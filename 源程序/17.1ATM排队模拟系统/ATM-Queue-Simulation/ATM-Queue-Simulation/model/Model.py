import pymysql
import random
import traceback

import numpy as np


class Model:
    def __init__(self):
        '''
        初始化变量
        '''
        self.arrive_time = []
        self.interval_time = []
        self.serve_time = []
        self.serve_start_time = []
        self.wait_time = []
        self.serve_end_time = []
        self.spend_time = []
        self.sys_free_time = []
        self.avg_wait_time = 0
        self.sys_util = 0

    def data_gen(self, num, max, min, probabilities):
        '''
        根据相应的数据，生成到达时间的随机值和服务时间的随机值
        :param num: 人数
        :param max: 间隔时间最大值
        :param min: 间隔时间最小值
        :param probabilities: 服务时间的概率
        :return:
        '''
        # 下面是生成到达时间的随机值
        tmp = True
        y = []
        lam = (max + min) / 2
        while tmp:
            time_list = np.random.poisson(lam, size=num).tolist()
            for i in time_list:
                if i > max or i < min:
                    time_list.remove(i)
            y = y + time_list
            if len(y) >= num:
                tmp = False
        if len(y) > num:
            y = y[:num]
        y.sort()
        self.arrive_time = y

        # 下面是生成服务时间的随机值
        seq = [1, 2, 3, 4, 5, 6]
        while len(self.serve_time) != num:
            z = random.uniform(0, 1)
            cumprob = 0.0
            for item, item_pro in zip(seq, probabilities):
                cumprob += item_pro
                if z < cumprob:
                    break
            self.serve_time.append(item)

    def result_cal(self, num):
        # 对第一次进行数据添加
        self.wait_time.append(0)
        self.serve_end_time.append(self.serve_time[0] + self.arrive_time[0])
        self.interval_time.append(0)
        self.serve_start_time.append(self.arrive_time[0])
        self.sys_free_time.append(0)
        # 对后面的进行数据添加
        for i in range(1, num):
            wait_time = self.serve_end_time[i - 1] - \
                        self.arrive_time[i]  # 等待时间=上一次的结束时间-到达时间
            if wait_time < 0:
                # 等待时间如果为0，第i个顾客的系统空闲时间就不为0
                self.sys_free_time.append(-wait_time)
                wait_time = 0
            else:
                self.sys_free_time.append(0)
            self.wait_time.append(wait_time)
            self.serve_end_time.append(self.arrive_time[i] + self.wait_time[i] + self
                                       .serve_time[i])  # 结束时间=等待时间+到达时间+服务时间
        wait_time = 0
        serve_time = self.serve_time[0]
        self.spend_time.append(self.wait_time[0] + self.serve_time[0])
        for i in range(1, num):
            self.serve_start_time.append(
                self.arrive_time[i] + self.wait_time[i])  # 开始时间=到达时间+等待时间
            self.spend_time.append(
                self.wait_time[i] + self.serve_time[i])  # 花费时间 = 等待时间+服务时间
            self.interval_time.append(
                self.arrive_time[i] - self.arrive_time[i - 1])  # 间隔时间 = 这次到达时间-上次到达时间
            wait_time = wait_time + self.wait_time[i]
            serve_time = serve_time + self.serve_time[i]
        self.avg_wait_time = wait_time / num  # 系统平均等待时间是等待时间之和除以人数
        # 系统总运行时间 = 最后一个人的结束时间 - 第一个人的到达时间
        all_time = self.serve_end_time[num - 1] - self.arrive_time[0]
        self.sys_util = serve_time / all_time  # 系统利用率 = 系统服务总时间 / 系统总运行时间

    def data_pool(self):
        '''
        返回所有数据
        :return:
        '''
        return {
                   'interval_time': self.interval_time,
                   'arrive_time': self.arrive_time,
                   'serve_time': self.serve_time,
                   'serve_start_time': self.serve_start_time,
                   'wait_time': self.wait_time,
                   'serve_end_time': self.serve_end_time,
                   'spend_time': self.spend_time,
                   'sys_free_time': self.sys_free_time
               }, {
                   'avg_wait_time': self.avg_wait_time,
                   'sys_util': self.sys_util
               }

    def data_check(self, probabilities, max_arr_time, min_arr_time, num_people):
        """  对数据进行检查.  """
        if len(probabilities) != 6 or num_people <= 1:
            return False
        if min_arr_time < 0 or max_arr_time < min_arr_time:
            return False
        total_prob = 0.0
        for every_prob in probabilities:
            if every_prob < 0 or every_prob > 1:
                return False
            total_prob = total_prob + every_prob
        return total_prob == 1

    def reset(self):
        '''
        重置，将所有值清0
        :return:
        '''
        self.arrive_time = []
        self.interval_time = []
        self.serve_time = []
        self.serve_start_time = []
        self.wait_time = []
        self.serve_end_time = []
        self.spend_time = []
        self.sys_free_time = []
        self.avg_wait_time = 0
        self.sys_util = 0

    def connect_db(self):
        config = {'host': 'localhost',
                  'port': 3306,
                  'user': 'root',
                  'password': '12345',
                  'db': 'song',
                  'charset': 'utf8'
                  }
        return pymysql.connect(**config)

    def create_table(self):
        """
        arg: self
        return: none
        To create a table describes the services for each experiment
        """
        conn = self.connect_db()
        cursor = conn.cursor()

        sql_createDB = """
                        CREATE TABLE IF NOT EXISTS group_data(
                        group_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        avg_wait_time FLOAT(6, 2),
                        sys_util FLOAT(6, 2)
                        )ENGINE=InnoDB DEFAULT CHARSET=utf8
                    """

        cursor.execute(sql_createDB)
        conn.commit()

        sql_createDB = """
                        CREATE TABLE IF NOT EXISTS serve(
                        client_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        arrive_time INT UNSIGNED,
                        interval_time INT UNSIGNED,
                        serve_time INT UNSIGNED,
                        serve_start_time INT UNSIGNED,
                        wait_time INT UNSIGNED,
                        serve_end_time INT UNSIGNED,
                        spend_time INT UNSIGNED,
                        sys_free_time INT UNSIGNED,
                        group_id int UNSIGNED,
                        FOREIGN KEY (group_id) REFERENCES group_data(group_id)
                        )ENGINE=InnoDB DEFAULT CHARSET=utf8
                        """
        cursor.execute(sql_createDB)
        conn.commit()
        cursor.close()
        conn.close()

    def insert_service(self, service):
        """
        arg: self
             service: a dict, the service item that will be inserted to table serve
        return: none
        Insert the item 'service' to table 'serve'
        """
        cols = ', '.join(service.keys())
        data = service.values()
        marks = ', '.join(['%s'] * len(service))

        data = list(data)
        for i in range(len(data)):
            data[i] = int(data[i])

        conn = self.connect_db()
        cursor = conn.cursor()
        sql_insert = "INSERT INTO serve (%s) VALUES (%s)" % (cols, marks)
        try:
            cursor.execute(sql_insert, data)
            conn.commit()
        except:
            # 失败回滚
            traceback.print_exc()
            conn.rollback()
            print("Exception: insert service failed!")
        conn.close()
        cursor.close()

    def delete_service(self, client_id):
        """
        :param client_id: the primary key that to be deleted
        :return: none
        To delete a service item whose primary key is client_id
        """
        sql_delete = "DELETE FROM serve where client_id = \"%s\"" % client_id
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(sql_delete)
            conn.commit()
        except:
            conn.rollback()
            print("Exception: delete service failed!")
        conn.close()
        cursor.close()
        pass

    def clean_database(self):
        """
        arg: self
        return: none
        Clean the table `xxq`
        """
        sql_drop_table = "DROP TABLE serve, group_data"
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(sql_drop_table)
            conn.commit()
            self.create_table()
        except:
            conn.rollback()
            print("Exception: clean database failed!")
        conn.close()
        cursor.close()
        pass

    def insert_group_data(self, group_items):
        """
        arg: self
             group_items: a dict, the service item that will be inserted to table serve
        return: none
        Insert the item 'group_items' to table 'serve'
        """
        cols = ', '.join(group_items.keys())
        data = group_items.values()
        marks = ', '.join(['%s'] * len(group_items))

        data = list(data)
        for i in range(len(data)):
            data[i] = float(data[i])

        conn = self.connect_db()
        cursor = conn.cursor()
        sql_insert = "INSERT INTO group_data (%s) VALUES (%s)" % (cols, marks)
        try:
            cursor.execute(sql_insert, data)
            conn.commit()
        except:
            # 失败回滚
            traceback.print_exc()
            conn.rollback()
            print("Exception: insert group_data failed!")
        conn.close()
        cursor.close()

    def delete_group_data(self, group_id):
        """
        :param group_id: the primary key that to be deleted
        :return: none
        To delete a service item whose primary key is group_id
        """
        sql_delete = "DELETE FROM group_data where group_id = \"%s\"" % group_id
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(sql_delete)
            conn.commit()
        except:
            conn.rollback()
            print("Exception: delete service failed!")
        conn.close()
        cursor.close()
        pass

    def delete_all(self):
        """
        :return: none
        To delete a all things in serve and group data
        """
        sql_delete_ser = "DELETE FROM serve;"
        sql_delete_gd = "DELETE FROM group_data;"
        conn = self.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(sql_delete_ser)
            cursor.execute(sql_delete_gd)
            conn.commit()
        except:
            traceback.print_exc()
            conn.rollback()
            print("Exception: delete failed!")
        conn.close()
        cursor.close()
        pass

    def read_group_id(self):
        sql_read = "SELECT group_id FROM group_data order by group_id desc limit 1"
        conn = self.connect_db()
        cursor = conn.cursor()
        result_id = 0
        try:
            cursor.execute(sql_read)
            result_id = cursor.fetchone()
        except:
            traceback.print_exc()
            conn.rollback()
            print("Exception: read failed!")
        conn.close()
        cursor.close()
        return result_id
        pass
