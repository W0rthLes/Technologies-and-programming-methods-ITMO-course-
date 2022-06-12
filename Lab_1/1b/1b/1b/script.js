function NotSaving(){
  document.onkeydown = function(event){
    if ((event.ctrlKey && event.keyCode == 83) || (event.keyCode == 123)){ //ctrl+s or f12 
      return false;
    }
  }
}

function Saving(){
  document.onkeydown = function(event){
    if ((event.ctrlKey && event.keyCode == 83) || (event.keyCode == 123)){
      return true;
    }
  }
}

var password = "ab34"




function block()
 {
  function noselect() {return false;}
  window.ondragstart = noselect; //запрет на то чтобы тянуть
  window.onselectstart = noselect; //запрет на выделение
  window.oncontextmenu = noselect; //запрет на пкм
  
  NotSaving(); 
  
  window.localStorage.setItem('blocked', true);
}


document.addEventListener('keyup', (event) => { //запрет на снимок экрана
  if (event.key == 'PrintScreen') 
  {
    var isblocked = window.localStorage.getItem('blocked')
    if (isblocked == "true")
    {
      navigator.clipboard.writeText('Screenshots are not allowed');  
    } 
  }
  });


function unblock() 
{
  window.ondragstart = select;
  window.onselectstart = select;
  window.oncontextmenu = select;
  function select() {return true;}

  Saving();

  window.localStorage.setItem('blocked', false);

}


window.onload = function()
{
  var isblocked = window.localStorage.getItem('blocked')
  if (isblocked == "true")
  {
    block();
  
  }
  else if (isblocked == null)
  {
    block();
  }
}



function checkPasKey(key) {
  return (key >= '0' && key <= '9')  || key == 'ArrowLeft' || key == 'ArrowRight' || key == 'Delete' || key == 'Backspace';
}

function checkPassword(){
  var input = document.getElementById('pas').value;

  var str = input.split("");

  for(var i = 0; i < str.length; i++)
  {
    if(str[i] == "1")
    {
      str[i] = "a";
    }
    if(str[i] == "2")
    {
      str[i] = "b";
    }

  }

  if (str.join('') != password)
  {
    alert('incorrect password')
    block()
  }
  else
  {
    alert("password correct")
    unblock();
  }

}











