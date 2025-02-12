function copycontent(flag) {
    var copyText = document.getElementById(flag);
    copyText.select();
    document.execCommand("Copy");
    alert("IP Address Copied");
}

function doActions(type) {
    var value = document.getElementById("dstaddr").value;
    if (value === "") {
        document.getElementById("inputWarn").innerHTML = "<p>Error: The destination address cannot be empty!</p>";
        document.getElementById("inputWarn").style.display = "block";
    }
    else {
        document.getElementById("lgResult").style.display = "none";
        document.getElementById("inputWarn").style.display = "none";
        const Http = new XMLHttpRequest();
        const url='/process/' + type + "/" + value;
        Http.open("GET", url);
        Http.send();
        Http.onreadystatechange = (e) => {
            if (Http.readyState === 4 && Http.status === 200) {
                document.getElementById("lgResult").innerHTML = Http.responseText;
                document.getElementById("lgResult").style.display = "block";
            }
        }
    }
}

function hideshowresult(flag) {
    if (flag === "hide") {
        document.getElementById("lgResult").style.display = "none";
    }
    else {
        document.getElementById("lgResult").style.display = "block";
    }
}