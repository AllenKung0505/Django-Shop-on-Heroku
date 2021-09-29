// 檢查cartorder.html中的客戶資料是否填妥
function chk(){
    if(document.buy.CustomerName.value==''){
      alert('請填寫客戶姓名，謝謝');
      return false;
    }
    if(document.buy.CustomerPhone.value==''){
      alert('請填寫客戶連絡電話，謝謝');
      return false;
    }
    if(document.buy.CustomerAddress.value==''){
      alert('請填寫客戶地址，謝謝');
      return false;
    }
    return true;
  }