function validate(){
    var diary = document.forms["myform"]["diary"].value;
    alert (diary);
    if (diary == null || diary == "") {
        alert("日记为空不能提交哦!!");
        return false;
    }
}