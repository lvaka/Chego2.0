function openClose(){
  //Sets the closing time and if restaurant is open or closed

  function isHoliday(){
  //Calculates Christmas, New Year's, and Thanksgiving
  var dateToday = new Date();
  if (dateToday.getDay() == 1){
    return true;
  } else if (dateToday.getDate() == 25 && dateToday.getMonth() == 11){
    return true;
  } else if (dateToday.getDate() == 1 && dateToday.getMonth() == 0){
    return true;
  } else if (dateToday.getMonth() == 10 && dateToday.getDate() == getThanksgivingDay()){
    return true;
  } else {
    return false;
  }
  }

  function openHours(){
  var dateToday = new Date();

  if (isHoliday() == false){
    if (dateToday.getDay() == 0 && dateToday.getHours() < 20 && dateToday.getHours() >= 10){
      return "We Are Open Until 9PM";
    } else if (dateToday.getDay() > 0 && dateToday.getHours() < 21 && dateToday.getHours() >= 10){
      return "We Are Open Until 10PM";
    } else if (dateToday.getDay() != 1){
      return "We Are Closed, but Will Open at 11am";
    } else {
      return "We Are Closed";
    }
  } else {
    return "We Are Closed"
  }
  }

  var dateToday = new Date();
  var bannerString = "Today is " + dateToday.toDateString() + " - " + openHours();
  var banner = document.getElementById('time');
  banner.textContent = bannerString;;
}

function backgroundSlideShow(){
  //Runs through a list of images to run in the background of div
  var bkg = document.getElementById("welcome-container").style;
  var list = ["01.jpg", "02.jpg", "03.jpg", "04.jpg", 
    "05.jpg", "06.jpg", "07.jpg", "08.jpg", "09.jpg", 
    "10.jpg", "11.jpg", "12.jpg", "13.jpg", "14.jpg", "15.jpg"];
  var x=0;

  setInterval(function(){
    bkg.backgroundImage = "url('/static/media/bowls/" + list[x] + "')";
    x++;
    if (x >= list.length){
      x = 0;
    }
  }, 700);
  
}

function cateringRequestOpen(){
  scrollToSection('#welcome-container');
  $('#form-modal').fadeIn();
}

function scrollToSection(selectSection){
  $('html, body').animate({scrollTop: ($(selectSection).offset().top-65)},800, "swing");
}

$(document).ready(function () {
  openClose();
  backgroundSlideShow();
  window.onclick = function(e) {
    if (e.target == document.getElementById('form-modal')){
      $('#form-modal').fadeOut();
    }
  }
  document.getElementById('closeForm').addEventListener('click',function(){$('#form-modal').fadeOut()});

});