var url = "http://localhost:70";

function insert1() {
    var api = url + "/api/v1/users";
    var uname = document.getElementById("username").value;
    var passwd = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    console.log(uname);
    console.log(passwd);
    //var curl=api +"?"+"username="+ uname + "&" + "password=" + passwd;
    var curl = api;
    console.log(curl);
    data = {};
    data["uname"] = uname;
    data["password"] = passwd;
    data['email'] = email;
    var json = JSON.stringify(data);
    console.log(json);
    // console.log(api);

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", curl, true);
    xhttp.setRequestHeader('Content-type', 'application/json; charset=utf-8');

    xhttp.onreadystatechange = function () {


        if (xhttp.readyState == 4 && xhttp.status == "200") {
            var res = xhttp.responseText;
            console.log(res);
            window.location.href = "login.html";
            alert("Registration succesful! Please login to continue")
        }
        else if (xhttp.readyState == 4) {
            var res = xhttp.responseText;
            console.log(res);
            document.getElementById("username").value = "";
            document.getElementById("password").value = "";
            alert(res);

        }

    }

    xhttp.send(json);
}