function openPage(pageName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(pageName).style.display = "block";
    elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

function hideStatisticDiv() {
  var x = document.getElementById("static");
  if (x.style.display === "none") {
    x.style.display = "flex";
  } else {
    x.style.display = "none";
  }
}
function hideDatasetDiv() {
  var x = document.getElementById("dataset");
  if (x.style.display === "none") {
    x.style.display = "flex";
  } else {
    x.style.display = "none";
  }
}
function toggleDiv(element){
    if (element==="dataset"){
         document.getElementById("dataset").style.display="block";
         document.getElementById("static").style.display="none";
    }else{
         document.getElementById("dataset").style.display="none";
         document.getElementById("static").style.display="flex";

    }

}