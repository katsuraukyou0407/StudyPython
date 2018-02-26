def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    for i, v in enumerate(argv):
        #数字かどうか判定し、それぞれの分岐を行う
        if v.isdigit():
            # 3のつく数字かどうかのflag
            flag = 0
            for j in range(len(v)):
                if v[j] == '3':
                    flag = 1
            #idiot、stupid、dumb、smartの条件分岐
            if int(v) % 3 == 0 and flag == 0:
                print('idiot')
            elif int(v) % 3 != 0 and flag == 1:
                print('stupid')
            elif int(v) % 3 == 0 and flag == 1:
                print('dumb')
            else:
                print('smart')
        else:
            print('invalid')
a = ['32']
main(a)