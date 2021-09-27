from django.shortcuts import render,redirect
from  Myweb import models

cartlist = []
customname = ''
customaddress = ''
customphone = ''



# Create your views here.
def login(request):
    # username = 'Tom'
    # password = '1234'

    if request.method == 'POST':  # 若是以<login.html>表單傳送
        name = request.POST['username']
        user = models.User.objects.get(u_username=name)    # 從models取得輸入的使用者資料
        if 'username' not in request.session:  # 若username這個session尚未建立
            if request.POST['password'] == user.u_password:   # 檢驗帳號密碼
                request.session['username'] = user.u_username  # 儲存session
                request.session['password'] = user.u_password
                message = user.u_username + '登入成功!'
                status = 'login'    # login.html裡會用到status

            else:
                status = ''
                message = '登入失敗，請重新登入'

    else:
        if 'username' in request.session:  # 若username這個session存在
            message = request.session['username'] + '您已登入'
            status = 'login'
    return render(request,'login.html',locals())


def logout(request):
    global cartlist
    if 'username' in request.session:  # 若username這個session存在
        message = request.session['username'] + '您已登出!'
        del request.session['username']
    cartlist = []
    request.session['cartlist'] = cartlist
    return render(request,'login.html',locals())

def product(request):   # 按'產品介紹'
    global cartlist
    if 'cartlist' in request.session:  # 若session中已有cartlist
        cartlist = request.session['cartlist']
    else:
        cartlist = []
    productall = models.Product.objects.all()
    cartnum = len(cartlist)
    return render(request,'product.html',locals())

def about(request):   # 按'關於我們'
    return render(request,'about.html',locals())

def showcart(request):   # 按'購物車'
    global cartlist
    cartlist1 = cartlist
    total = 0
    for unit in cartlist:
        total += (int(unit[2]) * int(unit[3]))
    grandtotal = total + 60  # 須加上運費60元
    return render(request,'cart.html',locals())

def addcart(request,ctype = None,productid = None):  # 按'加入購物車'
    global cartlist
    if ctype == 'add':  # 加入購物車
        product = models.Product.objects.get(id = productid)
        check = True
        for unit in cartlist:
            if product.p_name == unit[0]:  # 若購物車中已有同樣商品
                unit[3] = str(int(unit[3])+1)  # 商品數量加一
                unit[4] = str(int(unit[4]) + product.p_price)  # 計算總價
                check = False
                break
        if check:  # 若購物車中沒有同樣商品
            temp = []
            temp.append(product.p_name)  # 商品名稱
            temp.append(str(product.id))  # 商品id
            temp.append(str(product.p_price))  # 商品單價
            temp.append('1')  # 商品數量
            temp.append(str(product.p_price))  # 該項商品總價
            cartlist.append(temp)
        request.session['cartlist'] = cartlist  # 更新session中的購物車
        return redirect('/product/')

    if ctype == 'remove':
        del cartlist[int(productid)]  # 根據id刪除購物車中的該項產品
        request.session['cartlist'] = cartlist  # 更新session中的購物車
        return redirect('/cart/')

    if ctype == 'empty':  # 清空購物車
        cartlist = []
        request.session['cartlist'] = cartlist  # 更新session中的購物車
        return redirect('/cart/')

def order(request):  # 按'我要結帳'
    global cartlist,customname,customaddress,customphone
    cartlist1 = cartlist
    total = 0

    if not cartlist1:
        Message = '⇧ 購物車是空的? 趕快去逛逛!'
        return render(request,'cart.html',locals())

    for unit in cartlist:
        total += int(unit[4])  # 每項商品的總價相加
    grandtotal = total + 60
    customname1 = customname  # 以區域變數傳給模板
    customaddress1 = customaddress
    customphone1 = customphone
    return render(request,'cartorder.html',locals())

def buy(request):  # 按'確認購買'
    global cartlist,costomname,costomaddress,costomphone
    total = 0
    for unit in cartlist:
        total += int(unit[4])  # 每項商品的總價相加
    grandtotal = total + 60
    customname = request.POST.get('CustomerName','')
    customaddress = request.POST.get('CustomerPhone','')
    customphone = request.POST.get('CustomerAddress','')
    customname1 = customname

    if not customname or not customaddress or not customphone:
        information = 'correct'
    else:
        information = ''

    unitorder = models.Order.objects.create(o_customname=customname, o_customphone=customphone, o_customaddress=customaddress, o_subtotal=total, o_shipping=60, o_grandtotal=grandtotal)
    for unit in cartlist:
        total = int(unit[2]) * int(unit[3])
        unitdetail = models.Detail.objects.create(d_order=unitorder, d_product=unit[0], d_unitprice=unit[2], d_quantity=unit[3], d_total=total)
    cartlist = []
    request.session['cartlist'] = cartlist
    return render(request,'cartorder.html',locals())