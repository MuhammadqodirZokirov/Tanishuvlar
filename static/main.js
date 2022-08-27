let leftBtn = document.querySelector(".left_btn")
let links = document.querySelector('.left_content')
let send = document.querySelector(".send_btn")
let sendInput = document.querySelector(".send_input")
let userMessage = document.querySelector(".user_message")
let persons = document.querySelector(".users")
let lichTitle = document.querySelector(".lich_title")
let lichImg = document.querySelector(".lich_img")
let mod_title = document.querySelector(".mod_title")
let mod_img = document.querySelector(".mod_img")
let moon = document.querySelector('.moon')
let toggle = document.querySelector('.toggle')
let filt_btn = document.querySelector('.filt_btn')
let filter_menue = document.querySelector('.filter_menue')
let ban = document.querySelector('.ban')
let fradd = document.querySelector('.fradd')
let bandiv = document.querySelector('.bandiv')
let fradddiv = document.querySelector('.fradddiv')
bandiv.addEventListener('click', ()=>{
  ban.classList.toggle('dNone')
  if (fradd.classList.contains("dNone")!=true) {
    fradd.classList.add('dNone')
  }
})
fradddiv.addEventListener('click', ()=>{
  fradd.classList.toggle('dNone')

  if (ban.classList.contains("dNone") != true) {
      ban.classList.toggle('dNone')
  }

})



// lichTitle.innerHTML = firstlich[1].innerHTML
// lichImg.attributes[1].value = firstlich[0].currentSrc

sendInput.addEventListener("keypress", function (e) {

  if (e.key === "Enter") {
    // Cancel the default action, if needed
    e.preventDefault();
    sendMEssage(e)
  }
});
send.addEventListener("click", sendMEssage)


function sendMEssage(e) {

  let inpValue = sendInput.value;
  if (inpValue.length > 0) {
    const messageDiv = document.createElement('div');
    if (inpValue.length > 50) {
      messageDiv.classList.add('send_message');
      messageDiv.classList.add('width');
    } else {
      messageDiv.classList.add('send_message');
    }
    let kun = new Date()
    s = kun.getHours()
    m = kun.getMinutes()
    let m1 = 0
    if (m < 10) {
      m1 = `0${m}`
    } else {
      m1 = m
    }
    messageDiv.innerHTML = `
    <div class="mess_div">
      <div class="message_title">
        <span></span>
        <span><sub>${s}:${m1}</sub></span>
      </div>
      <p>${inpValue}</p>
    </div>`
    userMessage.appendChild(messageDiv)
    sendInput.value = ''
    userMessage.scrollTop = userMessage.scrollHeight

  }
}

users.forEach(function (person) {
  showUsers(person)
})

function showUsers(data) {
  const userDiv = document.createElement('div');
  userDiv.classList.add('user_fr');
  userDiv.innerHTML = `
        <div div class="imgd" >
          <img class="imgcr" src="${data.img}" alt="" />
        </div>
        <h6 class="click">${data.name}</h6>
      `
  persons.appendChild(userDiv)
}
links.addEventListener('click', (e) => {
  let thIs = e.target
  if (e.target.classList.contains("user_fr")) {
    // dark.classList.toggle("div_none")
    links.classList.remove("left_active")
    public = e.target.children
    lichTitle.innerHTML = public[1].innerHTML
    mod_title.innerHTML = public[1].innerHTML
    lichImg.attributes[1].value = public[0].children[0].currentSrc
    mod_img.attributes[1].value = public[0].children[0].currentSrc


    // dark.classList.toggle("div_none"
  } else if (e.target.classList.contains("click")) {
    let parentEl = thIs.parentElement;
    let userElement = parentEl.children
    lichTitle.innerHTML = userElement[1].innerHTML
    mod_title.innerHTML = userElement[1].innerHTML
    lichImg.attributes[1].value = userElement[0].children[0].currentSrc
    mod_img.attributes[1].value = userElement[0].children[0].currentSrc
    links.classList.remove("left_active")
  } else if (e.target.classList.contains("imgcr")) {
    let parentEl = thIs.parentElement.parentElement;
    let userElement = parentEl.children
    lichTitle.innerHTML = userElement[1].innerHTML
    mod_title.innerHTML = userElement[1].innerHTML
    lichImg.attributes[1].value = userElement[0].children[0].currentSrc
    mod_img.attributes[1].value = userElement[0].children[0].currentSrc
    links.classList.remove("left_active")
  }
})

leftBtn.addEventListener('click', (e) => {
  // dark.classList.toggle("div_none")
  links.classList.add("left_active")
  // dark.classList.toggle("div_none")
})
toggle.addEventListener('click', () => {
  document.body.classList.toggle('dark');
  moon.classList.toggle('fas')
})
filt_btn.addEventListener('click', (e) => {
  e.preventDefault()
  filter_menue.classList.toggle('dNone')
})
filter_menue.addEventListener('click', (e) => {
  console.log(e.target.innerHTML);
  filter_menue.classList.add('dNone')
})