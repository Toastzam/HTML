
  let addBtn = document.querySelector('.addBtn');

    addBtn.addEventListener('click',function(){
    const inputValue = document.getElementById("myInput").value;
    alert(inputValue);
        window.location.href = '/todo/create?todo='+inputValue;
    }, false);

