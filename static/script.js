$(document).ready(function(){
    console.log('hey')
  var interval_val = 2;
  var timeout_ =null;
  $(".scroll_contant").on("mouseover", function(){
    var this_ =this;
    timeout_ = setInterval(function(){
      $(this_).scrollLeft(interval_val);
      interval_val++;
    }, 50);
  });
  
  $(".scroll_contant").on("mouseout", function(){
      clearInterval(timeout_);
      $(this).scrollLeft(0);
      interval_val = 2;
  });
  
})

$(function(){
  
  $(".dropdown-menu-right a").click(function(){
    
    var text = $(this).text()
    if (text != "Overall performance") {
        text = "ID: " + text + " "
        document.getElementById("title").innerHTML = "Performance by user"
    } else {
        text = "Select a user from the list "
        document.getElementById("title").innerHTML = "Overall performance"
    }
      
    $(".btn:first-child").text(text);
     $(".btn:first-child").val($(this).text());
    console.log($(this).text())
  });

});