#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import xlwt
import pymysql


style1 = xlwt.XFStyle()  # 设置单元格格式
style1.num_format_str = 'yyyy-mm-dd'
alignment = xlwt.Alignment()  # 创建居中
alignment.horz = xlwt.Alignment.HORZ_CENTER  # 居中style.alignment = alignment
style1.alignment = alignment
#wsheet.col(i).width = 0x0d00 + 10


def export(f_name, f_path='E:\\text\\'):


    conn = pymysql.Connect(
        host='172.18.3.123',
        port=3306,
        user='shun',
        password='123456',
        db='test',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )

    cur = conn.cursor()

    sql1 = '''
			 select distinct 
			 b.indx_code
			 from  test.csi_indx_mkt a,test.csi_indx_gen_info b 
			 where a.isvalid=1 and b.isvalid=1 and a.indx_code=b.indx_code  limit 0,50
			 '''

    cur.execute(sql1)
    result1 = cur.fetchall()
    print(result1)
    code_list = []
    for row in result1:
        code = row.get('indx_code')
        code_list.append(code)

    cur.close()

    cur = conn.cursor()

    for indx_code in code_list:
        w = xlwt.Workbook(encoding='utf-8', style_compression=True)
        wsheet = w.add_sheet('Index Constituents Data',
                            cell_overwrite_ok=True)  # 创建一个sheet

        for a in range(8):

            first_col = wsheet.col(a)  # xlwt中是行和列都是从0开始计算的
            first_col.width = 150 * 20  # 定义宽度

            style = xlwt.XFStyle()  # 创建格式style
            alignment = xlwt.Alignment()  # 创建居中
            alignment.horz = xlwt.Alignment.HORZ_CENTER  # 居中
            style.alignment = alignment

        print(indx_code)
        sql = '''
						select 
						a.tradedate,
						a.indx_code,
						c.sec_code,
						a.sec_sname,
						a.sec_ename,
						(case when a.trade_mkt=1 then '深圳' 
							 when a.trade_mkt=2 then '上海'
						else null end) as trade_mkt,
						(case when a.trade_mkt=1 then 'shenzhen' 
							 when a.trade_mkt=2 then 'shanghai'
						else null end) as trade_emkt,
						a.weight
						from test.csi_index_weight_stock a,test.acsi_indices b,pgenius.pub_sec_code c
						where a.isvalid=1 and c.isvalid=1
						and a.indx_code=b.index_code
						and a.sec_inner_code=c.inner_code
						and a.tradedate=(select max(tradedate) from test.csi_index_weight_stock where indx_code=a.indx_code)
						and a.indx_code='{}'
						order by a.trade_mkt asc
					 '''.format(indx_code)

        cur.execute(sql)
        print(sql)
        columnName = ['tradedate', 'indx_code', 'sec_code', 'sec_sname',
                      'sec_ename', 'trade_mkt', 'trade_emkt', 'weight']  # 定义所有的列名

        for i in range(len(columnName)):  # 将列名插入表格
            wsheet.write(0, i, columnName[i])
            # print(i,columnName[i])

        results = cur.fetchall()
        #rows = len(results)

        # print(rows)
        i = 1
        for data in results:
            j = 0
            for key in columnName:
                # print(j,key,data[key])
                if key == "tradedate":
                    wsheet.write(i, j, data[key], style1)
                else:
                    wsheet.write(i, j, data[key], style)
                j += 1
            i += 1

        w.save('%(xx)s%(tt)s.xls' % ({"xx": f_path, "tt": indx_code + f_name}))

    cur.close()



# 结果测试
if __name__ == '__main__':
    export(f_name='closeweight')
